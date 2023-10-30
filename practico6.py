'''1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista.
Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.'''
'''2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.'''
'''3.	Imprimir la sumatoria de todos los números de la lista.'''
'''4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original,
que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.'''
# list_numbers = []

# while True:
#     numbers = int(input("Ingrese un numero. Para finalizar ingrese el numero 0. --> "))
#     if numbers == 0:
#         break
#     else:
#         list_numbers.append(numbers) #funcion append para integrar los numeros ingresados a la lista vacia

# print(f"Los numeros ingresados son: {list_numbers}")
# other_number = int(input("Ingrese un numero para removerlo de la lista: "))

# if other_number in list_numbers:
#     list_numbers.remove(other_number) #funcion remove para remover el numero en caso de encontrarlo en la lista
#     print(f"El numero {other_number} ha sido removido de la lista.")
#     print(f"Su nueva lista es: {list_numbers}")
# else:
#     print(f"El numero ingresado {other_number} no se encuentra en la lista.")
#     print(f"Su lista no ha sido modificiada: {list_numbers}")

# summation = sum(list_numbers) #funcion que suma los elementos en una secuancia, como una lista o tupla

# print(f"La sumatoria de los numeros ingresados es: {summation}")

# number2 = int(input("Ingrese un nuevo numero el cual se convertire en el nuevo numero mayor de la lista: "))

# # Elimina elementos de list_numbers que son mayores que number2
# list_numbers = [x for x in list_numbers if x < number2]

# list_numbers.append(number2)

# print(f"La nueva lista de numeros es: {list_numbers}")

