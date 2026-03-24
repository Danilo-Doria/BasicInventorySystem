import csv

def save_csv(inventory, path = "data/inventory.csv", incluir_header = True):

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

    try:

        with open(path, "w", newline="", encoding="utf-8") as file:

            fieldnames = ["nombre", "precio", "cantidad"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if incluir_header:
                writer.writeheader()

            writer.writerows(inventory)

            print(f"\nInventario guardado en: {path}\n")
            
    except PermissionError:
        print("\nError no tienes permisos de escritura para este archivo\n")


def load_csv(inventory, path = "data/inventory.csv"):
    
    """
    Carga datos desde un archivo CSV y los agrega al inventario.

    Args:
        inventario (list[dict]): Lista donde se almacenarán los productos cargados.
        ruta (str, opcional): Ruta del archivo CSV a leer.
            Por defecto "data/inventory.csv".

    Returns:
    """

    try:

        with open(path, "r", newline="", encoding="utf-8") as file:

            header = ["nombre", "precio", "cantidad"]

            error = 0

            reader = csv.DictReader(file)

            if reader.fieldnames != header:
                print("\nEncabezados invalidos se espera: 'nombre', 'precio' y 'cantidad'\n")
                return

            for row in reader:

                try:
                    price = float(row["precio"])

                    if price < 0:
                        print(f"\nPrecio negativo en la fila: {row}\n")
                        error += 1
                        continue
                    
                except ValueError:
                    print(f"\nPrecio inválido (no numérico) en la fila: {row}\n")
                    error += 1
                    continue

                try:
                    quantity = int(row["cantidad"])

                    if quantity < 0:
                        print(f"\nCantidad negativa en la fila: {row}\n")
                        error += 1
                        continue
                    
                except ValueError:
                    print(f"\nCantidad no numérica en la fila: {row}\n")
                    error += 1
                    continue

                product = {
                "nombre": row["nombre"],
                "precio": price,
                "cantidad": quantity
                }

                inventory.append(product)

            print(f"\nInventario cargado desde: {path}\n")

            if error > 0:
                print(f"{error} filas inválidas omitidas.\n")
            else:
                print("No se encontraron filas inválidas.\n")

    except FileNotFoundError:
        print("\nError no se puede cargar debido a que el archivo no existe\n")

    except PermissionError:
        print("\nError no tienes permisos para escribir en esa ubicación\n")

    except UnicodeDecodeError:
        print("\nError problema de codificación al cargar el archivo\n")