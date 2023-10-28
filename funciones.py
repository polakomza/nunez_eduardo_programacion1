<<<<<<< HEAD
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
=======
>>>>>>> 8ceb0774e2e028b4041330bc0ebdd8388b5c3f33
