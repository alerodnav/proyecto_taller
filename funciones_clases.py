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
            while l.sig!=None:
                l=l.sig
                agregar_elemento(l.nombre,ruta)
    except FileNotFoundError as error:
        print('El archivo no se encuentra')

#Prueba
lista_carreras = c.Carrera('Ingenieria En Gestion Ambiental')
lista_carreras.insertar(c.Carrera('Ingenieria en Fisica'))

almacenar_datos(lista_carreras,'datos/carreras.text')


def consultar_datos(ruta):
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


print(consultar_datos('datos/carreras.text').nombre)
print(consultar_datos('datos/carreras.text').sig.nombre)

