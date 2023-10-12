# Ejercicio 1
# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input("Ingrese la base del rectangulo: "))
height = int(input("Ingrese la altura del rectangulo: "))
calculation_base = base * height
print("El area del rectangulo es: ",calculation_base)
calculation_height = (base+base) + (height+height)
print("El perimetro del rectangulo es: ",calculation_height)
print("----------------------------------------------")

# Ejercicio 2
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

side1 = int(input("Ingrese el valor del primer lado de su triangulo rectangulo: "))
side2 = int(input("Ingrese el valor del segundo lado de su triangulo rectangulo: "))
hipotenusa = (side1**2) + (side2**2) #Calculo para la hipotenusa
print("La hipotenusa de su triangulo rectangulo es: ",hipotenusa)

# Ejercicio 3
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = int(input("Ingrese un valor numerico positivo: "))
num2 = int(input("Ingrese un segundo valor numerico positivo: "))
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
split = num1 / num2
print("El resultado de la suma de los numeros es: ",add)
print("El resultado de la resta de los numeros es: ",subtract)
print("El resultado de la division de los numeros es: ",split)
print("El resultado de la multiplicacion de los numeros es: ",multiply)

# Ejercicio 4
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Recordar que la fórmula para la conversión es: C = (F-32)*5/9

grades_f = int(input("Ingrese la temperatura en grados Fahrenheit que desea saber en grados Celcius: "))
grades_c = int((grades_f - 32) * 5 / 9) #Calculo para convertir los grados Farenheit a Celcius
print("La temperatura en grados Fahrenheit es: ",grades_f)
print("La temperatura en grados Celcius es: ",grades_c)

# Ejercicio 5
# ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#a)A = input(nombre, "¿Cuál es tu canción favorita?")

# La variable nombre no esta definida y dentro del input no se debe de pedir mas de un argumento.
# La solucion seria pedir un valor para la variable nombre y concatenar el nombre usando la cadena formateado (f-string)

nombre = input("Por favor, introduce tu nombre: ")
A = input(f"Hola {nombre}, ¿Cuál es tu canción favorita? ")

#b)	precio = input("Precio: ")
#total = precio + (precio * 0.1)

# La variable precio tomara un valor str en el input ya que no se le especifica que sea de tipo int o float
# La solucion seria especificar que el input tomara un valor tipo float o int (Se mostrara total en un print)

precio = float(input("Precio: "))
total = precio + (precio * 0.1)
print(total)

#c) edad = int(input("Edad: "))
#print(tu edad es, edad)

# En el print debemos de agregar "" para hacer referencia a que es una cadena de caracteres, las variables se ponen sin ""
# y se concatenan con ,

edad = int(input("Edad: "))
print("tu edad es", edad)

#d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)

# Dentro del print podemos concatenar una variable, en este caso edad pero no podemos definirla.
# Para solucionarlo podriamos hacer un if que valide si la edad es igual a 18 o menor o mayor y mostrarlo.

edad_1 = int(input("Edad: "))

if edad_1 == 18:
    print("Tienes 18 años!!!")
elif edad_1 < 18:
    print("Tienes menos de 18 años")
else:
    print("Tienes mas de 18 años!")

#Ejercicio 6
# Calcular la media de tres números pedidos por teclado.

value_1 = int(input("Ingrese un valor: "))
value_2 = int(input("Ingrese un segundo valor: "))
value_3 = int(input("Ingrese un tercer valor: "))
average = (value_1 + value_2 + value_3) / 3
print("La media de los tres valores ingresados es: ",average)

