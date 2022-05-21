# Clase principal lista con puntero

from tkinter.messagebox import showerror
from funciones_clases import *

class Lista:
    sig=None

    def insertar (self,p):
        self.__insertar(self,p)
    
    def __insertar (self,l,p):
        if l.sig==None:
            l.sig=p
        else:
            self.__insertar(l.sig,p)

    def agregar_elemento(self,elemento,archivo):
        try:
            with open(archivo,"ta") as archivo:
                archivo.writelines(elemento+"\n")
        except FileNotFoundError as error:
            with open(archivo,"tw") as archivo:
                archivo.writelines(elemento+"\n")

#Clase estudiante

class Estudiante (Lista):
    
    #Atributos de la clase estudiante (Nombre, usuario, contrasena,carreras,cursos,actividades)

    nombre_completo=None
    usuario=None
    passwd=None
    carreras=None
    cursos=None
    actividades=None

    #Constructor de la clase estudiante (Es obligatorio registrar el nombre,usuario y contrasena)

    def __init__(self,nombre,usuario,passwd):
        self.nombre_completo=nombre
        self.usuario=usuario
        self.passwd= passwd
        self.carreras=[]
        self.cursos=[]
        self.actividades=[]


    def login(self,u,p):
        aux = self
        while (aux.sig != None):
            if ((aux.usuario == u) and (aux.passwd == p)):
                return True
            else:
                aux = aux.sig
        if ((aux.usuario == u) and (aux.passwd == p)):
                return True
        else:
                return False
    
    def guardar_estudiante(self):
        puntero=self
        try:
            with open("./datos/estudiantes.txt","tw") as archivo:
                archivo.writelines([puntero.nombre_completo,puntero.usuario,puntero.passwd,puntero.carreras,puntero.cursos,puntero.actividades].__str__()+"\n")
                while puntero.sig!=None:
                    puntero=puntero.sig
                    archivo.writelines([puntero.nombre_completo,puntero.usuario,puntero.passwd,puntero.carreras,puntero.cursos,puntero.actividades].__str__()+"\n")
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de estudiantes')

    def detectar_estudiantes(self,u):
        aux = self
        while (aux.sig != None):
            if (aux.usuario == u):
                return aux.nombre_completo
            else:
                aux = aux.sig
        if (aux.usuario == u):
                return aux.nombre_completo
        else:
                return False
    
    def inic_carrera(self,n,c):
        aux = self
        while (aux.sig != None):
            if (aux.nombre_completo == n):
                aux.carreras.append(c)
                return
            else:
                aux = aux.sig
        if (aux.nombre_completo == n):
                aux.carreras.append(c)
        else:
                showerror(message='No se ha encontrado la carrera')


#Clase Administrador

class Administrador (Lista):
    
    #Atributos de la clase estudiante (Nombre, usuario, contrasena,carreras,cursos,actividades)

    nombre_completo=None
    usuario=None
    passwd=None
    telefono=None

    #Constructor de la clase estudiante (Es obligatorio registrar el nombre,usuario y contrasena)

    def login(self,u,p):
        aux = self
        while (aux.sig != None):
            if ((aux.usuario == u) and (aux.passwd == p)):
                return True
            else:
                aux = aux.sig
        if ((aux.usuario == u) and (aux.passwd == p)):
                return True
        else:
                return False

    def __init__(self,nombre,usuario,passwd):
        self.nombre=nombre
        self.usuario=usuario
        self.passwd= passwd

