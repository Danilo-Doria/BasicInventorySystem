# Solicitar dato al usuario
name = input("Ingrese el nombre del producto ")

# Este while repite la pregunta al usuario siempre que ingrese un valor incorrecto
while True:

    # Este try lo que hace es atrapar lo que el usuario ingresa y si el tipo de variable no es la correcta
    # entonces pasa al except mostrando el mensaje de error y el ciclo se repite, ya que nunca hubo break

    try:
        # Solicitar dato al usuario
        price = float(input("Ingrese el precio del producto "))
        # Solicitar dato al usuario
        if price < 0:
            print("Por favor ingrese valores numericos positivos")
            continue
        break
    except ValueError:
        print("Por favor ingrese solo valores numericos")

while True:

    try:
        # Solicitar dato al usuario
        quantity = int(input("Ingrese el la cantidad del prodcuto "))
        if quantity < 0:
            print("Por favor ingrese valores numericos positivos")
            continue
        break
    except ValueError:
        print("Por favor ingrese solo valores numericos")

# Calculo del costo total, se obtiene multiplicando precio por cantidad
costo_total = price * quantity

# Se imprime el nombre, precio, cantidad y el total del producto y se muestra por consola
print(
    f"Producto: {name} | Precio: {price} | Cantidad: {quantity} | Total: {costo_total}"
)

# Este programa lo que hace basicamente es pedir por consola al usuario el nombre del producto, precio, y la cantidad
# usando While True y try except validamos que lo que ingrese el usuario sea correcto, evitando asi errores
# luego se calcula el costo total y se imprime por consola lo que el usuario ingresó junto con el total.