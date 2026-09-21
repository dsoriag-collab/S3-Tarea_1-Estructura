# Tarea de Estructura de Datos
# Nombre: Dennis Ruben Soria Guaranga
# Curso: Software 3-B1

# 20 Ejercicios -- Clases y Colecciones

# Ej. 1 -- Validador de notas con promedio.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# Varias notas ingresadas al método cargar_notas().

#---- Proceso:
# Crear una clase llamada Calificador.
# Guardar las notas válidas dentro de una lista.
# Verificar cada nota usando validar_nota().
# Una nota es válida si está entre 0 y 100.
# Si la nota es válida,
# agregarla a la lista self.notas.
# Si la nota es inválida,
# simplemente no agregarla.
# Después calcular el promedio
# de todas las notas válidas.
# Si no existen notas válidas,
# retornar 0.

#---- Salida:
# Mostrar la lista de notas válidas.
# Mostrar el promedio de las notas válidas.

#-------- 2. BOSQUEJO A MANO ------------
# Se crea:
# c = Calificador()

# Al iniciar:
# self.notas = []

# Se cargan las notas:
# 85, 92, 110, 78, -5, 88

# Primera nota:
# nota = 85
# 0 <= 85 <= 100
# válida
# self.notas = [85]

# Segunda nota:
# nota = 92
# válida
# self.notas = [85, 92]

# Tercera nota:
# nota = 110
# 110 > 100
# inválida
# no se agrega

# Cuarta nota:
# nota = 78
# válida
# self.notas = [85, 92, 78]

# Quinta nota:
# nota = -5
# -5 < 0
# inválida
# no se agrega

# Sexta nota:
# nota = 88
# válida
# self.notas = [85, 92, 78, 88]

# Calcular promedio:
# suma = 85 + 92 + 78 + 88
# suma = 343

# cantidad de notas:
# len(self.notas) = 4

# promedio:
# 343 / 4 = 85.75

# resultado:
# [85, 92, 78, 88]
# 85.75

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Dentro de cargar_notas(),
# cada nota recibida pasa por el mismo proceso:
# 1. Tomar una nota.
# 2. Validar si está entre 0 y 100.
# 3. Si es válida,
#    agregarla a self.notas.
# Este proceso se repite para todas
# las notas recibidas en *args.
# El patrón principal es:
# for nota in args:
#     if self.validar_nota(nota):
#         self.notas.append(nota)
# Después, el promedio se calcula usando
# solamente las notas que fueron aceptadas.

#-------- 4. ESCRIBIR EL CÓDIGO --------
class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):

        if nota >= 0 and nota <= 100:
            return True

        else:
            return False

    def cargar_notas(self, *args):

        for nota in args:

            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):

        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


c = Calificador()

print(c.cargar_notas(85, 92, 110, 78, -5, 88))

print(c.promedio())

#-------- 5. PRUEBA DE ESCRITORIO --------
# self.notas = []

# nota    ¿válida?    self.notas
#  85       Sí        [85]
#  92       Sí        [85, 92]
# 110       No        [85, 92]
#  78       Sí        [85, 92, 78]
#  -5       No        [85, 92, 78]
#  88       Sí        [85, 92, 78, 88]

# Para el promedio:
# sum(self.notas) = 343
# len(self.notas) = 4
# promedio = 343 / 4
# promedio = 85.75

# pantalla:
# [85, 92, 78, 88]
# 85.75

## Reto: ---- Ejercicio práctica 1 ----

"""
Reto: Ejercicio: Clase RegistroTemperaturas

Crea una clase llamada RegistroTemperaturas que haga lo siguiente:

Tenga un método validar_temperatura(temp) que:
Retorne True si la temperatura está entre -20 y 50.
Retorne False si está fuera de ese rango.
Tenga un método cargar_temperaturas(*args) que:
Reciba varias temperaturas al mismo tiempo.
Revise una por una.
Use validar_temperatura() para comprobarlas.
Guarde solamente las temperaturas válidas en una lista interna.
Retorne esa lista.
Tenga un método promedio() que:
Calcule el promedio de todas las temperaturas válidas almacenadas.
Si todavía no hay temperaturas guardadas, retorne 0.###

"""

class RegistroTemperaturas:
    def __init__(self):
        self.temperaturas = []

    def validar_temperatura(self, temp):
        if temp >= -20 and temp <= 50:
            return True
        else:
            return False

    def cargar_temperaturas(self, *args):
        for temp in args:
            if self.validar_temperatura(temp):
                self.temperaturas.append(temp)
        return self.temperaturas

    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        else:
            return sum(self.temperaturas) / len(self.temperaturas)

r = RegistroTemperaturas()

print(r.cargar_temperaturas(85, 92, 110, 78, -5, 88))

print(r.promedio())

# Ej. 2 -- Contador de palabras únicas

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# Varias palabras ingresadas
# mediante agregar_multiples().

#---- Proceso:
# Crear un conjunto llamado palabras_unicas
# para guardar palabras sin repetir.
# Crear una lista llamada orden_palabras
# para conservar el orden de aparición.
# Cada vez que se agrega una palabra:
# Guardarla en palabras_unicas.
# Verificar si todavía no existe
# en orden_palabras.
# Si no existe,
# agregarla a la lista.
# Finalmente contar cuántas palabras
# diferentes existen.

#---- Salida:
# Mostrar las palabras únicas.
# Mostrar las palabras en el orden
# en que aparecieron por primera vez.
# Mostrar la cantidad de palabras únicas.

#-------- 2. BOSQUEJO A MANO ------------
# Se crea:
# at = AnalizadorTexto()


# Al iniciar:

# palabras_unicas = set()

# orden_palabras = []


# Se agregan:
# "hola", "mundo", "hola"

# Primera palabra:
# palabra = "hola"

# Se agrega al set:

# palabras_unicas = {"hola"}

# "hola" no está en orden_palabras

# entonces:

# orden_palabras = ["hola"]

# Segunda palabra:
# palabra = "mundo"

# Se agrega al set:

# palabras_unicas = {"hola", "mundo"}

# "mundo" no está en orden_palabras

# entonces:
# orden_palabras = ["hola", "mundo"]

# Tercera palabra:
# palabra = "hola"

# El set ya contiene "hola",
# por lo tanto no se duplica.

# palabras_unicas = {"hola", "mundo"}

# "hola" ya está en orden_palabras,
# por lo tanto tampoco se vuelve a agregar.

# orden_palabras = ["hola", "mundo"]

# Contar palabras únicas:
# len(palabras_unicas)

# 2

# resultado:
# palabras únicas:
# {"hola", "mundo"}

# orden:
# ["hola", "mundo"]

# cantidad:
# 2

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En agregar_multiples(),
# cada palabra pasa por el mismo proceso:
# 1. Tomar una palabra.
# 2. Enviarla a agregar_palabra().
# 3. Guardarla en el set.
# 4. Si todavía no aparece en la lista,
#    agregarla también a orden_palabras.
# Este proceso se repite para todas
# las palabras recibidas en *args.
# El patrón principal es:
# for palabra in args:
#     self.agregar_palabra(palabra)

#-------- 4. ESCRIBIR EL CÓDIGO --------
class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []

    def agregar_palabra(self, palabra):

        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)

    def contar_palabras(self):

        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):

        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()

at.agregar_multiples("hola", "mundo", "hola")

print(at.palabras_unicas)

print(at.orden_palabras)

print(at.contar_palabras())

#-------- 5. PRUEBA DE ESCRITORIO --------
# palabras_unicas = set()
# orden_palabras = []

# palabra    palabras_unicas       orden_palabras
# "hola"     {"hola"}              ["hola"]
# "mundo"    {"hola", "mundo"}     ["hola", "mundo"]
# "hola"     {"hola", "mundo"}     ["hola", "mundo"]

# contar palabras:
# len(palabras_unicas) = 2

# pantalla:
# {"hola", "mundo"}
# ["hola", "mundo"]
# 2

##Reto ---- Ejercicio práctica 2 ----

"""Ejercicio: Clase RegistroCorreos

Crea una clase llamada RegistroCorreos que:

Tenga un método agregar_correo(correo) que:
Agregue el correo a un conjunto para evitar duplicados.
Agregue el correo a una lista para conservar el orden en que fue registrado.
Si el correo ya existe, no debe volver a agregarse.
Tenga un método contar_correos() que:
Retorne cuántos correos únicos hay registrados.
Tenga un método agregar_varios(*args) que:
Reciba varios correos.
Los recorra uno por uno.
Reutilice agregar_correo() para agregarlos.
Retorne la lista de correos almacenados."""

class RegistroCorreos():
    def __init__(self):
        self.correos = set()
        self.listadecorreos = []

    def agregar_correo(self, correo):
        if correo not in self.correos:
            self.correos.add(correo)
            self.listadecorreos.append(correo)

    def contar_correos(self):
        return len(self.correos)

    def agregar_varios(self, *args):
        for correo in args:
            self.agregar_correo(correo)
        return self.listadecorreos

rc = RegistroCorreos()

print(rc.agregar_varios("Eso Tilin", "Mambo", "Mambo", "wazaaa", "Mambo Kings"))
print(rc.contar_correos())

# Ej. 3 -- Gestor de compras con totales

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# nombre del artículo
# precio del artículo
# precio_min
# precio_max

#---- Proceso:
# Crear un diccionario llamado articulos.
# Guardar cada artículo usando:
# nombre → precio
# Calcular el total del carrito
# sumando todos los precios guardados.
# Recorrer los artículos del diccionario.
# Comparar el precio de cada artículo
# con un precio mínimo y un precio máximo.
# Si el precio está dentro del rango,
# guardar el nombre del artículo
# en una lista llamada encontrados.

#---- Salida:
# Mostrar el total del carrito.
# Mostrar los artículos que se encuentran
# dentro del rango de precios indicado.

#-------- 2. BOSQUEJO A MANO ------------
# Se crea:
# c = CarroCompras()

# Al iniciar:
# articulos = {}

# Agregar pan:
# nombre = "pan"

# precio = 2.50

# articulos = {
#     "pan": 2.50
# }

# Agregar leche:
# nombre = "leche"

# precio = 3.00

# articulos = {
#     "pan": 2.50,
#     "leche": 3.00
# }

# Agregar arroz:
# nombre = "arroz"

# precio = 5.50

# articulos = {
#     "pan": 2.50,
#     "leche": 3.00,
#     "arroz": 5.50
# }

# Calcular total:
# 2.50 + 3.00 + 5.50
# total = 11.00


# Buscar artículos entre 2 y 4:

# precio_min = 2

# precio_max = 4


# pan:
# 2.50 >= 2 y 2.50 <= 4

# verdadero

# encontrados = ["pan"]


# leche:
# 3.00 >= 2 y 3.00 <= 4

# verdadero

# encontrados = ["pan", "leche"]


# arroz:
# 5.50 >= 2 y 5.50 <= 4

# falso

# no se agrega

# resultado:
# 11.0
# ["pan", "leche"]

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Dentro de articulos_por_rango(),
# se recorren todos los artículos guardados.
# Para cada artículo se repite:
# 1. Obtener su nombre y precio.
# 2. Verificar si el precio se encuentra
#    entre precio_min y precio_max.
# 3. Si cumple la condición,
#    agregar el nombre a encontrados.
# El patrón principal es:
# for nombre, precio in self.articulos.items():
#     if precio >= precio_min and precio <= precio_max:
#         encontrados.append(nombre)
# Este proceso se repite para cada artículo
# almacenado en el diccionario.

#-------- 4. ESCRIBIR EL CÓDIGO --------
class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        encontrados = []
        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                encontrados.append(nombre)
        return encontrados

c = CarroCompras()

c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.50)
print(c.total_carrito())
print(c.articulos_por_rango(2, 4))

#-------- 5. PRUEBA DE ESCRITORIO --------
# articulos = {
#     "pan": 2.50,
#     "leche": 3.00,
#     "arroz": 5.50
# }

# total_carrito:

# valores:
# 2.50 + 3.00 + 5.50 = 11.00

# articulos_por_rango(2, 4):

# nombre     precio     ¿entre 2 y 4?     encontrados
# pan        2.50            Sí           ["pan"]
# leche      3.00            Sí           ["pan", "leche"]
# arroz      5.50            No           ["pan", "leche"]

# pantalla:
# 11.0
# ['pan', 'leche']

##Reto: ---- Ejercicio de práctica 3 ----

"""Ejercicio: Clase RegistroNotas

Crea una clase llamada RegistroNotas que trabaje con un diccionario donde:
estudiante → nota

Por ejemplo:
"Ana" → 85
"Carlos" → 72

Debe tener estos métodos:
agregar_estudiante(nombre, nota)
Guarde el nombre como clave.
Guarde la nota como valor.
promedio_general()
Retorne el promedio de todas las notas almacenadas.
Si no existen estudiantes, retorne 0.
estudiantes_aprobados()
Recorra el diccionario.
Considere aprobado a quien tenga nota mayor o igual a 70.
Retorne una lista con los nombres de los estudiantes aprobados.
nota_mayor()
Retorne la nota más alta registrada.
Si no existen estudiantes, retorne 0.
buscar_estudiante(nombre)
Retorne True si el estudiante existe en el diccionario.
Retorne False si no existe."""

class RegistroNotas:
    def __init__(self):
        self.estudiante = {}

    def agregar_estudiante(self, nombre, nota):
        self.estudiante[nombre] = nota

    def promedio_general(self):
        if len(self.estudiante) == 0:
            return 0
        else:
            return sum(self.estudiante.values()) / len(self.estudiante.values())

    def estudiante_aprobado(self):
        aprobados = []
        for nombre, nota in self.estudiante.items():
            if nota >= 70 and nota <= 100:
                aprobados.append(nombre)
        return aprobados

    def nota_mayor(self):
        if len(self.estudiante) == 0:
            return 0
        return max(self.estudiante.values())

    def buscar_estudiante(self, nombre):
        if nombre not in self.estudiante:
            return False
        else:
            return True

rn = RegistroNotas()

rn.agregar_estudiante("Pepe", 34)
rn.agregar_estudiante("Emily", 87)
rn.agregar_estudiante("Dennis", 67)

print(rn.promedio_general())
print(rn.estudiante_aprobado())
print(rn.buscar_estudiante("Adrián"))
print(rn.nota_mayor())


