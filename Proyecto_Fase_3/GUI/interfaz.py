from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from clases import *
from funciones_clases import *
from emociones import *
import threading
import cv2 as cv
import os, io
from google.cloud import vision
from time import sleep
import datetime


v=Tk()
f = Frame(v) 
v.title("Control De Actividades")

# Listas
lista_actividades = consultar_actividades('./Proyecto_Fase_3/datos/actividades.txt')
pass

# Variables
estado = False
estado_concentracion = False
actividad_actual = ''


tiempo_foto = 3 # CAMBIAR A 60 

def f_login(v,fo):
    #Creación de objeto con lo básico del frame
    f = Frame(v)
    f.pack(fill = "both", expand=True)
    f.config(bg = "#222", width= "500",height= "500")

    fo.destroy()
    #Variables
    v_usuario = StringVar()
    v_password = StringVar()
    usuarios = {"Luis":"123","Juan":"123"}
    #Funciones 
    
    def validacion_login(u,p):
        permiso = False
        for key,value in usuarios.items():
            if (key == u) & (value == p):
                permiso = True
                f_agregar_actividad(v,f)
        if not(permiso):
            messagebox.showerror("Error","Usuario o contraseña incorrecta")

    #Creación de objeto con lo básico del frame
    l = Label(f,text="Inicio de Sesion")
    l.config(font=('Helvetica', 40, 'bold'),fg="#2196f3",bg="#ffffff", anchor="nw", padx=15)
    l.grid(row=0, column=0, padx=20, pady=20, columnspan=6)
    lbl_usuario = Label(f,text="Usuario")
    lbl_usuario.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    lbl_usuario.grid(row=1, column=0,padx=20,pady=20,sticky="e")
    lbl_password = Label(f,text="Contraseña")
    lbl_password.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    lbl_password.grid(row=2, column=0,padx=20,pady=20,sticky="e")
    txt_password = Entry(f, textvariable=v_usuario)
    txt_password.grid(row=1, column=1,padx=20,pady=20,sticky="e")
    txt_password = Entry(f,show="*", textvariable=v_password)
    txt_password.grid(row=2, column=1,padx=20,pady=20,sticky="e")
    
    #Boton Aceptar
    b = Button(f,text="Aceptar", command=lambda:validacion_login(v_usuario.get(),v_password.get()))
    b.config(bg="#2196f3", fg="#ffffff",font=('Helvetica', 12, 'bold'))
    b.grid(row=4, column=1, padx=20, pady=20)
    #Funciones para el frame
    f.grid_propagate(False)

