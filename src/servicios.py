import inventario

# Funcion para agregar productos
def add_product(name, price, quantity):

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
    inventario.inventory.append(product)


# Funcion para mostrar el inventario
def show_inventory():

    # Si el inventario esta vacio, imprime un mensaje que lo indique
    if not inventario.inventory:
        print("\nInventario vacio!!\n")

    else:

        # Usamos for para iterar cada producto en la lista inventario
        for product in inventario.inventory:

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

    if not inventario.inventory:
        print("\nInventario vacio, no se pueden calcular estadisticas\n")
        return

    else:
        for product in inventario.inventory:

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