# Ej. 4 -- Inversor de secuencias.

#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# Una lista para invertir.

# También se pueden recibir varias listas
# mediante invertir_multiples().


#---- Proceso:

# En invertir_lista():

# Crear una lista vacía llamada invertida.

# Recorrer la lista original
# desde la última posición hasta la primera.

# Agregar cada elemento a invertida.

# Devolver la nueva lista invertida.


# En invertir_multiples():

# Recibir varias listas usando *listas.

# Crear un diccionario vacío llamado resultado.

# Recorrer cada lista recibida.

# Convertir cada lista original en una tupla
# para poder usarla como clave del diccionario.

# Invertir cada lista usando invertir_lista().

# Guardar:

# tupla original -> lista invertida


#---- Salida:

# Mostrar una lista invertida.

# Mostrar un diccionario con las secuencias
# originales y sus versiones invertidas.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# inv.invertir_lista([1, 2, 3])


# lista = [1, 2, 3]

# invertida = []


# len(lista) = 3


# range:

# range(2, -1, -1)


# valores de i:

# 2, 1, 0


# Primera repetición:

# i = 2

# lista[2] = 3

# invertida = [3]


# Segunda repetición:

# i = 1

# lista[1] = 2

# invertida = [3, 2]


# Tercera repetición:

# i = 0

# lista[0] = 1

# invertida = [3, 2, 1]


# resultado:

# [3, 2, 1]



# Segunda llamada:

# inv.invertir_multiples(
#     [1, 2, 3],
#     [4, 5, 6]
# )


# resultado = {}


# Primera lista:

# lista = [1, 2, 3]

# original = tuple(lista)

# original = (1, 2, 3)


# invertir_lista([1, 2, 3])

# resultado invertido:

# [3, 2, 1]


# diccionario:

# {
#     (1, 2, 3): [3, 2, 1]
# }


# Segunda lista:

# lista = [4, 5, 6]

# original = tuple(lista)

# original = (4, 5, 6)


# invertir_lista([4, 5, 6])

# resultado invertido:

# [6, 5, 4]


# diccionario final:

# {
#     (1, 2, 3): [3, 2, 1],
#     (4, 5, 6): [6, 5, 4]
# }



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# En invertir_lista() se recorren
# los elementos desde el último hasta el primero.
#
# El patrón es:
#
# for i in range(len(lista) - 1, -1, -1):
#
#     invertida.append(lista[i])
#
# En cada repetición se toma un elemento
# y se agrega a la nueva lista.
#
#
# También existe repetición en invertir_multiples().
#
# Cada lista recibida pasa por el mismo proceso:
#
# 1. Convertirla en tupla.
#
# 2. Invertirla.
#
# 3. Guardarla en el diccionario.
#
# El patrón es:
#
# for lista in listas:
#
#     original = tuple(lista)
#
#     resultado[original] = self.invertir_lista(lista)



#-------- 4. ESCRIBIR EL CÓDIGO --------

class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            original = tuple(lista)
            resultado[original] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()

print(inv.invertir_lista([1, 2, 3]))
print(
    inv.invertir_multiples(
        [1, 2, 3],
        [4, 5, 6]
    )
)



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera llamada:

# invertir_lista([1, 2, 3])


# repetición    i    lista[i]    invertida

# inicio                         []

#     1         2       3        [3]

#     2         1       2        [3, 2]

#     3         0       1        [3, 2, 1]


# retorno:

# [3, 2, 1]



# Segunda llamada:

# invertir_multiples(
#     [1, 2, 3],
#     [4, 5, 6]
# )


# lista        original        invertida

# [1,2,3]     (1,2,3)         [3,2,1]

# [4,5,6]     (4,5,6)         [6,5,4]


# resultado:

# {
#     (1, 2, 3): [3, 2, 1],
#     (4, 5, 6): [6, 5, 4]
# }


# pantalla:

# [3, 2, 1]

# {(1, 2, 3): [3, 2, 1], (4, 5, 6): [6, 5, 4]}

## Reto: ---- Ejercicio práctica 4 ----

"""Ejercicio: Clase DuplicadorSecuencia

Crea una clase llamada DuplicadorSecuencia que:

Tenga un método duplicar_lista(lista) que reciba una lista y retorne 
una nueva lista donde cada elemento aparezca dos veces, usando un ciclo manual.
Tenga un método duplicar_multiples(*listas) que reciba varias listas, 
reutilice duplicar_lista() para procesarlas y retorne un diccionario donde:
La clave sea la lista original convertida a tuple.
El valor sea la lista duplicada.

Por ejemplo, conceptualmente:
[1, 2, 3]

debería convertirse en:
[1, 1, 2, 2, 3, 3]

Y si procesamos varias listas, queremos algo conceptualmente parecido a:

(1, 2, 3) → [1, 1, 2, 2, 3, 3]
("a", "b") → ["a", "a", "b", "b"]"""

class DuplicadorSecuencia:
    def duplicar_lista(self, lista):
        resultado = []

        for elemento in lista:
            resultado.append(elemento)
            resultado.append(elemento)

        return resultado

    def duplicar_multiples(self, *args):
        resultados = {}

        for lista in args:
            resultados[tuple(lista)] = self.duplicar_lista(lista)

        return resultados


d = DuplicadorSecuencia()

print(d.duplicar_lista([5, 8, 3]))

print(d.duplicar_multiples(
    [1, 2],
    [4, 5, 6],
    ["a", "b"]
))

# Ej. 5 -- Detector de números pares e impares


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# Varios números enviados al método separar().


#---- Proceso:

# Crear un diccionario llamado resultado
# con dos listas:

# "pares"

# "impares"

# Recibir varios números usando *numeros.

# Recorrer cada número.

# Verificar si el número es par
# utilizando el método es_par().

# Si el número es par,
# agregarlo a la lista "pares".

# Si el número es impar,
# agregarlo a la lista "impares".

# Después contar cuántos elementos
# existen en cada lista.


#---- Salida:

# Mostrar el diccionario con los números
# pares e impares separados.

# Mostrar la cantidad de números pares
# y la cantidad de números impares.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# an = AnalizadorNumeros()


# Al iniciar:

# resultado = {
#     "pares": [],
#     "impares": []
# }


# Se llama:

# separar(1, 2, 3, 4, 5)


# Primer número:

# numero = 1

# 1 % 2 = 1

# Es impar.

# resultado = {
#     "pares": [],
#     "impares": [1]
# }


# Segundo número:

# numero = 2

# 2 % 2 = 0

# Es par.

# resultado = {
#     "pares": [2],
#     "impares": [1]
# }


# Tercer número:

# numero = 3

# 3 % 2 = 1

# Es impar.

# resultado = {
#     "pares": [2],
#     "impares": [1, 3]
# }


# Cuarto número:

# numero = 4

# 4 % 2 = 0

# Es par.

# resultado = {
#     "pares": [2, 4],
#     "impares": [1, 3]
# }


# Quinto número:

# numero = 5

# 5 % 2 = 1

# Es impar.

# resultado = {
#     "pares": [2, 4],
#     "impares": [1, 3, 5]
# }


# Contar pares:

# len([2, 4])

# cantidad_pares = 2


# Contar impares:

# len([1, 3, 5])

# cantidad_impares = 3


# resultado:

# {"pares": [2, 4], "impares": [1, 3, 5]}

# (2, 3)



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Dentro de separar(),
# cada número pasa por el mismo proceso:
#
# 1. Tomar un número.
#
# 2. Verificar si es par.
#
# 3. Si es par,
#    agregarlo a la lista "pares".
#
# 4. Si no es par,
#    agregarlo a la lista "impares".
#
# El proceso se repite para todos
# los números recibidos en *numeros.
#
# El patrón principal es:
#
# for numero in numeros:
#
#     if self.es_par(numero):
#
#         self.resultado["pares"].append(numero)
#
#     else:
#
#         self.resultado["impares"].append(numero)



#-------- 4. ESCRIBIR EL CÓDIGO --------

class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        self.resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)
        return self.resultado

    def cantidad_pares_impares(self):
        cantidad_pares = len(self.resultado["pares"])
        cantidad_impares = len(self.resultado["impares"])
        return (cantidad_pares, cantidad_impares)

an = AnalizadorNumeros()

print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())



#-------- 5. PRUEBA DE ESCRITORIO --------

# numeros = (1, 2, 3, 4, 5)


# numero    numero % 2    tipo       pares      impares

#   1           1        impar       []         [1]

#   2           0        par         [2]        [1]

#   3           1        impar       [2]        [1, 3]

#   4           0        par         [2, 4]     [1, 3]

#   5           1        impar       [2, 4]     [1, 3, 5]


# cantidad_pares:

# len([2, 4]) = 2


# cantidad_impares:

# len([1, 3, 5]) = 3


# pantalla:

# {'pares': [2, 4], 'impares': [1, 3, 5]}

# (2, 3)

## Reto: ---- Ejercicio práctica 5 ----

"""Ejercicio: Clase AnalizadorNotas

Crea una clase llamada AnalizadorNotas que:

Tenga un método es_aprobada(nota) que:
Retorne True si la nota es mayor o igual a 70.
Retorne False si es menor a 70.
Tenga un método separar(*notas) que:
Reciba varias notas.
Reutilice es_aprobada().
Separe las notas en dos listas.
Retorne un diccionario con esta estructura:
{
    "aprobadas": [...],
    "reprobadas": [...]
}
Tenga un método cantidad_aprobadas_reprobadas() que:
Retorne una tupla:
(cantidad_aprobadas, cantidad_reprobadas)"""

class AnalizadorNotas:
    def __init__(self):
        self.aprobadas = []
        self.reprobadas = []

    def es_aprobada(self, nota):
        if nota >= 70:
            return True
        else:
            return False

    def separar(self, *notas):
        self.aprobadas = []
        self.reprobadas = []

        for nota in notas:
            if self.es_aprobada(nota):
                self.aprobadas.append(nota)
            else:
                self.reprobadas.append(nota)

        return {
            "aprobadas": self.aprobadas,
            "reprobadas": self.reprobadas
        }

    def cantidad_aprobadas_reprobadas(self):
        return (len(self.aprobadas), len(self.reprobadas))


a = AnalizadorNotas()

print(a.separar(85, 42, 70, 60, 95))
print(a.cantidad_aprobadas_reprobadas())

# Ej. 6 -- Estadísticas de temperatura

#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# Una o varias temperaturas.


#---- Proceso:

# Crear una lista llamada temperaturas.

# Registrar cada temperatura dentro de la lista.

# Permitir registrar varias temperaturas
# usando *temps.

# Calcular la temperatura mínima.

# Calcular la temperatura máxima.

# Calcular el promedio de las temperaturas.

# Si no existen temperaturas:

# minima() devuelve None.

# maxima() devuelve None.

# promedio() devuelve 0.


#---- Salida:

# Mostrar la temperatura mínima.

# Mostrar la temperatura máxima.

# Mostrar el promedio de temperaturas.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# gt = GestorTemperatura()


# Al iniciar:

# temperaturas = []


# Se registran:

# 20, 25, 18, 30


# Primera temperatura:

# temp = 20

# temperaturas = [20]


# Segunda temperatura:

# temp = 25

# temperaturas = [20, 25]


# Tercera temperatura:

# temp = 18

# temperaturas = [20, 25, 18]


# Cuarta temperatura:

# temp = 30

# temperaturas = [20, 25, 18, 30]


# Calcular mínima:

# min([20, 25, 18, 30])

# minima = 18


# Calcular máxima:

# max([20, 25, 18, 30])

# maxima = 30


# Calcular promedio:

# suma = 20 + 25 + 18 + 30

# suma = 93


# cantidad:

# len(temperaturas) = 4


# promedio:

# 93 / 4 = 23.25


# resultado:

# 18

# 30

# 23.25



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Dentro de registrar_multiples(),
# cada temperatura pasa por el mismo proceso:
#
# 1. Tomar una temperatura.
#
# 2. Enviarla a registrar_temperatura().
#
# 3. Agregarla a la lista temperaturas.
#
# El patrón principal es:
#
# for temp in temps:
#
#     self.registrar_temperatura(temp)
#
#
# Después, las estadísticas se calculan
# usando todos los valores almacenados:
#
# min() para la mínima.
#
# max() para la máxima.
#
# sum() y len() para el promedio.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class GestorTemperatura:

    def __init__(self):

        self.temperaturas = []

    def registrar_temperatura(self, temp):

        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):

        for temp in temps:

            self.registrar_temperatura(temp)

    def minima(self):

        if len(self.temperaturas) == 0:

            return None

        return min(self.temperaturas)

    def maxima(self):

        if len(self.temperaturas) == 0:

            return None

        return max(self.temperaturas)

    def promedio(self):

        if len(self.temperaturas) == 0:

            return 0

        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()

gt.registrar_multiples(20, 25, 18, 30)

print(gt.minima())

print(gt.maxima())

print(gt.promedio())



#-------- 5. PRUEBA DE ESCRITORIO --------

# temperaturas = []


# temp       temperaturas

#  20        [20]

#  25        [20, 25]

#  18        [20, 25, 18]

#  30        [20, 25, 18, 30]


# minima:

# min([20, 25, 18, 30]) = 18


# maxima:

# max([20, 25, 18, 30]) = 30


# promedio:

# sum([20, 25, 18, 30]) = 93

# len([20, 25, 18, 30]) = 4

# promedio = 93 / 4

# promedio = 23.25


# pantalla:

# 18

# 30

# 23.25

## Reto: ---- Ejercicio práctica 7 ----

"""Ejercicio: Clase GestorVelocidades

Crea una clase llamada GestorVelocidades que:

Tenga un método registrar_velocidad(velocidad) que guarde la velocidad en una lista interna.
Tenga los métodos:
minima() → retorna la velocidad más baja.
maxima() → retorna la velocidad más alta.
promedio() → retorna el promedio de las velocidades.
Si no existen velocidades registradas, estos métodos deben retornar 0.
Tenga un método registrar_multiples(*velocidades) que reciba varias velocidades y 
reutilice registrar_velocidad() para guardarlas."""

