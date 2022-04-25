from main import estudiantes, administradores, cursos, carreras, semanas
from funciones.funciones import *
from time import sleep

cursos_matriculados = []
actividades_registradas = []
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
            sleep(1)
            menu_principal()
        else:
            print("El usuario no existe o lo datos son invalidos")
            sleep(1)
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
             sleep(2)
             menu_principal()
        else:
            print("El usuario no existe o lo datos son invalidos")
            sleep(2)
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
    [5]- Ver Cursos
    [6]- Ver Carreras
    [7]- Cerrar Sesion
    [0]- Salir
    """.format(administradores[sesion_actual]['nombre_completo']))

def opciones_estudiantes():
    global cursos_matriculados,actividades_registradas
    cursos_matriculados = []
    actividades_registradas = estudiantes[sesion_actual]['actividades']
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
    [5] - Cerrar Sesion
    [0]- Salir
    """.format(estudiantes[sesion_actual]['nombre_completo']))

def menu_principal():
    global cursos,carreras,estudiantes
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
                cursos = agregar_curso(cursos, n, cre, hl, fi, ff, hc, c)
                print("""
                ---------------------------------
                Curso agregado correctamente
                ---------------------------------
                """) 
                sleep(2)                
            elif opcion == "0":
                inicio = False
            elif opcion=="2":
                n1 = input("Nombre del curso a modificar: ")
                n1 = validar_curso(cursos,n1)
                n2 = input("Nombre del nuevo nombre del curso: ")
                cre = input("Numero Creditos: ")
                hl = input("Numero de horas lectivas: ")
                fi = input("Fecha de inicio: (Solo fecha y mes, ej: \"24-04\")")
                ff = input("Fecha final: (Solo fecha y mes, ej: \"27-04\")")
                hc = input("El o los horarios del curso: ")
                c = input("La o las carreras que tiene este curso: ")
                modificar_curso(cursos, n1, n2, cre, hl, fi, ff, hc, c)
                print("""
                ---------------------------------
                Curso modificado correctamente
                ---------------------------------
                """) 
                sleep(2)  

            elif opcion == "3":
                global carreras
                temp_carreras = list(carreras)
                carrer = input('Escriba el nombre de la carrera que desea añadir: ')
                carreras = agregar_carrera(temp_carreras,carrer)
                print(carreras)
                sleep(5)
                
            elif opcion == "4":
                temp_carreras2 = list(carreras)
                limpiar_terminal()
                print(carreras)
                carrer = input('Escriba el nombre de la carrera que desea modificar: ')
                carrer2 = input('Escriba el nuevo nombre de la carrera: ')
                carreras = modificar_carrera(temp_carreras2,carrer,carrer2)
                print(carreras)
                sleep(5)


            elif opcion == "5":
                print(cursos)
                input("\nDigite una tecla para volver")
            elif opcion == "6":
                print(carreras)
                input("\nDigite una tecla para volver")

            elif opcion == "7":
                inicio_sesion() 
        else:
            opciones_estudiantes()
            opcion = input("Digite la opcion que desea realizar: ")
            global cursos_matriculados
            if opcion=="0":
                exit()
            if opcion=="1":
                opcion2 = 1
                while (opcion2!=2):
                    limpiar_terminal()
                    carreras = estudiantes[sesion_actual]['carreras']
                    opcion_curso = ver_cursos(carreras,cursos,'m')
                    num_semana = "*"
                    dia = opcion_curso[1][0][0] #solo envia el dia de la primer fecha
                    h_inicio = opcion_curso[1][0][1] #con un curso, no sirve con 2
                    h_fin = opcion_curso[1][0][2]
                    validacion = validar_matricula_curso(cursos_matriculados,num_semana,dia,h_inicio,h_fin,'c')
                    if(validacion[0]):
                        cursos_matriculados.append({'nombre':opcion_curso[0],'horario_clases':opcion_curso[1],'semana':'*'})
                        print(matricular_curso(opcion_curso[0],cursos,sesion_actual,estudiantes))
                    else:
                        print(validacion[1])

                    print("\nCursos matriculados: ")
                    print(estudiantes[sesion_actual]['cursos'])
                    sleep(2)
                    opcion2 = int(input(
                    """
    Desea matricular otro curso?\n
    [1] Si
    [2] No  """))
            elif opcion == "2":
                limpiar_terminal
                print("=============================")
                print("Nueva Actividad: ")
                print("=============================")
                opcion2 = 1
                while (opcion2!=2):
                    nombre = input("Nombre: ")
                    c_asoc = ver_cursos(carreras, cursos, 'i')
                    fi = input("Fecha Inicio: (Solo fecha y mes, ej: \"24-04\")")
                    ff = input("Fecha Final: (Solo fecha y mes, ej: \"27-04\")")
                    dia = "-"
                    hi = input("Hora Inicio: (Escribela como el ejemplo: \"14:20\")")
                    hf = input("Hora Final: (Escribela como el ejemplo: \"14:20\")")
                    num_semana = encontrar_semana(fi,ff,semanas)
                    estado = input("Estado del curso: 1 - Aprobado      2 - Reprobado       3 - En curso")
                    validacion1 = validar_matricula_curso(cursos_matriculados,num_semana,dia,hi,hf,'c')
                    print(validacion1)
                    validacion2 = validar_matricula_curso(actividades_registradas,num_semana,dia,hi,hf,'a')
                    if(validacion1[0] & validacion2[0]):
                        actividades_registradas.append({'nombre':nombre, 'horario_clases':[dia,hi,hf],'semana':num_semana})
                        print(actividades_registradas)
                        estudiantes[sesion_actual]['actividades'].append({'descripcion': nombre,'curso_asociado':c_asoc,'horario':[dia,hi,hf],'estado':estado})
                        print("Actividad registrada exitosamente")
                    else:
                        if(not(validacion1[0])):
                            print(validacion1[1])
                        if (not(validacion2[0])):
                            print(validacion2[1])
                    # imprimirlas actividades de estudiantes[activ]
                    sleep(2)
                    opcion2 = int(input(
                    """
    Desea matricular otra actividad?\n
    [1] Si
    [2] No  """))

            elif opcion == "3":
                if (comprobar_cantidad_carreras(estudiantes,sesion_actual) == True):
                    limpiar_terminal()
                    print("=============================")
                    print("Carreras Disponibles: ")
                    imprimir_carreras(carreras)
                    print("=============================")
                    carerra_a_iniciar = input("Escriba la carrera que quiere iniciar tal como se ve en pantalla: ")
                    if comprobar_carrera(carreras, carerra_a_iniciar):
                        iniciar_carrera(estudiantes, sesion_actual, carerra_a_iniciar)
                        print("Estas son sus carreras")
                        print(estudiantes[sesion_actual]['carreras'])
                        sleep(2)
                    else:
                        print("Carrera no valida")
                        sleep(2)
                else:
                    limpiar_terminal()
                    print("Usted está cursando 2 carreras, no puedo cursar más de 2 carreras")
                    sleep(2)
            elif opcion == "5":
                inicio_sesion()
    
inicio_sesion()