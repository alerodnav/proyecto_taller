#Funciones

def agregar_curso(carrera,diccionario,curso):
    """Esta funcion se encarga de agregar cursos a una carrera
    
    args:
        carrera (string): valor con nombre de la carrera
        diccionario (diccionario): diccionario que contiene las carreras y cursos
        curso (string): valor con el nuevo curso a agregar
    """
    for key, value in diccionario.items():
        if(key==carrera):
            value.append(curso)
    diccionario = sorted(diccionario.items())
    return diccionario

    

def modificar_curso(carrera,diccionario,curso1,curso2):
    """Esta funcion se encarga de modificar cursos de una carrera
    
    args:
        carrera (string): valor con nombre de la carrera
        diccionario (diccionario): diccionario que contiene las carreras y cursos
        curso1 (string): valor con el curso a modificar
        curso2 (string): valor con el nuevo curso
    """
    for key, value in diccionario.items():
        if(key==carrera):
            tam=len(value)-1
            for i in range(tam):
                if (value[i]==curso1):
                    value[i]=curso2
    diccionario = sorted(diccionario.items())
    return diccionario

def agregar_carrera(carrera,diccionario):
    """Esta funcion se encarga de agregar una nueva carrera
    
    args:
        carrera (string): valor con nombre de la carrera que se agregará
        diccionario (diccionario): diccionario que contiene las carreras y cursos
    """
    diccionario[carrera] = []
    diccionario = sorted(diccionario.items())
    return diccionario

def modificar_carrera(carrera1,carrera2,diccionario):
    """Esta funcion se encarga de modificar una carrera
    
    args:
        carrera1 (string): valor con nombre de la carrera que se modificará
        carrera2 (string): valor con nombre de la carrera modificada         
        diccionario (diccionario): diccionario que contiene las carreras y cursos
    """
    diccionario[carrera2]=diccionario[carrera1]
    del diccionario[carrera1]
    diccionario = sorted(diccionario.items())
    return diccionario