class GestorVelocidades:
    def __init__(self):
        self.velocidades = []

    def registrar_velocidad(self, velocidad):
        self.velocidades.append(velocidad)

    def minima(self):
        if len(self.velocidades) == 0:
            return 0

        return min(self.velocidades)

    def maxima(self):
        if len(self.velocidades) == 0:
            return 0

        return max(self.velocidades)

    def promedio(self):
        if len(self.velocidades) == 0:
            return 0

        return sum(self.velocidades) / len(self.velocidades)

    def registrar_multiples(self, *velocidades):
        for velocidad in velocidades:
            self.registrar_velocidad(velocidad)


gv = GestorVelocidades()

gv.registrar_multiples(60, 80, 45, 100, 75)

print(gv.velocidades)
print(gv.minima())
print(gv.maxima())
print(gv.promedio())

# Ej. 7 -- Mapeador de edades.

#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# nombre

# edad

# edad_minima


#---- Proceso:

# Crear un diccionario llamado personas.

# Guardar cada persona de esta forma:

# nombre -> edad

# Para buscar personas mayores:

# Recorrer cada nombre y edad
# almacenados en el diccionario.

# Comparar la edad de cada persona
# con edad_minima.

# Si la edad es mayor o igual
# a edad_minima,
# agregar el nombre a la lista mayores.

# Para calcular el promedio:

# Sumar todas las edades.

# Dividir entre la cantidad de personas.

# Si no existen personas registradas,
# retornar 0.


#---- Salida:

# Mostrar los nombres de las personas
# que cumplen con la edad mínima.

# Mostrar la edad promedio
# de todas las personas registradas.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# gp = GestorPersonas()


# Al iniciar:

# personas = {}


# Agregar Ana:

# nombre = "Ana"

# edad = 28


# personas = {
#     "Ana": 28
# }


# Agregar Bob:

# nombre = "Bob"

# edad = 17


# personas = {
#     "Ana": 28,
#     "Bob": 17
# }


# Agregar Carlos:

# nombre = "Carlos"

# edad = 40


# personas = {
#     "Ana": 28,
#     "Bob": 17,
#     "Carlos": 40
# }


# Buscar personas con edad mínima de 18:


# Ana:

# 28 >= 18

# verdadero

# mayores = ["Ana"]


# Bob:

# 17 >= 18

# falso

# mayores = ["Ana"]


# Carlos:

# 40 >= 18

# verdadero

# mayores = ["Ana", "Carlos"]


# Calcular promedio:

# 28 + 17 + 40 = 85


# cantidad de personas:

# 3


# promedio:

# 85 / 3

# promedio = 28.3333...


# resultado:

# ["Ana", "Carlos"]

# 28.3333...



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Dentro de personas_mayores(),
# cada persona pasa por el mismo proceso:
#
# 1. Obtener su nombre y edad.
#
# 2. Comparar la edad con edad_minima.
#
# 3. Si cumple la condición,
#    agregar el nombre a mayores.
#
# El patrón principal es:
#
# for nombre, edad in self.personas.items():
#
#     if edad >= edad_minima:
#
#         mayores.append(nombre)
#
# Este proceso se repite para todas
# las personas guardadas en el diccionario.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class GestorPersonas:

    def __init__(self):

        self.personas = {}

    def agregar_persona(self, nombre, edad):

        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):

        mayores = []

        for nombre, edad in self.personas.items():

            if edad >= edad_minima:

                mayores.append(nombre)

        return mayores

    def edad_promedio(self):

        if len(self.personas) == 0:

            return 0

        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()

gp.agregar_persona("Ana", 28)

gp.agregar_persona("Bob", 17)

gp.agregar_persona("Carlos", 40)

print(gp.personas_mayores(18))

print(gp.edad_promedio())



#-------- 5. PRUEBA DE ESCRITORIO --------

# personas:

# {
#     "Ana": 28,
#     "Bob": 17,
#     "Carlos": 40
# }


# personas_mayores(18):


# nombre     edad     edad >= 18     mayores

# Ana         28          Sí          ["Ana"]

# Bob         17          No          ["Ana"]

# Carlos      40          Sí          ["Ana", "Carlos"]


# edad_promedio:


# sum(self.personas.values())

# 28 + 17 + 40 = 85


# len(self.personas)

# 3


# promedio:

# 85 / 3 = 28.3333...


# pantalla:

# ['Ana', 'Carlos']

# 28.333333333333332

##Reto: ---- Ejercicio práctica 7 ----

"""Ejercicio: Clase GestorPeliculas

Crea una clase llamada GestorPeliculas que:

Tenga un método agregar_pelicula(titulo, duracion) que guarde las películas en un diccionario, donde:
El título sea la clave.
La duración en minutos sea el valor.
Tenga un método peliculas_largas(duracion_minima) que:
Retorne una lista con los títulos de las películas cuya duración sea mayor o igual a duracion_minima.
Tenga un método duracion_promedio() que:
Retorne el promedio de duración de todas las películas.
Si no hay películas registradas, retorne 0."""

class GestorPeliculas:
    def __init__(self):
        self.peliculas = {}

    def agregar_pelicula(self, titulo, duracion):
        self.peliculas[titulo] = duracion

    def peliculas_largas(self, duracion_minima):
        encontradas = []

        for titulo, duracion in self.peliculas.items():
            if duracion >= duracion_minima:
                encontradas.append(titulo)

        return encontradas

    def duracion_promedio(self):
        if len(self.peliculas) == 0:
            return 0

        return sum(self.peliculas.values()) / len(self.peliculas)


gp = GestorPeliculas()

gp.agregar_pelicula("Interstellar", 169)
gp.agregar_pelicula("Shrek", 90)
gp.agregar_pelicula("Avatar", 162)
gp.agregar_pelicula("Toy Story", 81)
gp.agregar_pelicula("Dune", 155)

print(gp.peliculas_largas(150))
print(gp.duracion_promedio())

# Ej. 8 -- Asignador de equipos

#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# nombre_equipo

# equipo

# jugador


#---- Proceso:

# Crear un diccionario llamado equipos.

# Cada nombre de equipo será una clave.

# Cada equipo tendrá como valor
# una lista de jugadores.


# Para crear un equipo:

# Verificar si todavía no existe.

# Si no existe,
# agregarlo al diccionario
# con una lista vacía.


# Para agregar un jugador:

# Verificar si el equipo existe.

# Si existe,
# agregar el jugador a su lista.


# Para buscar el equipo con más integrantes:

# Recorrer todos los equipos.

# Contar cuántos jugadores tiene cada uno.

# Comparar esa cantidad
# con la mayor encontrada hasta el momento.

# Si tiene más jugadores,
# actualizar el equipo ganador.


#---- Salida:

# Mostrar el diccionario con los equipos
# y sus jugadores.

# Mostrar el nombre del equipo
# con mayor cantidad de integrantes.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# eq = Equipos()


# Al iniciar:

# equipos = {}


# Crear equipo A:

# equipos = {
#     "A": []
# }


# Crear equipo B:

# equipos = {
#     "A": [],
#     "B": []
# }


# Agregar Juan al equipo A:

# equipos = {
#     "A": ["Juan"],
#     "B": []
# }


# Agregar Pedro al equipo A:

# equipos = {
#     "A": ["Juan", "Pedro"],
#     "B": []
# }


# Agregar Carlos al equipo B:

# equipos = {
#     "A": ["Juan", "Pedro"],
#     "B": ["Carlos"]
# }


# Buscar el equipo con más integrantes:


# Inicialmente:

# equipo_mayor = None

# mayor_cantidad = -1


# Equipo A:

# jugadores = ["Juan", "Pedro"]

# len(jugadores) = 2


# 2 > -1

# verdadero


# mayor_cantidad = 2

# equipo_mayor = "A"


# Equipo B:

# jugadores = ["Carlos"]

# len(jugadores) = 1


# 1 > 2

# falso


# equipo_mayor sigue siendo:

# "A"


# resultado:

# {
#     "A": ["Juan", "Pedro"],
#     "B": ["Carlos"]
# }

# A



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Dentro de equipo_mayor_integrantes(),
# cada equipo pasa por el mismo proceso:
#
# 1. Obtener el equipo y su lista de jugadores.
#
# 2. Contar cuántos jugadores tiene.
#
# 3. Comparar esa cantidad con
#    la mayor encontrada hasta el momento.
#
# 4. Si es mayor,
#    actualizar mayor_cantidad
#    y equipo_mayor.
#
# El patrón principal es:
#
# for equipo, jugadores in self.equipos.items():
#
#     if len(jugadores) > mayor_cantidad:
#
#         mayor_cantidad = len(jugadores)
#
#         equipo_mayor = equipo
#
# Este proceso se conoce como
# patrón campeón,
# porque se conserva el equipo
# con mayor cantidad encontrada hasta el momento.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class Equipos:

    def __init__(self):

        self.equipos = {}

    def crear_equipo(self, nombre_equipo):

        if nombre_equipo not in self.equipos:

            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):

        if equipo in self.equipos:

            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):

        if len(self.equipos) == 0:

            return None

        equipo_mayor = None

        mayor_cantidad = -1

        for equipo, jugadores in self.equipos.items():

            if len(jugadores) > mayor_cantidad:

                mayor_cantidad = len(jugadores)

                equipo_mayor = equipo

        return equipo_mayor


eq = Equipos()

eq.crear_equipo("A")

eq.crear_equipo("B")

eq.agregar_jugador("A", "Juan")

eq.agregar_jugador("A", "Pedro")

eq.agregar_jugador("B", "Carlos")

print(eq.equipos)

print(eq.equipo_mayor_integrantes())



#-------- 5. PRUEBA DE ESCRITORIO --------

# equipos:

# {
#     "A": ["Juan", "Pedro"],
#     "B": ["Carlos"]
# }


# equipo     jugadores            cantidad     mayor_cantidad     equipo_mayor

# inicio                                             -1              None

#   A       ["Juan", "Pedro"]         2               2               "A"

#   B       ["Carlos"]                1               2               "A"


# retorno:

# "A"


# pantalla:
# {'A': ['Juan', 'Pedro'], 'B': ['Carlos']}
# A

## Reto: ---- Ejercicio práctica 8 ----

"""Ejercicio: Clase Clubes

Crea una clase llamada Clubes que:

Tenga un método crear_club(nombre_club) que cree un club dentro de un diccionario y le asigne inicialmente una lista vacía.
Tenga un método agregar_miembro(club, miembro) que agregue un miembro a la lista correspondiente a ese club.
Tenga un método club_mayor_miembros() que retorne el nombre del club que tenga la mayor cantidad de miembros.

Por ejemplo, conceptualmente queremos llegar a algo así:

{
    "Programacion": ["Ana", "Carlos", "Luis"],
    "Ajedrez": ["Pedro", "Maria"],
    "Robotica": ["Juan"]
}

Entonces:

club_mayor_miembros()

debería retornar:

Programacion"""

class Clubes:
    def __init__(self):
        self.clubes = {}

    def crear_club(self, nombre_club):
        self.clubes[nombre_club] = []

    def agregar_miembro(self, club, miembro):
        self.clubes[club].append(miembro)

    def club_mayor_miembros(self):
        mayor_cantidad = -1
        club_mayor = None

        for nombre_club, miembros in self.clubes.items():
            if len(miembros) > mayor_cantidad:
                mayor_cantidad = len(miembros)
                club_mayor = nombre_club

        return club_mayor


c = Clubes()

c.crear_club("Programacion")
c.crear_club("Ajedrez")
c.crear_club("Robotica")

c.agregar_miembro("Programacion", "Ana")
c.agregar_miembro("Programacion", "Carlos")

c.agregar_miembro("Ajedrez", "Pedro")
c.agregar_miembro("Ajedrez", "Maria")
c.agregar_miembro("Ajedrez", "Luis")

c.agregar_miembro("Robotica", "Juan")

print(c.clubes)
print(c.club_mayor_miembros())

# Ej. 9 -- Validador de caracteres


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# texto


#---- Proceso:

# Crear una variable texto_mas_largo
# que inicialmente esté vacía.

# Crear un método solo_vocales()
# para verificar si una letra es vocal.

# Incluir vocales normales,
# vocales con tilde
# y mayúsculas.


# Al recibir un texto:

# Comparar su longitud con
# texto_mas_largo.

# Si el nuevo texto es más largo,
# guardarlo como texto_mas_largo.


# Crear un diccionario resultado
# con tres contadores:

# vocales

# consonantes

# digitos


# Recorrer cada carácter del texto.

# Si el carácter es un dígito,
# aumentar el contador de digitos.

# Si el carácter es una letra,
# verificar si es vocal.

# Si es vocal,
# aumentar vocales.

# Si no es vocal,
# aumentar consonantes.


#---- Salida:

# Mostrar un diccionario
# con la cantidad de vocales,
# consonantes y dígitos.

# Mostrar el texto más largo
# analizado hasta el momento.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# astr = AnalizadorString()


# Al iniciar:

# texto_mas_largo = ""


# Se analiza:

# texto = "Hola123"


# Comparar longitudes:

# len("Hola123") = 7

# len("") = 0


# 7 > 0

# verdadero


# texto_mas_largo = "Hola123"


# resultado = {
#     "vocales": 0,
#     "consonantes": 0,
#     "digitos": 0
# }


# Primer carácter:

# caracter = "H"

# "H".isdigit() → False

# "H".isalpha() → True

# solo_vocales("H") → False

# consonantes = 1


# Segundo carácter:

# caracter = "o"

# es letra

# es vocal

# vocales = 1


# Tercer carácter:

# caracter = "l"

# es letra

# no es vocal

# consonantes = 2


# Cuarto carácter:

# caracter = "a"

# es letra

# es vocal

# vocales = 2


# Quinto carácter:

# caracter = "1"

# es dígito

# digitos = 1


# Sexto carácter:

# caracter = "2"

# es dígito

# digitos = 2


# Séptimo carácter:

# caracter = "3"

# es dígito

# digitos = 3


# resultado final:

# {
#     "vocales": 2,
#     "consonantes": 2,
#     "digitos": 3
# }


# texto_mas_largo:

