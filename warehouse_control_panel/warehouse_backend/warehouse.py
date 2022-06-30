from warehouse_control_panel.data_structures.my_deque import Deque
from warehouse_control_panel.data_structures.my_priority_queue import PriorityQueue
from warehouse_control_panel.data_structures.parcel_dto import Parcel
from typing import List
from warehouse_control_panel.warehouse_backend.parcels_export import ParcelsExport


class Warehouse:
    def __init__(self):
        self._storage = {'normal': Deque(), 'prior': PriorityQueue()}
        self._parcels_send = 0
        self._trucks_send = 0

    @property
    def parcels_send(self):
        return self._parcels_send

    @property
    def trucks_send(self):
        return self._trucks_send

    @property
    def prior(self):
        return self._storage['prior']

    @property
    def normal(self):
        return self._storage['normal']

    def add_normal_parcel(self, parcel: Parcel) -> None:
        self.normal.push_back(parcel)

    def add_priority_parcels(self, parcels: List[Parcel]) -> None:
        for i, parcel in enumerate(parcels):
            self.prior.attach(parcel, i)

    def add_parcels_list(self, parcels: List[Parcel]) -> None:
        parcel_priors = []
        for parcel in parcels:
            if parcel.priority:
                parcel_priors.append(parcel)
            else:
                self.add_normal_parcel(parcel)
        sorted_prior_parcels = self.sort_priority_parcels(parcel_priors)
        self.add_priority_parcels(sorted_prior_parcels)

    def pop_normal(self) -> Parcel:
        return self.normal.pop_front()

    def pop_prior(self) -> Parcel:
        return self.prior.detach()

    def normal_is_empty(self):
        return self.normal.is_empty()

    def front_prior(self):
        return self.prior.front()

    def front_normal(self):
        return self.normal.front()

    def prior_is_empty(self):
        return self.prior.is_empty()

    @staticmethod
    def calculate_dimensions(width: float, height: float, length: float) -> float:
        return width*height*length

    @staticmethod
    def sort_priority_parcels(parcels_list: List[Parcel]) -> List[Parcel]:
        new_parcels_list = sorted(parcels_list, key=lambda x: x.date, reverse=True)
        return new_parcels_list

    def export_parcels(self, export: ParcelsExport) -> None:
        for truck in export.dq:
            flag = False
            while not self.prior_is_empty():
                parcel = self.front_prior()[0]
                volume = Warehouse.calculate_dimensions(parcel.height, parcel.width, parcel.length)
                if self.parcel_fits(truck.capacity, truck.used_capacity,
                                    volume, truck.weight_range, truck.used_weight_range, parcel.weight):
                    truck.add_parcel_to_trunk(parcel)
                    truck.used_weight_range += parcel.weight
                    truck.used_capacity += volume
                    self.pop_prior()
                    self._parcels_send += 1
                else:
                    export.pop_truck()
                    self._trucks_send += 1
                    flag = True
                    break

            while not self.normal_is_empty() and not flag:
                parcel = self.front_normal()
                volume = Warehouse.calculate_dimensions(parcel.height, parcel.width, parcel.length)
                if self.parcel_fits(max_capacity=truck.capacity, used_capacity=truck.used_capacity,
                                    volume=volume, max_weight=truck.weight_range,
                                    used_weight=truck.used_weight_range, weight=parcel.weight):
                    truck.add_parcel_to_trunk(parcel)
                    truck.used_weight_range += parcel.weight
                    truck.used_capacity += volume
                    self.pop_normal()
                    self._parcels_send += 1
                else:
                    export.pop_truck()
                    self._trucks_send += 1
                    break

            if self.normal_is_empty() and self.prior_is_empty():
                if truck.trunk:
                    export.pop_truck()
                break

    @staticmethod
    def parcel_fits(max_capacity: float, used_capacity: float, volume: float,
                    max_weight: float, used_weight: float, weight: float) -> bool:
        return ((used_capacity + volume) < max_capacity) and ((used_weight + weight) < max_weight)
