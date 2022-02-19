#Un centro médico necesita un programa que le permita operar con los datos de los diferentes pacientes que se atienden en él. De cada Paciente, se tiene un número historia clínica (una cadena que puede tener dígitos y caracteres),
# su nombre (una cadena), la descripción del diagnóstico que le dieron (una cadena con un texto terminado en punto y con palabras separadas por un blanco (por ejemplo:
# “Neumonía bilateral causada por COVID 19.”), el monto a abonar por su tratamiento,
# un número entre 1 y 15 que indica el tipo de plan de cobertura que tiene (por ejemplo: 1: Básico, 2: Completo, 3: Familiar, etc.), y otro número, pero entre 1 y 10 para indicar el tipo de fármaco que le recetaron (por ejemplo: 1: psicotrópico, 2: antibiótico, etc.).

#En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos:
#• En uno de ellos, definir la clase Paciente que represente al registro a usar en el programa, y las funciones básicas para operar con registros de ese tipo.
#• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de datos, aplique las validaciones que considere necesarias.
#  El programa debe basarse en un menú de opciones para desarrollar las siguientes tareas:

#1. Generar un arreglo de registros que contenga los datos de todos los pacientes. Puede generarlo cargando los datos en forma manual o generando los datos en forma aleatoria.
#  El arreglo debe permanecer ordenado por número de historia clínica en todo momento durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del programa,
#  y que en cada ejecución pueden agregarse tantos registros como desee el operador, sin eliminar los datos que ya estaban cargados.

#2. Mostrar el arreglo generado en el punto anterior, a razón de un registro por línea en la consola de salida.

#3. A partir del arreglo, generar otro arreglo unidimensional de registros que contenga los datos de todos los pacientes cuyo monto a abonar sea mayor a un valor p que se carga por teclado y
#  su tipo de plan de cobertura sea mayor a 5. Este arreglo debe también mantenerse ordenado en todo momento durante la carga, pero de acuerdo a los nombres de los pacientes.
#  Cada vez que esta opción se seleccione, el nuevo arreglo debe crearse otra vez, eliminando los anteriores registros que hubiese contenido.

#4. Mostrar todos los datos del arreglo que generó en el punto 3, a razón de un registro por línea.

#5. Recorra el primer arreglo y cree una cadena que contenga la concatenación de todos los textos contenidos en el campo descripción de diagnóstico de los registros en los que ese campo tenga una longitud mayor a c caracteres (el valor c se carga por teclado).
#  La cadena creada solo debe contener UN punto al final, y debe cumplirse que las palabras sigan separadas entre ellas por un y solo un espacio en blanco.
#  Retorne la cadena creada, o retorne una cadena de la forma ‘Imposible.’ si ningún registro cumplía la condición pedida.
#  En ambos casos, muestre la cadena retornada.

#6. Determine si existe en el primer arreglo un paciente en el que su nombre coincida con el valor nom que se carga por teclado. Si existe, muestre sus datos completos y detenga la búsqueda. Si no existe, informe con un mensaje.

#7. A partir del primer arreglo, determine cuántos pacientes existen para cada una de las posibles combinaciones entre tipos de planes y tipos de fármacos (un total de 15 * 10 = 150 contadores).
#  Muestre sólo los resultados que sean diferentes a cero.

#8. Tome la cadena retornada en el punto 5, y determine cuántas palabras de esa cadena contenían al menos una letra mayúscula y al menos una vez la combinación de dos letras c seguidas (por ejemplo: acción o protección).
#  Como se dijo, la cadena debe terminar con un punto y las palabras deben separarse entre ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella

import random
class Paciente:
    def __init__(self, numero, nombre, descripcion, monto, tipo_cobertura, tipo_farmaco):
        self.num = numero
        self.nom = nombre
        self.desc = descripcion
        self.mon = monto
        self.tipoC = tipo_cobertura
        self.tipoF = tipo_farmaco

cober = 'Basico', 'Completo', 'Familiar', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
far = 'Psicotropico', 'Antibiotico', 'Anagelsico', 'Antiacido', 'Antidepresivo', 'Anti', 'Antiviral', 'Anti8', 'Anti9', 'Anti10'

def toString(paciente):
    r = ""
    r += '{:<20}'.format("Numero: " + paciente.num)
    r += '{:<20}'.format("Nombre: " + paciente.nom)
    r += '{:<35}'.format("Descripcion: " + paciente.desc)
    r += '{:<15}'.format("Monto: " + str(paciente.mon))
    r += '{:<20}'.format("Cobertura: " + str(cober[paciente.tipoC -1]))
    r += '{:<25}'.format("Tipo Farmaco: " + str(far[paciente.tipoF -1]))
    return r

def validar_entre(texto, minimo, maximo):
    n = int(input(texto))
    while n < minimo or n > maximo:
        n = int(input("ERROR... " + texto))
    return n

def validar_mayor_A(texto,minimo):
    n = int(input(texto))
    while n < minimo:
        n = int(input("ERROR... Ingrese un numero mayor/igual a: " + str(minimo) + texto))
    return n


def menu():
    print("="*140)
    print('|{:^133}'.format('CENTRO MÉDICO') + '|')
    print("="*140)
    print("1) Cargar arreglo de pacientes")
    print("2) Mostrar arreglo generado")
    print("3) Generar arreglo de pacientes con monto mayor a p")
    print("4) Mostrar arreglo punto 3")
    print("5) Crear cadena de descripciones")
    print("6) Buscar paciente por nombre")
    print("7) Cantidad de tipos de planes por cada tipo de farmaco")
    print("8) Operar cadena punto 5")
    print("9) Salir")
    print("="*140)