# "Hola123"



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Cada carácter del texto pasa
# por el mismo proceso:
#
# 1. Verificar si es un dígito.
#
# 2. Si no es dígito,
#    verificar si es una letra.
#
# 3. Si es una letra,
#    comprobar si es vocal.
#
# 4. Aumentar el contador correspondiente.
#
# El patrón principal es:
#
# for caracter in texto:
#
#     if caracter.isdigit():
#
#         resultado["digitos"] += 1
#
#     elif caracter.isalpha():
#
#         if self.solo_vocales(caracter):
#
#             resultado["vocales"] += 1
#
#         else:
#
#             resultado["consonantes"] += 1
#
#
# También se guarda el texto más largo
# encontrado hasta el momento.
#
# Si aparece un texto más largo,
# se reemplaza el anterior.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class AnalizadorString:

    def __init__(self):

        self.texto_mas_largo = ""

    def solo_vocales(self, letra):

        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

        if letra in vocales:

            return True

        return False

    def contar_por_tipo(self, texto):

        if len(texto) > len(self.texto_mas_largo):

            self.texto_mas_largo = texto

        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for caracter in texto:

            if caracter.isdigit():

                resultado["digitos"] += 1

            elif caracter.isalpha():

                if self.solo_vocales(caracter):

                    resultado["vocales"] += 1

                else:

                    resultado["consonantes"] += 1

        return resultado


astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))

print(astr.texto_mas_largo)



#-------- 5. PRUEBA DE ESCRITORIO --------

# texto = "Hola123"


# carácter    tipo           vocales    consonantes    digitos

#   H        consonante         0             1            0

#   o        vocal              1             1            0

#   l        consonante         1             2            0

#   a        vocal              2             2            0

#   1        dígito             2             2            1

#   2        dígito             2             2            2

#   3        dígito             2             2            3


# resultado:

# {
#     "vocales": 2,
#     "consonantes": 2,
#     "digitos": 3
# }


# texto_mas_largo:

# "Hola123"


# pantalla:

# {'vocales': 2, 'consonantes': 2, 'digitos': 3}

# Hola123

## Reto: ---- Ejercicio práctica 9 ----

"""Ejercicio: Clase AnalizadorCaracteres

Crea una clase llamada AnalizadorCaracteres que:

Tenga un método es_mayuscula(letra) que:
Retorne True si la letra es mayúscula.
Retorne False en caso contrario.
Tenga un método contar_caracteres(texto) que:
Recorra el texto carácter por carácter.
Retorne un diccionario:
{
    "mayusculas": cantidad,
    "minusculas": cantidad,
    "digitos": cantidad
}
Debe reutilizar es_mayuscula() cuando corresponda.
Los espacios y símbolos como !, ?, @, etc. no se cuentan.
Tenga un atributo que guarde el texto más largo analizado hasta el momento."""

class AnalizadorCaracteres:
    def __init__(self):
        self.texto_mas_largo = ""

    def es_mayuscula(self, letra):
        if letra.isupper():
            return True
        else:
            return False

    def contar_caracteres(self, texto):
        mayusculas = 0
        minusculas = 0
        digitos = 0

        for caracter in texto:
            if caracter.isdigit():
                digitos += 1

            elif caracter.isalpha():
                if self.es_mayuscula(caracter):
                    mayusculas += 1
                else:
                    minusculas += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "mayusculas": mayusculas,
            "minusculas": minusculas,
            "digitos": digitos
        }


a = AnalizadorCaracteres()

print(a.contar_caracteres("Hola123!"))
print(a.contar_caracteres("PROGRAMACION2026"))
print(a.contar_caracteres("Sol"))

print("Texto más largo:", a.texto_mas_largo)

# Ej. 10 -- Gestor de tareas con prioridad


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# descripcion

# prioridad


#---- Proceso:

# Crear una lista llamada tareas.

# Cada tarea se guarda como una tupla:

# (descripcion, prioridad)


# Para agregar una tarea:

# Añadir la tupla a la lista tareas.


# Para buscar tareas prioritarias:

# Recorrer todas las tareas.

# Revisar la prioridad de cada una.

# Si la prioridad es "alta",
# agregar la tarea a prioritarias.


# Para eliminar una tarea completada:

# Recorrer todas las tareas.

# Comparar la descripción de cada tarea
# con la descripción recibida.

# Si coinciden,
# eliminar la tarea de la lista.

# Retornar True si se eliminó.

# Retornar False si no se encontró.


#---- Salida:

# Mostrar las tareas con prioridad alta.

# Mostrar la lista de tareas
# después de eliminar una completada.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# t = Tareas()


# Al iniciar:

# tareas = []


# Agregar:

# ("Estudiar", "alta")


# tareas = [
#     ("Estudiar", "alta")
# ]


# Agregar:

# ("Leer", "baja")


# tareas = [
#     ("Estudiar", "alta"),
#     ("Leer", "baja")
# ]


# Agregar:

# ("Hacer deberes", "alta")


# tareas = [
#     ("Estudiar", "alta"),
#     ("Leer", "baja"),
#     ("Hacer deberes", "alta")
# ]


# Buscar tareas prioritarias:


# Primera tarea:

# ("Estudiar", "alta")

# tarea[1] = "alta"

# se agrega


# prioritarias = [
#     ("Estudiar", "alta")
# ]


# Segunda tarea:

# ("Leer", "baja")

# tarea[1] = "baja"

# no se agrega


# Tercera tarea:

# ("Hacer deberes", "alta")

# tarea[1] = "alta"

# se agrega


# prioritarias = [
#     ("Estudiar", "alta"),
#     ("Hacer deberes", "alta")
# ]


# Eliminar:

# descripcion = "Leer"


# Se recorre la lista.


# tarea = ("Estudiar", "alta")

# tarea[0] == "Leer"

# falso


# tarea = ("Leer", "baja")

# tarea[0] == "Leer"

# verdadero


# eliminar:

# ("Leer", "baja")


# tareas queda:

# [
#     ("Estudiar", "alta"),
#     ("Hacer deberes", "alta")
# ]


# return True



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# En tareas_prioritarias(),
# cada tarea pasa por el mismo proceso:
#
# 1. Tomar una tarea.
#
# 2. Revisar su prioridad.
#
# 3. Si es "alta",
#    agregarla a prioritarias.
#
# El patrón es:
#
# for tarea in self.tareas:
#
#     if tarea[1] == "alta":
#
#         prioritarias.append(tarea)
#
#
# También existe repetición
# en eliminar_completada().
#
# Se recorren las tareas hasta encontrar
# una cuya descripción coincida.
#
# Cuando se encuentra:
#
# se elimina
#
# y se retorna True.
#
# Si termina el ciclo
# sin encontrarla,
# se retorna False.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class Tareas:

    def __init__(self):

        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):

        self.tareas.append(
            (descripcion, prioridad)
        )

    def tareas_prioritarias(self):

        prioritarias = []

        for tarea in self.tareas:

            if tarea[1] == "alta":

                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):

        for tarea in self.tareas:

            if tarea[0] == descripcion:

                self.tareas.remove(tarea)

                return True

        return False


t = Tareas()

t.agregar_tarea("Estudiar", "alta")

t.agregar_tarea("Leer", "baja")

t.agregar_tarea("Hacer deberes", "alta")

print(t.tareas_prioritarias())

t.eliminar_completada("Leer")

print(t.tareas)



#-------- 5. PRUEBA DE ESCRITORIO --------

# tareas:

# [
#     ("Estudiar", "alta"),
#     ("Leer", "baja"),
#     ("Hacer deberes", "alta")
# ]


# tareas_prioritarias():


# tarea                         prioridad    ¿agregar?

# ("Estudiar", "alta")          alta           Sí

# ("Leer", "baja")              baja           No

# ("Hacer deberes", "alta")     alta           Sí


# resultado:

# [
#     ("Estudiar", "alta"),
#     ("Hacer deberes", "alta")
# ]


# eliminar_completada("Leer"):


# tarea                         ¿coincide?

# ("Estudiar", "alta")             No

# ("Leer", "baja")                 Sí


# se elimina:

# ("Leer", "baja")


# tareas finales:

# [
#     ("Estudiar", "alta"),
#     ("Hacer deberes", "alta")
# ]


# pantalla:

# [('Estudiar', 'alta'), ('Hacer deberes', 'alta')]

# [('Estudiar', 'alta'), ('Hacer deberes', 'alta')]

##Reto: ---- Ejercicio práctica 10 ----

"""Ejercicio: Clase Pedidos

Crea una clase llamada Pedidos que:

Tenga un método agregar_pedido(producto, estado) que guarde cada pedido en una lista de tuplas:
(producto, estado)
Tenga un método pedidos_pendientes() que retorne una lista solamente con los pedidos cuyo estado sea "pendiente".
Tenga un método eliminar_entregado(producto) que elimine de la lista el pedido correspondiente al producto indicado.

Por ejemplo, podríamos terminar teniendo:

[
    ("Mouse", "pendiente"),
    ("Teclado", "entregado"),
    ("Monitor", "pendiente")
]"""

class Pedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, producto, estado):
        self.pedidos.append((producto, estado))

    def pedidos_pendientes(self):
        pendientes = []

        for producto, estado in self.pedidos:
            if estado == "pendiente":
                pendientes.append((producto, estado))

        return pendientes

    def eliminar_entregado(self, producto):
        for pedido in self.pedidos:
            if pedido[0] == producto and pedido[1] == "entregado":
                self.pedidos.remove(pedido)
                break


p = Pedidos()

p.agregar_pedido("Mouse", "pendiente")
p.agregar_pedido("Teclado", "entregado")
p.agregar_pedido("Monitor", "pendiente")
p.agregar_pedido("Webcam", "entregado")

print(p.pedidos)

print(p.pedidos_pendientes())

p.eliminar_entregado("Teclado")

print(p.pedidos)

# Ej. 11 -- Contador de frecuencia


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# elemento


#---- Proceso:

# Crear un diccionario llamado frecuencias.

# Cada elemento se guarda como clave.

# Su cantidad de apariciones
# se guarda como valor.


# Para agregar un elemento:

# Verificar si ya existe
# dentro del diccionario.

# Si existe,
# aumentar su frecuencia en 1.

# Si no existe,
# crear la clave con valor 1.


# Para encontrar el elemento más frecuente:

# Recorrer todos los elementos
# y sus frecuencias.

# Comparar cada frecuencia
# con la mayor encontrada.

# Si una frecuencia es mayor,
# actualizar:

# mayor_frecuencia

# mayor_elemento


# Para consultar una frecuencia:

# Verificar si el elemento existe.

# Si existe,
# retornar su frecuencia.

# Si no existe,
# retornar 0.


#---- Salida:

# Mostrar el diccionario de frecuencias.

# Mostrar el elemento más frecuente.

# Mostrar la frecuencia
# de un elemento específico.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# cf = ContadorFrecuencia()


# Al iniciar:

# frecuencias = {}


# Agregar "a":

# "a" no existe.

# frecuencias["a"] = 1


# frecuencias = {
#     "a": 1
# }


# Agregar "b":

# "b" no existe.

# frecuencias["b"] = 1


# frecuencias = {
#     "a": 1,
#     "b": 1
# }


# Agregar otra vez "a":

# "a" ya existe.

# frecuencias["a"] += 1


# frecuencias["a"] = 2


# resultado:

# frecuencias = {
#     "a": 2,
#     "b": 1
# }


# Buscar elemento más frecuente:


# Inicialmente:

# mayor_elemento = None

# mayor_frecuencia = 0


# Primer elemento:

# elemento = "a"

# frecuencia = 2


# 2 > 0

# verdadero


# mayor_frecuencia = 2

# mayor_elemento = "a"


# Segundo elemento:

# elemento = "b"

# frecuencia = 1


# 1 > 2

# falso


# mayor_elemento sigue siendo:

# "a"


# Consultar frecuencia de "a":

# frecuencias["a"] = 2


# resultado:

# {"a": 2, "b": 1}

# a

# 2



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Cada vez que se agrega un elemento,
# se verifica si ya existe.
#
# Si existe:
#
# frecuencia = frecuencia + 1
#
# Si no existe:
#
# frecuencia = 1
#
#
# También existe un proceso repetitivo
# dentro de elemento_mas_frecuente().
#
# Para cada elemento se hace:
#
# 1. Obtener su frecuencia.
#
# 2. Compararla con mayor_frecuencia.
#
# 3. Si es mayor,
#    actualizar el elemento ganador.
#
# Este proceso es un patrón campeón,
# porque se conserva el elemento
# con mayor frecuencia encontrada.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class ContadorFrecuencia:

    def __init__(self):

        self.frecuencias = {}

    def agregar_elemento(self, elemento):

        if elemento in self.frecuencias:

            self.frecuencias[elemento] += 1

        else:

            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):

        if len(self.frecuencias) == 0:

            return None

        mayor_elemento = None

        mayor_frecuencia = 0

        for elemento, frecuencia in self.frecuencias.items():

            if frecuencia > mayor_frecuencia:

                mayor_frecuencia = frecuencia

                mayor_elemento = elemento

        return mayor_elemento

    def frecuencia_elemento(self, elemento):

        if elemento in self.frecuencias:

            return self.frecuencias[elemento]

        return 0


cf = ContadorFrecuencia()

cf.agregar_elemento("a")

cf.agregar_elemento("b")

cf.agregar_elemento("a")

print(cf.frecuencias)

print(cf.elemento_mas_frecuente())

print(cf.frecuencia_elemento("a"))



#-------- 5. PRUEBA DE ESCRITORIO --------

# agregar_elemento():


# elemento    frecuencias después

#   "a"      {"a": 1}

#   "b"      {"a": 1, "b": 1}

#   "a"      {"a": 2, "b": 1}



# elemento_mas_frecuente():


# elemento    frecuencia    mayor_frecuencia    mayor_elemento

# inicio                         0                  None

#   "a"          2              2                   "a"

#   "b"          1              2                   "a"


# retorno:

# "a"



# frecuencia_elemento("a"):

# "a" existe en frecuencias.

# return frecuencias["a"]

# return 2


# pantalla:

# {'a': 2, 'b': 1}

# a

# 2

## Reto: ---- Ejercicio práctica 11 ----

"""Ejercicio: Clase RegistroVisitas

Crea una clase llamada RegistroVisitas que:

Tenga un método registrar_visita(pagina) que registre cuántas veces se ha visitado cada página usando un diccionario.
Tenga un método pagina_mas_visitada() que retorne el nombre de la página que tenga mayor cantidad de visitas.
Tenga un método cantidad_visitas(pagina) que retorne cuántas veces se ha visitado una página.
Si la página nunca fue registrada, debe retornar 0.

Por ejemplo, después de registrar:

"Inicio"
"Productos"
"Inicio"
"Contacto"
"Inicio"
"Productos"

queremos tener conceptualmente:

{
    "Inicio": 3,
    "Productos": 2,
    "Contacto": 1
}"""

