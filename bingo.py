import random
import time

'''Crea un juego de Bingo donde el usuario pueda ingresar los números para generar su propio cartón de bingo. A
continuación, se detalla cómo se debe implementar el juego:
1. Solicita al usuario que ingrese 25 números únicos, uno a la vez, para completar su cartón de bingo. Los
números deben estar en el rango de 1 a 75.
2. Valida que los números ingresados sean únicos y estén dentro del rango permitido. Si el usuario ingresa un
número duplicado o fuera del rango, debe mostrar un mensaje de error y solicitar otro número.
3. Después de que el usuario haya completado su cartón, inicia el juego de Bingo.
4. Extrae bolas de bingo al azar y verifica si los números extraídos están en el cartón del usuario.
5. Continúa extrayendo bolas de bingo hasta que el jugador complete una línea horizontal, vertical o diagonal
en su cartón.
6. Muestra mensajes informativos al usuario a medida que se extraen bolas y cuando gana.
7. Pregunta al usuario si desea jugar de nuevo al finalizar el juego.
Recuerda proporcionar instrucciones claras y manejar las entradas del usuario de manera amigable. El objetivo es
crear un juego interactivo que permita al usuario disfrutar del Bingo personalizado'''

# Función para generar los números al azar del bingo
def balls_bingo(balls):
    cardboard_bingo = []
    ball_set = set(balls)
    for _ in range(5):
        row = []
        for _ in range(5):
            random_ball = random.choice(list(ball_set))
            row.append(random_ball)
            ball_set.remove(random_ball)
        cardboard_bingo.append(row)
    return cardboard_bingo

# Función para ingresar los números en el cartón del jugador
def numbers_bingo(number):
    for i in range(5):
        for j in range(5):
            while True:
                number[i][j] = int(input(f"Ingrese el número {j + 1} de la fila {i + 1}: "))
                if number[i][j] < 1 or number[i][j] > 75:
                    print("El número es incorrecto. Vuelve a ingresarlo.")
                elif is_duplicate(number, i, j):
                    print("El número ingresado ya se encuentra en su cartón. Elija otro por favor.")
                else:
                    break
    return number

# Función para verificar si el número ingresado está repetido
def is_duplicate(number, row, col):
    for i in range(5):
        for j in range(5):
            if i == row and j == col:
                continue
            if number[i][j] == number[row][col]:
                return True
    return False

# Función para verificar si el número sorteado del bingo está en el cartón y cambiarlo por un 0
def is_in_bingo(number, cardboard_bingo):
    for i in range(5):
        for j in range(5):
            if number == cardboard_bingo[i][j]:
                cardboard_bingo[i][j] = 0
                return True
    return False

# Función para imprimir el cartón
def print_cardboard(cardboard):
    print("Cartón actual:\n")
    for row in cardboard:
        print(row)

def has_bingo(cardboard):
    # Verificar líneas horizontales
    for row in cardboard:
        if all(cell == 0 for cell in row):
            return True

    # Verificar líneas verticales
    for col in range(5):
        if all(cardboard[row][col] == 0 for row in range(5)):
            return True

    # Verificar diagonales
    if all(cardboard[i][i] == 0 for i in range(5)) or all(cardboard[i][4 - i] == 0 for i in range(5)):
        return True

    return False

print("Bienvenido/a a su Bingo favorito!")
print("Por favor, introduzca 25 numeros del 1 al 75 para hacer su carton personalizado!!")
print(' ')
replay = 'S'  # Inicializar replay como 'S' para comenzar

while replay == 'S':
    number = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    balls = list(range(1, 76))
    cardboard_bingo = balls_bingo(balls)
    cardboard = numbers_bingo(number)

    print(" ")

    while not has_bingo(cardboard):
        for i in range(5):
            for j in range(5):
                numero = cardboard[i][j]
                is_in_bingo(numero, cardboard_bingo)

        new_ball = random.choice(balls)
        if is_in_bingo(new_ball, cardboard):
            print(f"Se sorteó el número {new_ball}. Lo tienes!")
            print(" ")
            print_cardboard(cardboard)
            print(" ")
            time.sleep(1.4)  # Agregar un retraso entre bolas
        else:
            print(" ")
            print(f"Se sorteó el número {new_ball}, No lo tienes :(")
            print(" ")
            time.sleep(1)
        if has_bingo(cardboard) is True:
            print("¡Bingo! Felicitaciones!!\n")

    replay = input("Deseas jugar otra partida? Presiona 'S' para sí y 'N' para salir: ").upper()

if replay == 'N':
    print("Que pena! Me encanto jugar contigo, hasta la proxima!")
