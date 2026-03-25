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


def load_csv(path = "data/inventory.csv"):
    
    """
    Carga datos desde un archivo CSV y los agrega al inventario.

    Args:
        inventario (list[dict]): Lista donde se almacenarán los productos cargados.
        ruta (str, opcional): Ruta del archivo CSV a leer.
            Por defecto "data/inventory.csv".

    Returns:
    """

    new_inventory = []
    error = 0

    try:

        with open(path, "r", newline="", encoding="utf-8") as file:

            header = ["nombre", "precio", "cantidad"]
            reader = csv.DictReader(file)

            if reader.fieldnames != header:
                print("\nEncabezados invalidos se espera: 'nombre', 'precio' y 'cantidad'\n")
                return []
            
            print(f"\nInventario cargado desde: {path}\n")

            for row in reader:
                
                try:
                    price = float(row["precio"])
                    quantity = int(row["cantidad"])

                    if price < 0 or quantity < 0:
                        print(f"Valores negativos en la fila: {row}\n")
                        error += 1
                        continue

                except ValueError:
                    print(f"Valor no numérico en la fila: {row}\n")
                    error += 1
                    continue

                product = {
                "nombre": row["nombre"],
                "precio": price,
                "cantidad": quantity
                }

                new_inventory.append(product)

            if error > 0:
                print(f"{error} filas inválidas omitidas.\n")
            else:
                print("No se encontraron filas inválidas.\n")

            return new_inventory

    except FileNotFoundError:
        print("\nError no se puede cargar debido a que el archivo no existe\n")

    except PermissionError:
        print("\nError no tienes permisos para escribir en esa ubicación\n")

    except UnicodeDecodeError:
        print("\nError problema de codificación al cargar el archivo\n")


def load_option(inventory, new_data):
    
    if not new_data:
        print("El inventario actual esta vacío\n")
        return
    
    option = input("\n¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    
    while option not in ["S", "N"]:
        
        option = input("\nOpción inválida. Por favor ingrese 'S' para sobrescribir o 'N' para mantener el inventario actual: ").strip().upper()
        
    if option == "S":
        inventory.clear()
        inventory.extend(new_data)
        print("\nInventario sobrescrito exitosamente\n")
    else:
        pass