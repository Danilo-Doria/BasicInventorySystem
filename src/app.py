def inventory_system_managment():
    import inventory
    import services
    import files

    print("\nBienvenido al sistema de inventarios")

    option = ""

    # While repite indefinidamente las opciones hasta que el usuario decida salir (9)
    while option != 9:

        # Este try captura el imput del usuario, si el tipo de variable no es la correcta
        # entonces pasa al except mostrando el mensaje de error y el ciclo se repite, ya que nunca hubo break
        try:
            print("\n1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Buscar en inventario")
            print("4. Actualizar")
            print("5. Eliminar")
            print("6. Calcular estadísticas")
            print("7. Guardar CSV")
            print("8. Cargar CSV (Asegurese de que el nombre del archivo sea 'inventory.csv')")
            print("9. Salir")

            # Variable option recibe la opcion que desea el usuario
            option = int(input("\nIngresa una opcion: "))

            # Si "option" no esta en el rango de las opciones descritas,
            # imprime un mensaje de error y entra continue omitiendo la iteraccion reiniciando el ciclo
            if option not in range(1, 10):
                print("\nOpción inválida")
                continue
        # Si 'option' no es un valor numericos, imprime un mensaje de error
        except ValueError:
            print("\nPor favor solo digite valores numericos")
            continue

        if option == 1:

            # Solicitar dato al usuario y guardarlo en la variable "product_name"
            product_name = input("\nIngrese el nombre del producto: ").strip().lower()

            # Se llama a la funcion de agregar productos
            services.add_product(inventory.inventory, product_name)

        elif option == 2:
            # Se llama a la funcion de mostrar inventario
            services.show_inventory(inventory.inventory)

        elif option == 3:
            # Solicitar el nombre del producto
            product_name = input("\nIngrese el nombre del producto: ").strip().lower()
            # Se llama a la funcion de buscar producto
            services.search_inventory(inventory.inventory, product_name)

        elif option == 4:

            # Solicitar el nombre del producto
            product_name = input("\nIngrese el nombre del producto: ").strip().lower()
            # Se llama a la funcion de actualizar producto
            services.update_inventory(inventory.inventory, product_name)

        elif option == 5:

            # Solicitar el nombre del producto
            product_name = input("\nIngrese el nombre del producto: ").strip().lower()
            # Se llama a la funcion de eliminar producto
            services.delete_inventory(inventory.inventory, product_name)

        elif option == 6:
            # Se llama a la funcion de calcular estadisticas
            services.calculate_statistics(inventory.inventory)

        elif option == 7:
            # Se llama a la funcion de guardar inventario en un archivo CSV
            files.save_csv(inventory.inventory)

        elif option == 8:
            # Se le asigna el inventario desde un archivo CSV a un variable 'new_data'
            new_data = files.load_csv()
            # Se llama a la funcion de cargar inventario desde un archivo CSV
            files.load_option(inventory.inventory, new_data)

        # Si el usuario ingresa el valor 9 el programa finaliza y rompe el ciclo
        else:
            print("\nAdios")


    # Este programa gestiona los productos en el inventario usando un menu interactivo
    # usando While True y try except se valida en cada input que el usuario ingrese los datos correctos
    # Se usa el ciclo for para recorrer los diccionarios en la lista de inventario, logrando asi observar el inventario y obtener las estadisticas.
