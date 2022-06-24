# klaudia
import json
from my_deque import Deque
from typing import List, Dict
from parcels_import import ParcelsImport


class ParcelsExport:

    def __init__(self):
        self.d = Deque()

    @staticmethod
    def import_json(filename: str = 'trucks.json') -> Dict[str, List[dict]]:
        with open(filename) as trucks_data:
            trucks = json.load(trucks_data)
            trucks_data.close()
        return trucks

    def warehouse_parcel():
        capacity_list = [capacity for capacity in v for v in ParcelsExport.import_json().values() if v['capacity']]
        # for v_export in ParcelsExport.import_json().values():
        #     for capacity in v_export:
        #         capacity = capacity['capacity']
        #         for v_import in ParcelsImport.import_json().values():
        #             for weight in v_import:
        #                 weight = weight['weight']
        #                 if capacity >= weight:
        #                     capacity -= weight
        return capacity_list


    def truck_parcel(self):
        # wkladanie paczki z magazynu do ciezarowki
        pass


for v in ParcelsExport.import_json().values():
    for capacity in v:
        print(capacity['capacity'])

# print(ParcelsExport.warehouse_parcel())

