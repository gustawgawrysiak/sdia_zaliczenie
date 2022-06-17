# klaudia
from parcel_dto import *
import json
from my_deque import Deque


class ParcelsExport:

    def __init__(self):
        self.d = Deque()

    def import_json(self, file_name="truck.json"):
        with open(file_name) as trucks_data:
            trucks = json.load(trucks_data)
            trucks_data.close()
        return trucks

    def warehouse_parcel(self):
        '''pobieranie paczki z magazynu'''
        pass

    def truck_parcel(self):
        '''wkladanie paczki z magazynu do ciezarowki'''
        pass

p = ParcelsExport()
print(p.import_json())


