import json
import re

lista_menu_inicial = [
    "Menú de opciones:",
    "1. Mostrar lista de todos los jugadores del Dream Team",
    "2. Ingresar el indice y mostrar estadisticas de el jugador correspondiente",
    "3. Guardar las estadísticas del jugador elegido en la opcion anterior en un archivo CSV.",
    "4. Ingresar un nombre y mostrar logros de ese jugador",
    "5. Mostrar el promedio de puntos por partido de todo el equipo y una lista en ascendente con los nombres de los jugadores",
    "6. Ingresar un nombre y mostrar si ese jugador es Miembro del Salón de la Fama del Baloncesto.",
    "7. Mostrar el jugador con la mayor cantidad de rebotes totales.",
    "8. Mostrar el jugador con el mayor porcentaje de tiros de campo.",
    "9. Mostrar el jugador con la mayor cantidad de asistencias totales.",
    "10. Mostrar el jugador con la mayor cantidad de temporadas jugadas",
    "11. Mostrar el jugador con la mayor cantidad de bloqueos totales.",
    "12. Mostrar el jugador con la mayor cantidad de robos totales.",
    "13. Mostrar el jugador con la mayor cantidad de logros obtenidos",
    "14. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.",
    "15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.",
    "16. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.",
    "17. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.",
    "18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.",
    "19. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.",
    "20. Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.",
    "0. Salir del programa"
]

def es_entero(palabra:str) -> bool:
    '''
    valida si un string es un entero
    '''
    if re.match(r'^-?\d+$', palabra):
        return True
    else:
        return False

def es_numero(palabra:str) -> bool:
    '''
    valida si un string es un numero
    '''
    if re.match(r'^-?\d+(\.\d+)?$', palabra):
        return True
    else:
        return False
    
def es_solo_texto(texto) -> bool:
    '''
    valida si un string es texto
    '''
    if re.match(r'^[a-zA-Z ]+$', texto):
        return True
    else:
        return False
    
def mostrar_listas(lista:list):
    '''
    muestra la lista
    '''
    for i in range(len(lista)):
        print(lista[i])

def mensaje_error():
    '''
    muestra un mensaje de error y 
    pide que reeingresen el dato
    '''
    respuesta = input("ERROR. Reeingrese el dato ")
    return respuesta

def abrir_json(nombre_archivo:str, funcion):
    '''
    abre un archivo json, pide una funcion para 
    utilizar y crea una lista para usar como 
    parametro de la funcion
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        print(funcion(lista))

def crear_archivo_csv(nombre_archivo:str, diccionario:dict):
    '''
    con la ruta y la data pedida crea un archivo csv 
    '''
    with open(nombre_archivo, 'w') as archivo:
        titulos = "NOMBRE \t POSICION \t ESTADISTICAS \n"
        data = "{0},{1},{2}\n".format(diccionario["nombre"], 
                                      diccionario["posicion"], 
                                      diccionario["estadisticas"])
        archivo.write(titulos)
        archivo.write(data)

def json_crear_archivo_csv(nombre_archivo:str, indice:int):
    '''
    pide el nombre de un archivo json y el indice 
    de un jugador, utilizandolos para
    la funcion crear_archivo_csv 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        nombre_archivo_csv = r"\Users\sotom\OneDrive\Escritorio\Python\primer parcial\dt.csv"
        crear_archivo_csv(nombre_archivo_csv, lista[indice])

def mostrar_jugadores_y_variable(lista:list, variable:str) -> list:
    '''
    devuelve una lista con los nombres de los jugadores y la variable 
    '''
    lista_nueva = []
    for i in range(len(lista)):
        lista_nueva.append("{0} - {1}".format(lista[i]["nombre"], lista[i][variable]))
    return lista_nueva

