from main import estudiantes, administradores
from funciones.funciones import cifrar_contrasena, limpiar_terminal
from menu import menu_principal
from time import sleep

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
    if (tipo):
        user_dic = administradores
    else:
        user_dic = estudiantes 
    validar = False
    for x in range(len(user_dic)):
        if ((user_dic[x]['usuario'] == user) and (user_dic[x]['contrasena'] == pswd)):
            global sesion_actual #Esta variable guarda la persona que ha iniciado sesion
            sesion_actual = x
            validar = True
            break
        else:
            validar = False
    return(validar)

def inicio_sesion():
    menu_login()
    opcion_login = input("Digite la opcion: ")

    if opcion_login == "1":
        es_us = input("Digite el usuario: ") 
        es_pswd = input("Digite la contraseña: ")
        if (validar_usuario_contrasena(es_us, cifrar_contrasena(es_pswd), False)):
            print("Has iniciado sesion correctamente")
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
             print("Has iniciado sesion correctamente")
             sleep(3)
             menu_principal()
        else:
            print("El usuario no existe o lo datos son invalidos")
            sleep(3)
            inicio_sesion()

    return()

inicio_sesion()