class RegistroVisitas:
    def __init__(self):
        self.visitas = {}

    def registrar_visita(self, pagina):
        if pagina in self.visitas:
            self.visitas[pagina] += 1
        else:
            self.visitas[pagina] = 1

    def pagina_mas_visitada(self):
        if len(self.visitas) == 0:
            return None

        pagina_mayor = None
        mayor_frecuencia = 0

        for pagina, cantidad in self.visitas.items():
            if cantidad > mayor_frecuencia:
                mayor_frecuencia = cantidad
                pagina_mayor = pagina

        return pagina_mayor

    def cantidad_visitas(self, pagina):
        if pagina in self.visitas:
            return self.visitas[pagina]
        else:
            return 0


rv = RegistroVisitas()

rv.registrar_visita("Inicio")
rv.registrar_visita("Productos")
rv.registrar_visita("Inicio")
rv.registrar_visita("Contacto")
rv.registrar_visita("Inicio")
rv.registrar_visita("Productos")

print(rv.visitas)
print(rv.pagina_mas_visitada())
print(rv.cantidad_visitas("Productos"))
print(rv.cantidad_visitas("Blog"))

# Ej. 12 -- Selector de rango con tuplas


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# inicio

# fin

# uno o varios rangos


#---- Proceso:

# Crear un método crear_rango().

# Recorrer los números desde inicio
# hasta fin inclusive.

# Guardar cada número en una lista.

# Convertir la lista en una tupla
# y retornarla.


# Para varios rangos:

# Recibirlos mediante *rangos.

# Crear un set llamado elementos
# para evitar números repetidos.

# Recorrer cada rango recibido.

# Obtener:

# inicio = rango[0]

# fin = rango[1]

# Crear los números del rango
# usando crear_rango().

# Recorrer esos números
# y agregarlos al set.

# Finalmente convertir el set
# en una lista y ordenarla.


#---- Salida:

# Mostrar una tupla con todos
# los números de un rango.

# Mostrar una lista ordenada
# con los elementos de varios rangos
# sin números repetidos.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# crear_rango(1, 3)


# inicio = 1

# fin = 3

# numeros = []


# Primera repetición:

# numero = 1

# numeros = [1]


# Segunda repetición:

# numero = 2

# numeros = [1, 2]


# Tercera repetición:

# numero = 3

# numeros = [1, 2, 3]


# Convertir a tupla:

# tuple([1, 2, 3])

# (1, 2, 3)


# resultado:

# (1, 2, 3)



# Segunda llamada:

# elementos_en_multiples_rangos(
#     (1, 3),
#     (2, 4)
# )


# elementos = set()


# Primer rango:

# rango = (1, 3)

# inicio = 1

# fin = 3


# crear_rango(1, 3)

# numeros = (1, 2, 3)


# Agregar al set:

# elementos = {1, 2, 3}


# Segundo rango:

# rango = (2, 4)

# inicio = 2

# fin = 4


# crear_rango(2, 4)

# numeros = (2, 3, 4)


# Agregar al set:

# 2 y 3 ya existen.

# 4 es nuevo.


# elementos = {1, 2, 3, 4}


# Convertir a lista:

# [1, 2, 3, 4]


# Ordenar:

# [1, 2, 3, 4]


# resultado:

# [1, 2, 3, 4]



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# Dentro de crear_rango(),
# se recorren los números desde inicio hasta fin.
#
# En cada repetición:
#
# 1. Tomar un número.
#
# 2. Agregarlo a numeros.
#
# El patrón es:
#
# for numero in range(inicio, fin + 1):
#
#     numeros.append(numero)
#
#
# También existe repetición dentro de
# elementos_en_multiples_rangos().
#
# Primero se recorren todos los rangos.
#
# Después se recorren los números
# de cada rango.
#
# El set evita que los números repetidos
# se almacenen más de una vez.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class SelectorRango:

    def crear_rango(self, inicio, fin):

        numeros = []

        for numero in range(inicio, fin + 1):

            numeros.append(numero)

        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):

        elementos = set()

        for rango in rangos:

            inicio = rango[0]

            fin = rango[1]

            numeros = self.crear_rango(inicio, fin)

            for numero in numeros:

                elementos.add(numero)

        return sorted(list(elementos))


sr = SelectorRango()

print(sr.crear_rango(1, 3))

print(
    sr.elementos_en_multiples_rangos(
        (1, 3),
        (2, 4)
    )
)



#-------- 5. PRUEBA DE ESCRITORIO --------

# crear_rango(1, 3):


# numero       numeros

# inicio       []

#   1          [1]

#   2          [1, 2]

#   3          [1, 2, 3]


# convertir a tupla:

# (1, 2, 3)



# elementos_en_multiples_rangos():


# rango      numeros creados      elementos

# (1, 3)     (1, 2, 3)           {1, 2, 3}

# (2, 4)     (2, 3, 4)           {1, 2, 3, 4}


# convertir a lista:

# [1, 2, 3, 4]


# ordenar:

# [1, 2, 3, 4]


# pantalla:

# (1, 2, 3)

# [1, 2, 3, 4]

## Reto: ---- Ejercicio práctico 12 ----

"""Ejercicio: Clase GeneradorIntervalos

Crea una clase llamada GeneradorIntervalos que:

Tenga un método generar_intervalo(desde, hasta) que retorne una tupla con 
todos los números comprendidos entre desde y hasta, incluyendo ambos extremos.
Tenga un método combinar_intervalos(*intervalos) que:
Reciba múltiples tuplas con esta forma:
(desde, hasta)
Reutilice generar_intervalo().
Combine todos los números obtenidos.
Evite números repetidos utilizando un conjunto.
Retorne finalmente una lista con los números únicos."""

class GeneradorIntervalos:
    def generar_intervalo(self, desde, hasta):
        return tuple(range(desde, hasta + 1))

    def combinar_intervalos(self, *intervalos):
        numeros_unicos = set()

        for inicio, fin in intervalos:
            numeros = self.generar_intervalo(inicio, fin)

            for numero in numeros:
                numeros_unicos.add(numero)

        return list(numeros_unicos)


g = GeneradorIntervalos()

print(g.generar_intervalo(3, 7))

print(g.combinar_intervalos(
    (1, 4),
    (3, 6),
    (8, 10)
))

# Ej. 13 -- Combinador de listas


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# lista1

# lista2

# Una o varias listas mediante *listas


#---- Proceso:

# Crear una lista vacía llamada resultado.

# Calcular cuál de las dos listas
# tiene mayor longitud.

# Recorrer las posiciones desde 0
# hasta la longitud de la lista más larga.

# Si existe un elemento en lista1
# para esa posición,
# agregarlo a resultado.

# Si existe un elemento en lista2
# para esa posición,
# agregarlo también a resultado.

# De esta manera,
# los elementos se van intercalando.


# Para intercalar varias listas:

# Verificar si no se recibió ninguna lista.

# Si no hay listas,
# retornar una lista vacía.

# Tomar la primera lista
# como resultado inicial.

# Después recorrer las demás listas.

# Intercalar el resultado actual
# con cada nueva lista.

# Guardar nuevamente el resultado.


#---- Salida:

# Mostrar dos listas intercaladas.

# Mostrar varias listas combinadas
# mediante intercalaciones sucesivas.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# intercalar(
#     [1, 2],
#     [3, 4]
# )


# lista1 = [1, 2]

# lista2 = [3, 4]


# mayor = max(2, 2)

# mayor = 2


# resultado = []


# Primera repetición:

# i = 0


# i < len(lista1)

# 0 < 2 → verdadero

# agregar lista1[0]

# resultado = [1]


# i < len(lista2)

# 0 < 2 → verdadero

# agregar lista2[0]

# resultado = [1, 3]


# Segunda repetición:

# i = 1


# agregar lista1[1]

# resultado = [1, 3, 2]


# agregar lista2[1]

# resultado = [1, 3, 2, 4]


# resultado:

# [1, 3, 2, 4]



# Segunda llamada:

# intercalar_multiples(
#     [1, 2],
#     [3, 4],
#     [5, 6]
# )


# Inicialmente:

# resultado = [1, 2]


# Primera intercalación:

# resultado =
# intercalar([1, 2], [3, 4])


# resultado:

# [1, 3, 2, 4]


# Segunda intercalación:

# resultado =
# intercalar(
#     [1, 3, 2, 4],
#     [5, 6]
# )


# Intercalar:

# 1 con 5

# 3 con 6

# después quedan 2 y 4


# resultado:

# [1, 5, 3, 6, 2, 4]



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# Dentro de intercalar(),
# se recorren las posiciones de las listas.
#
# En cada repetición se intenta:
#
# 1. Agregar el elemento de lista1.
#
# 2. Agregar el elemento de lista2.
#
# Antes de agregar,
# se verifica que la posición exista.
#
# El patrón principal es:
#
# for i in range(mayor):
#
#     if i < len(lista1):
#
#         resultado.append(lista1[i])
#
#     if i < len(lista2):
#
#         resultado.append(lista2[i])
#
#
# También existe un proceso repetitivo
# en intercalar_multiples().
#
# Se toma el resultado actual
# y se intercala con la siguiente lista.
#
# El patrón es:
#
# for i in range(1, len(listas)):
#
#     resultado = self.intercalar(
#         resultado,
#         listas[i]
#     )



#-------- 4. ESCRIBIR EL CÓDIGO --------

class CombinadorListas:

    def intercalar(self, lista1, lista2):

        resultado = []

        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):

            if i < len(lista1):

                resultado.append(lista1[i])

            if i < len(lista2):

                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):

        if len(listas) == 0:

            return []

        resultado = listas[0]

        for i in range(1, len(listas)):

            resultado = self.intercalar(
                resultado,
                listas[i]
            )

        return resultado


cl = CombinadorListas()

print(
    cl.intercalar(
        [1, 2],
        [3, 4]
    )
)

print(
    cl.intercalar_multiples(
        [1, 2],
        [3, 4],
        [5, 6]
    )
)



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera llamada:

# intercalar([1, 2], [3, 4])


# i    lista1[i]    lista2[i]    resultado

# 0        1            3         [1, 3]

# 1        2            4         [1, 3, 2, 4]


# retorno:

# [1, 3, 2, 4]



# Segunda llamada:

# intercalar_multiples(
#     [1, 2],
#     [3, 4],
#     [5, 6]
# )


# resultado inicial:

# [1, 2]


# primera intercalación:

# [1, 2] con [3, 4]

# resultado:

# [1, 3, 2, 4]


# segunda intercalación:

# [1, 3, 2, 4] con [5, 6]


# posición    lista1    lista2    resultado

#    0           1        5       [1, 5]

#    1           3        6       [1, 5, 3, 6]

#    2           2        -       [1, 5, 3, 6, 2]

#    3           4        -       [1, 5, 3, 6, 2, 4]


# pantalla:

# [1, 3, 2, 4]

# [1, 5, 3, 6, 2, 4]

## Reto: ---- Ejercicio práctica 13 ----

"""Ejercicio: Clase MezcladorSecuencias

Crea una clase llamada MezcladorSecuencias que:

Tenga un método mezclar(lista1, lista2) que:
Reciba dos listas.
Retorne una nueva lista alternando sus elementos.
Si una lista tiene elementos sobrantes, estos deben agregarse al final.
Tenga un método mezclar_varias(*listas) que:
Reciba varias listas.
Reutilice mezclar() para combinarlas progresivamente.
Retorne la lista final.

Por ejemplo:

lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

Queremos:

[1, "a", 2, "b", 3, "c"]

Y si las longitudes son diferentes:

lista1 = [1, 2, 3, 4]
lista2 = ["a", "b"]

queremos:

[1, "a", 2, "b", 3, 4]"""

class MezcladorSecuencias:

    def mezclar(self, lista1, lista2):
        resultado = []

        longitud_mayor = max(len(lista1), len(lista2))

        for i in range(longitud_mayor):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def mezclar_varias(self, *listas):

        if len(listas) == 0:
            return []

        resultado = listas[0]

        for lista in listas[1:]:
            resultado = self.mezclar(resultado, lista)

        return resultado


m = MezcladorSecuencias()

print(m.mezclar(
    [1, 2, 3, 4],
    ["a", "b"]
))

print(m.mezclar_varias(
    [1, 2],
    ["a", "b"],
    [True, False]
))

# Ej. 14 -- Mapeo de estudiantes a notas


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# estudiante

# nota

# nota_minima


#---- Proceso:

# Crear un diccionario llamado notas.

# Guardar cada estudiante como clave
# y su nota como valor.

# Para encontrar estudiantes aprobados:

# Recorrer todos los estudiantes.

# Comparar su nota con nota_minima.

# Si la nota es mayor o igual,
# agregar el nombre a aprobados.


# Para encontrar el mejor estudiante:

# Verificar primero si el diccionario
# está vacío.

# Crear una variable mejor_nombre.

# Crear una variable mejor_nota.

# Recorrer todos los estudiantes.

# Comparar cada nota
# con la mejor encontrada hasta el momento.

# Si la nueva nota es mayor,
# actualizar mejor_nota
# y mejor_nombre.

# Finalmente retornar ambos valores
# dentro de una tupla.


#---- Salida:

# Mostrar los estudiantes aprobados.

# Mostrar el nombre y la nota
# del mejor estudiante.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# rn = RegistroNotas()


# Al iniciar:

# notas = {}


# Registrar Ana:

# notas = {
#     "Ana": 95
# }


# Registrar Bob:

# notas = {
#     "Ana": 95,
#     "Bob": 70
# }


# Registrar Carlos:

# notas = {
#     "Ana": 95,
#     "Bob": 70,
#     "Carlos": 88
# }


# Buscar aprobados con nota mínima 70:


# Ana:

# 95 >= 70

# verdadero

# aprobados = ["Ana"]


# Bob:

# 70 >= 70

# verdadero

# aprobados = ["Ana", "Bob"]


# Carlos:

# 88 >= 70

# verdadero

