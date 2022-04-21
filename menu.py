from main import estudiantes, administradores
from funciones.funciones import cifrar_contrasena, limpiar_terminal, agregar_curso
from time import sleep
from main import cursos


def menu_login():
    """Esta funcion despliguea el menu de login en la consola
    """
    limpiar_terminal()
    print("""
    ==============================================

    ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
    ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
    ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
    ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
    ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║

    Digite una opcion

    [1] Iniciar sesion como Estudiante
    [2] Iniciar sesion como Administrador

    ==============================================
    """)
    return()

def validar_usuario_contrasena(user,pswd,tipo):
    """Esta valida si el usuario y contrasena son correctos
    
    args:
        user (string): Usuario
        pswd (string): Contrasena del usuario
        tipo (bool): Indica si el usuario es estudiante o administrador
    """
    if (tipo):
        user_dic = administradores
    else:
        user_dic = estudiantes 
    validar = False
    largo_dic = len(user_dic)
    for x in range(largo_dic):
        if ((user_dic[x]['usuario'] == user) and (user_dic[x]['contrasena'] == pswd)):
            global sesion_actual #Esta variable guarda la persona que ha iniciado sesion
            sesion_actual = x
            validar = True
            break
        else:
            validar = False
    return(validar)

def inicio_sesion():
    global permisos_adm 
    menu_login()
    opcion_login = input("Digite la opcion: ")

    if opcion_login == "1":
        es_us = input("Digite el usuario: ") 
        es_pswd = input("Digite la contraseña: ")
        if (validar_usuario_contrasena(es_us, cifrar_contrasena(es_pswd), False)):
            print("""
            ---------------------------------
            Has iniciado sesion correctamente
            ---------------------------------
            """) 
            permisos_adm = False
            sleep(3)
            menu_principal()
        else:
            print("El usuario no existe o lo datos son invalidos")
            sleep(3)
            inicio_sesion()
            

    elif opcion_login == "2":
        adm_us = input("Digite el usuario: ") 
        adm_pswd = input("Digite la contraseña: ")
        if (validar_usuario_contrasena(adm_us, cifrar_contrasena(adm_pswd), True)):
             print("""
            ---------------------------------
            Has iniciado sesion correctamente
            ---------------------------------
            """)
             permisos_adm = True
             sleep(3)
             menu_principal()
        else:
            print("El usuario no existe o lo datos son invalidos")
            sleep(3)
            inicio_sesion()

    return()

def opciones_administador():
    limpiar_terminal()
    print("""
    ==============================================
    =                                            =
    =       BIENVENIDO AL MENU PRINCIPAL         =
    =                                            =       
    ==============================================
    
    Usuario: {0}

    OPCIONES

    [1]- Agregar Curso
    [2]- Modificar Curso
    [3]- Agregar Carrera
    [4]- Modificar Carrera
    [0]- Salir
    """.format(administradores[sesion_actual]['nombre_completo']))

def opciones_estudiantes():
    limpiar_terminal()
    print("""
    ==============================================
    =                                            =
    =       BIENVENIDO AL MENU PRINCIPAL         =
    =                                            =       
    ==============================================
    
    Usuario: {0}

    OPCIONES

    [1]- Matricular Cursos
    [2]- Agregar actividades
    [3]- Iniciar Carrera
    [4]- Cambiar Carrera
    [0]- Salir
    """.format(estudiantes[sesion_actual]['nombre_completo']))


def menu_principal():
    inicio = True
    while(inicio):
        if (permisos_adm):
            opciones_administador()
            opcion = input("Digite la opcion que desea realizar: ")

            if opcion == "1":
                n = input("Nombre del curso: ")
                cre = input("Numero Creditos: ")
                hl = input("Numero de horas lectivas: ")
                fi = input("Fecha de inicio (): ")
                ff = input("Fecha Final (): ")
                hc = input("El o los horarios del curso: ")
                c = input("La o las carreras que tiene este curso: ")
                agregar_curso(cursos, n, cre, hl, fi, ff, hc, c)
            elif opcion == "0":
                inicio = False
        
        else:
            opciones_estudiantes()
            opcion = input("Digite la opcion que desea realizar")
    
inicio_sesion()




    