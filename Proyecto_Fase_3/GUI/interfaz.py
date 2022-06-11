from tkinter import *
from tkinter import messagebox
from clases import *
from funciones_clases import *

v=Tk()
f = Frame(v) 
v.title("Control De Actividades")


# Listas
lista_actividades = consultar_actividades('./Proyecto_Fase_3/datos/actividades.txt')

def f_login(v,fo):
    #Creación de objeto con lo básico del frame
    f = Frame(v)
    f.pack(fill = "both", expand=True)
    f.config(bg = "#ffffff", width= "500",height= "500")

    fo.destroy()
    #Variables
    v_usuario = StringVar()
    v_password = StringVar()
    usuarios = {"Luis":"123","Juan":"123"}
    #Funciones 
    def validacion_login(u,p):
        for key,value in usuarios.items():
            if (key == u) & (value == p):
                f_agregar_actividad(v,f)

    #Creación de objeto con lo básico del frame
    l = Label(f,text="Inicio de Sesion")
    l.config(font=("Times New Roman",50),fg="#ffffff",bg="#4ca2f8", anchor="nw", padx=15)
    l.grid(row=0, column=0, padx=20, pady=20, columnspan=6)
    lbl_usuario = Label(f,text="Usuario")
    lbl_usuario.grid(row=1, column=0,padx=20,pady=20,sticky="e")
    lbl_password = Label(f,text="Contraseña")
    lbl_password.grid(row=2, column=0,padx=20,pady=20,sticky="e")
    txt_password = Entry(f, textvariable=v_usuario)
    txt_password.grid(row=1, column=1,padx=20,pady=20,sticky="e")
    txt_password = Entry(f,show="*", textvariable=v_password)
    txt_password.grid(row=2, column=1,padx=20,pady=20,sticky="e")
    
    #Boton Aceptar
    b = Button(f,text="Aceptar", command=lambda:validacion_login(v_usuario.get(),v_password.get()))
    b.grid(row=4, column=1, padx=20, pady=20)
    #Funciones para el frame
    f.grid_propagate(False)

def f_agregar_actividad(v,fo):
    #Creación de objeto con lo básico del frame
    f = Frame(v)
    f.pack(fill = "both", expand=True)
    f.config(bg = "#ffffff", width= "900",height= "500")
    fo.destroy()
    
    # menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Nueva Actividad")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    #+++++++++++++++ Variables Agregar Actividad ++++++++++++++++++ 
    global lista_cursos
    v_nombre = StringVar()
    v_c_asoc = StringVar()
    v_f_inicio = StringVar()
    v_f_final = StringVar()
    v_h_inicio = StringVar()
    v_h_final = StringVar()
    v_estado = StringVar()

    #Funciones

    def agregar_actividad():
        lista_actividades.insertar(c.Actividad(v_nombre.get(),v_c_asoc.get(),v_f_inicio.get(),v_f_final.get(),v_h_inicio.get(),v_h_final.get(),v_estado.get()))
        lista_actividades.guardar_actividades('./Proyecto_Fase_3/datos/actividades.txt')




    #+++++++++++++++ Widgets ++++++++++++++++++ 
    lbl_nombre = Label(f,text="Nombre: ")
    txt_nombre = Entry (f, textvariable=v_nombre)
    lbl_f_inicio = Label(f,text="Fecha Inicio: ")
    txt_f_inicio = Entry (f, textvariable=v_f_inicio)
    lbl_f_final = Label(f,text="Fecha Final: ")
    txt_f_final = Entry (f, textvariable=v_f_final)
    lbl_h_inicio = Label(f,text="Hora Inicio: ")
    txt_h_inicio = Entry (f, textvariable=v_h_inicio)
    lbl_h_final = Label(f,text="Hora Final: ")
    txt_h_final = Entry (f, textvariable=v_h_final)
    lbl_estado = Label(f,text="Estado: ")
    txt_estado = Entry (f, textvariable=v_estado)
    btn_agregar = Button(f,text="Agregar: ",command=lambda: agregar_actividad())
    

    #+++++++++++++++ Posiciones en grid ++++++++++++++++++ 
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    lbl_nombre.grid(row=1, column=0, sticky="e", padx=20, pady=20)
    txt_nombre.grid(row=1, column=1, padx=20, pady=20)
    lbl_f_inicio.grid(row=2, column=0, sticky="e", padx=20, pady=20)
    txt_f_inicio.grid(row=2, column=1, padx=20, pady=20)
    lbl_f_final.grid(row=2, column=2, sticky="e", padx=20, pady=20)
    txt_f_final.grid(row=2, column=3, padx=20, pady=20)
    lbl_h_inicio.grid(row=3, column=0, sticky="e", padx=20, pady=20)
    txt_h_inicio.grid(row=3, column=1, padx=20, pady=20)
    lbl_h_final.grid(row=3, column=2, sticky="e", padx=20, pady=20)
    txt_h_final.grid(row=3, column=3, padx=20, pady=20)
    lbl_estado.grid(row=4, column=0, sticky="e", padx=20, pady=20)
    txt_estado.grid(row=4, column=1, padx=20, pady=20)
    btn_agregar.grid(row=5, column=3, padx=20, pady=20)

    f.grid_propagate(False)



f_login(v,f)
v.mainloop()