'''1.	Escribe un programa que tome una lista de números como entrada y 
la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.'''
# def bubble_sort(list_numbers):
#     n = len(list_numbers)
#     # Recorre todos los elementos de la lista
#     for i in range(n):
        
#         # Últimos i elementos ya están en su lugar
#         for j in range(0, n - i - 1):
            
#             # Intercambia si el elemento encontrado es mayor que el siguiente elemento
#             if list_numbers[j] > list_numbers[j + 1]:
#                 list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]

# list_numbers = [56,89,65,23,4,5,67,25,48]
# bubble_sort(list_numbers)
# print("Lista ordenada de menor a mayor: ", end=" ")
# for i in range(len(list_numbers)):
#     print(list_numbers[i], end=" ")

'''2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden 
ascendente utilizando el método de ordenamiento de selección.'''

# def selection_sort(list_words):
#     n = len(list_words)

#     # Recorre todos los elementos de la lista
#     for i in range(n):
#         # Encuentra el mínimo elemento en el resto de la lista
#         min_index = i
#         for j in range(i + 1, n):
#             if list_words[j] < list_words[min_index]:
#                 min_index = j

#         # Intercambia el mínimo elemento encontrado con el elemento en la posición actual
#         list_words[i], list_words[min_index] = list_words[min_index], list_words[i]

# list_words = ["arbol","abuelo", "casa", "ejercicio", "puente", "ordenamiento", "seleccion"]
# selection_sort(list_words)

# print("Lista ordenada:",end=" ")
# for i in range(len(list_words)):
#     print(list_words[i],end=" ")

'''4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden
ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.'''
# list_sentences = []

# while True:
#     sentence = input("Ingrese una oración o deje en blanco para salir: ")
#     list_sentences.append(sentence)
#     if sentence == "":
#         break

# def insertion_sort_by_length(sentences):
#     n = len(sentences)

#     for i in range(1, n):
#         current_sentence = sentences[i]
#         current_length = len(current_sentence)

#         j = i - 1
#         # Desplaza las oraciones más largas hacia la derecha
#         while j >= 0 and len(sentences[j]) > current_length:
#             sentences[j + 1] = sentences[j]
#             j -= 1
#         # Inserta la oración actual en su posición correcta
#         sentences[j + 1] = current_sentence

# insertion_sort_by_length(list_sentences)

# print("Oraciones ordenadas por longitud (de menor a mayor):")
# for sentence in list_sentences:
#     print(sentence,end=" ")

'''5.	Modifica uno de los ejercicios anteriores
para ordenar la lista de números en orden descendente en lugar de ascendente.'''

# def bubble_sort(list_numbers):
#     n = len(list_numbers)
#     # Recorre todos los elementos de la lista
#     for i in range(n):
        
#         # Últimos i elementos ya están en su lugar
#         for j in range(0, n - i - 1):
            
#             # Intercambia si el elemento encontrado es mayor que el siguiente elemento
#             if list_numbers[j] < list_numbers[j + 1]: #Para este ejercicio solo debo de cambiar la comparacion.
#                 list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]

# list_numbers = [56,89,65,23,4,5,67,25,48]
# bubble_sort(list_numbers)
# print("Lista ordenada de mayor a menor: ", end=" ")
# for i in range(len(list_numbers)):
#     print(list_numbers[i], end=" ")