#Clase Carrera    
class Carrera(Lista):
    #Atributos de la clase carrera (Nombre)
    nombre=None

    def __init__(self,nombre):
        self.nombre=nombre

    def guardar_carreras(self,ruta):
        puntero=self
        try:
            with open(ruta,"tw") as archivo:
                self.agregar_elemento(puntero.nombre,ruta)
                while puntero.sig!=None:
                    puntero=puntero.sig
                    self.agregar_elemento(puntero.nombre,ruta)
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de carreras')

    def listar_carreras(self):
        return(self.__listar_carreras(self))
    
    def __listar_carreras(self,l):
        datos=[]
        if l!=None:
            datos.append(l.nombre)
            datos+=self.__listar_carreras(l.sig)
        return (datos)

    def modificar_carrera(self,c,nc):
        aux = self
        while (aux.sig != None):
            if (aux.nombre == c):
                aux.nombre = nc
                return
            else:
                aux = aux.sig
        if ((aux.nombre == c)):
                aux.nombre == nc
        else:
                showerror(message='No se ha encontrado la carrera que se desea modificar')

    def buscar_x_nombre(self,c):
        aux = self
        while (aux.sig != None):
            if (aux.nombre == c):
                return aux.nombre
            else:
                aux = aux.sig
        if (aux.nombre == c):
                return aux.nombre
        else:
                showerror(message='No se ha encontrado la carrera')


    

class Curso(Lista):

    nombre=None
    creditos=None
    horas_lectivas=None
    fecha_inicio=None
    fecha_final=None
    carreras=None

    def __init__(self,nombre,creditos,horas_lectivas,fecha_inicio,fecha_final,carreras):
        self.nombre=nombre
        self.creditos=creditos
        self.horas_lectivas=horas_lectivas
        self.fecha_inicio=fecha_inicio
        self.fecha_final=fecha_final
        self.carreras=carreras
        
    def guardar_cursos(self,ruta):
        puntero=self
        try:
            with open(ruta,"tw") as archivo:
                self.agregar_elemento(puntero.nombre,ruta)
                self.agregar_elemento(puntero.creditos,ruta)
                self.agregar_elemento(puntero.horas_lectivas,ruta)
                self.agregar_elemento(puntero.fecha_inicio,ruta)
                self.agregar_elemento(puntero.fecha_final,ruta)
                self.agregar_elemento(puntero.carreras,ruta)
                while puntero.sig!=None:
                    puntero=puntero.sig
                    self.agregar_elemento(puntero.nombre,ruta)
                    self.agregar_elemento(puntero.creditos,ruta)
                    self.agregar_elemento(puntero.horas_lectivas,ruta)
                    self.agregar_elemento(puntero.fecha_inicio,ruta)
                    self.agregar_elemento(puntero.fecha_final,ruta)
                    self.agregar_elemento(puntero.carreras,ruta)
        except FileNotFoundError as error:
            showerror(message='No se pudo guardar en el archivo de cursos')

    def listar_cursos(self):
        return(self.__listar_cursos(self))
    
    def __listar_cursos(self,l):
        datos=[]
        if l!=None:
            datos.append(l.nombre)
            datos.append(l.creditos)
            datos.append(l.horas_lectivas)
            datos.append(l.fecha_inicio)
            datos.append(l.fecha_final)
            datos.append(l.carreras)
            datos+=self.__listar_cursos(l.sig)
        return (datos)

    def modificar_cursos(self,n1,n2,c2,hl2,fi2,ff2,ca2):
        aux = self
        while (aux.sig != None):
            if (aux.nombre == n1):
                aux.nombre = n2
                aux.creditos = c2
                aux.horas_lectivas = hl2
                aux.fecha_inicio = fi2
                aux.fecha_final = ff2
                aux.carreras = ca2
                return
            else:
                aux = aux.sig
        if ((aux.nombre == n1)):
                aux.nombre = n2
                aux.creditos = c2
                aux.horas_lectivas = hl2
                aux.fecha_inicio = fi2
                aux.fecha_final = ff2
                aux.carreras = ca2
        else:
                showerror(message='No se ha encontrado el curso que se desea modificar')

 
    

class Actividad(Lista):

    descripcion=None
    curso_asociado=None
    horario=None
    hora_inicio=None
    hora_final=None
    estado=None

    def __init__(self,descripcion,curso_asociado,horario,hora_inicio,hora_final,estado):
        self.descripcion=descripcion
        self.curso_asociado=curso_asociado
        self.horario=horario
        self.hora_inicio=hora_inicio
        self.hora_final=hora_final
        self.estado=estado
    




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




