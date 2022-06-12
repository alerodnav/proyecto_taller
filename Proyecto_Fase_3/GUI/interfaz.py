from tkinter import *
from tkinter import messagebox
from clases import *
from funciones_clases import *
from emociones import *
import threading
import cv2 as cv
import os, io
from google.cloud import vision
from time import sleep


v=Tk()
f = Frame(v) 
v.title("Control De Actividades")

# Listas
lista_actividades = consultar_actividades('./Proyecto_Fase_3/datos/actividades.txt')

# Variables 

tiempo_fotos = 7

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

    
    #Creación de objeto con lo básico del frame
    f = Frame(v)
    f.pack(fill = "both", expand=True)
    f.config(bg = "#222", width= "1020",height= "500")
    fo.destroy()
    
    # menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Nueva Actividad")
    lbl_titulo.config(bg="#222",fg="#ffffff",font=('Helvetica', 40, 'bold'))
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse",pady=20)

    #+++++++++++++++ Variables Agregar Actividad ++++++++++++++++++ 
    global lista_cursos
    v_nombre = StringVar()
    v_c_asoc = StringVar()
    v_f_inicio = StringVar()
    v_f_final = StringVar()
    v_h_inicio = StringVar()
    v_h_final = StringVar()
    v_estado = StringVar()
    v_n_semana = StringVar()

    #Funciones

    

    def agregar_actividad():
        lista_actividades.insertar(c.Actividad(v_nombre.get(),v_c_asoc.get(),v_f_inicio.get(),v_f_final.get(),v_h_inicio.get(),v_h_final.get(),v_estado.get()))
        lista_actividades.guardar_actividades('./Proyecto_Fase_3/datos/actividades.txt')


    def iniciar_registro():
        estado=[True]
        parametros=[estado]
        proceso=threading.Thread(target=tarea_paralela,args=parametros)
        proceso.start()

    def tarea_paralela(estado):
        global tiempo_fotos
        mi_rostro= rostro()
        while estado[0]:
            sleep(tiempo_fotos)
            print('Tomando foto: ')
            imagen = mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False)
            detectar_emociones(imagen)
            
            

    # funcion de prueba 
    def imprimir_emociones():
        global emocion_dominante
        print('Alegre: '+ str(emocion_dominante['Alegre']))
        print('Triste: '+ str(emocion_dominante['Triste']))
        print('Enojado: '+ str(emocion_dominante['Enfadado']))
        print('Sorprendido: '+ str(emocion_dominante['Sorprendido']))
        print('Bajo Expuesto: '+ str(emocion_dominante['Bajo Expuesto']))
        print('Borroso: '+ str(emocion_dominante['Borroso']))
        print('Sombrero: '+ str(emocion_dominante['Sombrero']))


    #+++++++++++++++ Widgets ++++++++++++++++++ 
    lbl_nombre = Label(f,text="Nombre: ")
    lbl_nombre.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_nombre = Entry (f, textvariable=v_nombre)
    lbl_n_semana = Label(f,text="Numero Semana: ")
    lbl_n_semana.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_n_semana = Entry (f, textvariable=v_n_semana)
    lbl_f_inicio = Label(f,text="Fecha Inicio: ")
    lbl_f_inicio.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_f_inicio = Entry (f, textvariable=v_f_inicio)
    lbl_f_final = Label(f,text="Fecha Final: ")
    lbl_f_final.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_f_final = Entry (f, textvariable=v_f_final)
    lbl_h_inicio = Label(f,text="Hora Inicio: ")
    lbl_h_inicio.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_h_inicio = Entry (f, textvariable=v_h_inicio)
    lbl_h_final = Label(f,text="Hora Final: ")
    lbl_h_final.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_h_final = Entry (f, textvariable=v_h_final)
    lbl_estado = Label(f,text="Estado: ")
    lbl_estado.config(bg="#222",fg="#ffffff",font=('Helvetica', 11, 'bold'))
    txt_estado = Entry (f, textvariable=v_estado)
    btn_agregar = Button(f,text="Agregar Actividad",command=lambda: agregar_actividad())
    btn_agregar.config(bg="#2196f3", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_fotos_on = Button(f,text="Iniciar Registro",command=lambda: iniciar_registro())
    btn_fotos_on.config(bg="#02e80a", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_fotos_off = Button(f,text="Detener Registro",command=lambda: imprimir_emociones())
    btn_fotos_off.config(bg="#e00104", fg="#ffffff",font=('Helvetica', 12, 'bold'))
    
    btn_concentrarse_on = Button(f,text="Iniciar Concentracion",command=lambda:print("Funcion Detener Concetracion"))
    btn_concentrarse_on.config(bg="#02e80a", fg="#ffffff",font=('Helvetica', 12, 'bold'))

    btn_concentrarse_off = Button(f,text="Detener Concentracion",command=lambda:print("Funcion Detener Concetracion"))
    btn_concentrarse_off.config(bg="#e00104", fg="#ffffff",font=('Helvetica', 12, 'bold'))

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
    btn_agregar.grid(row=4, column=0,columnspan=2, padx=20, pady=20,sticky="e")

    btn_fotos_on.grid(row=4, column=2,columnspan=2,padx=20, pady=20,sticky="e")
    btn_fotos_off.grid(row=5, column=2,columnspan=2,padx=20, pady=20,sticky="e")
    btn_concentrarse_on.grid(row=4, column=4,columnspan=2,padx=20, pady=20,sticky="e")
    btn_concentrarse_off.grid(row=5, column=4,columnspan=2,padx=20, pady=20,sticky="e")

    f.grid_propagate(False)

f_login(v,f)
v.mainloop()