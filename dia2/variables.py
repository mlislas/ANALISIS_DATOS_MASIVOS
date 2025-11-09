#Ejercicio 1.

# a) Crea una carpeta llamada dia2 y dentro de esta carpeta crea un archivo llamado variables.py
# (Este paso se realiza fuera del código, en el explorador o terminal) 

# b) Escribe un comentario en Python que diga 'Día 2: 30 días de programación en Python' 
# Día 2: 30 días de programación en Python 

# c) Declara una variable de nombre y asígnale un valor. 
nombre = "María" 

# d) Declara una variable de apellido y asígnale un valor. 
apellido = "León"

# e) Declara una variable de nombre completo y asignarle un valor. 
nombre_completo = nombre + " " + apellido 

# f) Declara una variable de país y asígnale un valor. 
pais = "México" 

# g) Declara una variable de ciudad y asígnale un valor. 
ciudad = "Querétaro" 

# h) Declara una variable de edad y asignarle un valor. 
edad = 50

# i) Declara una variable de año y asígnale un valor. 
anio = 2025 

# j) Declara una variable is_married y asígnale un valor. 
is_married = True 

# k) Declara una variable is_true y asígnale un valor. 
is_true = True 

# l) Declara una variable is_light_on y asignale un valor. 
is_light_on = True 

# m) Usando la función incorporada len(), encuentra la longitud de su nombre. 
longitud_nombre = len(nombre) 
print("m) Longitud de mi nombre:", longitud_nombre) 

# n) Declara 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

# o) Suma num_one y num_two y asigna el valor a una variable total. 
total = num_one + num_two 
print("o) Suma:", total)

# p) Resta num_two de num_one y asigna el valor a una variable diff. 
diff = num_one - num_two 
print("p) Resta:", diff) 

# q) Multiplica num_two y num_one y asigna el valor a un producto variable. 
producto = num_one * num_two 
print("q) Multiplicación:", producto)

# r) Divide num_one por num_two y asigna el valor a una división variable. 
division = num_one / num_two 
print("r) División:", division) 

# s) Utiliza la división de módulo para encontrar num_two dividido por num_one y asigna el valor a un resto variable. 
resto = num_two % num_one 
print("s) Módulo:", resto) 

# t) Calcula num_one elevado a num_two y asigna el valor a una variable exp. 
exp = num_one ** num_two 
print("t) Exponente:", exp)

# u) Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division. 
floor_division = num_one // num_two 
print("u) División de piso:", floor_division)

# Ejercicio 2. 
# Dia 2: Cálculos con círculos en Python
 
# Si el radio de un círculo es de 30 metros:
# a) Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle.
radio = 30
pi = 3.1416
area_of_circle = pi * (radio ** 2)
print("a) El área del círculo con radio 30 m es:", area_of_circle, "metros cuadrados")
 
# b) Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle.
circum_of_circle = 2 * pi * radio
print("b) La circunferencia del círculo con radio 30 m es:", circum_of_circle, "metros")
 
# c) Tome el radio como entrada del usuario y calcule el área.
radio_usuario = float(input("c) Ingresa el valor del radio del círculo en metros: "))
area_usuario = pi * (radio_usuario ** 2)
print("   El área del círculo con radio", radio_usuario, "m es:", area_usuario, "metros cuadrados")


# Ejercicio 3.
# Día 2: Estructuras de datos en Python (Diccionarios)

# a) Crea un diccionario vacío llamado perro.
perro = {}
print("a) Diccionario perro:", perro)

# b) Agrega nombre, color, raza, patas y edad al diccionario de perros.
perro = {
    "nombre": "Coco",
    "color": "Negro",
    "raza": "Terrier Escocés",
    "patas": 4,
    "edad": 6
}
print("\nb) Diccionario perro con datos:", perro)

# c) Crea un diccionario de estudiantes con varias claves.
estudiante = {
    "nombre": "María",
    "apellido": "León",
    "sexo": "Femenino",
    "edad": 50,
    "estado_civil": "Casada",
    "habilidades": ["Java", "JavaScript", "HTML"],
    "país": "México",
    "ciudad": "Querétaro",
    "direccion": "Cumbres del Citlaltepetl 66"
}
print("\nc) Diccionario estudiante:", estudiante)

# d) Obtén la longitud del diccionario del estudiante.
longitud_estudiante = len(estudiante)
print("\nd) Longitud del diccionario estudiante: {longitud_estudiante}")

# e) Obtén el valor de las habilidades y verifica el tipo de datos.
habilidades = estudiante["habilidades"]
print("\ne) Habilidades del estudiante:", habilidades)
print("   Tipo de dato de habilidades:", type(habilidades))

# f) Modifica los valores de las habilidades agregando una o dos habilidades.
estudiante["habilidades"].extend(["Spring",  "SQL"])
print("\nf) Habilidades modificadas:", estudiante["habilidades"])

# g) Obtén las claves del diccionario como una lista.
claves = list(estudiante.keys())
print("\ng) Claves del diccionario:", claves)

# h) Obtén los valores del diccionario como una lista.
valores = list(estudiante.values())
print("\nh) Valores del diccionario:", valores )

# i) Cambia el diccionario a una lista de tuplas usando el método items().
tuplas_estudiante = list(estudiante.items())
print("\ni) Diccionario convertido a lista de tuplas:")
print(tuplas_estudiante)