# Ejercicio 7
# Realiza un programa que reciba una cantidad 
# de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutes = int(input("Ingrese la cantidad de minutos para saber cuantas horas corresponden: "))
hours = (minutes // 60)
minutes_remainings = (minutes % 60)
print(minutes, "minutos son", hours, "horas", minutes_remainings, "y minutos.")

# Ejercicio 8
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
# ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

salary = int(input("Ingrese su salario base: "))
sale_1 = float(input("Ingrese el valor de la primer venta realizada en el mes: "))
sale_2 = float(input("Ingrese el valor de la segunda venta realizada en el mes: "))
sale_3 = float(input("Ingrese el valor de la tercer venta realizada en el mes: "))
commission = (sale_1 + sale_2 + sale_3) * 0.1
total_salary = salary + commission
print("Usted recibira por comisiones: ", commission)
print("Y su salario total del mes sera de: ", total_salary)

# Ejercicio 9
# Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuanto deberá pagar finalmente por su compra.

buys = float(input("Ingrese el valor de su compra para conocer su descuento: "))
total_to_pay = buys - (buys * 0.15)
print("Usted debera de pagar: ", total_to_pay)

# Ejercicio 10
# Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

exam_1 = int(input("Ingrese la nota de su primer examen: "))
exam_2 = int(input("Ingrese la nota de su segundo examen: "))
exam_3 = int(input("Ingrese la nota de su tercer examen: "))
final_exam = int(input("Ingrese la nota de su examen final: "))
final_work = int(input("Ingrese la nota de su trabajo final: "))

first_percentage = ((exam_1 + exam_2 + exam_3) / 3) * 0.55
second_percentage = final_exam * 0.30
third_percentage = final_work * 0.15

qualification = round(first_percentage + second_percentage + third_percentage)
print("Su nota final para la materia de Algoritmos es: ", qualification)

# Ejercicio 11
# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia,
# de modo que el resultado sea siempre positivo).

number_1 = int(input("Ingrese un primer valor: "))
number_2 = int(input("Ingrese un segundo valor: "))
distance_of_numbers = abs(number_1 - number_2)
print("La distancia entre los valores ingresados es: ", distance_of_numbers)

# Ejercicio 12
# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

number = int(input("Ingrese un valor para obtener su raiz cuadrada y su raiz cubica: "))

number_root = number ** 0.5
number_root3 = number ** 1/3
print("La raiz cuadrada de:", number, "es: ",number_root,".", "Y la raiz cubica es: ",number_root3)

# Ejercicio 13
# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.

def invertir_numero_dos_cifras(numero):
    if not (10 <= numero <= 99):
        return "El número debe tener dos cifras."

    unidades = numero % 10
    decenas = numero // 10

    numero_invertido = unidades * 10 + decenas

    return numero_invertido

numero_dos_cifras = int(input("Ingrese un número de dos cifras: "))

numero_invertido = invertir_numero_dos_cifras(numero_dos_cifras)
print("El número invertido es:", numero_invertido)

# Ejercicio 14
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar 
# un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

var_1 = int(input("Ingrese un primer valor: "))
var_2 = int(input("Ingrese el segundo valor: "))
aux = var_1
var_1 = var_2
var_2 = aux
print("Los valores intercambiados quedaron asi: \n")
print("Primer valor: ", var_1 , "Segundo valor: ", var_2)

# Ejercicio 15

HH=int(input("Ingrese la hora a la que salio el ciclista(de 0hs a 23hs): "))
MM=int(input("Ingrese los minutos a los que salio el ciclista(de 0 a 59): "))
SS=int(input("Ingrese los segundos a los que salio el ciclista(de 0 a 59): "))
T=int(input("Ingrese la duracion del viaje en segundos: "))

hora_llegada_segundos = (HH*3600)+(MM*60)+SS +T  # convierto las horas y minutos en segundo totales


HH_llegada = hora_llegada_segundos // 3600  # convierto los segundos en horas,minutos y segundos en la hora de llegada del ciclista
hora_llegada_segundos = hora_llegada_segundos % 3600
MM_llegada = hora_llegada_segundos // 60
SS_llegada = hora_llegada_segundos % 60

print("La hora de llegada del ciclista es de",HH_llegada,"/",MM_llegada,"/",SS_llegada)

# Ejercicio 16
nombre=input("Ingrese el nombre de una persona: ")
primer_apellido=input("Ingrese el primer apellido de una persona: ")
segundo_apellido=input("Ingrese el segundo apellido de una persona: ")
letra_nombre=nombre[0] # Guardo la primera letra del nombre y los apellidos para luego mostrarlas 
letra_primer_apellido=primer_apellido[0]
letra_segundo_apellido=segundo_apellido[0]

print("La primera letra del nombres es",letra_nombre,"la primera letra del primer apellido es",letra_primer_apellido,"la primera letra del segundo apellido es",letra_segundo_apellido)

# Ejercicio 17
usuario = input("Ingresa tu nombre: ")

print(f"Ahora estás en la matrix, {usuario}.")

# Ejercicio 18
costo_cena=float(input("Ingrese el costo de la cena: "))
servicio=costo_cena*6.2/100 # calculo el servicio para despues sumarla al costo
propina=costo_cena*0.10  # calculo la propina para despues sumarla al costo
costo_cena_final=costo_cena+servicio+propina

print("El costo de la cena con servicio y propina es de",costo_cena_final)

# Ejercicio 19
año=int(input("Ingrese el año en el que naciste: "))
mes=int(input("Ingrese el mes en el que naciste: "))
dia=int(input("Ingrese el dia en el que naciste: "))

print("La fecha de nacimiento es",dia,"/",mes,"/",año) 

# Ejercicio 20
fecha_nacimiento = input("Ingresa tu fecha de nacimiento toda seguida sin barras(DDMMAAAA): ")

dia = int(fecha_nacimiento[0:2]) #agarro los dos primero numero del array
mes = int(fecha_nacimiento[2:4]) #agarro el tercer y cuarto numero del array
año = int(fecha_nacimiento[4:])  #agarro del 5 numero en adelante

print("La fecha de nacimiento es",dia,"/",mes,"/",año)

# Ejercicio 21
kilometros_litro=float(input("Ingrese la cantidad de kilometros que consume un litro de la moto: "))
litros_tanque=float(input("Ingrese la capacidad de litros del tanque: "))
cant_kilometros=float(input("Ingrese la cantidad de kilometros que recorreran: "))

tanque=cant_kilometros/(kilometros_litro*litros_tanque) # calculo la cantidad de tanques que necesitaremos para realizar el viaje

print("La cantidad de tanques que necesitares es de",tanque)
