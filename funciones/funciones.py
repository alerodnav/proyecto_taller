#Funciones
#Imports
from hashlib import md5

def limpiar_terminal():
    """Esta funcion se encarga de limpiar la terminal
    """
    print (chr(27) + "[2J")


def cifrar_contrasena(passwd):
    """Esta funcion encripta la contrasena del usuario
    
    args:
        passwd (string): Contrasena que va ser encriptada
    """
    entrada_binaria=passwd.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())


def agregar_curso(l,n,cre,hl,fi,ff,hc,c):
    """Esta funcion se encarga de agregar un curso
    
    args:
        l (lista): Lista de los cursos
        n (string): Nombre del curso
        cre (int): Numero de creditos del curso
        hl (int): Numero de horas lectivas del curso
        fi (string): Fecha de inicio del curso
        ff (string): Fecha final del curso
        hc (lista): El o los horarios del curso
        c (lista): La o las carreras que tienen ese curso  
    """
    for i in l:
        if i['nombre']==n:
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
    return l

    

def modificar_curso(l,n1,n2,cre,hl,fi,ff,hc,c):
    """Esta funcion se encarga de agregar un curso
    
    args:
        l (lista): Listas de los cursos
        n1 (string): Nombre del curso a modificar
        n2 (string): Nuevo nombre del curso
        cre (int): Numero de creditos del curso
        hl (int): Numero de horas lectivas del curso
        fi (string): Fecha de inicio del curso
        ff (string): Fecha final del curso
        hc (lista): El o los horarios del curso
        c (lista): La o las carreras que tienen ese curso  
    """
    for i in l:
        if(i['nombre']==n1):
            i['nombre']=n2

    return l

def agregar_carrera(lista,carrera):
    """Esta funcion se encarga de agregar una nueva carrera
    
    args:
        lista (lista): Lista de carreras
        carrera (string): Nombre de la carrera que se agregará
    """
    if carrera in lista:
        return "Esta carrera ya existe"
    lista.append(carrera)
    return lista

def modificar_carrera(lista,carrera1,carrera2):
    """Esta funcion se encarga de modificar una carrera
    
    args:
        lista (lista): Lista de las carreras
        carrera1 (string): Nombre de la carrera que se modificará
        carrera2 (string): Nuevo nombre de la carrera        
    """
    tam=len(lista)
    for i in range(tam):
        if(lista[i]==carrera1):
            lista[i]=carrera2
    return lista

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

def modificar_actividad(lista,act1,act2):
    """Esta funcion se encarga de modificar una actividad
    
    args:
        lista (lista): Lista de actividades
        act1 (string): Actividad que se modificará
        act2 (string): Nuevo nombre de la actividad          
    """
    tam=len(lista)
    for i in range(tam):
        if(lista[i]==act1):
            lista[i]=act2
    return lista