from operator import le
from tkinter.messagebox import askyesno, showerror
from time import sleep

import clases as c

def agregar_elementos (elemento,archivo):
    """Esta funcion recibe el elemento que se desea agregar y lo escribe en el archivo que se desea
    args:
        elemento (string): Texto que se desea agrega
        archivo (string): ruta del archivo     
    """
    try:
        with open(archivo,"ta") as archivo:
            archivo.writelines(elemento+"\n")
    except FileNotFoundError as error:
        with open(archivo,"tw") as archivo:
            archivo.writelines(elemento+"\n")


def almacenar_datos(l,ruta):
    """Esta funcion recibe el elemento que se desea agregar y lo escribe en el archivo que se desea
    args:
        l (lista enlazada): Texto que se desea agrega
        ruta (string): ruta del archivo     
    """
    try:
        with open(ruta,"ta") as archivo:
            agregar_elementos(l.nombre,ruta)
            agregar_elementos(l.usuario,ruta)
            agregar_elementos(l.passwd,ruta)
            while l.sig!=None:
                l=l.sig
                agregar_elementos(l.nombre,ruta)
                agregar_elementos(l.usuario,ruta)
                agregar_elementos(l.passwd,ruta)
    except FileNotFoundError as error:
        print('El archivo no se encuentra')

#Prueba


lista_estudiantes = c.Estudiante('Alejandro','arn','a123')
lista_estudiantes.insertar(c.Estudiante('Deivid','dmg','d123'))




def consultar_carreras(ruta):
    """Carga los datos del archivo de carreras
    args:
        ruta (string): Ruta del archivo     
    """
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            datos=c.Carrera(nombre)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Carrera(nombre))
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con ese nombre, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)

def buscar_cursos(n):
    """Busca un curso
    args:
        n (string): nombre del curso     
    """
    ruta = "./datos/cursos.txt"
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            creditos=lector.readline()[:-1]
            h_lectivas=lector.readline()[:-1]
            f_inicio=lector.readline()[:-1]
            f_final=lector.readline()[:-1]
            carreras=lector.readline()[:-1]
            while (nombre!=n):
                nombre=lector.readline()[:-1]
                creditos=lector.readline()[:-1]
                h_lectivas=lector.readline()[:-1]
                f_inicio=lector.readline()[:-1]
                f_final=lector.readline()[:-1]
                carreras=lector.readline()[:-1]
            if (nombre==n):
                datos=[nombre,creditos,h_lectivas,f_inicio,f_final,carreras]        
                return datos
            else:
                showerror(title="Error", message="No encontramos el curso")
    except FileNotFoundError as error:
        respuesta=askyesno(title="Error", message="No encontramos el archivo de datos desea crear un nuevo archivo de registro")
        if respuesta:
            open("./datos/cursos.txt","tw").close()
        

def consultar_estudiantes():
    """Carga los datos del archivo de estudiantes     
    """
    respuesta=None
    try:
        with open("./datos/estudiantes.txt","tr") as lector:
            lectura= eval(lector.readline()[:-1])
            if lectura!='':
                respuesta=c.Estudiante(nombre=lectura[0],usuario=lectura[1],passwd=lectura[2])
            lectura= eval(lector.readline()[:-1])
            while (lectura!=''):
                respuesta.insertar(c.Estudiante(nombre=lectura[0],usuario=lectura[1],passwd=lectura[2]))
                lectura= eval(lector.readline()[:-1])
    except FileNotFoundError as error:
        respuesta=askyesno(title="Error", message="No encontramos el archivo de datos desea crear un nuevo archivo de registro (s/n)")
        if respuesta:
            open("./datos/estudiantes.txt","tw").close()
    finally:
        return respuesta

def consultar_administradores():
    """Carga los datos del archivo de administradores    
    """
    respuesta=None
    try:
        with open("./datos/administradores.txt","tr") as lector:
            lectura= eval(lector.readline()[:-1])
            if lectura!='':
                respuesta=c.Administrador(nombre=lectura[0],usuario=lectura[1],passwd=lectura[2])
            lectura= eval(lector.readline()[:-1])
            while (lectura!=''):
                respuesta.insertar(c.Administrador(nombre=lectura[0],usuario=lectura[1],passwd=lectura[2]))
                lectura= eval(lector.readline()[:-1])
    except FileNotFoundError as error:
        respuesta=askyesno(title="Error", message="No encontramos el archivo de datos desea crear un nuevo archivo de registro (s/n)")
        if respuesta:
            open("./datos/estudiantes.txt","tw").close()
    finally:
        return respuesta


