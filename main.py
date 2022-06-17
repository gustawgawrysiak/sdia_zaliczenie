# main script path
from warehouse import Warehouse
from parcels_import import ParcelsImport


def run() -> None:
    e = ParcelsImport.import_json()
    a = ParcelsImport.create_parcels_list(e)
    w = Warehouse()
