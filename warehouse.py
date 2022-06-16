from my_deque import Deque
from my_priority_queue import PriorityQueue
from parcels_import import create_parcels_list, create_parcel, import_json
from parcel_dto import Parcel
from typing import List
# gucio


class Warehouse:
    def __init__(self):
        self.storage = {'normal': Deque(), 'prior': PriorityQueue()}

    @property
    def prior(self):
        return self.storage['prior']

    @property
    def normal(self):
        return self.storage['normal']

    def add_parcel(self, parcel: Parcel) -> None:
        if not parcel.priority:
            self.storage['normal'].push_back(parcel)
        else:
            self.storage['prior'].attach(parcel)

    def add_parcels_list(self, parcels: List[Parcel]) -> None:
        for parcel in parcels:
            self.add_parcel(parcel)

    def pop_normal(self) -> Parcel:
        return self.normal.pop_front()

    def pop_prior(self) -> Parcel:
        return self.prior.detach()

    def give_parcel_priority(self, parcel: Parcel) -> int:
        # tu nadanie priorytetu dla paczki, operacje na priorze i szukanie
        pass


e = Warehouse()
e.add_parcels_list(create_parcels_list(parcels=import_json()))