#Punto 1
def generar_historiaC():
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    historia_clinica = ""
    for i in range(6):
        historia_clinica += random.choice(l)
    return historia_clinica

def add_in_order(vec, nuevo):
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) //2
        if vec[c].num == nuevo.num:
            pos = c
            break
        if nuevo.num > vec[c].num:
            izq = c+1
        else:
            der = c-1
    if izq > der:
        pos = izq
    vec[pos:pos] = [nuevo]

def generar_arreglo(vec):
    nombres = 'Sandra', 'Martin', 'Carlos', 'Matias', 'Franco', 'Andrea'
    descrip = 'Neumonia covid Mcc.', 'Dolor por Infeccion.', 'Prueba punto 5.', 'Para el p5.'
    n = validar_mayor_A("Ingrese cantidad de pacientes: ", 1)
    for i in range(n):
        num = generar_historiaC()
        nom = random.choice(nombres)
        des = random.choice(descrip)
        mon = random.randint(500,999)
        tipC = random.randint(1,15)
        tipF = random.randint(1,10)
        pac = Paciente(num,nom,des,mon,tipC,tipF)
        add_in_order(vec,pac)

#Punto 2 y 4
def mostrar_arreglo(vec):
    for i in range(len(vec)):
        print(toString(vec[i]))

#Punto 3
def ordenar_nombre(vec):
    n = len(vec)
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if vec[j].nom > vec[j + 1].nom:
                ordenado = False
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if ordenado:
            break

def arreglo_punto3(vec):
    p = validar_entre("Ingrese un monto: ", 500,999)
    vec2 = []
    for i in range(len(vec)):
        if vec[i].mon > p and vec[i].tipoC > 5:
            vec2.append(vec[i])
    ordenar_nombre(vec2)
    return vec2

#Punto 5
def cadena_nueva(vector):
    cad2 = ""
    for i in vector:
        if i != ".":
            cad2 += i
        else:
            cad2 += " "
    return cad2

def punto5(vec):
    cad = ""
    bandera = False
    c = int(input("Ingrese cantidad de caracteres: "))
    for i in range(len(vec)):
        if len(vec[i].desc) > c:
            cad2 = cadena_nueva(vec[i].desc)
            cad += cad2
            bandera = True
    cad += "."
    if not bandera:
        cad = "Imposible."
    return cad

#Punto 6
def buscar_nom(vec):
    nombre = input("Ingrese nombre a buscar: ")
    band = False
    for i in range(len(vec)):
        if vec[i].nombre == nombre:
            band = True
            print(toString(vec[i]))
            break
    if not band:
        print("No se encontro arreglo que cumpla con la condicion: ")

#Punto 7
def generar_matriz(vec):
    mat = [[0] * 15 for i in range(10)]
    for i in range(len(vec)):
        fila = vec[i].tipoF -1
        col = vec[i].tipoC -1
        mat[fila][col] += 1
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] != 0:
                print('{:<30}'.format("Tipo Cobertura: " + str(cober[c])),'{:<30}'.format("Tipo Farmaco: " + str(far[f])), '{:<30}'.format("Cantidad: " + str(mat[f][c])))

#Punto 8
def cadena(cadena):
    mayor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c_pal = 0
    hay_may = False
    hay_cc = False
    ant = ""
    for i in cadena:
        if i != " " and i != ".":
            if i in mayor:
                hay_may = True
            if i == "c" and ant == "c":
                hay_cc = True
        else:
            if hay_may and hay_cc:
                c_pal += 1
            hay_cc = False
            hay_may = False
        ant = i
    print("Cantidad de palabras que cumple la condicon: ", c_pal)

def test():
    vec = []
    opcion = -1
    bandera1 = False
    bandera2 = False
    while opcion != 9:
        menu()
        opcion = validar_entre("Ingrese una opcion entre 1 y 8: ",1,9)
        print("=" * 135)
        if opcion == 1:
            generar_arreglo(vec)
        elif opcion == 2:
            if len(vec) != 0:
                mostrar_arreglo(vec)
            else:
                print("Primero debe cargar el arreglo en la opcion 1")
        elif opcion == 3:
            if len(vec) != 0:
                vec2 = arreglo_punto3(vec)
                bandera2 = True
            else:
                print("Primero debe cargar el arreglo en la opcion 1")
        elif opcion == 4:
            if bandera2:
                mostrar_arreglo(vec2)
            else:
                print("Primero debe cargar el arreglo en la opcion 3")
        elif opcion == 5:
            if len(vec) != 0:
                cad = punto5(vec)
                bandera1 = True
                print(cad)
            else:
                print("Primero debe cargar el arreglo en la opcion 3")
        elif opcion == 6:
            if len(vec) != 0:
                buscar_nom(vec)
            else:
                print("Primero deber cargar el arreglo en la opcion 1")
        elif opcion == 7:
            if len(vec) != 0:
                generar_matriz(vec)
            else:
                print("Primero deber cargar el arreglo en la opcion 1")
        elif opcion == 8:
            if bandera1:
                cadena(cad)
            else:
                print("Primero deber crear la cadena en el punto 5")
    print("=" * 140)
    print('|{:^133}'.format('FIN DEL PROGRAMA') + '|')
    print("=" * 140)
test()