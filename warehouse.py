from my_deque import Deque
from my_priority_queue import PriorityQueue
from parcels_import import ParcelsImport
from parcel_dto import Parcel
from typing import List


class Warehouse:
    def __init__(self):
        self.storage = {'normal': Deque(), 'prior': PriorityQueue()}

    @property
    def prior(self):
        return self.storage['prior']

    @property
    def normal(self):
        return self.storage['normal']

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

    def pop_normal(self) -> Parcel:
        return self.normal.pop_front()

    def pop_prior(self) -> Parcel:
        return self.prior.detach()

    @staticmethod
    def sort_priority_parcels(parcels_list: List[Parcel]) -> List[Parcel]:
        new_parcels_list = sorted(parcels_list, key=lambda x: x.date, reverse=True)
        return new_parcels_list


e = Warehouse()
a = e.add_parcels_list(ParcelsImport.create_parcels_list(ParcelsImport.import_json()))
# print(e.prior)
Warehouse().add_parcels_list(ParcelsImport.create_parcels_list(ParcelsImport.import_json()))
