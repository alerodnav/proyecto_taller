# Clase principal lista con puntero

from time import time
from tkinter.messagebox import showerror
from funciones_clases import *
from datetimerange import DateTimeRange
import datetime

datos = []

class Lista:
    """Clase lista
    Atributos:
        sig (objeto): Siguiente objeto de la lista 
            
    """

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
    """Clase Actividades
    Atributos:
        descrpicion (string): Descripción de la actividad
        semana(string): Numero de semana 
        fecha_inicio(string): Fecha inicio 
        fecha_final(string): Fecha final
        hora_inicio(string): Hora de inicio
        hora_final(string): Hora final
        estado(string): Estado (Pendiente - Completada) 
        emociones(string) Emocion predominante
            
    """
    descripcion=None
    semana=None
    curso_asociado=None
    fecha_inicio=None
    fecha_final=None
    hora_inicio=None
    hora_final=None
    estado=None
    emociones=None
    iz=None
    der=None

    def __init__(self,descripcion,semana,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado,emociones):
        self.descripcion=descripcion
        self.semana=semana
        self.curso_asociado=curso_asociado
        self.fecha_inicio=fecha_inicio
        self.fecha_final=fecha_final
        self.hora_inicio=hora_inicio
        self.hora_final=hora_final
        self.estado=estado
        self.emociones=emociones
    
    def guardar_actividades(self,ruta):
        """Guarda las actividades en un archivo
    args:
        ruta (string): Ruta del archivo   
    """
        
        puntero=self
        try:
            with open(ruta,"tw") as archivo:
                self.agregar_elemento(puntero.descripcion,ruta)
                self.agregar_elemento(puntero.semana,ruta)
                self.agregar_elemento(puntero.curso_asociado,ruta)
                self.agregar_elemento(puntero.fecha_inicio,ruta)
                self.agregar_elemento(puntero.fecha_final,ruta)
                self.agregar_elemento(puntero.hora_inicio,ruta)
                self.agregar_elemento(puntero.hora_final,ruta)
                self.agregar_elemento(puntero.estado,ruta)
                self.agregar_elemento(puntero.emociones,ruta)
                while puntero.sig!=None:
                    puntero=puntero.sig
                    self.agregar_elemento(puntero.descripcion,ruta)
                    self.agregar_elemento(puntero.semana,ruta)
                    self.agregar_elemento(puntero.curso_asociado,ruta)
                    self.agregar_elemento(puntero.fecha_inicio,ruta)
                    self.agregar_elemento(puntero.fecha_final,ruta)
                    self.agregar_elemento(puntero.hora_inicio,ruta)
                    self.agregar_elemento(puntero.hora_final,ruta)
                    self.agregar_elemento(puntero.estado,ruta)
                    self.agregar_elemento(puntero.emociones,ruta)
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de actividades')

    def agregar_emocion(self,actividad,emocion):
        """Agrega la emocion predominante a una actividad
            args:
            actividad (string): Descripcion de la actividad
            emocion (string): Emocion predominante     
        """
        aux = self

        while(aux.sig != None):
            if(aux.descripcion == actividad):
                aux.emociones = emocion
                return(True)
            else:
                aux = aux.sig

        if(aux.descripcion == actividad):
            aux.emociones = emocion
            return(True)
        else:
            showerror(message='No se ha encontrado una actividad')



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

    def listar_actividades(self):
        return(self.__listar_actividades(self))
    
    def __listar_actividades(self,l):
        """Genera una lista de la actividades
    args:
        lista (lista): Lista de actividades      
    """
        datos=[]
        if l!=None:
            datos.append(' [Actividad:] '+l.descripcion +' [Curso:]'+l.curso_asociado+ ' [Estado de ánimo:] ' +l.emociones )
            datos+=self.__listar_actividades(l.sig)
        return (datos)
    


        

    def arbol (self,lista):
        """Inserta una actividad
        """
        l = lista
        raiz = Actividad(l.descripcion,l.semana,l.curso_asociado,l.fecha_inicio,l.fecha_final,l.hora_inicio,l.hora_final,l.estado,l.emociones)
        pass
        self.__arbol(self,l.sig)

    def __arbol(self,raiz,nn):
        """Inserta una actividad en el arbol (Por Semana)
        Args
        -raiz : (arbol) Raiz 
        -nn: (instancia) Nueva Actividad
        """
        if nn == None:
            return
        else:
            if (int(raiz.semana) > int(nn.semana)):
                if raiz.iz==None:
                    raiz.iz=nn
                    self.__arbol(raiz.iz,nn.sig)
                else:
                    self.__arbol(raiz.iz,nn.sig)
            else:
                if raiz.der==None:
                    raiz.der=nn
                    self.__arbol(raiz.der,nn.sig)
                else:
                    self.__arbol(raiz.der,nn.sig)


    def listar_orden(self):
        """Imprime el Arbol en orden Alfabetico
        """
        self.__listar_orden(self)

    def __listar_orden(self,raiz):
        global datos
        if raiz!=None:
            self.__listar_orden(raiz.der)
            datos.append('[Semana:]'+raiz.semana+' [Actividad:] '+raiz.descripcion +' [Curso:]'+raiz.curso_asociado+ ' [Estado de ánimo:] ' +raiz.emociones )
            self.__listar_orden(raiz.iz)

     
