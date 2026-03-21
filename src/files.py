import csv

def save_csv(inventory, ruta = "data/inventory.csv", incluir_header = True):

    """
    Guarda el inventario en un archivo CSV, si el inventario está vacío no se crea el archivo, 
    si el archivo ya existe se sobrescribe.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.

        ruta: Ruta del archivo CSV donde se guardarán los datos, por defecto "data/inventory.csv".

        incluir_header: Booleano que indica si se deben escribir los encabezados en el archivo CSV. 
            Por defecto True.

    Returns:
        None
    """

    if not inventory:
        print("\nInventario vacio, no se puede guardar el archivo\n")
        return

    else:

        try:

            with open(ruta, "w", newline="", encoding="utf-8") as file:

                fieldnames = ["nombre", "precio", "cantidad"]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                if incluir_header:
                    writer.writeheader()

                writer.writerows(inventory)

                print(f"\nInventario guardado en: {ruta}\n")
                
        except PermissionError:
            print("\nError no tienes permisos de escritura para este archivo\n")


def load_csv(inventory, ruta = "data/inventory.csv"):
    
    """
    Carga datos desde un archivo CSV y los agrega al inventario.

    Args:
        inventario (list[dict]): Lista donde se almacenarán los productos cargados.
        ruta (str, opcional): Ruta del archivo CSV a leer.
            Por defecto "data/inventory.csv".

    Returns:
    """

    try:

        with open(ruta, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                product = {
                "nombre": row["nombre"],
                "precio": float(row["precio"]),
                "cantidad": int(row["cantidad"]),
                }

                inventory.append(product)

            print(f"\nInventario cargado desde: {ruta}\n")

    except FileNotFoundError:
        print("\nError no se puede cargar debido a que el archivo no existe\n")

    except PermissionError:
        print("\nError no tienes permisos para escribir en esa ubicación\n")

    except UnicodeDecodeError:
        print("\nError problema de codificación al cargar el archivo\n")
