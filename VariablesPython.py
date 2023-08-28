# Python tiene 4 tipos Primitivos:

# strings>>Arreglo de caracteres que forman cadenas para formar un mensaje.Se pueden crear usando comillas simples,dobles o triples.
nombre = "Salvador"
apellido = 'Cartagena'
cursos = """
1. Web Development Fundamentals
2. Fundamentos de Programacion con Python
3. Fundamentos Git
4. Bases de Datos
5. Procesamiento de Datos
"""
print (f"Nombre: {nombre} {apellido}")
print (f"Cursos: {cursos}")
nombre_completo = (f'{nombre} {apellido}')
print (nombre_completo)
#Enteros>>(int) se utilizan para representar datos numericos, solo numeros enteros, tanto positivo como negativo.
year = 2023
dia = 24
edad = 39
temp = -15
print (year , dia , edad , temp, sep = "/")
suma_int = year + dia + edad
print (suma_int)
# Flotantes>>NUmeros con decimales
pi = 3.1416
altura = 1.81
peso = 84.5
temperatura = 28.5
suma_flotantes = pi + altura + peso + temperatura
print ("Total suma Flotantes:" , suma_flotantes)

# Booleanos>>son tipo de datos binarios,es desir que toman los valores de True y False.
fuma = False
suma_bol = 4 == 3 + 1 > 2
print (suma_bol)
print (fuma)
####
a = "cadena"
b = 12
c = 12.2
d = False
e = a + str(b) + str(c) + str(d)
print (e)

#Limite de enteros y flotantes
'''
En Python, un entero y un entero largo son tipos de datos diferentes. 
Un número entero tiene un límite de 231 - 1, y si el valor excede el límite, el tipo de datos de la variable cambiará 
automáticamente a largo y no se generará ninguna excepción. Una vez que el tipo de datos variable se cambia a tipo de 
datos largos, podría ser tan grande como la máquina pueda almacenar, lo que significa que no hay un límite explícito 
en Python.

#Aplica la fórmula de la suma de los primeros n números pares (investigar).
'''
print("Numero Inicial")
n_ini = int(input())
print("Numero final")
n_fin = int(input())
suma = 0
print("Suma de Numeros Pares")
while n_ini <= n_fin:
    if n_ini % 2 == 0:
        print(n_ini)
        suma = suma+n_ini
    n_ini+=1
print ("Suma de Pares: " ,suma)