import inventario


def add_product(product_name):
    """
    Agrega producto a la lista inventario.

    Verifica si ya existe, si es asi muestra un mensaje indicandolo
    Si no, existe solicita el precio y la cantidad por consola al usuario.

    Parametro:
        product_name (str): Nombre del producto.

    Retorna:
        None
    """

    for product in inventario.inventory:

        if product["nombre"] == product_name:

            print("\nEste producto ya  existe\n")
            return

    while True:

        try:

            price = float(input("\nIngrese el precio del producto: "))

            quantity = int(input("\nIngrese la cantidad del producto: "))

        except ValueError:
            print("\nPor favor ingrese solo valores numericos\n")
            continue

        if price < 0 or quantity < 0:
            print("\nPor favor ingrese valores numericos positivos\n")
            continue
        break

    total_cost = price * quantity

    print(
        f"\nProducto: {product_name} | Precio: {price} | Cantidad: {quantity} | Total: {total_cost}\n"
    )

    product = {
        "nombre": product_name,
        "precio": price,
        "cantidad": quantity,
    }

    inventario.inventory.append(product)


def show_inventory():
    """
    Muestra el inventario completo.

    Si el inventario esta vacio, muestra un mensaje indicandolo.

    Retorna:
        None
    """

    if not inventario.inventory:
        print("\nInventario vacio!!\n")

    else:

        for product in inventario.inventory:

            print(
                f"\nProducto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}\n"
            )


def search_inventory(product_name):
    """
    Busca el producto en el inventario.

    Si el producto no existe, muestra un mensaje indicandolo

    Parametro:
        product_name (str): Nombre del producto.

    Retorna:
        dict: Producto encontrado.
        None: Si el producto no existe.
    """

    for product in inventario.inventory:

        if product["nombre"] == product_name:
            return product
    else:
        return None


def update_inventory(product_name):
    """
    Actualiza el producto en el inventario.

    Si el producto no existe, mmuestra un mensaje indicandolo,
    Si existe solicita el precio y la cantidad por consola al usuario.

    Parametro:
        product_name (str): Nombre del producto.

    Retorna:
        None
    """

    for product in inventario.inventory:

        if product["nombre"] == product_name:

            while True:

                try:

                    new_price = float(input("\nIngrese el precio del producto: "))

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

            print("\nProducto actualizado correctamente\n")
            return

    else:
        print("\nProducto no encontrado\n")


def delete_inventory(product_name):
    """
    Elimina el producto en el inventario.

    Si el producto no existe, muestra un mensaje indicandolo

    Parametro:
        product_name (str): Nombre del producto.

    Retorna:
        None
    """

    for product in inventario.inventory:

        if product["nombre"] == product_name:

            inventario.inventory.remove(product)

            print("\nProducto eliminado correctamente\n")
            return

    else:
        print("\nProducto no encontrado\n")


def calculate_statistics():
    """
    Calcula las estadisticas del inventario.

    Si el inventario esta vacio, muestra un mensaje indicandolo,
    Si no esta vacio calcula el valor total del inventario y la cantidad total de productos.

    Retorna:
        None
    """

    total_inventory_value = 0

    total_quantity_registered_products = 0

    if not inventario.inventory:
        print("\nInventario vacio, no se pueden calcular estadisticas\n")
        return

    else:
        for product in inventario.inventory:

            total_inventory_value += product["precio"] * product["cantidad"]

            total_quantity_registered_products += product["cantidad"]

    print(f"\nEl valor total del inventario es: {total_inventory_value}")

    print(
        f"\nLa cantidad total de productos registrados es: {total_quantity_registered_products}\n"
    )


def save_csv():
    return


def load_csv():
    return