# aprobados = ["Ana", "Bob", "Carlos"]


# Buscar mejor estudiante:


# Inicialmente:

# mejor_nombre = None

# mejor_nota = -1


# Ana:

# nota = 95

# 95 > -1

# verdadero

# mejor_nota = 95

# mejor_nombre = "Ana"


# Bob:

# nota = 70

# 70 > 95

# falso


# Carlos:

# nota = 88

# 88 > 95

# falso


# resultado:

# ["Ana", "Bob", "Carlos"]

# ("Ana", 95)



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# Dentro de estudiantes_aprobados(),
# cada estudiante pasa por el mismo proceso:
#
# 1. Obtener su nombre y nota.
#
# 2. Comparar la nota con nota_minima.
#
# 3. Si cumple la condición,
#    agregar el nombre a aprobados.
#
# El patrón es:
#
# for estudiante, nota in self.notas.items():
#
#     if nota >= nota_minima:
#
#         aprobados.append(estudiante)
#
#
# También existe un proceso repetitivo
# dentro de mejor_estudiante().
#
# Cada nota se compara con
# la mejor encontrada hasta el momento.
#
# Si una nota es mayor:
#
# mejor_nota = nota
#
# mejor_nombre = estudiante
#
# Este proceso se conoce como
# patrón campeón.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class RegistroNotas:

    def __init__(self):

        self.notas = {}

    def registrar(self, estudiante, nota):

        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):

        aprobados = []

        for estudiante, nota in self.notas.items():

            if nota >= nota_minima:

                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):

        if len(self.notas) == 0:

            return None

        mejor_nombre = None

        mejor_nota = -1

        for estudiante, nota in self.notas.items():

            if nota > mejor_nota:

                mejor_nota = nota

                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()

rn.registrar("Ana", 95)

rn.registrar("Bob", 70)

rn.registrar("Carlos", 88)

print(rn.estudiantes_aprobados(70))

print(rn.mejor_estudiante())



#-------- 5. PRUEBA DE ESCRITORIO --------

# notas:

# {
#     "Ana": 95,
#     "Bob": 70,
#     "Carlos": 88
# }


# estudiantes_aprobados(70):


# estudiante    nota    nota >= 70    aprobados

# Ana            95         Sí         ["Ana"]

# Bob            70         Sí         ["Ana", "Bob"]

# Carlos         88         Sí         ["Ana", "Bob", "Carlos"]


# retorno:

# ["Ana", "Bob", "Carlos"]



# mejor_estudiante():


# estudiante    nota    mejor_nota    mejor_nombre

# inicio                    -1             None

# Ana            95         95             "Ana"

# Bob            70         95             "Ana"

# Carlos         88         95             "Ana"


# retorno:

# ("Ana", 95)


# pantalla:

# ['Ana', 'Bob', 'Carlos']

# ('Ana', 95)

## Reto: ---- Ejercicio práctica 14 ----

"""Ejercicio: Clase RegistroVentas

Crea una clase llamada RegistroVentas que:

Tenga un método registrar_vendedor(nombre, ventas) que guarde en un diccionario:
vendedor → cantidad de ventas
Tenga un método vendedores_objetivo(ventas_minimas) que:
Retorne una lista con los nombres de los vendedores cuyas ventas sean mayores o iguales a ventas_minimas.
Tenga un método mejor_vendedor() que:
Retorne el nombre y la cantidad de ventas del vendedor con más ventas.
Si no existen vendedores registrados, retorne None."""

class RegistroVentas:
    def __init__(self):
        self.vendedores = {}

    def registrar_vendedor(self, nombre, ventas):
        self.vendedores[nombre] = ventas

    def vendedores_objetivo(self, ventas_minimas):
        encontrados = []

        for nombre, ventas in self.vendedores.items():
            if ventas >= ventas_minimas:
                encontrados.append(nombre)

        return encontrados

    def mejor_vendedor(self):
        if len(self.vendedores) == 0:
            return None

        mejor_nombre = None
        mayor_ventas = -1

        for nombre, ventas in self.vendedores.items():
            if ventas > mayor_ventas:
                mayor_ventas = ventas
                mejor_nombre = nombre

        return (mejor_nombre, mayor_ventas)


rv = RegistroVentas()

rv.registrar_vendedor("Ana", 35)
rv.registrar_vendedor("Carlos", 20)
rv.registrar_vendedor("Maria", 48)
rv.registrar_vendedor("Pedro", 31)
rv.registrar_vendedor("Lucia", 12)

print(rv.vendedores_objetivo(30))
print(rv.mejor_vendedor())

# Ej. 15 -- Divisores de un número


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# numero

# varios números mediante *numeros


#---- Proceso:

# Crear un método encontrar_divisores().

# Recorrer los números desde 1
# hasta numero.

# Verificar cuáles dividen exactamente
# al número.

# Si numero % i == 0,
# agregar i a la lista divisores.

# Convertir la lista en una tupla
# y retornarla.


# Para verificar si un número es perfecto:

# Obtener sus divisores.

# Sumar todos los divisores
# excepto el mismo número.

# Comparar la suma con numero.

# Si son iguales,
# retornar True.

# Si no,
# retornar False.


# Para varios números:

# Recorrer cada número recibido.

# Obtener sus divisores.

# Guardar en un diccionario:

# numero -> divisores


#---- Salida:

# Mostrar los divisores de un número.

# Mostrar True o False
# dependiendo de si es perfecto.

# Mostrar un diccionario
# con varios números y sus divisores.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# encontrar_divisores(12)


# divisores = []


# Probar desde 1 hasta 12:


# i = 1

# 12 % 1 = 0

# divisores = [1]


# i = 2

# 12 % 2 = 0

# divisores = [1, 2]


# i = 3

# 12 % 3 = 0

# divisores = [1, 2, 3]


# i = 4

# 12 % 4 = 0

# divisores = [1, 2, 3, 4]


# i = 5

# 12 % 5 != 0

# no se agrega


# i = 6

# 12 % 6 = 0

# divisores = [1, 2, 3, 4, 6]


# i = 12

# 12 % 12 = 0

# divisores = [1, 2, 3, 4, 6, 12]


# convertir a tupla:

# (1, 2, 3, 4, 6, 12)



# Segunda llamada:

# es_perfecto(6)


# divisores de 6:

# (1, 2, 3, 6)


# sumar todos excepto 6:

# 1 + 2 + 3

# suma = 6


# comparar:

# 6 == 6

# verdadero


# return True



# Tercera llamada:

# encontrar_multiples_divisores(6, 10, 12)


# resultado:

# {
#     6: (1, 2, 3, 6),
#     10: (1, 2, 5, 10),
#     12: (1, 2, 3, 4, 6, 12)
# }



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# Dentro de encontrar_divisores(),
# se prueba cada número desde 1
# hasta numero.
#
# En cada repetición se verifica:
#
# numero % i == 0
#
# Si se cumple,
# significa que i es divisor.
#
# Entonces:
#
# divisores.append(i)
#
#
# También existe repetición
# dentro de es_perfecto().
#
# Se recorren los divisores
# y se suman todos menos el propio número.
#
#
# Finalmente,
# encontrar_multiples_divisores()
# repite el proceso para varios números
# recibidos mediante *numeros.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class DivisorFinder:

    def encontrar_divisores(self, numero):

        divisores = []

        for i in range(1, numero + 1):

            if numero % i == 0:

                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):

        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:

            if divisor != numero:

                suma += divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):

        resultado = {}

        for numero in numeros:

            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


df = DivisorFinder()

print(df.encontrar_divisores(12))

print(df.es_perfecto(6))

print(df.encontrar_multiples_divisores(6, 10, 12))



#-------- 5. PRUEBA DE ESCRITORIO --------

# encontrar_divisores(12):


# i      12 % i      ¿divisor?      divisores

# 1         0            Sí          [1]

# 2         0            Sí          [1, 2]

# 3         0            Sí          [1, 2, 3]

# 4         0            Sí          [1, 2, 3, 4]

# 5         2            No          [1, 2, 3, 4]

# 6         0            Sí          [1, 2, 3, 4, 6]

# 7         5            No          [1, 2, 3, 4, 6]

# 8         4            No          [1, 2, 3, 4, 6]

# 9         3            No          [1, 2, 3, 4, 6]

# 10        2            No          [1, 2, 3, 4, 6]

# 11        1            No          [1, 2, 3, 4, 6]

# 12        0            Sí          [1, 2, 3, 4, 6, 12]


# retorno:

# (1, 2, 3, 4, 6, 12)



# es_perfecto(6):


# divisores:

# (1, 2, 3, 6)


# divisor      suma

# 1             1

# 2             3

# 3             6

# 6             6


# comparar:

# 6 == 6

# True



# encontrar_multiples_divisores:


# numero      divisores

#   6         (1, 2, 3, 6)

#  10         (1, 2, 5, 10)

#  12         (1, 2, 3, 4, 6, 12)


# pantalla:

# (1, 2, 3, 4, 6, 12)

# True

# {6: (1, 2, 3, 6), 10: (1, 2, 5, 10), 12: (1, 2, 3, 4, 6, 12)}

## Reto: ---- Ejercicio práctica 15 ----

"""Ejercicio: Clase FactorAnalyzer

Crea una clase llamada FactorAnalyzer que:

Tenga un método encontrar_factores_pares(numero) que retorne una tupla con todos los divisores pares del número.
Tenga un método tiene_muchos_factores_pares(numero) que:
Reutilice encontrar_factores_pares(numero).
Retorne True si el número tiene 3 o más divisores pares.
Retorne False en caso contrario.
Tenga un método analizar_varios(*numeros) que:
Reciba varios números.
Reutilice encontrar_factores_pares().
Retorne un diccionario:
{
    numero: tupla_de_factores_pares
}

Por ejemplo:

12 → (2, 4, 6, 12)
10 → (2, 10)
8  → (2, 4, 8)"""

class FactorAnalyzer:
    def encontrar_factores_pares(self, numero):
        factores = []

        for divisor in range(1, numero + 1):
            if numero % divisor == 0 and divisor % 2 == 0:
                factores.append(divisor)

        return tuple(factores)

    def tiene_muchos_factores_pares(self, numero):
        factores = self.encontrar_factores_pares(numero)

        if len(factores) >= 3:
            return True
        else:
            return False

    def analizar_varios(self, *numeros):
        resultados = {}

        for numero in numeros:
            resultados[numero] = self.encontrar_factores_pares(numero)

        return resultados


f = FactorAnalyzer()

print(f.encontrar_factores_pares(12))
print(f.tiene_muchos_factores_pares(12))
print(f.tiene_muchos_factores_pares(10))

print(f.analizar_varios(
    12,
    10,
    18,
    15
))

# Ej. 16 -- Codificador/Decodificador


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# palabra

# desplazamiento


#---- Proceso:

# Crear una clase llamada CodificadorCesar.

# Crear un diccionario llamado historial
# para guardar las palabras codificadas.


# Para codificar una letra:

# Verificar si la letra es minúscula.

# Obtener su posición dentro del alfabeto
# usando ord().

# Sumar el desplazamiento.

# Usar % 26 para evitar salir
# de las 26 letras del alfabeto.

# Convertir nuevamente la posición
# en una letra usando chr().


# Si la letra es mayúscula:

# realizar el mismo procedimiento,
# pero tomando como referencia "A".


# Si el carácter no es una letra:

# devolverlo sin modificar.


# Para codificar una palabra:

# Recorrer cada letra.

# Codificarla mediante codificar_letra().

# Agregar cada letra codificada
# a la variable resultado.

# Guardar en historial:

# (palabra, desplazamiento) -> resultado


#---- Salida:

# Mostrar la palabra codificada.

# Mostrar el historial
# de codificaciones realizadas.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# cc = CodificadorCesar()


# Al iniciar:

# historial = {}


# Se llama:

# codificar_palabra("hola", 3)


# resultado = ""


# Primera letra:

# letra = "h"


# Obtener posición:

# ord("h") - ord("a")

# posicion = 7


# Aplicar desplazamiento:

# nueva_posicion = (7 + 3) % 26

# nueva_posicion = 10


# Convertir nuevamente a letra:

# chr(10 + ord("a"))

# resultado de la letra:

# "k"


# resultado = "k"



# Segunda letra:

# letra = "o"

# posicion = 14

# nueva_posicion = 17

# letra nueva = "r"


# resultado = "kr"



# Tercera letra:

# letra = "l"

# posicion = 11

# nueva_posicion = 14

# letra nueva = "o"


# resultado = "kro"



# Cuarta letra:

# letra = "a"

# posicion = 0

# nueva_posicion = 3

# letra nueva = "d"


# resultado = "krod"


# Guardar en historial:

# historial[
#     ("hola", 3)
# ] = "krod"


# resultado:

# krod

# {
#     ("hola", 3): "krod"
# }



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Dentro de codificar_palabra(),
# cada letra pasa por el mismo proceso:
#
# 1. Tomar una letra.
#
# 2. Enviarla a codificar_letra().
#
# 3. Aplicar el desplazamiento.
#
# 4. Agregar la nueva letra
#    a resultado.
#
# El patrón principal es:
#
# for letra in palabra:
#
#     resultado += self.codificar_letra(
#         letra,
#         desplazamiento
#     )
#
#
# También se repite una lógica
# dentro de codificar_letra():
#
# obtener posición
#
# sumar desplazamiento
#
# aplicar % 26
#
# convertir nuevamente a letra.
#
# El % 26 permite volver al inicio
# del alfabeto cuando se supera la "z".



#-------- 4. ESCRIBIR EL CÓDIGO --------

class CodificadorCesar:

    def __init__(self):

        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):

        if letra.islower():

            posicion = ord(letra) - ord("a")

            nueva_posicion = (posicion + desplazamiento) % 26

            return chr(nueva_posicion + ord("a"))

        elif letra.isupper():

            posicion = ord(letra) - ord("A")

            nueva_posicion = (posicion + desplazamiento) % 26

            return chr(nueva_posicion + ord("A"))

        else:

            return letra

    def codificar_palabra(self, palabra, desplazamiento):

        resultado = ""

        for letra in palabra:

            resultado += self.codificar_letra(
                letra,
                desplazamiento
            )

        self.historial[(palabra, desplazamiento)] = resultado

        return resultado


