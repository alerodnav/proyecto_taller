# Funciones
# Imports
from hashlib import md5
from operator import indexOf
from time import sleep

def imprimir_carreras(tupla):
    for x in tupla:
        print(x)
    return()

def comprobar_carrera(lista_carreras, c):
    for x in lista_carreras:
        if x == c:
            valido = True
            break
        else:
            valido = False
    return(valido)



def comprobar_cantidad_carreras(lista, estudiante):
    """Comprueba si un estudiante tiene 2 carreras, si las tiene, no podrá agregar más
    args:
        lista (lista): Lista de estudiantes
        estudiante (string): Indice de la lista estudiantes (Estudiante que se verifica si tiene dos carreras activas)      
    """
    if (len(lista[estudiante]["carreras"]) == 2):
        permitir_iniciar = False
    else:
        permitir_iniciar = True
    return(permitir_iniciar)

def iniciar_carrera(lista,estudiante,carrera):
    """Esta funcion se encarga de agregar una carrera a las carreras del estudiante

    args:
        lista (lista): Lista de estudiantes
        estudiante (string): Estudiante que va a iniciar la carrera
        carrera (string): Carrera que va a iniciar         
    """
    lista[estudiante]['carreras'].append(carrera)
    return()


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

def ver_cursos(c,cursos,v):
    """Función para desplegar los cursos que un estudiante puede matricular

    args:
    c (lista): Lista de la o las carrreras del estudiante
    cursos (tuple): Lista de todos los cursos
    v (string): Letra para validar si se quiere matricular o elegir curso asociado
    """
    cursos = list(cursos)
    cursos_posibles = []
    nombres_cursos = []
    for i in c:
        for j in cursos:
            if i in j['carreras']:   
                valor = "{0}  /  {1} de {2} a {3}".format(j['nombre'],str(j['horario_clases'][0][0]),str(j['horario_clases'][0][1]),str(j['horario_clases'][0][2]))             
                if not (valor in cursos_posibles):
                    tam = len(j['horario_clases'])
                    if(tam < 2):
                        cursos_posibles.append(valor)
                    else:
                        cursos_posibles.append("{0}  /  {1} de {2} a {3} y los {4} de {5} a {6}".format(j['nombre'],str(j['horario_clases'][0][0]),str(j['horario_clases'][0][1]),str(j['horario_clases'][0][2]),str(j['horario_clases'][1][0]),str(j['horario_clases'][1][1]),str(j['horario_clases'][1][2])))   
                    nombres_cursos.append([j['nombre'],j['horario_clases']])
        
    cont1 = 1
    cont2 = 1
    print("Cursos: \n")

    opciones = {}

    for x in nombres_cursos:
        if x not in opciones.items():
            opciones[cont1]=x[0]
        cont1+=1
    opciones[cont1]='Libre'
    for i in cursos_posibles:
        print(cont2,"- "+i)
        cont2+=1
    
    if v=="m":
        opcion_curso = int(input("Ingrese la opción del curso a matricular: "))
        return [opciones[opcion_curso],nombres_cursos[opcion_curso-1][1]]
    elif (v=="i"):
        print(cont2, "- Libre")
        opcion_curso = int(input("Ingrese la opción del curso asociado: "))
        return [opciones[opcion_curso]]

        


def ver_hora(h):
    """Funcion que devuelve la hora de un formato de hora
    
    arg:
    h (string) Cadena con la hora completa
    """
    hora = ""
    for i in h:
        if i == ":":
            return int(hora)
        hora=hora+i

def ver_minutos(h):
    """Funcion que devuelve los minutos de un formato de hora
    
    arg:
    h (string) Cadena con la hora completa
    """
    minutos = ""
    aux = indexOf(h,":")
    tam = len(h)
    cont = 0
    for i in range(tam):
        if i>aux:
            minutos=minutos+h[cont]
        cont+=1
    return minutos