def json_mostrar_jugadores_y_variable(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza
    la funcion mostrar_jugadores_y_variable 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        lista_jugadores = mostrar_jugadores_y_variable(lista, "posicion")
        print("Los jugadores del Dream Team son:\n")
        mostrar_listas(lista_jugadores)

def mostrar_variable(lista:list, variable:str) -> list:
    '''
    devuelve una lista de los valores almacenadoa
    en  la variable ingresada con sus respectivos indices
    '''
    lista_nueva = []
    for i in range(len(lista)):
        lista_nueva.append("{0} - {1}".format(i,lista[i][variable]))
    return lista_nueva

def json_mostrar_nombres(nombre_archivo:str) -> list:
    '''
    pide el nombre de un archivo json e utiliza
    la funcion mostrar_variable 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        return mostrar_variable(lista, "nombre")

def indice_jugador_seleccionado(lista:list) -> int:
    '''
    le pide al ususario que eliga el indice del jugador 
    que quiere, devuleve el indice del jugador elegido
    '''
    opcion = input("\nIngrese la opcion deseada: ")
    while True:
        if es_entero(opcion) == True:
            opcion = int(opcion)
            if opcion > 11:
               opcion = mensaje_error()
            else:
                break
        else:
            opcion = mensaje_error()
    return opcion

def json_indice_jugador_seleccionado(nombre_archivo:list) -> int:
    '''
    pide el nombre de un archivo json e utiliza
    la funcion indice_jugador_seleccionado, muestra las
    estadisticas del jugador y devuelve el indice
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        indice = indice_jugador_seleccionado(lista)
        print(lista[indice]["estadisticas"])
        return indice

def buscar_indice_mediante_nombre(lista:list, nombre:str) -> list:
    '''
    busca las coincidencias del nombre ingresado
    en la lista pasada, devuelve una lista con estas 
    '''
    verificacion = r"{0}+".format(nombre.capitalize())
    lista_indices = []
    for i in range(len(lista)):
        if re.search(verificacion, lista[i]["nombre"]):
            lista_indices.append(i)
    return lista_indices

def buscar_logros_mediante_nombre(lista:list) -> list:
    '''
    utiliza la funcion buscar_indice_mediante_nombre para 
    obtener los indices e usarlos para ubicar al jugador 
    elegido, devuelvolviendo una lista con los logros de este
    '''
    nombre = input("\nIngrese el nombre del jugador: ")
    lista_jugadores = []
    while True:
        if es_solo_texto(nombre) == True:
            indices_jugadores = buscar_indice_mediante_nombre(lista, nombre)
            for indice in indices_jugadores:
                lista_jugadores.append(lista[indice]["logros"])
            if len(lista_jugadores) < 0:
                nombre = mensaje_error()
            else:
                return lista_jugadores
        else:
            nombre = mensaje_error()

def json_buscar_logros_mediante_nombre(nombre_archivo:str):
    '''
    pide el nombre de un archivo json y una variable 
    para utilizar la funcion buscar_logros_mediante_nombre 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        logros = buscar_logros_mediante_nombre(lista)
        print(logros)

def calcular_promedio(lista:list, variable:str) -> float:
    '''
    calcula el promedio de los valores de la variable ingresada,
    almacenados dentro de el diccionario 'estadisticas'
    '''
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]["estadisticas"][variable]
    promedio = suma / len(lista)
    return promedio
    
def json_calcular_promedio_puntos(nombre_archivo:str):
    '''
    pide el nombre de un archivo json y una variable 
    para utilizar la funcion calcular_promedio 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        promedio = calcular_promedio(lista,"promedio_puntos_por_partido")
        print(promedio)

def quick_sort(lista:list, variable1:str, variable2:str) -> list:
    '''
    ordena una lista de forma ascendente
    '''
    if (len(lista) <= 1):
        return lista
    lista_derecha = []
    lista_izquierda = []
    pivot_indice = 0
    for indice in range(len(lista)):
        if lista[indice][variable1][variable2] < lista[pivot_indice][variable1][variable2]:
            lista_derecha.append(indice)
        else:
            lista_izquierda.append(indice)
    lista_izquierda = quick_sort(lista_izquierda, variable1, variable2)
    lista_izquierda.append(pivot_indice) 
    lista_derecha = quick_sort(lista_derecha, variable1, variable2)
    lista_izquierda.extend(lista_derecha) 
    return lista_izquierda
    
def json_mostrar_nombres_en_ascendente(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza
    la funcion quick_sort 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        lista_jugadores = []
        lista_indices = quick_sort(lista,"estadisticas","promedio_puntos_por_partido")
        for num in lista_indices:
            lista_jugadores.append(lista[num]["nombre"])
        print(lista_jugadores)

def pertenece_al_salon_de_la_fama(lista:list) -> bool:
    '''
    le pide al usuario que ingrese un nombre y muestra si 
    ese jugador es "Miembro del Salón de la Fama del Baloncesto".
    '''
    nombre = input("\nIngrese el nombre del jugador: ")
    lista_jugadores = []
    while True:
        if es_solo_texto(nombre) == True:
            indices_jugadores = buscar_indice_mediante_nombre(lista, nombre)
            for indice in indices_jugadores:
                if "Miembro del Salon de la Fama del Baloncesto" in lista[indice]["logros"]:
                        lista_jugadores.append(lista[indice]["nombre"])
                else:
                    return False
            if len(lista_jugadores) > 0:
                return True
            else:
                nombre = mensaje_error()
                
        else:
            nombre = mensaje_error()

def json_pertenece_al_salon_de_la_fama(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza
    la funcion pertenece_al_salon_de_la_fama 
    '''
    abrir_json(nombre_archivo,pertenece_al_salon_de_la_fama)

def mostrar_jugador_mayor_variable(lista:list, variable:str) -> str:
    '''
    calcula el maximo de los valores de la variable ingresada,
    almacenados dentro de el diccionario 'estadisticas'. Devolviendo
    el nombre del jugador correspondiente
    '''
    maximo = lista[0]["estadisticas"][variable]
    nombre_mayor_variable = lista[0]["nombre"]
    for i in range(len(lista)):
        if lista[i]["estadisticas"][variable] > maximo:
            maximo = lista[i]["estadisticas"][variable]
            nombre_mayor_variable = lista[i]["nombre"]
    return nombre_mayor_variable

def json_mostrar_jugador_mayor_variable(nombre_archivo:str, variable:str):
    '''
    pide el nombre de un archivo json y una variable 
    para utilizar la funcion mostrar_jugador_mayor_variable 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        print("El jugador con la mayor cantidad de {0} es {1}".format(
            variable,
            mostrar_jugador_mayor_variable(lista, variable)))

def mostrar_jugador_mayor_logros(lista:list) -> str:
    '''
    calcula quien tiene mas logros, devolviendo
    el nombre del jugador correspondiente
    '''
    maximo = len(lista[0]["logros"])
    nombre_mayores_logros = lista[0]["nombre"]
    for i in range(len(lista)):
        if len(lista[i]["logros"]) > maximo:
            maximo = len(lista[i]["logros"])
            nombre_mayores_logros = lista[i]["nombre"]
    return nombre_mayores_logros

def json_mostrar_jugador_mayor_logros(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza
    la funcion mostrar_jugador_mayor_logros 
    '''
    abrir_json(nombre_archivo,mostrar_jugador_mayor_logros)

def es_mayor_que(lista:list, variable:str) -> list:
    '''
    le pide al usuario un numero calculando que valores de la
    variable ingresada son mayores que el numero del usuario, 
    devolviendo los nombres de los jugadores correspondientes
    '''
    valor_ingresado = input("\nIngrese un valor: ")
    lista_jugadores = []
    while True:
        if es_numero(valor_ingresado) == True:
            valor_ingresado = float(valor_ingresado)
            for i in range(len(lista)):
                if lista[i]["estadisticas"][variable] > valor_ingresado:
                    lista_jugadores.append(lista[i]["nombre"])
            return lista_jugadores
        else:
            valor_ingresado = mensaje_error()

def json_es_mayor_que(nombre_archivo:str, variable:str):
    '''
    pide el nombre de un archivo json y una variable 
    para utilizar la funcion es_mayor_que 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        nombres_jugadores = es_mayor_que(lista, variable)
        print("El/los jugador/es con una cantidad mayor a la ingresada de {0} son {1}".format(
            variable,
            nombres_jugadores))
    
def mostrar_promedio_variable_menos_minimo(lista:list, variable:str)-> float:
    '''
    calcula el promedio de puntos por partido de todos 
    los jugadores exepto por el que tiene el menor puntaje
    '''
    suma = 0
    menos_puntos = lista[0]["estadisticas"][variable]
    for i in range(len(lista)):
        suma += lista[i]["estadisticas"][variable]
        if lista[i]["estadisticas"][variable] < menos_puntos:
            menos_puntos = lista[i]["estadisticas"][variable]
    promedio = (suma - menos_puntos) / (len(lista) - 1)
    return promedio

def json_mostrar_promedio_variable_menos_minimo(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza la 
    funcion mostrar_promedio_variable_menos_minimo 
    '''
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]
        promedio = mostrar_promedio_variable_menos_minimo(lista,"promedio_puntos_por_partido")
        print("El promedio de puntos por partido del equipo menos el jugador con la menor cantidad de puntos es {0}".format(promedio))

def mas_porcentaje_tiros_de_campo_que(lista:list) -> dict:
    '''
    le pide al usuario un numero calculando que porcentaje
    de tiros de campo son mayores que el numero del usuario, 
    devolviendo los nombres de los jugadores correspondientes 
    y su posicion  
    '''
    valor_ingresado = input("\nIngrese un valor: ")
    diccionario = {}
    while True:
        if es_numero(valor_ingresado) == True:
            valor_ingresado = float(valor_ingresado)
            for i in range(len(lista)):
                if valor_ingresado < lista[i]["estadisticas"]["porcentaje_tiros_de_campo"]:
                    categoria = lista[i]["posicion"]
                    if categoria in diccionario:
                        diccionario[categoria] += lista[i]["nombre"] + " "
                    else:
                        diccionario[categoria] = lista[i]["nombre"] + " "
            return diccionario
        else:
            valor_ingresado = mensaje_error()
    
def json_mas_porcentaje_tiros_de_campo_que(nombre_archivo:str):
    '''
    pide el nombre de un archivo json e utiliza la 
    funcion mas_porcentaje_tiros_de_campo_que 
    '''
    abrir_json(nombre_archivo,mas_porcentaje_tiros_de_campo_que)

while True:
    nombre_archivo = r"C:\Users\sotom\OneDrive\Escritorio\Python\primer parcia\Primer-Parcial\dt.json"
    jugadores = json_mostrar_nombres(nombre_archivo)
    
    mostrar_listas(lista_menu_inicial)
    opcion = input("\nIngrese la opción deseada: ")
    while True:
        if es_entero(opcion) == True:
            opcion = int(opcion)
            break
        else:
            opcion = input("\nOpcion invalida. Ingrese la opcion deseada: ")
    
    if opcion == 1:
        json_mostrar_jugadores_y_variable(nombre_archivo)
   
    elif opcion == 2:
        mostrar_listas(jugadores)
        indice = json_indice_jugador_seleccionado(nombre_archivo)
        
    elif opcion == 3:
        if  "indice" in locals():
            json_crear_archivo_csv(nombre_archivo, indice)
        else:
            print("ERROR. Primero debe seleccionar un jugador en el punto 2")

    elif opcion == 4:
        mostrar_listas(jugadores)
        json_buscar_logros_mediante_nombre(nombre_archivo)

    elif opcion == 5: 
        json_calcular_promedio_puntos(nombre_archivo)
        json_mostrar_nombres_en_ascendente(nombre_archivo)
    
    elif opcion == 6:
        mostrar_listas(jugadores)
        if json_pertenece_al_salon_de_la_fama(nombre_archivo) == True:
            print("Es miembro del salon de la Fama del Baloncesto")
        else:
            print("No es miembro del salon de la Fama del Baloncesto")
    
    elif opcion == 7:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "rebotes_totales")

    elif opcion == 8:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "porcentaje_tiros_de_campo")
    
    elif opcion == 9:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "asistencias_totales")
    
    elif opcion == 10:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "temporadas")
    
    elif opcion == 11:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "bloqueos_totales")
   
    elif opcion == 12:
        json_mostrar_jugador_mayor_variable(nombre_archivo, "robos_totales")
 
    elif opcion == 13:
        json_mostrar_jugador_mayor_logros(nombre_archivo)
    
    elif opcion == 14:
        json_es_mayor_que(nombre_archivo, "promedio_puntos_por_partido")
   
    elif opcion == 15:
        json_es_mayor_que(nombre_archivo, "porcentaje_tiros_libres")
  
    elif opcion == 16:
        json_es_mayor_que(nombre_archivo, "promedio_rebotes_por_partido")
   
    elif opcion == 17:
       json_es_mayor_que(nombre_archivo, "promedio_asistencias_por_partido")
   
    elif opcion == 18:
        json_es_mayor_que(nombre_archivo, "porcentaje_tiros_triples")
 
    elif opcion == 19:
        json_mostrar_promedio_variable_menos_minimo(nombre_archivo)

    elif opcion == 20:
        json_mas_porcentaje_tiros_de_campo_que(nombre_archivo)
    
    elif opcion == 0:
        break
    
    else:
        opcion = input("\nOpcion invalida. Ingrese la opcion deseada: ")