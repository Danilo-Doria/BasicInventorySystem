import csv

def save_csv(inventory, path="data/inventory.csv", incluir_header=True):
    """
    Guarda el inventario en un archivo CSV, si el inventario está vacío no se crea el archivo,
    si el archivo ya existe se sobrescribe.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto (En memoria).
        ruta: Ruta del archivo CSV donde se guardarán los datos, por defecto "data/inventory.csv".
        incluir_header: Booleano que indica si se deben escribir los encabezados en el archivo CSV, Por defecto True.

    Retorna:
        None: Si el inventario se guardo exitosamente.
        None: Si se genero un error al guardar el archivo.
    """

    try:
        with open(path, "w", newline="", encoding="utf-8") as file:

            fieldnames = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if incluir_header:
                writer.writeheader()
            writer.writerows(inventory)
            print(f"\nInventario guardado en: {path}")
            return None
    except PermissionError:
        print("\nError no tienes permisos de escritura para este archivo")
        return None


def load_csv(path="data/inventory.csv"):
    """
    Carga datos desde un archivo CSV y los agrega al inventario.

    Parametros:
        Ruta del archivo CSV a leer, Por defecto "data/inventory.csv".

    Retorna: lista vacia si no se pueden cargar los datos.
    """

    # Nueva lista para almacenar los productos cargados desde el archivo CSV.
    new_inventory = []
    # Variable para contar el numero de filas invalidas encontradas durante la carga del archivo CSV.
    error = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:

            header = ["nombre", "precio", "cantidad"]
            reader = csv.DictReader(file)

            if reader.fieldnames != header:
                print("\nEncabezados invalidos se espera: 'nombre', 'precio' y 'cantidad'")
                return []

            print(f"\nInventario cargado desde: {path}")

            for row in reader:
                if len(row) != 3 or None in row.values():
                    print(f"\nFila inválida, cantidad de columnas incorrectas: {row}")
                    error += 1
                    continue
                try:
                    price = float(row["precio"])
                    quantity = int(row["cantidad"])

                    if price < 0 or quantity < 0:
                        print(f"\nFila inválida,valores negativos en la fila: {row}")
                        error += 1
                        continue
                except ValueError:
                    print(f"\nFila inválida, valor no numérico en la fila: {row}")
                    error += 1
                    continue

                product = {
                    "nombre": row["nombre"],
                    "precio": price,
                    "cantidad": quantity,
                }

                new_inventory.append(product)
            
            if new_inventory:
                if error > 0:
                    print(f"\n{error} filas inválidas omitidas")
                    print("\nInventario cargado exitosamente")
                else:
                    print("\nNo se encontraron filas inválidas")
                    print("\nInventario cargado exitosamente")
            return new_inventory

    except FileNotFoundError:
        print("\nError no se puede cargar debido a que el archivo no existe")
        return []

    except PermissionError:
        print("\nError no tienes permisos para escribir en esa ubicación")
        return []

    except UnicodeDecodeError:
        print("\nError problema de codificación al cargar el archivo")
        return []


def load_option(inventory, new_data):
    """
    Gestiona la carga de los datos si ya hay productos en memoria, si hay entonces pregunta
    al usuario si los quiere sobreescribir o fusionar.

    Sobreescribir: Borra el inventario en memoria y carga el que se encuantra en CSV.
    Fusionar: Si hay productos iguales suma sus cantidades y actualiza el precio al que se encuentra en el CSV.

    Parametros:
        inventory (list[dict]): Lista donde se almacenarán los productos cargados (En memoria).
        new_data (list[dict]): Lista donde se almacenarán los productos cargados (En archivo CSV).

    Retorna: 
        None: Si el inventario (new_data) esta vacio.
        None: Si el inventario se sobrescribió exitosamente.
        None: Si el inventario se fusionó exitosamente.
    """

    if not new_data:
        print("\nNo se cargaron productos debido a que el inventario está vacío")
        return None
    
    if inventory:
        print("\nPolitica de inventarios para la opcion de fusion (N): Si un producto ya existe, \n"
            "se suman sus cantidades y se actualiza el precio al del archivo CSV, si no solo se agregan los productos nuevos.")

        option = (input("\n¿Sobrescribir inventario actual(S) o fusionar (N)? (S/N): ").strip().upper())

        while option not in ["S", "N"]:

            option = (input("\nOpción inválida. Por favor ingrese 'S' para sobrescribir o 'N' para mantener el inventario actual: ").strip().upper())

        if option == "S":
            inventory.clear()
            inventory.extend(new_data)
            print("\nInventario sobreescrito exitosamente")
            return None
        else:
            for new_product in new_data:
                for old_product in inventory:
                    if (old_product["nombre"].strip().lower() == new_product["nombre"].strip().lower()):
                        old_product["precio"] = new_product["precio"]
                        old_product["cantidad"] += new_product["cantidad"]
                        break
                else:
                    inventory.append(new_product)
            print("\nInventario fusionado exitosamente")
            return None
    else:
        inventory.extend(new_data)
        return None