def consultar_cursos(ruta):
    """Carga los datos del archivo de cursos
    args:
        ruta (string): Ruta del archivo     
    """
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            creditos=lector.readline()[:-1]
            h_lectivas=lector.readline()[:-1]
            f_inicio=lector.readline()[:-1]
            f_final=lector.readline()[:-1]
            carreras=lector.readline()[:-1]
            datos=c.Curso(nombre,creditos,h_lectivas,f_inicio,f_final,carreras)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                creditos=lector.readline()[:-1]
                h_lectivas=lector.readline()[:-1]
                f_inicio=lector.readline()[:-1]
                f_final=lector.readline()[:-1]
                carreras=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Curso(nombre,creditos,h_lectivas,f_inicio,f_final,carreras))
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con ese nombre, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)

def consultar_actividades(ruta):
    """Carga los datos del archivo de actividades
    args:
        ruta (string): Ruta del archivo     
    """
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            curso_asociado=lector.readline()[:-1]
            fecha_inicio=lector.readline()[:-1]
            fecha_final=lector.readline()[:-1]
            hora_inicio=lector.readline()[:-1]
            hora_final=lector.readline()[:-1]
            estado=lector.readline()[:-1]
            datos=c.Actividad(nombre,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                curso_asociado=lector.readline()[:-1]
                fecha_inicio=lector.readline()[:-1]
                fecha_final=lector.readline()[:-1]
                hora_inicio=lector.readline()[:-1]
                hora_final=lector.readline()[:-1]
                estado=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Actividad(nombre,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado))
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con ese nombre, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)

def nombre_actividades(ruta):
    """Carga los nombres del las actividades
    args:
        ruta (string): Ruta del archivo     
    """
    datos=[]
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            curso_asociado=lector.readline()[:-1]
            fecha_inicio=lector.readline()[:-1]
            fecha_final=lector.readline()[:-1]
            hora_inicio=lector.readline()[:-1]
            hora_final=lector.readline()[:-1]
            estado=lector.readline()[:-1]
            datos.append(nombre)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                curso_asociado=lector.readline()[:-1]
                fecha_inicio=lector.readline()[:-1]
                fecha_final=lector.readline()[:-1]
                hora_inicio=lector.readline()[:-1]
                hora_final=lector.readline()[:-1]
                estado=lector.readline()[:-1]
                if (nombre!=''):
                    datos.append(nombre)
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con actividades, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)


def ver_cursos_disponibles(c):
    """Carga lista de cursos disponibles para una o dos carreras
    """
    datos=[]
    try:
        with open("./datos/cursos.txt","tr") as lector:
            nombre=lector.readline()[:-1]
            num_creditos=lector.readline()[:-1]
            h_lectivas=lector.readline()[:-1]
            f_inicio=lector.readline()[:-1]
            f_final=lector.readline()[:-1]
            carreras=lector.readline()[:-1]
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                num_creditos=lector.readline()[:-1]
                h_lectivas=lector.readline()[:-1]
                f_inicio=lector.readline()[:-1]
                f_final=lector.readline()[:-1]
                carreras=lector.readline()[:-1]
                for i in c:
                    if i in carreras:
                        if not(nombre in datos):
                            datos.append(nombre)
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con cursos, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open("./datos/cursos.txt","tw")
    return (datos)

"""
def guardar_carreras(l,ruta):
    try:
        with open(ruta,"tw") as archivo:
            agregar_elemento(l.nombre,ruta)
            while l.sig!=None:
                l=l.sig
                agregar_elemento(l.nombre,ruta)
    except FileNotFoundError as error:
        showerror(message='No se pudo guardar en el archivo de carreras')


"""


#lista_estudiantes = c.Estudiante('Alejandro','arn','a123')
#lista_estudiantes.insertar(c.Estudiante('Deivid','dmg','d123'))
#lista_estudiantes.insertar(c.Estudiante('Mario','mcr','m123'))

#almacenar_datos(lista_estudiantes,'datos/estudiantes.txt')

"""
def consultar_estudiantes(ruta):
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            us=lector.readline()[:-1]
            ps=lector.readline()[:-1]
            datos=c.Estudiante(nombre,us,ps)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                us=lector.readline()[:-1]
                ps=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Estudiante(nombre,us,ps))
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con ese nombre, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)
"""

"""

def consultar_administradores(ruta):
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            us=lector.readline()[:-1]
            ps=lector.readline()[:-1]
            datos=c.Administrador(nombre,us,ps)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                us=lector.readline()[:-1]
                ps=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Administrador(nombre,us,ps))
    except FileNotFoundError as error:
        lectura=input("No hay un archivo con ese nombre, Desea crear uno? (s/n)")
        if  lectura.lower()=="s":
            open(ruta,"tw")
    return (datos)

"""

