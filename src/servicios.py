import inventario

# Funcion para agregar productos
def add_product(product_name, price, quantity):

    for product in inventario.inventory:

        if product["nombre"] == product_name:

            print("\nEste producto ya  existe\n")
        return
            
    # Calculo del costo total, se obtiene multiplicando precio por cantidad
    total_cost = price * quantity

    # Se imprime el nombre, precio, cantidad y el total del producto y se muestra por consola
    print(
        f"\nProducto: {product_name} | Precio: {price} | Cantidad: {quantity} | Total: {total_cost}\n"
    )

    # Se crea el diccionario de los productos para ser alamacenados
    product = {
        "nombre": product_name,
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
            print(f"\nProducto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}\n")

def search_inventory(product_name):

    for product in inventario.inventory:

        if product["nombre"] == product_name:
            return product
    else:
        return None

def update_inventory(product_name):

    for product in inventario.inventory:

        if product["nombre"] == product_name:

            while True:

                try:
                    # Solicitar dato al usuario
                    new_price = float(input("\nIngrese el precio del producto: "))

                    # Solicitar dato al usuario
                    new_quantity = int(input("\nIngrese la cantidad del producto: "))

                except ValueError:
                    print("\nPor favor ingrese solo valores numericos\n")
                    continue

                if new_price < 0 or new_quantity < 0:
                    print("\nPor favor ingrese valores numericos positivos\n")
                    continue
                break

            product["precio"] = new_price
            product["cantidad"] = new_quantity

    else:
        return print("\nProducto no encontrado\n")


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

    print(f"\nLa cantidad total de productos registrados es: {total_quantity_registered_products}\n")

def save_csv():
    return

def load_csv():
    return