def f_agregar_actividad(v,fo):
    """Funcio que despliga ventana de agregar actividades
    args:
        v (instancia): Ventana
        fo (instancia): Control ventana    
    """

    
    #Creación de objeto con lo básico del frame
    f = Frame(v)
    f.pack(fill = "both", expand=True)
    f.config(bg = "#222", width= "1200",height= "600")
    fo.destroy()
    
    # menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Nueva Actividad")
    lbl_titulo.config(bg="#222",fg="#ffffff",font=('Helvetica', 40, 'bold'))
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse",pady=20)

    #+++++++++++++++ Variables Agregar Actividad ++++++++++++++++++ 
    global lista_cursos,lista_actividades
    v_nombre = StringVar()
    v_c_asoc = StringVar()
    v_f_inicio = StringVar()
    v_f_final = StringVar()
    v_h_inicio = StringVar()
    v_h_final = StringVar()
    v_estado = StringVar()
    v_n_semana = StringVar()
    v_curso = StringVar()

    #Funciones

    def agregar_actividad():
        """Esta función agrega una actividad en la lista y la almacena en un archivo    
        """
        lista_actividades.insertar(c.Actividad(v_nombre.get(),v_n_semana.get(),v_curso.get(),v_f_inicio.get(),v_f_final.get(),v_h_inicio.get(),v_h_final.get(),v_estado.get(),''))
        lista_actividades.guardar_actividades('./Proyecto_Fase_3/datos/actividades.txt')


    def iniciar_registro():
        """Esta función inicia el registro de fotos   
        """
        btn_fotos_on.grid_forget()
        btn_fotos_off.grid(row=6, column=2,columnspan=2,padx=20, pady=20,sticky="e")
        global estado,actividad_actual
        if not(estado):
            fecha_actual = datetime.datetime.now()
            hora_actual = datetime.datetime.now().strftime('%H:%M')
            actividad_actual = lista_actividades.buscar_x_fecha_hora(fecha_actual,hora_actual)
            pass
            estado=[True]
            parametros=[estado]
            proceso=threading.Thread(target=tarea_paralela,args=parametros)
            proceso.start()

    def tarea_paralela(estado):
        """Funcion que inicia la tarea paralela para no detener el programa principal
        args:
            estado(bool): Estado de la tarea
        """
        global estado_concentracion
        mi_rostro= rostro()
        while estado[0]:
            sleep(5)
            print('Tomando foto: ')
            imagen = mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False)
            if estado_concentracion:
                detectar_emociones(imagen,True,True)
            else:
                detectar_emociones(imagen,False,True)
            
            
    def iniciar_concentracion():   
        """Función que inicia el control de concentración   
        """ 
        btn_concentrarse_on.grid_forget()
        btn_concentrarse_off.grid(row=6, column=4,columnspan=2,padx=20, pady=20,sticky="w")
        global estado_concentracion
        if not(estado_concentracion):
            fecha_actual = datetime.datetime.now()
            hora_actual = datetime.datetime.now().strftime('%H:%M')
            actividad_actual = lista_actividades.buscar_x_fecha_hora(fecha_actual,hora_actual)
            pass
            estado_concentracion=[True]
            parametros=[estado_concentracion]
            proceso=threading.Thread(target=concentracion_paralela,args=parametros)
            proceso.start()

    def concentracion_paralela(estado_concentracion):
        """Permite que la ejecución del control de concentración se ejecute de forma paralela 
        args:
            estado_concentracion(bool): Estado de la tarea  
        """
        global tiempo_foto,estado
        mi_rostro= rostro()
        while estado_concentracion[0]:
            if usuario_concentrado():
                sleep(tiempo_foto)
                print('Tomando foto Concentracion...')
                imagen = mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False)
                if estado:
                    detectar_emociones(imagen,True,True)
                else:
                    detectar_emociones(imagen,True,False)
    
    def detener_concentracion(): 
        """Función que detiene el control de concentración   
        """ 
        btn_concentrarse_off.grid_forget()
        btn_concentrarse_on.grid(row=6, column=4,columnspan=2,padx=20, pady=20,sticky="w")
        global estado_concentracion
        estado_concentracion[0]=False  # Aca se detiene la toma de fotos
            
    def detener_registro(): 
        """Función que detiene el registro de capturas y alamacena la emoción predominante   
        """ 
        btn_fotos_off.grid_forget()
        btn_fotos_on.grid(row=6, column=2,columnspan=2,padx=20, pady=20,sticky="e")
        global emocion_dominante,estado,lista_actividades,actividad_actual
        estado[0]=False  # Aca se detiene la toma de fotos

        em = sorted(emocion_dominante.items(), key=lambda x: x[1]) 

        lista_actividades.agregar_emocion(actividad_actual,em[6][0])

        lista_actividades.guardar_actividades('./Proyecto_Fase_3/datos/actividades.txt')

    def actualizar_cmb():
        """Función que actualiza el combobox del reporte de actividades  
        """ 
        global lista_actividades

        reportes_act = lista_actividades.listar_actividades()
        cmb_reportes["values"]= reportes_act


    def arbol_actividades():

        global lista_actividades,datos
        lista_actividades.arbol(lista_actividades)
        
        lista_actividades.listar_orden()
        cmb_reporte_sem["values"]= datos
        datos=[]
       

   

    #+++++++++++++++ Widgets ++++++++++++++++++ 
    lbl_nombre = Label(f,text="Nombre: ")
    lbl_nombre.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_nombre = Entry (f, textvariable=v_nombre)
    lbl_n_semana = Label(f,text="Numero Semana: ")
    lbl_n_semana.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_n_semana = Entry (f, textvariable=v_n_semana)
    lbl_f_inicio = Label(f,text="Fecha Inicio: ")
    lbl_f_inicio.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_f_inicio = Entry (f, textvariable=v_f_inicio)
    lbl_f_final = Label(f,text="Fecha Final: ")
    lbl_f_final.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_f_final = Entry (f, textvariable=v_f_final)
    lbl_h_inicio = Label(f,text="Hora Inicio: ")
    lbl_h_inicio.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_h_inicio = Entry (f, textvariable=v_h_inicio)
    lbl_h_final = Label(f,text="Hora Final: ")
    lbl_h_final.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_h_final = Entry (f, textvariable=v_h_final)
    lbl_estado = Label(f,text="Estado: ")
    lbl_estado.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_estado = Entry (f, textvariable=v_estado)

    lbl_curso = Label(f,text="Curso Asociado: ")
    lbl_curso.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    txt_curso = Entry (f, textvariable=v_curso)

    lbl_reporte = Label(f,text="Reportes: ")
    lbl_reporte.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    cmb_reportes = Combobox(f,state="readonly",width=80)
    reportes_act = lista_actividades.listar_actividades()
    cmb_reportes["values"]= reportes_act


    lbl_reporte_sem = Label(f,text="Reportes Semanales: ")
    lbl_reporte_sem.config(bg="#222",fg="#ffffff",font=('Helvetica', 11))
    cmb_reporte_sem = Combobox(f,state="readonly",width=80)
  
    btn_agregar = Button(f,text="Agregar Actividad",command=lambda: agregar_actividad())
    btn_agregar.config(bg="#2196f3", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_fotos_on = Button(f,text="Iniciar Registro",command=lambda: iniciar_registro())
    btn_fotos_on.config(bg="#02e80a", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_fotos_off = Button(f,text="Detener Registro",command=lambda: detener_registro())
    btn_fotos_off.config(bg="#e00104", fg="#ffffff",font=('Helvetica', 12, 'bold'))
    
    btn_concentrarse_on = Button(f,text="Iniciar Concentracion",command=lambda:iniciar_concentracion())
    btn_concentrarse_on.config(bg="#02e80a", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_act_c = Button(f,text="Actualizar",command=lambda: actualizar_cmb())
    btn_act_c.config(bg="#2196f3", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_concentrarse_off = Button(f,text="Detener Concentracion",command=lambda:detener_concentracion())
    btn_concentrarse_off.config(bg="#e00104", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_reporte_sem = Button(f,text="Ver Reporte Semanal",command=lambda: arbol_actividades())
    btn_reporte_sem.config(bg="#2196f3", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    

    #+++++++++++++++ Posiciones en grid ++++++++++++++++++ 
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    lbl_nombre.grid(row=1, column=0, sticky="e", padx=20, pady=20)
    txt_nombre.grid(row=1, column=1, padx=20, pady=20)
    lbl_n_semana.grid(row=1, column=2, sticky="e", padx=20, pady=20)
    txt_n_semana.grid(row=1, column=3, padx=20, pady=20)
    lbl_f_inicio.grid(row=1, column=4, sticky="e", padx=20, pady=20)
    txt_f_inicio.grid(row=1, column=5, padx=20, pady=20)
    lbl_f_final.grid(row=2, column=0, sticky="e", padx=20, pady=20)
    txt_f_final.grid(row=2, column=1, padx=20, pady=20)
    lbl_h_inicio.grid(row=2, column=2, sticky="e", padx=20, pady=20)
    txt_h_inicio.grid(row=2, column=3, padx=20, pady=20)
    lbl_h_final.grid(row=2, column=4, sticky="e", padx=20, pady=20)
    txt_h_final.grid(row=2, column=5, padx=20, pady=20)
    lbl_estado.grid(row=3, column=0, sticky="e", padx=20, pady=20)
    txt_estado.grid(row=3, column=1, padx=20, pady=20)

    lbl_curso.grid(row=3, column=2, sticky="e", padx=20, pady=20)
    txt_curso.grid(row=3, column=3, padx=20, pady=20)

    lbl_reporte.grid(row=4, column=0, sticky="e", padx=20, pady=20)
    cmb_reportes.grid(row=4,column=1,columnspan=3, padx=20,pady=20,sticky="nsew")


    cmb_reporte_sem.grid(row=5,column=1,columnspan=3, padx=20,pady=20,sticky="nsew")
    lbl_reporte_sem.grid(row=5, column=0, sticky="e", padx=20, pady=20)
    cmb_reportes.grid(row=4,column=1,columnspan=3, padx=20,pady=20,sticky="nsew")

    btn_reporte_sem.grid(row=5, column=4, padx=20, pady=20,sticky="w") # BTN DE PRUEBA


    btn_agregar.grid(row=3, column=4,columnspan=2, padx=20, pady=20,sticky="w")

    btn_fotos_on.grid(row=6, column=2,columnspan=2,padx=20, pady=20,sticky="e")
    btn_fotos_off.grid_forget()

    btn_concentrarse_on.grid(row=6, column=4,columnspan=2,padx=20, pady=20,sticky="w")
    btn_concentrarse_off.grid_forget()
    btn_act_c.grid(row=4, column=4,padx=20, pady=20,sticky="w")

    f.grid_propagate(False)

f_login(v,f)
v.mainloop()