cc = CodificadorCesar()

print(cc.codificar_palabra("hola", 3))

print(cc.historial)



#-------- 5. PRUEBA DE ESCRITORIO --------

# palabra = "hola"

# desplazamiento = 3


# letra    posición    +3    nueva letra    resultado

#  h          7        10        k           "k"

#  o         14        17        r           "kr"

#  l         11        14        o           "kro"

#  a          0         3        d           "krod"


# historial:

# {
#     ("hola", 3): "krod"
# }


# pantalla:

# krod

# {('hola', 3): 'krod'}

## Reto: ---- Ejercicio práctica 16 ----

"""Ejercicio: Clase CodificadorDigitos

Crea una clase llamada CodificadorDigitos que:

Tenga un método desplazar_digito(digito, desplazamiento) que:
Reciba un dígito entre 0 y 9.
Lo desplace cierta cantidad de posiciones.
Cuando llegue después del 9, vuelva a comenzar desde 0.
Debe utilizar el operador %.
Tenga un método codificar_secuencia(secuencia, desplazamiento) que:
Reciba una cadena formada por números.
Reutilice desplazar_digito() para codificar cada dígito.
Retorne la nueva secuencia codificada.
Tenga un diccionario como atributo llamado historial que:
Guarde cada secuencia original como clave.
Guarde la secuencia codificada como valor.

Por ejemplo:

"7892" con desplazamiento 3

debería convertirse en:

"0125" """

class CodificadorDigitos:
    def __init__(self):
        self.historial = {}

    def desplazar_digito(self, digito, desplazamiento):
        nuevo_digito = (digito + desplazamiento) % 10
        return nuevo_digito

    def codificar_secuencia(self, secuencia, desplazamiento):
        resultado = ""

        for digito in secuencia:
            numero = int(digito)

            nuevo_digito = self.desplazar_digito(
                numero,
                desplazamiento
            )

            resultado += str(nuevo_digito)

        self.historial[secuencia] = resultado

        return resultado


c = CodificadorDigitos()

print(c.codificar_secuencia("7892", 3))
print(c.codificar_secuencia("9087", 4))
print(c.codificar_secuencia("123", 2))

print(c.historial)

# Ej. 17 -- Grupo de edades


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# Una o varias edades.

# categoria


#---- Proceso:

# Crear un diccionario llamado grupos
# con cuatro categorías:

# niño

# adolescente

# adulto

# mayor


# Crear un método clasificar_edad().

# Si la edad es menor o igual a 12,
# clasificar como "niño".

# Si la edad está entre 13 y 17,
# clasificar como "adolescente".

# Si la edad está entre 18 y 64,
# clasificar como "adulto".

# Si la edad es mayor a 64,
# clasificar como "mayor".


# Para agrupar varias edades:

# Reiniciar el diccionario grupos.

# Recorrer cada edad recibida.

# Obtener su categoría.

# Agregar la edad a la lista
# correspondiente.


# Para calcular el promedio:

# Obtener las edades
# de la categoría indicada.

# Si la categoría está vacía,
# retornar 0.

# Si tiene edades,
# sumar todas y dividir
# entre la cantidad.


#---- Salida:

# Mostrar las edades agrupadas
# según su categoría.

# Mostrar el promedio de edad
# de una categoría determinada.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# ae = AgrupadorEdades()


# Se reciben las edades:

# 5, 15, 30, 70


# Primera edad:

# edad = 5

# 5 <= 12

# categoria = "niño"


# grupos:

# {
#     "niño": [5],
#     "adolescente": [],
#     "adulto": [],
#     "mayor": []
# }


# Segunda edad:

# edad = 15

# 15 <= 12 → falso

# 15 <= 17 → verdadero

# categoria = "adolescente"


# grupos:

# {
#     "niño": [5],
#     "adolescente": [15],
#     "adulto": [],
#     "mayor": []
# }


# Tercera edad:

# edad = 30

# 30 <= 64

# categoria = "adulto"


# grupos:

# {
#     "niño": [5],
#     "adolescente": [15],
#     "adulto": [30],
#     "mayor": []
# }


# Cuarta edad:

# edad = 70

# No cumple las condiciones anteriores.

# categoria = "mayor"


# grupos:

# {
#     "niño": [5],
#     "adolescente": [15],
#     "adulto": [30],
#     "mayor": [70]
# }


# Calcular promedio de "adulto":

# edades = [30]

# sum(edades) = 30

# len(edades) = 1

# promedio = 30 / 1

# promedio = 30


# resultado:

# {
#     "niño": [5],
#     "adolescente": [15],
#     "adulto": [30],
#     "mayor": [70]
# }

# 30.0



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe
# un proceso repetitivo.
#
# Dentro de agrupar_por_categoria(),
# cada edad pasa por el mismo proceso:
#
# 1. Tomar una edad.
#
# 2. Clasificarla.
#
# 3. Obtener su categoría.
#
# 4. Agregarla a la lista
#    correspondiente.
#
# El patrón principal es:
#
# for edad in edades:
#
#     categoria = self.clasificar_edad(edad)
#
#     self.grupos[categoria].append(edad)
#
# Este proceso se repite
# para todas las edades recibidas.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class AgrupadorEdades:

    def __init__(self):

        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):

        if edad <= 12:

            return "niño"

        elif edad <= 17:

            return "adolescente"

        elif edad <= 64:

            return "adulto"

        else:

            return "mayor"

    def agrupar_por_categoria(self, *edades):

        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:

            categoria = self.clasificar_edad(edad)

            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):

        edades = self.grupos[categoria]

        if len(edades) == 0:

            return 0

        return sum(edades) / len(edades)


ae = AgrupadorEdades()

print(
    ae.agrupar_por_categoria(
        5, 15, 30, 70
    )
)

print(ae.edad_promedio_categoria("adulto"))



#-------- 5. PRUEBA DE ESCRITORIO --------

# edades = (5, 15, 30, 70)


# edad    categoría         grupo después

#  5     niño              niño = [5]

# 15     adolescente       adolescente = [15]

# 30     adulto            adulto = [30]

# 70     mayor             mayor = [70]


# grupos finales:

# {
#     "niño": [5],
#     "adolescente": [15],
#     "adulto": [30],
#     "mayor": [70]
# }


# promedio de "adulto":

# edades = [30]

# sum(edades) = 30

# len(edades) = 1

# promedio = 30 / 1

# promedio = 30.0


# pantalla:

# {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# 30.0

## Reto: ---- Ejercicio práctica 17 ----

"""Ejercicio: Clase AgrupadorNotas

Crea una clase llamada AgrupadorNotas que:

Tenga un método clasificar_nota(nota) que retorne una categoría según la nota:
Menor de 60 → "baja"
De 60 a 79 → "media"
De 80 a 89 → "alta"
De 90 a 100 → "excelente"
Tenga un método agrupar_por_nivel(*notas) que:
Reciba varias notas.
Reutilice clasificar_nota().
Retorne un diccionario con esta estructura:
{
    "baja": [notas],
    "media": [notas],
    "alta": [notas],
    "excelente": [notas]
}
Tenga un método promedio_nivel(nivel) que:
Reciba una categoría, por ejemplo "alta".
Calcule el promedio de las notas pertenecientes a esa categoría.
Si la categoría no existe o no tiene notas, retorne 0."""

class AgrupadorNotas:
    def __init__(self):
        self.grupos = {
            "baja": [],
            "media": [],
            "alta": [],
            "excelente": []
        }

    def clasificar_nota(self, nota):
        if nota < 60:
            return "baja"
        elif nota < 80:
            return "media"
        elif nota < 90:
            return "alta"
        else:
            return "excelente"

    def agrupar_por_nivel(self, *notas):
        self.grupos = {
            "baja": [],
            "media": [],
            "alta": [],
            "excelente": []
        }

        for nota in notas:
            categoria = self.clasificar_nota(nota)
            self.grupos[categoria].append(nota)

        return self.grupos

    def promedio_nivel(self, nivel):
        if nivel not in self.grupos:
            return 0

        if len(self.grupos[nivel]) == 0:
            return 0

        return sum(self.grupos[nivel]) / len(self.grupos[nivel])


a = AgrupadorNotas()

print(a.agrupar_por_nivel(
    45,
    72,
    93,
    85,
    51,
    78,
    99
))

print(a.promedio_nivel("media"))
print(a.promedio_nivel("excelente"))

# Ej. 18 -- Matriz de distancias

#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# p1

# p2

# referencia

# uno o varios puntos


#---- Proceso:

# Crear una lista llamada distancias.

# Para calcular la distancia entre dos puntos:

# Obtener las coordenadas de p1:

# x1

# y1

# Obtener las coordenadas de p2:

# x2

# y2

# Aplicar la fórmula de distancia euclidiana.

# Guardar la distancia calculada
# dentro de self.distancias.

# Retornar la distancia.


# Para buscar el punto más cercano:

# Recibir un punto de referencia.

# Recibir varios puntos mediante *puntos.

# Si no existen puntos,
# retornar None.

# Recorrer todos los puntos.

# Calcular la distancia entre
# la referencia y cada punto.

# Comparar cada distancia
# con la menor encontrada.

# Si la nueva distancia es menor,
# actualizar:

# menor_distancia

# cercano


#---- Salida:

# Mostrar la distancia entre dos puntos.

# Mostrar el punto más cercano
# al punto de referencia.

# Mostrar todas las distancias
# calculadas durante el programa.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# cd = CalculadorDistancia()


# Al iniciar:

# distancias = []


# Primera llamada:

# distancia_euclidiana(
#     (0, 0),
#     (3, 4)
# )


# p1 = (0, 0)

# p2 = (3, 4)


# x1 = 0

# y1 = 0

# x2 = 3

# y2 = 4


# Calcular:

# distancia =
# ((3 - 0) ** 2 + (4 - 0) ** 2) ** 0.5


# distancia =
# (3 ** 2 + 4 ** 2) ** 0.5


# distancia =
# (9 + 16) ** 0.5


# distancia =
# 25 ** 0.5


# distancia = 5


# Guardar:

# distancias = [5.0]


# resultado:

# 5.0



# Segunda llamada:

# punto_mas_cercano(
#     (0, 0),
#     (5, 5),
#     (1, 1),
#     (10, 10)
# )


# referencia = (0, 0)


# Inicialmente:

# cercano = None

# menor_distancia = None


# Primer punto:

# punto = (5, 5)


# distancia:

# ((5 - 0)² + (5 - 0)²) ** 0.5

# distancia ≈ 7.07


# Como menor_distancia es None:

# menor_distancia ≈ 7.07

# cercano = (5, 5)



# Segundo punto:

# punto = (1, 1)


# distancia:

# ((1 - 0)² + (1 - 0)²) ** 0.5

# distancia ≈ 1.41


# 1.41 < 7.07

# verdadero


# menor_distancia ≈ 1.41

# cercano = (1, 1)



# Tercer punto:

# punto = (10, 10)


# distancia:

# ((10 - 0)² + (10 - 0)²) ** 0.5

# distancia ≈ 14.14


# 14.14 < 1.41

# falso


# cercano sigue siendo:

# (1, 1)


# resultado:

# (1, 1)



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe
# un proceso repetitivo.
#
# Dentro de punto_mas_cercano(),
# cada punto pasa por el mismo proceso:
#
# 1. Tomar un punto.
#
# 2. Calcular su distancia
#    respecto a la referencia.
#
# 3. Comparar esa distancia
#    con la menor encontrada.
#
# 4. Si es menor,
#    actualizar el punto más cercano.
#
# El patrón principal es:
#
# for punto in puntos:
#
#     distancia = self.distancia_euclidiana(
#         referencia,
#         punto
#     )
#
#     if menor_distancia is None
#     or distancia < menor_distancia:
#
#         menor_distancia = distancia
#
#         cercano = punto
#
#
# Este proceso funciona como
# un patrón campeón,
# pero buscando el valor menor.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class CalculadorDistancia:

    def __init__(self):

        self.distancias = []

    def distancia_euclidiana(self, p1, p2):

        x1 = p1[0]

        y1 = p1[1]

        x2 = p2[0]

        y2 = p2[1]

        distancia = (
            (x2 - x1) ** 2
            + (y2 - y1) ** 2
        ) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):

        if len(puntos) == 0:

            return None

        cercano = None

        menor_distancia = None

        for punto in puntos:

            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )

            if (
                menor_distancia is None
                or distancia < menor_distancia
            ):

                menor_distancia = distancia

                cercano = punto

        return cercano


cd = CalculadorDistancia()

print(
    cd.distancia_euclidiana(
        (0, 0),
        (3, 4)
    )
)

print(
    cd.punto_mas_cercano(
        (0, 0),
        (5, 5),
        (1, 1),
        (10, 10)
    )
)

print(cd.distancias)



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera llamada:


# p1        p2        distancia

# (0,0)     (3,4)        5.0


# distancias:

# [5.0]



# punto_mas_cercano():

# referencia = (0, 0)


# punto      distancia     menor_distancia     cercano

# (5,5)       7.07             7.07           (5,5)

# (1,1)       1.41             1.41           (1,1)

# (10,10)    14.14             1.41           (1,1)


# retorno:

# (1, 1)


# self.distancias contiene
# todas las distancias calculadas:

# 5.0

# distancia hacia (5,5) ≈ 7.071

# distancia hacia (1,1) ≈ 1.414

# distancia hacia (10,10) ≈ 14.142


# pantalla:

# 5.0

# (1, 1)

# [5.0, 7.0710678118654755, 1.4142135623730951, 14.142135623730951]

## Reto: ---- Ejercicio práctica 18 ----

"""Ejercicio: Clase AnalizadorCoordenadas

Crea una clase llamada AnalizadorCoordenadas que:

Tenga un método distancia_manhattan(p1, p2) que:
Reciba dos puntos representados mediante tuplas (x, y).
Calcule la distancia Manhattan entre ellos.
Guarde cada distancia calculada en una lista interna.
Retorne la distancia.
Tenga un método punto_mas_proximo(referencia, *puntos) que:
Reciba un punto de referencia.
Reciba varios puntos mediante *puntos.
Reutilice distancia_manhattan().
Retorne el punto cuya distancia respecto a la referencia sea menor.
Tenga un atributo llamado historial_distancias que:
Guarde todas las distancias que se hayan calculado."""

