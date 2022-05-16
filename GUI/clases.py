# Clase principal lista con puntero

class Lista:
    sig=None

    def insertar (self,p):
        self.__insertar(self,p)
    
    def __insertar (self,l,p):
        if l.sig==None:
            l.sig=p
        else:
            self.__insertar(l.sig,p)

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
        self.nombre=nombre
        self.usuario=usuario
        self.passwd= passwd


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

#Clase Administrador

class Administrador (Lista):
    
    #Atributos de la clase estudiante (Nombre, usuario, contrasena,carreras,cursos,actividades)

    nombre_completo=None
    usuario=None
    passwd=None
    telefono=None

    #Constructor de la clase estudiante (Es obligatorio registrar el nombre,usuario y contrasena)

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




