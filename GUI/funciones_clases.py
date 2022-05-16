import clases as c
def agregar_elemento (elemento,archivo):
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
            agregar_elemento(l.nombre,ruta)
            agregar_elemento(l.usuario,ruta)
            agregar_elemento(l.passwd,ruta)
            while l.sig!=None:
                l=l.sig
                agregar_elemento(l.nombre,ruta)
                agregar_elemento(l.usuario,ruta)
                agregar_elemento(l.passwd,ruta)
    except FileNotFoundError as error:
        print('El archivo no se encuentra')

#Prueba


lista_estudiantes = c.Estudiante('Alejandro','arn','a123')
lista_estudiantes.insertar(c.Estudiante('Deivid','dmg','d123'))

#almacenar_datos(lista_estudiantes,'datos/estudiantes.txt')


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



#lista_estudiantes = c.Estudiante('Alejandro','arn','a123')
#lista_estudiantes.insertar(c.Estudiante('Deivid','dmg','d123'))
#lista_estudiantes.insertar(c.Estudiante('Mario','mcr','m123'))

print(lista_estudiantes.login('dmg','d1123'))
