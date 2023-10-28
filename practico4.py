'''1 - Create a while loop with the following characteristics:
• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes:'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 
'The execution of the loop was broken when x was ' + x. '''
# x = 0
# while x <= 30:
#     x += 1
#     if x == 4 or x == 6 or x == 10:
#         print(f"El valor {x} de 'x' ha sido saltado.")
#     else:
#         print(x)
#     if x == 14: #Hago que la variable x termine en 14 asi no se imprime el numero 15
#         break
# print(f"La ejecucion del bucle ha finalizado cuando 'x' valia {x+1}") 

'''2- Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas.
Deje una línea en blanco para indicar que ha finalizado la entrada de líneas'''

# sentences_in_mayus = []

# while True:
#     sentence = input("Ingrese una secuencia de lineas (o deje en blanco para finalizar): ").upper()
    
#     if sentence == "":
#         break
    
#     sentences_in_mayus.append(sentence) #Guardo las lineas ingresadas en una variable que luego meto en la lista

# print("Lineas en mayúsculas: ")
# for sentence in sentences_in_mayus: #Itero sobre la lista para imprimir cada linea ingresada
#     print(sentence)

'''3- Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos
'''

# print("Bienvenido a su cuenta bancaria. ¿Qué operación desea realizar el día de hoy?")
# print("Para depositar dinero, ingrese D y el monto a depositar.\nPor ejemplo: D 500\nPara retirar, ingrese R y el monto a retirar.\nPor ejemplo: R 1000")
# print("Para dejar de operar presione la tecla 'ENTER' dejando el espacio en blanco.")
# balance = 0

# while True:
#     operation = input().upper()
#     if operation:
#         letter, amount = operation.split()
#         amount = int(amount)
#         if letter == 'D':
#             balance += amount
#         elif letter == 'R':
#             if (balance - amount) < 0:
#                 print("Saldo insuficiente. Vuelva a intentarlo o presione la tecla 'ENTER' dejando el espacio en blanco para salir.")
#             else:
#                 balance -= amount
#         else:
#             print("Operación no válida.")
#     else:
#         break
# print("Muchas gracias por utilizar nuestro banco.")
# print(f"Su saldo actual es: {balance}$")

'''3- Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores
que 1,finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos 
divisores distintos: él mismo y el 1.'''

# prime_number = 0

# while True:
#     print("Ingrese un numero mayor a 1. Para dejar de ingresar numeros ingrese el 0.")
#     number = int(input("--> "))
#     if number == 0:
#         break
#     divisor = 0
#     for i in range(2, number):
#         if number % i == 0:
#             divisor += 1
#     if divisor == 0:
#         prime_number += 1

# print(f"Usted ha ingresado {prime_number} numero/s primos.")

'''4- Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango,
que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
excepto que también sea divisible por 400.'''

# leap_year = 0
# # Bucle validando que el segundo año sea mayor al primero. El primero puede ser negativo (año A.C)
# while leap_year == 0:
#     first_year = int(input("Ingrese un año, Ejemplo: 1650\n--> "))
#     second_year = int(input("Ingrese un año mayor al anterior, Ejemplo: 2023\n--> "))
#     if first_year < 0 or second_year < first_year:
#         print("Los años ingresados son incorrectos. Por favor ingrese numeros validos.")
#         first_year = int(input("Ingrese nuevamente el primer año: "))
#         second_year = int(input("Ingrese nuevamente el segundo año: "))

# # Bucle que valida los años entre el primero ingresado y el segundo y cuenta los bisiestos
#     for i in range(first_year, second_year + 1):
#         if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#             leap_year += 1

# print(f"Entre el año {first_year} y el año {second_year} hay {leap_year} años bisiestos.")

'''5- Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
Utiliza la declaración continue para omitir los números impares.'''
# number = 20
# even = 0
# for i in range(1, number +1):
#     if i % 2 == 0:
#         even += 1
#     else:
#         continue
#     print(f"Numero par {i}")

'''6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico.
Cuando encuentres el número, usa break para salir del bucle.'''

# number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# number = int(input("Ingrese un numero del 1 al 20 para encontrarlo en la lista: "))

# for i in number_list:
#     print(f"Numero {i}")
#     if i == number:
#         print(f"Encontro su numero en la posicion {i}")
#         break
#     else:
#         continue

'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0",
utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).'''

# menu = int(input("Seleccione entre la opcion '1' , '2' o '3'. Si desea salir ingrese '0' --> "))

# while menu != 0:
#     if menu < 0 or menu > 3:
#         print("Esa opcion no esta en el menu.")
#         menu = int(input("Seleccione entre la opcion '1' , '2' o '3'. Si desea salir ingrese '0' --> "))
#     if menu == 1:
#         print("----------------------------------")
#         print("Usted eligio la opcion 1.")
#         print("----------------------------------")
#         menu = int(input("Seleccione entre la opcion '1' , '2' o '3'. Si desea salir ingrese '0' --> ")) 
#     elif menu == 2:
#         print("----------------------------------")
#         print("Usted eligio la opcion 2.")
#         print("----------------------------------")
#         menu = int(input("Seleccione entre la opcion '1' , '2' o '3'. Si desea salir ingrese '0' --> "))
#     elif menu == 3:
#         print("----------------------------------")
#         print("Usted eligio la opcion 3.")
#         print("----------------------------------")
#         menu = int(input("Seleccione entre la opcion '1' , '2' o '3'. Si desea salir ingrese '0' --> "))
#     elif menu == 0:
#         break

# print("Muchas gracias. Adios")
