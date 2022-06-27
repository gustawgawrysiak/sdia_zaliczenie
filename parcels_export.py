# klaudia
import json
from my_deque import Deque
from typing import List, Dict
from parcel_dto import Parcel, Truck
from parcels_import import ParcelsImport
from warehouse import Warehouse
from time import perf_counter


class ParcelsExport:

    def __init__(self):
        self._d = []

    @property
    def lst(self):
        return self._d

    @staticmethod
    def import_json(filename: str = 'trucks.json') -> Dict[str, List[dict]]:
        with open(filename) as trucks_data:
            trucks = json.load(trucks_data)
            trucks_data.close()
        return trucks

    @staticmethod
    def create_truck(truck: dict) -> Truck:
        return Truck(**truck, trunk=[])

    def insert_trucks(self, trucks: Dict[str, List[dict]]):
        for truck in trucks.get('trucks'):
            self.d.append(ParcelsExport.create_truck(truck))

    def pop_truck(self, parcel: Parcel) -> None:
        return self.d.pop(0)

    def export_parcels(self, warehouse: Warehouse) -> None:
        start = perf_counter()
        for truck in self.d:
            while not warehouse.prior_is_empty():
                parcel = warehouse.front_prior()
                volume = Warehouse.calculate_dimensions(parcel.height, parcel.width, parcel.length)
                if not (truck.capacity + volume) >= truck.capacity:
                    truck.add_parcel_to_trunk(parcel)
                else:
                    break
            while not warehouse.normal_is_empty():
                parcel = warehouse.front_prior()
                volume = Warehouse.calculate_dimensions(parcel.height, parcel.width, parcel.length)
                if not (truck.capacity + volume) > truck.capacity:
                    truck.add_parcel_to_trunk(parcel)
                else:
                    break
            end = perf_counter()
            self._d.pop(self.lst.find())
            print(end-start)
