import servicios

print("\nBienvenido al sistema de inventarios\n")

# Este while repite indefinidamente las opciones hasta que el usuario decida salir
while True:

    # Este try lo que hace es atrapar lo que el usuario ingresa y si el tipo de variable no es la correcta
    # entonces pasa al except mostrando el mensaje de error y el ciclo se repite, ya que nunca hubo break
    try:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar en inventario")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Calcular estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        # La variable option recibe la opcion que desea el usuario
        option = int(input("\nIngresa una opcion: "))

        # Si option no se encuatra en las opciones descritas, imprime un mensaje de error y entra continue omitiendo la iteraccion reiniciando el ciclo
        if option not in range(1, 10):
            print("\nOpción inválida\n")
            continue

    except ValueError:
        print("\nPor favor solo digite valores numericos\n")
        continue

    if option == 1:
        servicios.add_product()

    elif option == 2:
        servicios.show_inventory()

    elif option == 3:
        servicios.search_inventory()

    elif option == 4:
        servicios.update_inventory

    elif option == 5:
        servicios.delete_inventory
    
    elif option == 6:
        servicios.calculate_statistics

    elif option == 7:
        servicios.save_csv()
    
    elif option == 8:
        servicios.load_csv()

    # Si el usuario ingresa el valor 0 el programa finaliza
    else:
        print("\nAdios")
        break

# Este programa gestiona los productos en el inventario usando un menu interactivo
# usando While True y try except se valida en cada input que el usuario ingrese los datos correctos
# Se usa el ciclo for para recorrer los diccionarios en la lista de inventario, logrando asi observar el inventario y obtener las estadisticas.
