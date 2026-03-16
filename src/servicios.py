# Crear una variable inventario y asignarle una lista vacia
inventory = []

# Funcion para agregar productos
def add_product():

    # Solicitar dato al usuario
    name = input("\nIngrese el nombre del producto: ")

    # Este while repite la pregunta al usuario siempre que ingrese un valor incorrecto
    while True:

        try:
            # Solicitar dato al usuario
            price = float(input("\nIngrese el precio del producto: "))
            # Solicitar dato al usuario
            if price < 0:
                print("\nPor favor ingrese valores numericos positivos\n")
                continue
            break
        except ValueError:
            print("\nPor favor ingrese solo valores numericos\n")

    while True:

        try:
            # Solicitar dato al usuario
            quantity = int(input("\nIngrese el la cantidad del producto: "))
            if quantity < 0:
                print("\nPor favor ingrese valores numericos positivos\n")
                continue
            break
        except ValueError:
            print("\nPor favor ingrese solo valores numericos\n")

    # Calculo del costo total, se obtiene multiplicando precio por cantidad
    total_cost = price * quantity

    # Se imprime el nombre, precio, cantidad y el total del producto y se muestra por consola
    print(
        f"\nProducto: {name} | Precio: {price} | Cantidad: {quantity} | Total: {total_cost}\n"
    )

    # Se crea el diccionario de los productos para ser alamacenados
    product = {
        "nombre": name,
        "precio": price,
        "cantidad": quantity,
    }

    # Se agrega el diccionario al final de la lista de inventarios
    inventory.append(product)


# Funcion para mostrar el inventario
def show_inventory():

    # Si el inventario esta vacio, imprime un mensaje que lo indique
    if not inventory:
        print("\nInventario vacio!!\n")

    else:

        # Usamos for para iterar cada producto en la lista inventario
        for product in inventory:

            # Se imprime los valores del diccionario llamando las claves
            print(
                f"\nProducto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}\n"
            )

def search_inventory():
    return

def update_inventory():
    return

def delete_inventory():
    return

# Funcion paracalcular las estadisticas
def calculate_statistics():

    # Agregamos la variable valor total de inventario, la cual sera un acumulador
    total_inventory_value = 0

    # Agregamos la variable cantidad total de productos registrados, la cual sera un acumulador
    total_quantity_registered_products = 0

    if not inventory:
        print("\nInventario vacio, no se pueden calcular estadisticas\n")
        return

    else:
        for product in inventory:

            # Se multiplica el precio por la cantidad y el resultado se suma a la variable de valor total de inventario
            total_inventory_value += product["precio"] * product["cantidad"]

            # Se suma la cantidad de cada producto a la variable de cantidad total de productos registrados
            total_quantity_registered_products += product["cantidad"]

    print(f"\nEl valor total del inventario es: {total_inventory_value}")

    print(
        f"\nLa cantidad total de productos registrados es: {total_quantity_registered_products}\n"
    )

def save_csv():
    return

def load_csv():
    return
