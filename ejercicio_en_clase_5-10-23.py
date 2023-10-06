'''Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.'''
#Ejercicio numero 1
sliding = int(input("Ingrese un número para comenzar a encriptar su mensaje: ")) #sliding = corrimiento
print(sliding)
list_message = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result_message = 0
for _ in range(5):
    chain = ""
    message = input("Ingrese una palabra para encriptar: ").lower()
    for i in message:
        if i in abc:
            result_message = (abc.index(i) + sliding) % 27
            chain += abc[result_message]
        else:
            chain += i
    list_message.append(chain.upper())
print(list_message)

#Ejercicio numero 2
'''Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.'''
number = 1
count_pair = 0
count_odd = 0

while number > 0:
    number = int(input("ingrese un numero entero positivo, si desea salir ingrese 0: "))
    number_str= str(number)
    for i in number_str: 
        dig = int(i)
        print(dig)
        if dig%2 == 0:
            count_pair+=1
        else:
            count_odd+=1
print("numeros impares: ", count_odd)
print("numeros pares: ", count_pair)