class AnalizadorCoordenadas:
    def __init__(self):
        self.historial_distancias = []

    def distancia_manhattan(self, p1, p2):
        distancia_x = abs(p1[0] - p2[0])
        distancia_y = abs(p1[1] - p2[1])

        distancia = distancia_x + distancia_y

        self.historial_distancias.append(distancia)

        return distancia

    def punto_mas_proximo(self, referencia, *puntos):
        menor_distancia = float("inf")
        punto_cercano = None

        for punto in puntos:
            distancia = self.distancia_manhattan(
                referencia,
                punto
            )

            if distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto

        return punto_cercano


a = AnalizadorCoordenadas()

print(a.distancia_manhattan(
    (2, 3),
    (5, 7)
))

print(a.punto_mas_proximo(
    (0, 0),
    (4, 5),
    (1, 2),
    (3, 3)
))

print(a.historial_distancias)

# Ej. 19 -- Inventario de productos


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# producto

# cantidad

# minimo


#---- Proceso:

# Crear un diccionario llamado productos.

# Cada producto se guarda como clave.

# Su cantidad disponible
# se guarda como valor.


# Para agregar stock:

# Verificar si el producto ya existe.

# Si existe,
# aumentar su cantidad.

# Si no existe,
# crear el producto
# con la cantidad indicada.


# Para restar stock:

# Verificar si el producto existe.

# Si no existe,
# retornar False.

# Si existe,
# verificar si tiene suficiente stock.

# Si la cantidad disponible
# es mayor o igual a la solicitada,
# restar la cantidad
# y retornar True.

# Si no hay suficiente stock,
# retornar False.


# Para buscar productos con bajo stock:

# Recorrer todos los productos.

# Comparar su cantidad con minimo.

# Si la cantidad es menor,
# agregar el nombre del producto
# a la lista bajos.


#---- Salida:

# Mostrar True o False
# según si se pudo restar el stock.

# Mostrar el inventario actualizado.

# Mostrar los productos
# que tienen bajo stock.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# inv = Inventario()


# Al iniciar:

# productos = {}


# Agregar pan:

# producto = "pan"

# cantidad = 50


# "pan" no existe.


# productos = {
#     "pan": 50
# }


# Agregar leche:

# producto = "leche"

# cantidad = 10


# "leche" no existe.


# productos = {
#     "pan": 50,
#     "leche": 10
# }


# Restar stock de pan:

# producto = "pan"

# cantidad = 30


# "pan" existe.


# stock actual:

# 50


# verificar:

# 50 >= 30

# verdadero


# restar:

# 50 - 30 = 20


# productos = {
#     "pan": 20,
#     "leche": 10
# }


# return True



# Buscar productos bajo stock:

# minimo = 15


# pan:

# cantidad = 20

# 20 < 15

# falso


# leche:

# cantidad = 10

# 10 < 15

# verdadero


# bajos = ["leche"]


# resultado:

# True

# {
#     "pan": 20,
#     "leche": 10
# }

# ["leche"]



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe
# un proceso repetitivo.
#
# Dentro de productos_bajo_stock(),
# cada producto pasa por el mismo proceso:
#
# 1. Obtener su nombre y cantidad.
#
# 2. Comparar la cantidad con minimo.
#
# 3. Si la cantidad es menor,
#    agregar el producto a bajos.
#
# El patrón principal es:
#
# for producto, cantidad in self.productos.items():
#
#     if cantidad < minimo:
#
#         bajos.append(producto)
#
#
# En agregar_stock() no hay ciclo.
#
# Solo se verifica si el producto existe
# para decidir si se suma a su stock
# o se crea por primera vez.
#
#
# En restar_stock() tampoco hay ciclo.
#
# Se realizan validaciones
# antes de modificar la cantidad.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class Inventario:

    def __init__(self):

        self.productos = {}

    def agregar_stock(self, producto, cantidad):

        if producto in self.productos:

            self.productos[producto] += cantidad

        else:

            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):

        if producto not in self.productos:

            return False

        if self.productos[producto] >= cantidad:

            self.productos[producto] -= cantidad

            return True

        return False

    def productos_bajo_stock(self, minimo):

        bajos = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:

                bajos.append(producto)

        return bajos


inv = Inventario()

inv.agregar_stock("pan", 50)

inv.agregar_stock("leche", 10)

print(inv.restar_stock("pan", 30))

print(inv.productos)

print(inv.productos_bajo_stock(15))



#-------- 5. PRUEBA DE ESCRITORIO --------

# productos iniciales:

# {
#     "pan": 50,
#     "leche": 10
# }


# restar_stock("pan", 30):


# producto    stock    cantidad a restar    ¿se puede?

# pan          50             30               Sí


# nuevo stock:

# pan = 20


# return:

# True


# productos:

# {
#     "pan": 20,
#     "leche": 10
# }



# productos_bajo_stock(15):


# producto    cantidad    cantidad < 15    bajos

# pan            20            No           []

# leche          10            Sí           ["leche"]


# pantalla:

# True

# {'pan': 20, 'leche': 10}

# ['leche']

## Reto: ---- Ejercicio práctica 19 ----

"""Ejercicio: Clase BilleteraVirtual

Crea una clase llamada BilleteraVirtual que:

Tenga un método agregar_saldo(cuenta, cantidad) que:
Guarde las cuentas y sus saldos en un diccionario.
Si la cuenta ya existe, debe sumar la nueva cantidad al saldo existente.
Si no existe, debe crearla con esa cantidad.
Tenga un método retirar_saldo(cuenta, cantidad) que:
Reste dinero solamente si la cuenta existe y tiene saldo suficiente.
Retorne True si pudo realizar el retiro.
Retorne False si no pudo hacerlo.
Tenga un método cuentas_bajo_saldo(minimo) que:
Retorne una lista con los nombres de las cuentas cuyo saldo sea menor que minimo.

Por ejemplo, podríamos tener:

{
    "Ana": 500,
    "Carlos": 120,
    "Maria": 850
}"""

class BilleteraVirtual:
    def __init__(self):
        self.cuentas = {}

    def agregar_saldo(self, cuenta, cantidad):
        if cuenta in self.cuentas:
            self.cuentas[cuenta] += cantidad
        else:
            self.cuentas[cuenta] = cantidad

    def retirar_saldo(self, cuenta, cantidad):
        if cuenta in self.cuentas and self.cuentas[cuenta] >= cantidad:
            self.cuentas[cuenta] -= cantidad
            return True
        else:
            return False

    def cuentas_bajo_saldo(self, minimo):
        encontrados = []

        for cuenta, saldo in self.cuentas.items():
            if saldo < minimo:
                encontrados.append(cuenta)

        return encontrados


b = BilleteraVirtual()

b.agregar_saldo("Ana", 500)
b.agregar_saldo("Carlos", 150)
b.agregar_saldo("Maria", 900)
b.agregar_saldo("Pedro", 80)

b.agregar_saldo("Ana", 200)

print(b.cuentas)

print(b.retirar_saldo("Ana", 250))
print(b.retirar_saldo("Carlos", 500))

print(b.cuentas_bajo_saldo(200))

print(b.cuentas)

# Ej. 20 -- Analizador de patrones en texto


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# texto

# patron


#---- Proceso:

# Crear una variable ultimo_texto
# para guardar el texto más reciente analizado.


# En encontrar_palabras():

# Guardar el texto recibido
# en ultimo_texto.

# Separar el texto en palabras
# usando split().

# Crear una lista vacía llamada encontradas.

# Recorrer cada palabra.

# Verificar si la palabra
# comienza con el patrón indicado.

# Si comienza con el patrón,
# agregarla a encontradas.


# En agrupar_por_longitud():

# Guardar el nuevo texto
# en ultimo_texto.

# Separar el texto en palabras.

# Crear un diccionario llamado grupos.

# Obtener la longitud de cada palabra.

# Si esa longitud todavía no existe
# como clave del diccionario,
# crear una lista vacía.

# Agregar la palabra
# a la lista correspondiente.


# En palabras_unicas():

# Tomar ultimo_texto.

# Separarlo en palabras.

# Convertir las palabras en un set
# para eliminar duplicados.


#---- Salida:

# Mostrar las palabras
# que empiezan con un patrón.

# Mostrar las palabras agrupadas
# según su longitud.

# Mostrar las palabras únicas
# del último texto analizado.



#-------- 2. BOSQUEJO A MANO ------------

# Se crea:

# ap = AnalizadorPatrones()


# Primera llamada:

# encontrar_palabras(
#     "el gato grande juega",
#     "g"
# )


# ultimo_texto = "el gato grande juega"


# palabras:

# ["el", "gato", "grande", "juega"]


# encontradas = []


# Primera palabra:

# palabra = "el"

# "el".startswith("g")

# falso


# Segunda palabra:

# palabra = "gato"

# "gato".startswith("g")

# verdadero

# encontradas = ["gato"]


# Tercera palabra:

# palabra = "grande"

# "grande".startswith("g")

# verdadero

# encontradas = ["gato", "grande"]


# Cuarta palabra:

# palabra = "juega"

# no empieza con "g"


# resultado:

# ["gato", "grande"]



# Segunda llamada:

# agrupar_por_longitud(
#     "el gato está aquí"
# )


# ultimo_texto = "el gato está aquí"


# palabras:

# ["el", "gato", "está", "aquí"]


# palabra = "el"

# longitud = 2

# grupos = {
#     2: ["el"]
# }


# palabra = "gato"

# longitud = 4

# grupos = {
#     2: ["el"],
#     4: ["gato"]
# }


# palabra = "está"

# longitud = 4

# grupos = {
#     2: ["el"],
#     4: ["gato", "está"]
# }


# palabra = "aquí"

# longitud = 4

# grupos = {
#     2: ["el"],
#     4: ["gato", "está", "aquí"]
# }


# resultado:

# {
#     2: ["el"],
#     4: ["gato", "está", "aquí"]
# }



# Tercera llamada:

# palabras_unicas()


# El último texto guardado es:

# "el gato está aquí"


# separar:

# ["el", "gato", "está", "aquí"]


# convertir a set:

# {"el", "gato", "está", "aquí"}



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen
# procesos repetitivos.
#
# En encontrar_palabras(),
# cada palabra pasa por el mismo proceso:
#
# 1. Tomar una palabra.
#
# 2. Verificar si empieza
#    con el patrón.
#
# 3. Si cumple,
#    agregarla a encontradas.
#
# El patrón principal es:
#
# for palabra in palabras:
#
#     if palabra.startswith(patron):
#
#         encontradas.append(palabra)
#
#
# También existe repetición
# en agrupar_por_longitud().
#
# Para cada palabra:
#
# 1. Obtener su longitud.
#
# 2. Crear el grupo si no existe.
#
# 3. Agregar la palabra
#    al grupo correspondiente.



#-------- 4. ESCRIBIR EL CÓDIGO --------

class AnalizadorPatrones:

    def __init__(self):

        self.ultimo_texto = ""

    def encontrar_palabras(self, texto, patron):

        self.ultimo_texto = texto

        palabras = texto.split()

        encontradas = []

        for palabra in palabras:

            if palabra.startswith(patron):

                encontradas.append(palabra)

        return encontradas

    def agrupar_por_longitud(self, texto):

        self.ultimo_texto = texto

        palabras = texto.split()

        grupos = {}

        for palabra in palabras:

            longitud = len(palabra)

            if longitud not in grupos:

                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):

        palabras = self.ultimo_texto.split()

        return set(palabras)


ap = AnalizadorPatrones()

print(
    ap.encontrar_palabras(
        "el gato grande juega",
        "g"
    )
)

print(
    ap.agrupar_por_longitud(
        "el gato está aquí"
    )
)

print(ap.palabras_unicas())



#-------- 5. PRUEBA DE ESCRITORIO --------

# encontrar_palabras():


# palabra    empieza con "g"    encontradas

# "el"            No            []

# "gato"          Sí            ["gato"]

# "grande"        Sí            ["gato", "grande"]

# "juega"         No            ["gato", "grande"]


# retorno:

# ["gato", "grande"]



# agrupar_por_longitud():


# palabra    longitud    grupos

# "el"          2       {2: ["el"]}

# "gato"        4       {2: ["el"], 4: ["gato"]}

# "está"        4       {2: ["el"], 4: ["gato", "está"]}

# "aquí"        4       {2: ["el"], 4: ["gato", "está", "aquí"]}


# retorno:

# {
#     2: ["el"],
#     4: ["gato", "está", "aquí"]
# }



# palabras_unicas():

# ultimo_texto:

# "el gato está aquí"


# retorno:

# {"el", "gato", "está", "aquí"}


# pantalla:

# ['gato', 'grande']

# {2: ['el'], 4: ['gato', 'está', 'aquí']}

# {'el', 'gato', 'está', 'aquí'}

## Reto: ---- Ejercicio práctica 20 ----

"""Ejercicio: Clase OrganizadorPalabras

Crea una clase llamada OrganizadorPalabras que:

Tenga un método buscar_terminacion(texto, terminacion) que:
Separe el texto en palabras.
Busque las palabras que terminen con la terminación indicada.
Retorne una lista con las palabras encontradas.
Tenga un método agrupar_por_inicial(texto) que:
Separe el texto en palabras.
Agrupe las palabras según su primera letra.
Retorne un diccionario con esta estructura:
{
    "p": ["python", "programar"],
    "c": ["codigo", "casa"]
}
Tenga un método palabras_distintas(texto) que:
Retorne un conjunto con las palabras del texto.
Las palabras repetidas deben aparecer una sola vez."""

class OrganizadorPalabras:

    def buscar_terminacion(self, texto, terminacion):
        palabras = texto.split()
        encontradas = []

        for palabra in palabras:
            if palabra.endswith(terminacion):
                encontradas.append(palabra)

        return encontradas

    def agrupar_por_inicial(self, texto):
        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            inicial = palabra[0]

            if inicial not in grupos:
                grupos[inicial] = []

            grupos[inicial].append(palabra)

        return grupos

    def palabras_distintas(self, texto):
        palabras = texto.split()

        return set(palabras)


o = OrganizadorPalabras()

texto = "python perro casa codigo python programar"

print(o.buscar_terminacion(texto, "o"))

print(o.agrupar_por_inicial(texto))

print(o.palabras_distintas(texto))