# j) Elimina uno de los elementos del diccionario.
estudiante.pop("direccion")
print("\nj) Diccionario tras eliminar 'direccion':", estudiante)

# k) Elimina uno de los diccionarios (por ejemplo, el diccionario perro).
del perro
print("\nk) Diccionario 'perro' eliminado correctamente.")


# Ejercicio 4.
# Día 2: Estructuras de control - Ciclos en Python
 
# a) Itera de 0 a 10 usando cualquier ciclo.
print("a) Iterar de 0 a 10:")
for i in range(11):
    print(i)
 
# b) Itera de 10 a 0 usando cualquier ciclo.
print("\nb) Iterar de 10 a 0:")
for i in range(10, -1, -1):
    print(i)
 
# c) Escribe un ciclo que haga siete llamadas a print() para formar un triángulo.
print("\nc) Triángulo con símbolo #:")
for i in range(1, 8):
    print("#" * i)
 
# d) Utiliza ciclos anidados para crear el siguiente patrón.
print("\nd) Cuadro de 8x8 con símbolos #:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()  # salto de línea
 
# e) Imprime el siguiente patrón de multiplicación.
print("\ne) Patrón de multiplicación (n x n = resultado):")
for i in range(11):
    print(f"{i} x {i} = {i * i}")
 
# f) Itera a través de la lista ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] e imprime los elementos.
print("\nf) Iterar sobre la lista de tecnologías:")
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tecnologias:
    print(tech)
 
# g) Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números pares.
print("\ng) Números pares del 0 al 100:")
for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print()  # salto de línea
 
# h) Utiliza el ciclo for para iterar de 0 a 100 e imprimir solo números impares.
print("\nh) Números impares del 0 al 100:")
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print()  # salto de línea final


# Ejercicio 5.
# Día 2: Funciones en Python
 
# a) Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.
def add_two_numbers(a, b):
    return a + b

print("a) Suma de 5 + 3 =", add_two_numbers(5, 3))
 
# b) Escribe una función que calcule el área del círculo.
def area_del_circulo(radio):
    pi = 3.1416
    area = pi * (radio ** 2)
    return area
 
print("b) Área de un círculo con radio 7 =", area_del_circulo(7))
 
 
# c) Función add_all_nums que sume un número arbitrario de argumentos.
def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
            total += i
        else:
            return "Error: Todos los elementos deben ser numéricos."
    return total
 
print("c) Suma de varios números (2, 4, 6, 8) =", add_all_nums(2, 4, 6, 8))
 
 
# d) Convierte temperatura de °C a °F.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
 
print("d) 25°C equivale a", convert_celsius_to_fahrenheit(25), "°F")
 
 
# e) Calcula las soluciones de una ecuación cuadrática ax² + bx + c = 0.
import math
 
def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2 * a)
        return f"Una solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Dos soluciones: x1 = {x1}, x2 = {x2}"
 
print("e)", solve_quadratic_eqn(1, -3, 2))
 
 
# f) Función que imprime los elementos de una lista.
def print_list(lista):
    for elemento in lista:
        print(elemento)
 
print("f) Elementos de la lista [1, 2, 3, 4]:")
print_list([1, 2, 3, 4])
 
 
# g) Función que devuelve una lista inversa usando bucles.
def lista_inversa(lista):
    inversa = []
    for i in range(len(lista) - 1, -1, -1):
        inversa.append(lista[i])
    return inversa
 
print("g) Lista inversa de [10, 20, 30, 40] =", lista_inversa([10, 20, 30, 40]))
 
 
# h) Repetición — función add_two_numbers.
def add_two_numbers(a, b):
    return a + b
 
print("h) Suma de 10 + 15 =", add_two_numbers(10, 15))
 
 
# i) Repetición — función para calcular el área del círculo.
def area_del_circulo(radio):
    pi = 3.1416
    return pi * (radio ** 2)
 
print("i) Área de un círculo con radio 5 =", area_del_circulo(5))
 
 
# j) Repetición — función add_all_nums.
def add_all_nums(*args):
    total = 0
    for i in args:
        if not isinstance(i, (int, float)):
            return "Error: Todos los elementos deben ser números."
        total += i
    return total
 
print("j) Suma de varios números (3, 6, 9, 12) =", add_all_nums(3, 6, 9, 12))
 
 
# k) Repetición — función para convertir °C a °F.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
 
print("k) 0°C equivale a", convert_celsius_to_fahrenheit(0), "°F")
 
 
# l) Repetición — función para resolver ecuaciones cuadráticas.
def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos soluciones: x1 = {x1}, x2 = {x2}"
 
print("l)", solve_quadratic_eqn(1, 2, 1))
 
 
# m) Repetición — función print_list.
def print_list(lista):
    for elemento in lista:
        print(elemento)
 
print("m) Elementos de la lista ['Python', 'SQL', 'Tableau']:")
print_list(['Python', 'SQL', 'Tableau'])
 
 
# n) Repetición — función lista_inversa.
def lista_inversa(lista):
    inversa = []
    for i in range(len(lista) - 1, -1, -1):
        inversa.append(lista[i])
    return inversa
 
print("n) Lista inversa de ['A', 'B', 'C', 'D'] =", lista_inversa(['A', 'B', 'C', 'D']))


