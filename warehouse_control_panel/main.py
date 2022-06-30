# main script path
from warehouse_control_panel.warehouse_backend.parcels_export import ParcelsExport
from warehouse_control_panel.warehouse_backend.warehouse import Warehouse
from warehouse_control_panel.warehouse_backend.parcels_import import ParcelsImport
from time import perf_counter


def run() -> dict:
    start_main = perf_counter()

    warehouse = Warehouse()
    trucks = ParcelsExport()

    start_import_parcels = perf_counter()
    parcels_dict = ParcelsImport.import_json()
    parcels_list = ParcelsImport.create_parcels_list(parcels_dict)
    end_import_parcels = perf_counter()

    start_import_trucks = perf_counter()
    trucks_dict = ParcelsExport.import_json()
    trucks.insert_trucks(trucks_dict)
    end_import_trucks = perf_counter()

    start_warehouse = perf_counter()
    warehouse.add_parcels_list(parcels_list)
    warehouse.export_parcels(export=trucks)
    end_warehouse = perf_counter()

    end_main = perf_counter()
    return {
        'main_time': end_main-start_main,
        'warehouse_time': end_warehouse-start_warehouse,
        'trucks_import_time': end_import_trucks-start_import_trucks,
        'parcels_import_time': end_import_parcels-start_import_parcels,
        'parcels_send': warehouse.parcels_send,
        'trucks_send': warehouse.trucks_send
    }


if __name__ == '__main__':
    e = run()
