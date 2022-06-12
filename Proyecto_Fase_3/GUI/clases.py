# Clase principal lista con puntero

from time import time
from tkinter.messagebox import showerror
from funciones_clases import *
from datetimerange import DateTimeRange
import datetime

class Lista:
    sig=None

    def insertar (self,p):
        self.__insertar(self,p)
    
    def __insertar (self,l,p):
        """Esta función inserta un elemento en la parte final de la lista
    args:
        lista (lista): Lista 
        p (instancia): Elemento que se desea insertar      
    """
        if l.sig==None:
            l.sig=p
        else:
            self.__insertar(l.sig,p)

    def agregar_elemento(self,elemento,archivo):
        """Añade un elemento en el archivo
    args:
        elemento (string): Elemento que se desea agregar
        archivo (string): Ruta del archivo    
    """
        try:
            with open(archivo,"ta") as archivo:
                archivo.writelines(elemento+"\n")
        except FileNotFoundError as error:
            with open(archivo,"tw") as archivo:
                archivo.writelines(elemento+"\n")

class Actividad(Lista):

    descripcion=None
    curso_asociado=None
    fecha_inicio=None
    fecha_final=None
    hora_inicio=None
    hora_final=None
    estado=None

    def __init__(self,descripcion,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado):
        self.descripcion=descripcion
        self.curso_asociado=curso_asociado
        self.fecha_inicio=fecha_inicio
        self.fecha_final=fecha_final
        self.hora_inicio=hora_inicio
        self.hora_final=hora_final
        self.estado=estado
    
    def guardar_actividades(self,ruta):
        """Guarda las actividades en un archivo
    args:
        ruta (string): Ruta del archivo   
    """
        
        puntero=self
        try:
            with open(ruta,"tw") as archivo:
                self.agregar_elemento(puntero.descripcion,ruta)
                self.agregar_elemento(puntero.curso_asociado,ruta)
                self.agregar_elemento(puntero.fecha_inicio,ruta)
                self.agregar_elemento(puntero.fecha_final,ruta)
                self.agregar_elemento(puntero.hora_inicio,ruta)
                self.agregar_elemento(puntero.hora_final,ruta)
                self.agregar_elemento(puntero.estado,ruta)
                while puntero.sig!=None:
                    puntero=puntero.sig
                    self.agregar_elemento(puntero.descripcion,ruta)
                    self.agregar_elemento(puntero.curso_asociado,ruta)
                    self.agregar_elemento(puntero.fecha_inicio,ruta)
                    self.agregar_elemento(puntero.fecha_final,ruta)
                    self.agregar_elemento(puntero.hora_inicio,ruta)
                    self.agregar_elemento(puntero.hora_final,ruta)
                    self.agregar_elemento(puntero.estado,ruta)
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de actividades')

    def buscar_x_fecha_hora(self,fecha,hora):
        """Busca una actividad por la fecha y hora
        args:
            hora (string): Hora actual
            fecha (string): Fecha actual
        """
        aux = self
        while (aux.sig != None):

            time_range = DateTimeRange(str(aux.hora_inicio), str(aux.hora_final))
            time_range.end_time_format = "%H:%M"
            time_range.start_time_format = "%H:%M"

            inicio= datetime.datetime.strptime(str(aux.fecha_inicio), "%d-%m-%Y")
            fin = datetime.datetime.strptime(str(aux.fecha_final), "%d-%m-%Y")

            if ((inicio <= fecha <= fin) and (hora in time_range)):
                return aux.descripcion
            else:
                aux = aux.sig

        time_range = DateTimeRange(str(aux.hora_inicio), str(aux.hora_final))
        time_range.end_time_format = "%H:%M"
        time_range.start_time_format = "%H:%M"

        inicio= datetime.datetime.strptime(str(aux.fecha_inicio), "%d-%m-%Y")
        fin = datetime.datetime.strptime(str(aux.fecha_final), "%d-%m-%Y")

       
        
        if ((inicio <= fecha <= fin)and (hora in time_range)):
                pass
                return aux.descripcion
        else:
                showerror(message='No se ha encontrado una actividad')

 #  
        

        

"""
l_cursos = Actividad('Estudiar Mate Discreta','Mate','5 a 8','6 a 12','12 a 18',True)
print(l_cursos.descripcion)
#Pruebas con las clases
l_estudiantes = Estudiante('Alejandro Rodriguez Navarro','arodnav','a123')

l_estudiantes.insertar(Estudiante('Andres Carvajal','jcarv','j123'))

l_administradores = Administrador('Marvin Angulo','mangulo','m123')

l_carreras=Carrera("Ingeniería en Computación")
l_carreras.insertar(Carrera("Ingeniería en Electrónica"))

print(l_estudiantes.nombre)
print(l_estudiantes.sig.nombre)
print(l_administradores.nombre)
print(l_carreras.nombre)
    
"""