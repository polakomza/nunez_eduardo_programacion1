import funciones
'''1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''

# dni = input("Ingrese su numero de DNI sin los puntos.: ")

# if funciones.validation(dni) == True:
#     print("Su numero de DNI es valido")
# else:
#     print("Numero de DNI invalido")

'''2.	Escribir una función que, dado un string, retorne la longitud de la última palabra.
Se considera que las palabras están separadas por uno o más espacios.
También podría haber espacios al principio o al final del string pasado por parámetro.'''

# word = input("Ingrese una oracion para conocer la longitud de su ultima palabra\n ---> ").strip().capitalize()
# last_word_quantity = funciones.strings(word)
# print(f"La ultima palabra de su oracion tiene {last_word_quantity} letras")

'''3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los 
socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que 
finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre,
en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar
al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre,
la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254
'''

# while True:
#     partner = input("Ingrese nombres y apellido del socio/a (o deje en blanco para salir): ").strip().capitalize()
    
#     # Verifica si el usuario ingresó un nombre vacío para salir del bucle
#     if partner == "":
#         print("Saliendo del programa.")
#         break
    
#     names = funciones.complete_name(partner)
    
#     while names == "Nombre no válido":
#         partner = input("Nombre no válido. Ingrese nombres y apellido del socio/a: ").strip().capitalize()
#         names = funciones.complete_name(partner)
    
#     dni = input("Ingrese el DNI del/a socio/a: ")
#     dni1 = funciones.validation(dni)
    
#     while dni1 == False:
#         dni = input("El DNI ingresado no es válido. Ingrese nuevamente su DNI: ")
#         dni1 = funciones.validation(dni)
    
#     id_partner = funciones.identify(names, dni)
    
#     print(f"{names}. Su ID como socio/a es: {id_partner}")

'''7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.'''

# numbers = []
# while True:
#     entry = int(input("Ingrese un numero. Para dejar de ingresar, ingrese 0. --> "))
#     if entry == 0:
#         break
#     numbers.append(entry)

# result = funciones.max_min(numbers)

# print(f"El numero minimo y maximo ingresado son: {result}")