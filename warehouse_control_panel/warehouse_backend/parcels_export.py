# klaudia
import json
from typing import List, Dict
from warehouse_control_panel.data_structures.parcel_dto import Truck


class ParcelsExport:

    def __init__(self):
        self._dq = []

    @property
    def dq(self):
        return self._dq

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
            self._dq.append(ParcelsExport.create_truck(truck))

    def pop_truck(self) -> None:
        return self._dq.pop(0)
