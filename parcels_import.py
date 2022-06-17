import json
from datetime import datetime
from parcel_dto import Parcel
from typing import List, Dict


class ParcelsImport:
    @staticmethod
    def import_json(filename: str = 'parcels.json') -> Dict[str, List[dict]]:
        with open(filename) as parcels_data:
            parcels = json.load(parcels_data)
            parcels_data.close()
        return parcels

    @staticmethod
    def create_parcel(parcel: Dict) -> Parcel:
        date_format = '%d/%M/%Y'
        date_str = parcel.pop('date')
        return Parcel(**parcel, date=datetime.strptime(date_str, date_format))

    @staticmethod
    def create_parcels_list(parcels: Dict[str, List[dict]]) -> List[Parcel]:
        result = []
        for parcel in parcels["parcels"]:
            result.append(ParcelsImport.create_parcel(parcel))
        return result
