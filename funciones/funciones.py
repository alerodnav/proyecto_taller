# Funciones
# Imports
from hashlib import md5

def limpiar_terminal():
    """Esta funcion se encarga de limpiar la terminal
    """
    print(chr(27) + "[2J")


def cifrar_contrasena(passwd):
    """Esta funcion encripta la contrasena del usuario

    args:
        passwd (string): Contrasena que va ser encriptada
    """
    entrada_binaria = passwd.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())


def agregar_curso(l, n, cre, hl, fi, ff, hc, c):
    """Esta funcion se encarga de agregar un curso

    args:
        l (tuple): Tupla de los cursos
        n (string): Nombre del curso
        cre (int): Numero de creditos del curso
        hl (int): Numero de horas lectivas del curso
        fi (string): Fecha de inicio del curso
        ff (string): Fecha final del curso
        hc (lista): El o los horarios del curso
        c (lista): La o las carreras que tienen ese curso  
    """
    l=list(l)
    for i in l:
        if i['nombre'] == n:
            return "Este curso ya existe"

    l.append(
        {
            'nombre': n,
            'creditos': cre,
            'horas lectivas': hl,
            'fecha_inicio': fi,
            'fecha_final': ff,
            'horario_clases': hc,
            'carreras': c
        }
    )
    return tuple(l)

def validar_curso(l, n):
    """Función que valida si el curso está en la tupla de cursos

    args:
    l (tuple): Tupla con todos los cursos
    n (string): Nombre del curso que se modificará
    """
    l=list(l)
    while True:
        for i in l:
            if n in i['nombre']:
                return n
        print("\nEste curso no existe. Intentalo de nuevo\n")
        n = input("Nombre del curso a modificar: ")

def modificar_curso(l, n1, n2, cre, hl, fi, ff, hc, c):
    """Esta funcion se encarga de agregar un curso

    args:
        l (tuple): Tupla de los cursos
        n1 (string): Nombre del curso a modificar
        n2 (string): Nuevo nombre del curso
        cre (int): Numero de creditos del curso
        hl (int): Numero de horas lectivas del curso
        fi (string): Fecha de inicio del curso
        ff (string): Fecha final del curso
        hc (lista): El o los horarios del curso
        c (lista): La o las carreras que tienen ese curso  
    """
    l = list(l)
    for i in l:
        if(i['nombre'] == n1):
            i['nombre'] = n2 #, cre, hl, fi, ff, hc, c
            i['creditos'] = cre
            i['horas_lectivas'] = hl
            i['fecha_inicio'] = fi
            i['fecha_final'] = ff
            i['horario_clases'] = hc
            i['carreras'] = c

    return tuple(l)


def agregar_carrera(l, carrera):
    """Esta funcion se encarga de agregar una nueva carrera

    args:
        l (tuple): Tupla de las carreras
        carrera (string): Nombre de la carrera que se agregará
    """
    l=list(l)
    if carrera in l:
        return "Esta carrera ya existe"
    l.append(carrera)
    return tuple(l)


def modificar_carrera(l, carrera1, carrera2):
    """Esta funcion se encarga de modificar una carrera

    args:
        l (tuple): Lista de las carreras
        carrera1 (string): Nombre de la carrera que se modificará
        carrera2 (string): Nuevo nombre de la carrera        
    """
    l=list(l)
    tam = len(l)
    for i in range(tam):
        if(l[i] == carrera1):
            l[i] = carrera2
    return tuple(l)


def agregar_actividad(lista, actividad):
    """Esta funcion agrega una nueva actividad a la lista actividades

    args:
        lista (lista): Lista de actividades
        actividad (string): Actividad que se agregará
    """
    if actividad in lista:
        return "Esta actividad ya existe"
    lista.append(actividad)
    return lista


def modificar_actividad(lista, act1, act2):
    """Esta funcion se encarga de modificar una actividad

    args:
        lista (lista): Lista de actividades
        act1 (string): Actividad que se modificará
        act2 (string): Nuevo nombre de la actividad          
    """
    tam = len(lista)
    for i in range(tam):
        if(lista[i] == act1):
            lista[i] = act2
    return lista

def ver_cursos(c,cursos):
    """Función para desplegar los cursos que un estudiante puede matricular

    args:
    c (lista): Lista de la o las carrreras del estudiante
    cursos (tuple): Lista de todos los cursos
    """
    cursos = list(cursos)
    cursos_posibles = []
    for i in c:
        for j in cursos:
            if i in j['carreras']:                
                if not (j['nombre'] in cursos_posibles):
                    cursos_posibles.append(j['nombre'])
        
    cont = 1
    print("Cursos Discponibles \n")
    for i in cursos_posibles:
        print(cont,"- "+i)
        cont+=1
    print("")