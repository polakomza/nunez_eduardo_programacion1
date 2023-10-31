import random
#Sumar digitos de un numero ingresado.
def sum_digit(number):
    summary=0
    while number>10:
        summary += number%10
        number//=10
    summary += number
    return summary

# Guiones bajos y muestra de letras
def choiced_word(word,phrase):
    characters = ""
    for i in word:
        if i in phrase:
            characters += i
        else:
            characters += "_"
    return characters

# validar DNI

def validation(dni):
    is_valid = True
    if len(dni) == 7 or len(dni) == 8:
        is_valid = True
    else:
        is_valid = False
    return is_valid

# longitud palabras
def strings(word):
    words = word.split()
    if len(words) > 0:
        last_words = words[-1]
    if last_words[-1] == ' ':
        last_words = last_words[-1 + 2]
    return len(last_words)

# dividir nombre y apellido del socio, dar bienvenida
def complete_name(partner):
    split_name = partner.split(' ')
    if len(split_name) == 3:
        name1 = split_name[0]
        name2 = split_name[1]
        surname = split_name[2]
        return f"Bienvenido/a {name1} {name2} {surname}" #Return en caso de que tenga 2 nombres
    elif len(split_name) == 2:
        name1 = split_name[0]
        surname = split_name[1]
        return f"Bienvenido/a {name1} {surname}" # Return en caso de que solo tenga 1 nombre y 1 apellido
    
    return "Nombre no válido" # Return en caso de que tenga mas de un apellido

#Identificador de socios
def identify(split_name, dni1):
    id_name = split_name.split()[1]
    id_dni = len(dni1)
    dni_split = dni1[0:3]
    id = f"{id_name}{id_dni}{dni_split}"
    return id

#Valor maximo y minimo de numeros en una lista
def max_min(numbers):
    bubble = len(numbers)
    for i in range(bubble):
        for j in range(0, bubble - i - 1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    min_max = (numbers[0], numbers[-1])
    return min_max

# Contar cuantos digitos tiene un numero de forma recursiva
def count_digits(number):
    # Caso base: si n es un solo dígito, retornar 1
    if number < 10:
        return 1
    # Caso recursivo: llamar a la función con n/10
    # para contar los dígitos del número sin el último dígito,
    # y sumar 1 al resultado para contar el dígito actual.
    else:
        return 1 + count_digits(number // 10)

# Saber si n es potencia de b de manera recursiva
def potency(n, b):
    if n < b:
        return False
    elif n == b:
        return True
    else:
        return potency(n // b, b)

# Saber si es par
def even(n):
    if n == 0:
        return True  # El 0 se considera par
    else:
        return odd(n - 1)
# Saber si es impar
def odd(n):
    if n == 0:
        return False  # El 0 se considera par
    else:
        return even(n - 1)