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

def consultar_actividades(ruta):
    """Carga los datos del archivo de actividades
    args:
        ruta (string): Ruta del archivo     
    """
    datos=None
    try:
        with open(ruta,"tr") as lector:
            nombre=lector.readline()[:-1]
            semana=lector.readline()[:-1]
            curso_asociado=lector.readline()[:-1]
            fecha_inicio=lector.readline()[:-1]
            fecha_final=lector.readline()[:-1]
            hora_inicio=lector.readline()[:-1]
            hora_final=lector.readline()[:-1]
            estado=lector.readline()[:-1]
            emociones=lector.readline()[:-1]
            datos=c.Actividad(nombre,semana,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado,emociones)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                curso_asociado=lector.readline()[:-1]
                fecha_inicio=lector.readline()[:-1]
                fecha_final=lector.readline()[:-1]
                hora_inicio=lector.readline()[:-1]
                hora_final=lector.readline()[:-1]
                estado=lector.readline()[:-1]
                emociones=lector.readline()[:-1]
                if (nombre!=''):
                    datos.insertar(c.Actividad(nombre,semana,curso_asociado,fecha_inicio,fecha_final,hora_inicio,hora_final,estado,emociones))
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
            semana=lector.readline()[:-1]
            curso_asociado=lector.readline()[:-1]
            fecha_inicio=lector.readline()[:-1]
            fecha_final=lector.readline()[:-1]
            hora_inicio=lector.readline()[:-1]
            hora_final=lector.readline()[:-1]
            estado=lector.readline()[:-1]
            datos.append(nombre)
            while (nombre!=''):
                nombre=lector.readline()[:-1]
                semana=lector.readline()[:-1]
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