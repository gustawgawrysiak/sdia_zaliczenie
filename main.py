# main script path
from parcels_export import ParcelsExport
from warehouse import Warehouse
from parcels_import import ParcelsImport
from time import perf_counter


def run() -> float:

    start = perf_counter()

    warehouse = Warehouse()
    trucks = ParcelsExport()

    parcels_dict = ParcelsImport.import_json()
    parcels_list = ParcelsImport.create_parcels_list(parcels_dict)

    trucks_dict = ParcelsExport.import_json()
    trucks.insert_trucks(trucks_dict)

    warehouse.add_parcels_list(parcels_list)
    warehouse.export_parcels(export=trucks)

    end = perf_counter()
    return end-start


if __name__ == '__main__':
    e = run()
    print(e)
