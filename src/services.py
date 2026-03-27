def add_product(inventory, product_name):
    """
    Agrega producto a la lista inventario.

    Verifica si ya existe, si es asi muestra un mensaje indicandolo
    Si no, existe solicita el precio y la cantidad por consola al usuario.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto..
        product_name (str): Nombre del producto.

    Retorna:
        None: Si el producto ya existe.
        None: Si el producto no existe, se agrega al inventario.
    """
    
    for product in inventory:
        if product["nombre"] == product_name:
            print("\nEste producto ya  existe\n")
            return None
        
    retry = False

    while not retry:
        try:
            price = float(input("\nIngrese el precio del producto: "))
            quantity = int(input("\nIngrese la cantidad del producto: "))

            if price < 0 or quantity < 0:
                print("\nPor favor ingrese valores numericos positivos")
            else:
                retry = True
        except ValueError:
            print("\nPor favor ingrese solo valores numericos")

    total_cost = price * quantity

    print(f"\nProducto: {product_name} | Precio: {price} | Cantidad: {quantity} | Total: {total_cost}")

    product = {
        "nombre": product_name,
        "precio": price,
        "cantidad": quantity,
    }

    inventory.append(product)
    return None


def show_inventory(inventory):
    """
    Muestra el inventario completo.

    Si el inventario esta vacio, muestra un mensaje indicandolo.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.

    Retorna:
        None: Si el inventario esta vacio.
        None: Muestra todos los productos en inventario.
    """

    if not inventory:
        print("\nInventario vacio!!")
        return None
    else:
        for product in inventory:
            print(f"\nProducto: {product["nombre"]} | Precio: {product["precio"]} | Cantidad: {product["cantidad"]}")
        return None


def search_inventory(inventory, product_name):
    """
    Busca el producto en el inventario.

    Si el producto no existe, muestra un mensaje indicandolo

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.
        product_name (str): Nombre del producto.

    Retorna:
        None: Si el producto es encontrado.
        None: Si el producto no es encontrado.

    """

    for product in inventory:
        if product["nombre"] == product_name:
            print(f"\nEl producto es: {product["nombre"]} | Precio: {product["precio"]} | Cantidad: {product["cantidad"]}")
            return None
    else:
        print("\nProducto no encontrado")
        return None


def update_inventory(inventory, product_name):
    """
    Actualiza el producto en el inventario.

    Si el producto no existe, mmuestra un mensaje indicandolo,
    Si existe solicita el precio y la cantidad por consola al usuario.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.
        product_name (str): Nombre del producto.

    Retorna:
        None: Si el producto es encontrado, actualice el precio y la cantidad.
        None: Si el producto no es encontrado.
    """

    for product in inventory:
        if product["nombre"] == product_name:

            retry = False

            while not retry:
                try:
                    new_price = float(input("\nIngrese el precio del producto: "))
                    new_quantity = int(input("\nIngrese la cantidad del producto: "))

                    if new_price < 0 or new_quantity < 0:
                        print("\nPor favor ingrese valores numericos positivos\n")
                    else:
                        retry = True
                except ValueError:
                    print("\nPor favor ingrese solo valores numericos\n")
                    
            product["precio"] = new_price
            product["cantidad"] = new_quantity

            print("\nProducto actualizado correctamente")
            return None
    else:
        print("\nProducto no encontrado")
        return None


def delete_inventory(inventory, product_name):
    """
    Elimina el producto en el inventario.

    Si el producto no existe, muestra un mensaje indicandolo

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.
        product_name (str): Nombre del producto.

    Retorna:
        None: Si el producto es encontrado, se elimina del inventario.
        None: Si el producto no es encontrado.
    """

    for product in inventory:
        if product["nombre"] == product_name:
            inventory.remove(product)
            print("\nProducto eliminado correctamente")
            return None
    else:
        print("\nProducto no encontrado")
        return None


def calculate_statistics(inventory):
    """
    Calcula las estadisticas del inventario.

    Si el inventario esta vacio, muestra un mensaje indicandolo,
    Si no esta vacio calcula el valor total del inventario, la cantidad total de productos
    El producto mas costoso y el producto con mayor stock.

    Parametros:
        inventory (list[dict]): Lista de diccionarios, donde cada diccionario es un producto.

    Retorna:
        None: Si el inventario esta vacio.
        None: Si el inventario no esta vacio, se muestran las estadisticas.
    """

    total_inventory_value = 0
    total_quantity_registered_products = 0

    most_expensive_product_name = ""
    product_name_with_the_most_stock = ""
    
    most_expensive_product = 0
    product_with_the_most_stock = 0
    

    if not inventory:
        print("\nInventario vacio, no se pueden calcular estadisticas")
        return None
    else:
        for product in inventory:
            total_inventory_value += product["precio"] * product["cantidad"]
            total_quantity_registered_products += product["cantidad"]

            if product["precio"] > most_expensive_product:
                most_expensive_product = product["precio"]
                most_expensive_product_name = product["nombre"]

            if product["cantidad"] > product_with_the_most_stock:
                product_with_the_most_stock = product["cantidad"]
                product_name_with_the_most_stock = product["nombre"]

    print(f"\nEl valor total del inventario es: {total_inventory_value}")
    print(f"\nLa cantidad total de productos registrados es: {total_quantity_registered_products}")
    print(f"\nEl producto mas costoso es: {most_expensive_product_name} con un precio de {most_expensive_product}")
    print(f"\nEl producto con mayor stock es: {product_name_with_the_most_stock} con una cantidad de {product_with_the_most_stock} en inventario")
    return None