def matricular_curso(op,c,id,est):
    """Funcion para matricular cursos del estudiante
    
    args: 
    op (string) Nombre del curso a matricular
    c (list) Lista de cursos disponibles
    id (int) Index (id) del usuario de la sesion actual
    est (list) Lista de estudiantes
    """
    # validar()
    puede_matricular = True
    for i in c:
        if i['nombre'] == op:
            tam = len(est[id]['cursos'])
            cont=0
            for j in range (tam):
                if est[id]['cursos'][cont][0] == op:
                    puede_matricular = False       
                cont+=1
            if puede_matricular:
                est[id]['cursos'].append([i['nombre'],i['horario_clases']])
                return "Curso Matriculado"
            else:
                return "Este curso ya fue matriculado"
            
    return "Error al matricular curso"
    
def encontrar_semana(fi,ff,s):
    """Función para encontrar el número de la semana

    args:
    fi (string): Cadena con fecha de inicio
    ff (string): Cadena con fecha final
    s (string): Lista de las semanas
    """
    for i in s:
        if ((i['inicio'][-1] == fi[-1]) & (i['inicio'][-2] == fi[-2])) & ((i['fin'][-1] >= ff[-1]) & (i['fin'][-2] == ff[-2])):
            if (fi[0]+fi[1]) < (ff[0]+ff[1]):
                if ((int(i['inicio'][0] + i['inicio'][1])<=(int(fi[0] + fi[1]))) & (i['fin'][-1] > ff[-1])):
                    return i['numero']
                elif(int(i['fin'][0] + i['fin'][1])>=(int(ff[0] + ff[1]))):
                    return i['numero']
    return "-"

def validar_matricula_curso(l,ns,d,hi,hf,v):
    """Función para valiidar si esta hora ya esta ocupada este mismo dia de esta semana 

    args:
    l (list): Lista de cursos o actividades
    ns (int): Numero de la semana
    d (string): Dia de la semana
    hi (string): Hora de inicio
    hf (string): Hora final
    v (string): Determina si se agregará un curso o una actividad
    """
    result=[False]
    tam = len(l)
    if (tam > 0) & (v=="m"):
        for i in l:
            for j in i['horario_clases']: 
                if ((ns=="-")|(ns=="*")|(ns == i['semana'])) & ((d == j[0]) | (d=="-")): #Misma semana y dia
                    if ver_hora(hi)==ver_hora(j[1]): 
                        result.append("Inicia a la misma hora que {0}.".format(i['nombre']))
                        return result
                    if (ver_hora(hi)<ver_hora(j[1])) & ((ver_hora(hf)>ver_hora(j[2]))|((ver_hora(hf)>ver_hora(j[1])))):
                        result.append("Debes terminar antes, porque chocaría con el horario de {0}".format(i['nombre']))
                        return result
                    if (ver_hora(hi)>ver_hora(j[1])) & (ver_hora(hi)<ver_hora(j[2])):
                        result.append("Esta hora no te sirve, te choca con {0}".format(i['nombre']))
                        return result
        result[0] = True
        return result
    elif (tam > 0) & (v=="a"):
        for i in l:
            for j in i['horario']: 
                if ((ns=="-")|(ns=="*")|(ns == i['semana'])) & ((d == j[0]) | (d=="-")): #Misma semana y dia
                    h_inicio = ver_hora(i['horario'][1])
                    h_final = ver_hora(i['horario'][2])
                    if ver_hora(hi)==h_inicio:
                        result.append("Inicia a la misma hora que {0}.".format(i['nombre']))
                        return result
                    if (ver_hora(hi)< h_inicio) & ((ver_hora(hf)>h_final)|(ver_hora(hf)>h_inicio)):
                        result.append("Debes terminar antes, porque chocaría con el horario de {0}".format(i['nombre']))
                        return result
                    if (ver_hora(hi)>h_inicio) & (ver_hora(hi)<h_final):
                        result.append("Esta hora no te sirve, te choca con {0}".format(i['nombre']))
                        return result
        result[0] = True
        return result    
    result[0]=True 
    return result    
    
    
