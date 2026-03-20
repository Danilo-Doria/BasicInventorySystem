import csv

def save_csv(inventario, ruta = "Inventory.csv", incluir_header = True):

    if not inventario:
        print("\nInventario vacio, no se puede guardar el archivo\n")
        return

    else:

        try:

            with open(ruta, "w", newline="", encoding="utf-8") as file:

                fieldnames = ["nombre", "precio", "cantidad"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                if incluir_header:
                    writer.writeheader()

                writer.writerows(inventario)

                print(f"\nInventario guardado en: {ruta}\n")
                
        except PermissionError:
            print("\nError no tienes permisos de escritura para este archivo\n")
