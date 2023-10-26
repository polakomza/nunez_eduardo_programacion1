import random
def numbers_bingo(number):
    for i in range(5):
        for j in range(5):
            while True:
                number[i][j] = int(input(f"Ingrese el número {j+1} de la lista {i+1}: "))
                if number[i][j] < 1 or number[i][j] > 75:
                    print("El número es incorrecto. Vuelve a ingresarlo.")
                elif is_duplicate(number, i, j):
                    print("El número ingresado ya se encuentra en su cartón. Elija otro por favor.")
                else:
                    break
    return number

def is_duplicate(number, row, col):
    for i in range(5):
        for j in range(5):
            if i == row and j == col:
                continue  # Saltar la misma celda
            if number[i][j] == number[row][col]:
                return True
    return False


def balls_bingo(balls):
    carton = []
    
    # Crear un conjunto de bolas para evitar repeticiones
    ball_set = set(balls)
    
    for _ in range(5):
        row = []
        for _ in range(5):
            random_ball = random.choice(list(ball_set))  # Elegir una bola aleatoria del conjunto
            row.append(random_ball)
            ball_set.remove(random_ball)  # Eliminar la bola del conjunto para evitar repeticiones
        carton.append(row)
    return carton


