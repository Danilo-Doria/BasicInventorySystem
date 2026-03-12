inventory = []
print("\nBienvenido al sistema de inventarios\n")

while True:
    try:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        option = int(input("\nIngresa una opcion: "))

        if option not in (1, 2, 3, 4):
            print("\nOpción inválida\n")
            continue

    except ValueError:
        print("\nPor favor solo digite valores numericos\n")
        continue

    if option == 1:

        # Solicitar dato al usuario
        name = input("Ingrese el nombre del producto: ")

        # Este while repite la pregunta al usuario siempre que ingrese un valor incorrecto
        while True:

            # Este try lo que hace es atrapar lo que el usuario ingresa y si el tipo de variable no es la correcta
            # entonces pasa al except mostrando el mensaje de error y el ciclo se repite, ya que nunca hubo break

            try:
                # Solicitar dato al usuario
                price = float(input("Ingrese el precio del producto: "))
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
                quantity = int(input("Ingrese el la cantidad del producto: "))
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

        product = {
            "nombre": name,
            "precio": price,
            "cantidad": quantity,
        }

        inventory.append(product)

    elif option == 2:

        if inventory == []:
            print("\nInventario vacio!!\n")

        else:

            for product in inventory:
                print(
                    f"\nProducto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}\n"
                )

    elif option == 3:
        total_inventory_value = 0

        for product in inventory:
            total_inventory_value += product["precio"] * product["cantidad"]

        print(f"\nEl valor total del inventario es: {total_inventory_value}\n")

    else:
        print("\nAdios")
        break
