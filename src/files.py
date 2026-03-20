import csv

def save_csv(inventario, ruta="Inventory.csv", incluir_header=True):

    if not inventario:
        print("\nInventario vacio, no se puede guardar el archivo\n")
    else:
        with open(ruta, "w", newline="", encoding="utf-8") as file:

            fieldnames = list(inventario[0].keys())

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(inventario)
