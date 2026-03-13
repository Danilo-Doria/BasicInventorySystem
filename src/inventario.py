# Crear una variable inventario y asignarle una lista vacia
inventory = []

# Funcion para gregar productos
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
        if inventory == []:
            print("\nInventario vacio!!\n")

        else:

            # Usamos for para iterar cada producto en la lista inventario
            for product in inventory:

                # Se imprime los valores del diccionario llamando las claves
                print(
                    f"\nProducto: {product['nombre']} | Precio: {product['precio']} | Cantidad: {product['cantidad']}\n"
                )

# Funcion paracalcular las estadisticas
def calculate_statistics():
        
    # Agregamos la variable valor total de inventario, la cual sera un acumulador

        total_inventory_value = 0

        for product in inventory:

            # Se multiplica el precio por la cantidad y el resultado se suma a la variable de valor total de inventario
            total_inventory_value += product["precio"] * product["cantidad"]

        print(f"\nEl valor total del inventario es: {total_inventory_value}\n")


print("\nBienvenido al sistema de inventarios\n")

# Este while repite indefinidamente las opciones hasta que el usuario decida salir
while True:
    
    # Este try lo que hace es atrapar lo que el usuario ingresa y si el tipo de variable no es la correcta
    # entonces pasa al except mostrando el mensaje de error y el ciclo se repite, ya que nunca hubo break
    try:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("0. Salir")

        # La variable option recibe la opcion que desea el usuario
        option = int(input("\nIngresa una opcion: "))

        # Si option no se encuatra en las opciones descritas, imprime un mensaje de error y entra continue omitiendo la iteraccion reiniciando el ciclo
        if option not in (0, 1, 2, 3):
            print("\nOpción inválida\n")
            continue

    except ValueError:
        print("\nPor favor solo digite valores numericos\n")
        continue

    if option == 1:
        add_product()        

    elif option == 2:
        show_inventory()

    elif option == 3:
         calculate_statistics()

    # Si el usuario ingresa el valor 0 el programa finaliza
    else:
        print("\nAdios")
        break

# Este programa gestiona los productos en el inventario usando un menu interactivo
# usando While True y try except se valida en cada input que el usuario ingrese los datos correctos
# Se usa el ciclo for para recorrer los diccionarios en la lista de inventario, logrando asi observar el inventario y obtener las estadisticas.