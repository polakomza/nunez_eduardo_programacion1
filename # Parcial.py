# Parcial 1 Programacion
''' Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros 
(condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.

Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y 
mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!'''

name = input("Ingrese su nombre por favor: ").lower()
print(f"Hola, {name.capitalize()}! Tengo dos juegos disponibles.")

menu = int(input("Presione '1' para el Juego de numeros o '2' para el Juego de palabras: "))
# Variables a utilizar en el programa
max_even = 0
count_odds = 0
sum_odds = 0
vocals = ['a', 'e', 'i', 'o', 'u']
count_vocals_a = 0
count_vocals_e = 0
count_vocals_i = 0
count_vocals_o = 0
count_vocals_u = 0
total_vocals = count_vocals_a + count_vocals_e + count_vocals_i + count_vocals_o + count_vocals_u

# Hago una validacion para que ingrese un numero correcto del menu
while menu != 1 and menu != 2:
    print(f"{name.capitalize()} El numero ingresado no corresponde a un juego disponible. Vuelve a intentarlo por favor: ")
    menu = int(input(" --> "))


if menu == 1:
    while True:
        number = int(input(f"Genial {name.capitalize()}, Ingresa un numero entero mayor a '0'. Si deseas dejar de jugar, ingresa '0': "))
        if number == 0: # Si el numero ingresado es 0 se termina el programa.
            break
        elif number % 2 == 0: # Si el numero es par, se asigna a una variable
            max_even = number
        elif number % 2 == 1: # Si el numero es impar, se suma a una variable que almacena la cantidad de numeros 
            count_odds += 1 # impares (count_odds) y el valor de ese numero impar (sum_odds)
            sum_odds += number
    if count_odds > 0: 
        average = sum_odds / count_odds
        print("El promedio de los numeros impares ingresados es:", average)
    else:
        print("No se ingresaron numeros impares.")
    if max_even:
        print("El numero par mas grande ingresado es:", max_even)
    else:
        print("No se ingresaron números pares.")

# Juego de palabras, en un bucle for valido si el iterador es una vocal y lo sumo a una variable para luego mostrarla
if menu == 2: # A diferencia del juego de numeros, este se ejecuta una sola vez.
        phrase = input(f"Genial {name.capitalize()}. Ingresa una frase para conocer su cantidad de vocales: " )
        for i in phrase:
            if i == vocals[0]:
                count_vocals_a += 1
            elif i == vocals[1]:
                count_vocals_e += 1
            elif i == vocals[2]:
                count_vocals_i += 1
            elif i == vocals[3]:
                count_vocals_o += 1
            elif i == vocals[4]:
                count_vocals_u += 1
                print(f"{name.capitalize()}, Tu frase contiene {count_vocals_a} 'a', {count_vocals_e} 'e', {count_vocals_i} 'i', {count_vocals_o} 'o', y {count_vocals_u} 'u'.")
            else: 
                total_vocals == 0
                print(f"{name.capitalize()}, tu frase no contiene vocales.. que frase rara!!")
                break