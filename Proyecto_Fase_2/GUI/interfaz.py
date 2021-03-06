from gc import callbacks
from glob import glob
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
#from GUI.clases import Carrera
from funciones_clases import *
import clases as c


v=Tk()
v.iconbitmap("GUI/software.ico")
f = Frame(v) 

#Variables
texto = StringVar()
op_tipoUsuario = IntVar()
validar_usuario = StringVar()
validar_password = StringVar()

autoguardado_est = IntVar()

autoguardado_adm = IntVar()

#Usuario_Actual
usuario_estudiante=''
usuario_actual=''

#listas
lista_estudiantes = consultar_estudiantes()
lista_administradores = consultar_administradores()
lista_carreras = consultar_carreras('./datos/carreras.txt')
lista_cursos = consultar_cursos('./datos/cursos.txt')
lista_actividades = consultar_actividades('./datos/actividades.txt')
pass

#Clase frame
class frame():
    ventana = None
    titulo = None
    bg = None
    width = None
    height = None

    def __init__(self,ventana,titulo,bg,width,height):
        ventana.title(titulo)
        self.f = Frame(ventana)
        self.f.pack(fill = "both", expand=True)
        self.f.pack
        self.f.config(bg = bg, width= width,height= height)


#Funciones


def guardar_lista_carreras():
    """Guarda los datos de la lista de carreras   
    """
    global listas_carreras
    lista_carreras.guardar_carreras('./datos/carreras.txt')

def guardar_lista_cursos():
    """Guarda los datos de la lista de cursos   
    """
    global listas_cursos
    lista_cursos.guardar_cursos('./datos/cursos.txt')

def guardar_lista_actividades():
    """Guarda los datos de la lista de actividades   
    """
    global lista_actividades
    lista_actividades.guardar_actividades('./datos/actividades.txt')
    
def guardar_cursos_estudiante():
    """Guarda los datos de la lista de cursos de estudiantes   
    """
    global lista_estudiantes
    lista_estudiantes.guardar_estudiante('./datos/estudiantes.txt',usuario_estudiante)
    
def validacion_login(v,f,op,u,c):
    global usuario_actual,usuario_estudiante
    usuario_estudiante=u
    if op==0: 
        if lista_administradores.login(u,c):
            
            f_administrador(v,f)
        else:
            messagebox.showwarning('Error','Los datos ingresados no son correctos')
    elif op==1: 
        if lista_estudiantes.login(u,c):

            usuario_actual = lista_estudiantes.detectar_estudiantes(u)
            pass
            f_estudiante(v,f)
        else:
            messagebox.showwarning('Error','Los datos ingresados no son correctos')
    else:
        messagebox.showwarning("Atenci??n","No has marcado ningun tipo de usuario")

def cerrar_ventana():
    opcion = messagebox.askquestion("Salir","??Deseas salir del programa?")
    if opcion == "yes":
        v.destroy()

def cerrar_sesion(v,f):
    opcion = messagebox.askquestion("Cerrar Sesi??n","??Deseas cerrar sesi??n?")
    if opcion == "yes":
        #+++++++++++ FALTARIA CERRAR LA SESION_ACTUAL (EL ID VOLVERLO NULL O ALGO)++++++
        f_login(v,f)

#Cargar los men??s desde una sola funcion
def menu_estudiante(v,f):

    global autoguardado_est

    seccionMenu = Menu(f)
    v.config(menu=seccionMenu, width=300, height=300)
    accionesMenu = Menu(seccionMenu, tearoff=0)
    accionesMenu.add_command(label="Iniciar Carrera",command=lambda:f_iniciar_carrera(v,f))
    accionesMenu.add_command(label="Cambiar Carrera", command=lambda:f_cambiar_carrera(v,f))
    accionesMenu.add_separator()
    accionesMenu.add_command(label="Matricular Cursos", command=lambda:f_matricular_curso(v,f))
    accionesMenu.add_command(label="Agregar Actividades", command=lambda:f_agregar_actividad(v,f))
    sesionMenu=Menu(seccionMenu, tearoff=0)
    sesionMenu.add_command(label= "Cerrar sesi??n", command=lambda:cerrar_sesion(v,f))
    sesionMenu.add_command(label= "Salir",command=lambda:cerrar_ventana())
    verMenu = Menu(seccionMenu, tearoff=0)
    # verMenu.add_command(label="Ver Reportes", command=lambda:f_reportes(v,f))
    verMenu.add_command(label="Ver Cursos matriculados", command=lambda:f_cursos_matriculados(v,f))
    verMenu.add_separator()
    verMenu.add_command(label="Ver Actividades registradas",command=lambda:f_actividades_registradas(v,f))

    #Menu de guardado

    guardarMenu = Menu(seccionMenu, tearoff=0)
    guardarMenu.add_command(label="Guardar", command=lambda:[guardar_lista_actividades(),guardar_cursos_estudiante()])
    guardarMenu.add_checkbutton(label="Autoguardado", variable=autoguardado_est,onvalue=1, offvalue=0)
   

    seccionMenu.add_cascade(label="Archivo", menu=guardarMenu)
    seccionMenu.add_cascade(label="Acciones", menu=accionesMenu)
    seccionMenu.add_cascade(label="Ver", menu=verMenu)
    seccionMenu.add_cascade(label="Sesi??n", menu=sesionMenu)
   

def menu_administrador(v,f):

    global autoguardado_adm

    seccionMenu = Menu(f)
    v.config(menu=seccionMenu, width=300, height=300)
    accionesMenu = Menu(seccionMenu, tearoff=0)
    accionesMenu.add_command(label="Agregar Carrera",command=lambda:f_agregar_carrera(v,f))
    accionesMenu.add_command(label="Modificar Carrera",command=lambda:f_modificar_carrera(v,f))
    accionesMenu.add_separator()
    accionesMenu.add_command(label="Agregar Curso", command=lambda:f_agregar_curso(v,f))
    accionesMenu.add_command(label="Modificar Curso",command=lambda:f_modificar_curso(v,f))
    sesionMenu=Menu(seccionMenu, tearoff=0)
    sesionMenu.add_command(label= "Cerrar sesi??n",command=lambda:cerrar_sesion(v,f))
    sesionMenu.add_command(label= "Salir",command=lambda:cerrar_ventana())
    verMenu = Menu(seccionMenu, tearoff=0)
    verMenu.add_command(label="Ver Cursos",command=lambda:f_ver_cursos(v,f))
    verMenu.add_separator()
    verMenu.add_command(label="Ver Carreras", command=lambda:f_ver_carreras(v,f))

    #Menu de guardado
    guardarMenu = Menu(seccionMenu, tearoff=0)
    guardarMenu.add_command(label="Guardar", command=lambda:[guardar_lista_carreras(),guardar_lista_cursos()])
    guardarMenu.add_checkbutton(label="Autoguardado",variable=autoguardado_adm, onvalue=1, offvalue=0)

    seccionMenu.add_cascade(label="Archivo", menu=guardarMenu)
    seccionMenu.add_cascade(label="Acciones", menu=accionesMenu)
    seccionMenu.add_cascade(label="Ver", menu=verMenu)
    seccionMenu.add_cascade(label="Sesi??n", menu=sesionMenu)

#Frames
def f_login(v,fo):
    #Creaci??n de objeto con lo b??sico del frame
    contenido_frame = frame(v,"Inicio de sesi??n","#ffffff","500","500")
    fo.destroy()
    f = contenido_frame.f
    # Widgets extras
    l = Label(f,text="Inicio de sesi??n")
    l.config(font=("Times New Roman",50),fg="#ffffff",bg="#4ca2f8", anchor="nw", padx=15)
    l.grid(row=0, column=0, padx=20, pady=20, columnspan=6)
    lbl_tipo_usuario = Label(f,text="Tipo de usuario")
    lbl_tipo_usuario.grid(row=1, column=0,padx=20,pady=20,sticky="e")

    #Prueba del comboBox++++++++++++++++++++++++++++++
    carreras_disponibles=["Administrador", "Estudiante"]
    cmb_tipo_usuario = Combobox(f,state="readonly",width=15)
    cmb_tipo_usuario.grid(row=1,column=1, padx=20,pady=20,sticky="nsew")
    cmb_tipo_usuario["values"]=carreras_disponibles
    cmb_tipo_usuario.set("Elige una opci??n")

    #Usuario Y Contrase??a
    lbl_usuario=Label(f,text="Usuario")
    txt_usuario=Entry(f, textvariable=validar_usuario)
    lbl_password=Label(f, text="Contrase??a")
    txt_password=Entry(f, show="*", textvariable=validar_password)
    lbl_usuario.grid(row=2,column=0, padx=20, pady=20, sticky="e")
    txt_usuario.grid(row=2,column=1, padx=20, pady=20, sticky="e")
    lbl_password.grid(row=3,column=0, padx=20, pady=20, sticky="e")
    txt_password.grid(row=3,column=1, padx=20, pady=20, sticky="e")
    
    #Boton Aceptar
    b = Button(f,text="Aceptar", command=lambda:validacion_login(v,f,cmb_tipo_usuario.current(),validar_usuario.get(),validar_password.get()))
    b.grid(row=4, column=1, padx=20, pady=20)
    


    #Funciones para el frame
    f.grid_propagate(False)

def f_estudiante(v,fo):
    global usuario_actual
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    #Men??
    menu_estudiante(v,f)


    #Widgets del frame
    l = Label(f,text="Bienvenido: "+ usuario_actual)
    l.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    l.grid(row=0, column=1, padx=20, pady=20, columnspan=6)


    f.grid_propagate(False)

def f_administrador(v,fo):
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f

    #Men??
    menu_administrador(v,f)

    #Widgets del frame
    l = Label(f,text="Bienvenido Administrador")
    l.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    l.grid(row=0, column=1, padx=20, pady=20, columnspan=6)
    f.grid_propagate(False)

def f_iniciar_carrera(v,fo):
    global lista_carreras, usuario_actual
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Iniciar Carrera")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    lbl_carreras = Label(f,text="Seleccione la carrera")
    lbl_carreras.grid(row=1,column=0, padx=20,pady=20,sticky="nsew")
    carreras_disponibles= lista_carreras.listar_carreras()  #Hay que validar si ya inicio una carrera
    cmb_carreras = Combobox(f,state="readonly",width=30)
    cmb_carreras.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    cmb_carreras["values"]=carreras_disponibles
    cmb_carreras.set("Elige una opci??n")
    btn_aceptar = Button(f,text="Matricular",command=lambda:[lista_estudiantes.inic_carrera(usuario_actual,cmb_carreras.get()),lista_estudiantes.guardar_estudiante1()])
    btn_aceptar.grid(row=2,column=1, padx=20,pady=20,sticky="nsew")


    

    f.grid_propagate(False)
    
def f_matricular_curso(v,fo):
    global lista_cursos, lista_estudiantes,usuario_actual
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Matricular Curso")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    #Funciones
    
    
    def matricular_curso():
        lista_estudiantes.guardar_cursos_estudiante(usuario_estudiante,cmb_cursos.get())
        curso_est_autoguardado_est()
        cmb_cursos.set("Elige una opci??n")


    lbl_curso = Label(f,text="Seleccione el curso")
    lbl_curso.grid(row=1,column=0, padx=20,pady=20,sticky="nsew")
    cmb_cursos = Combobox(f,state="readonly",width=30)
    cmb_cursos.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    carrera_estudiante = lista_estudiantes.carrera_estudiante(usuario_estudiante)
    cmb_cursos["values"]=ver_cursos_disponibles(carrera_estudiante)
    cmb_cursos.set("Elige una opci??n")
    btn_aceptar = Button(f,text="Matricular",command=lambda:matricular_curso())
    btn_aceptar.grid(row=2,column=1, padx=20,pady=20,sticky="nsew")

    f.grid_propagate(False)

def f_agregar_actividad(v,fo):
    
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
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
        borrar_texto()
        actividad_autoguardado_est()

    def borrar_texto():
        v_nombre.set('')
        cmb_c_asoc.set('Curso Asociado')
        v_f_inicio.set('')
        v_f_final.set('')
        v_h_inicio.set('')
        v_h_final.set('')
        v_estado.set('')

    #+++++++++++++++ Widgets ++++++++++++++++++ 
    lbl_nombre = Label(f,text="Nombre: ")
    txt_nombre = Entry (f, textvariable=v_nombre)
    lbl_c_asoc = Label(f,text="Curso Asociado: ")
    cmb_c_asoc = Combobox(f,textvariable=v_c_asoc, state="readonly",width=30)
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
    btn_agregar = Button(f,text="Agregar: ",command=lambda:agregar_actividad())

    #+++++++++++++++ Posiciones en grid ++++++++++++++++++ 
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    lbl_nombre.grid(row=1, column=0, sticky="e", padx=20, pady=20)
    txt_nombre.grid(row=1, column=1, padx=20, pady=20)
    lbl_c_asoc.grid(row=1, column=2, sticky="e", padx=20, pady=20)
    cmb_c_asoc.grid(row=1, column=3, padx=20, pady=20)
    cmb_c_asoc["values"]=lista_cursos.listar_nombre_cursos()
    cmb_c_asoc.set("Elige una opci??n")
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


def f_cambiar_carrera(v,fo):
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Cambiar Carrera")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    
    lbl_carreras1 = Label(f,text="Seleccione la Carrera Actual")
    lbl_carreras1.grid(row=1,column=0, padx=20,pady=20,sticky="nsew")
    carreras_disponibles=["Ingenieria En Computacion", "Administraci??n De Empresas","Ingenieria en Produccion Industrial"]
    cmb_carreras1 = Combobox(f,state="readonly",width=30)
    cmb_carreras1.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    cmb_carreras1["values"]=carreras_disponibles
    cmb_carreras1.set("Elige una opci??n")

    lbl_carreras2 = Label(f,text="Seleccione la Nueva Carrera")
    lbl_carreras2.grid(row=2,column=0, padx=20,pady=20,sticky="nsew")
    cmb_carreras2 = Combobox(f,state="readonly",width=30)
    cmb_carreras2.grid(row=2,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    cmb_carreras2["values"]=carreras_disponibles
    cmb_carreras2.set("Elige una opci??n")

    btn_aceptar = Button(f,text="Cambiar",command=lambda:print("Aqui va la funcion de iniciar carrera"))
    btn_aceptar.grid(row=3,column=1, padx=20,pady=20,sticky="nsew")
    
    f.grid_propagate(False)



def f_cursos_matriculados(v,fo):
    global lista_estudiantes
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Cursos Matriculados")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    cmb_cursos = Combobox(f,state="readonly",width=30)
    cmb_cursos.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    cmb_cursos["values"]=lista_estudiantes.ver_cursos_matriculados(usuario_estudiante)
    cmb_cursos.set("Cursos Matriculados")

    f.grid_propagate(False)

def f_actividades_registradas(v,fo):
    contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_estudiante(v,f)
    lbl_titulo = Label(f,text="Actividades Registradas")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    
    actividades = nombre_actividades("./datos/actividades.txt")
    cmb_actividades = Combobox(f,state="readonly",width=30)
    cmb_actividades.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=3)
    cmb_actividades["values"]=actividades
    cmb_actividades.set("Actividades Registradas")
    f.grid_propagate(False)


# def f_reportes(v,fo):
#     contenido_frame = frame(v,"Usuario Estudiante","#ffffff","900","500")
#     fo.destroy()
#     f = contenido_frame.f
#     menu_estudiante(v,f)
#     lbl_titulo = Label(f,text="Reportes")
#     lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
#     lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
#     f.grid_propagate(False)

def f_ver_cursos(v,fo):
    global lista_cursos
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Cursos")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    
    cmb_cursos = Combobox(f,state="readonly",width=30)
    cmb_cursos.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=6)
    cmb_cursos["values"]=lista_cursos.listar_nombre_cursos()
    cmb_cursos.set("Cursos Registrados")
    f.grid_propagate(False)


def f_ver_carreras(v,fo):

    global lista_carreras

    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Carreras")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    cmb_carreras = Combobox(f,state="readonly",width=30)
    cmb_carreras.grid(row=1,column=1, padx=20,pady=20,sticky="nsew",columnspan=6)
    cmb_carreras["values"]=lista_carreras.listar_carreras()
    cmb_carreras.set("Carreras Registradas")
    f.grid_propagate(False)

def f_agregar_curso(v,fo):
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Agregar Curso")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    #Variables
    global lista_cursos
    v_nuevo_curso = StringVar()
    v_num_creditos = StringVar()
    v_h_lectivas = StringVar()
    v_f_inicio = StringVar()
    v_f_final = StringVar()
    c_administracion = IntVar()
    c_computacion = IntVar()
    c_agronomia = IntVar()
    c_produccion = IntVar()
    c_electronica = IntVar()



    def ver_carreras_elegidas(carreras_elegidas):
        if c_administracion.get() == 1:
            carreras_elegidas+='Administracion De Empresas, '
        if c_produccion.get() == 1:
            carreras_elegidas+='Ingenieria En Produccion Industrial, '
        if c_computacion.get() == 1:
            carreras_elegidas+='Ingenieria En Computacion, '
        if c_electronica.get() == 1:
            carreras_elegidas+='Ingenieria Electronica, '
        if c_agronomia.get() == 1:
            carreras_elegidas+='Ingenieria En Agronomia, '
        return carreras_elegidas[:-2]
        
    def agregar_nuevo_curso():
        carreras_elegidas = ''
        carreras_elegidas = ver_carreras_elegidas(carreras_elegidas)
        if v_nuevo_curso.get() != "":
            lista_cursos.insertar(c.Curso(v_nuevo_curso.get(),v_num_creditos.get(),v_h_lectivas.get(),v_f_inicio.get(),v_f_final.get(),carreras_elegidas))
        borrar_texto()
        cursos_autoguardado_adm()

    # ++++++++++++++++ Widgets de este frame ++++++++++++++
    lbl_curso = Label(f,text="Nombre Curso")
    txt_curso = Entry(f, textvariable=v_nuevo_curso)
    lbl_num_creditos = Label(f,text="Numero de Cr??ditos")
    txt_num_creditos = Entry(f, textvariable=v_num_creditos)
    lbl_h_lectivas = Label(f,text="Horas Lectivas")
    txt_h_lectivas = Entry(f, textvariable=v_h_lectivas)
    lbl_f_inicio = Label(f,text="Fecha Inicio")
    txt_f_inicio = Entry(f, textvariable=v_f_inicio)
    lbl_f_final = Label(f,text="Fecha Final")
    txt_f_final = Entry(f, textvariable=v_f_final)
    lbl_carreras_asoc = Label(f,text="Carreras Del Curso")
    c1 = Checkbutton(f, text="Ingenier??a En Computaci??n", variable=c_computacion, onvalue=1, offvalue=0)
    c2 = Checkbutton(f, text="Administraci??n De Empresas", variable=c_administracion, onvalue=1, offvalue=0)
    c3 = Checkbutton(f, text="Ingenier??a En Producci??n Industrial", variable=c_produccion, onvalue=1, offvalue=0)
    c4 = Checkbutton(f, text="Ingenier??a Electr??nica", variable=c_electronica, onvalue=1, offvalue=0)
    c5 = Checkbutton(f, text="Ingenier??a En Agronom??a", variable=c_agronomia, onvalue=1, offvalue=0)
    btn_agregar = Button(f,text="Agregar",command=lambda:agregar_nuevo_curso())

    # +++++++++++++ Posicion en grid +++++++++++++
    lbl_curso.grid(row=1,column=0,padx=20,pady=20)
    txt_curso.grid(row=1,column=1,padx=20,pady=20)
    lbl_num_creditos.grid(row=1,column=2,padx=20,pady=20)
    txt_num_creditos.grid(row=1,column=3,padx=20,pady=20)
    lbl_h_lectivas.grid(row=2,column=0,padx=20,pady=20)
    txt_h_lectivas.grid(row=2,column=1,padx=20,pady=20)
    lbl_f_inicio.grid(row=2,column=2,padx=20,pady=20)
    txt_f_inicio.grid(row=2,column=3,padx=20,pady=20)
    lbl_f_final.grid(row=3,column=0,padx=20,pady=20)
    txt_f_final.grid(row=3,column=1,padx=20,pady=20)
    lbl_carreras_asoc.grid(row=4,column=0,padx=20,pady=20)
    c1.grid(row=4,column=1,padx=20,pady=20)
    c2.grid(row=4,column=2,padx=20,pady=20)
    c3.grid(row=4,column=3,padx=20,pady=20)
    c4.grid(row=5,column=1,padx=20,pady=20)
    c5.grid(row=5,column=2,padx=20,pady=20)
    btn_agregar.grid(row=6,column=3,padx=20,pady=20)

    def borrar_texto():
        v_f_final.set('')
        v_f_inicio.set('')
        v_nuevo_curso.set('')
        v_h_lectivas.set('')
        v_num_creditos.set('')
        c_administracion.set(0)
        c_computacion.set(0)
        c_produccion.set(0)
        c_electronica.set(0)
        c_agronomia.set(0)

    f.grid_propagate(False)

def f_modificar_curso(v,fo):
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Modificar Curso")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

#Variables
    global lista_cursos
    v_nuevo_curso = StringVar()
    v_viejo_curso = StringVar()
    v_num_creditos = StringVar()
    v_h_lectivas = StringVar()
    v_f_inicio = StringVar()
    v_f_final = StringVar()
    c_administracion = IntVar()
    c_computacion = IntVar()
    c_agronomia = IntVar()
    c_electronica = IntVar()
    c_produccion = IntVar()
    cursos=lista_cursos.listar_nombre_cursos()
    
    
    
    # Funciones

    def encontrar_curso():
        datos = buscar_cursos(cmb_cursos.get())
        v_f_final.set(datos[4])
        v_f_inicio.set(datos[3])
        v_nuevo_curso.set(datos[0])
        v_h_lectivas.set(datos[2])
        v_num_creditos.set(datos[1])
        if "Administracion De Empresas" in datos[5]:
            c_administracion.set(1)
        else:
            c_administracion.set(0)
        if "Ingenieria En Computacion" in datos[5]:
            c_computacion.set(1)
        else:
            c_computacion.set(0)
        if "Ingenieria En Produccion Industrial" in datos[5]:
            c_produccion.set(1)
        else:
            c_produccion.set(0)
        if "Ingenieria Electronica" in datos[5]:
            c_electronica.set(1)
        else:
            c_electronica.set(0)
        if "Ingenieria En Agronomia" in datos[5]:
            c_agronomia.set(1)
        else:
            c_agronomia.set(0)

    def ver_carreras_elegidas(carreras_elegidas):
        if c_administracion.get() == 1:
            carreras_elegidas+='Administracion De Empresas, '
        if c_produccion.get() == 1:
            carreras_elegidas+='Ingenieria En Produccion Industrial, '
        if c_computacion.get() == 1:
            carreras_elegidas+='Ingenieria En Computacion, '
        if c_electronica.get() == 1:
            carreras_elegidas+='Ingenieria Electronica, '
        if c_agronomia.get() == 1:
            carreras_elegidas+='Ingenieria En Agronomia, '
        return carreras_elegidas[:-2]

    def modificar_curso():
        carreras_elegidas = ''
        carreras_elegidas = ver_carreras_elegidas(carreras_elegidas)
        lista_cursos.modificar_cursos(v_viejo_curso.get(),v_nuevo_curso.get(),v_num_creditos.get(),v_h_lectivas.get(),v_f_inicio.get(),v_f_final.get(),carreras_elegidas)
        borrar_texto()
        cursos_autoguardado_adm()
        
    def borrar_texto():
        v_f_final.set('')
        v_f_inicio.set('')
        v_nuevo_curso.set('')
        v_h_lectivas.set('')
        v_num_creditos.set('')
        c_administracion.set(0)
        c_computacion.set(0)
        c_produccion.set(0)
        c_electronica.set(0)
        c_agronomia.set(0)
        cmb_cursos.set('Elige una opci??n')

    # ++++++++++++++++ Widgets de este frame ++++++++++++++
    lbl_curso1 = Label(f,text="Curso A Modicar")
    cmb_cursos = Combobox(f,textvariable=v_viejo_curso,state="readonly", width=30)
    cmb_cursos["values"] = cursos
    cmb_cursos.set("Elige una opci??n")
    cmb_cursos.bind("<<ComboboxSelected>>",lambda _ : encontrar_curso())
    lbl_curso2 = Label(f,text="Nombre Curso")
    txt_curso2 = Entry(f, textvariable=v_nuevo_curso)
    lbl_num_creditos = Label(f,text="Numero de Cr??ditos")
    txt_num_creditos = Entry(f, textvariable=v_num_creditos)
    lbl_h_lectivas = Label(f,text="Horas Lectivas")
    txt_h_lectivas = Entry(f, textvariable=v_h_lectivas)
    lbl_f_inicio = Label(f,text="Fecha Inicio")
    txt_f_inicio = Entry(f, textvariable=v_f_inicio)
    lbl_f_final = Label(f,text="Fecha Final")
    txt_f_final = Entry(f, textvariable=v_f_final)
    lbl_carreras_asoc = Label(f,text="Carreras Del Curso")
    c1 = Checkbutton(f, text="Ingenieria En Computacion", variable=c_computacion, onvalue=1, offvalue=0)
    c2 = Checkbutton(f, text="Administracion De Empresas", variable=c_administracion, onvalue=1, offvalue=0)
    c3 = Checkbutton(f, text="Ingenieria En Produccion Industrial", variable=c_produccion, onvalue=1, offvalue=0)
    c4 = Checkbutton(f, text="Ingenieria Electronica", variable=c_electronica, onvalue=1, offvalue=0)
    c5 = Checkbutton(f, text="Ingenieria En Agronomia", variable=c_agronomia, onvalue=1, offvalue=0)
    btn_modificar = Button(f,text="Modificar",command=lambda:modificar_curso())

    # +++++++++++++ Posicion en grid +++++++++++++
    lbl_curso1.grid(row=1,column=0,padx=20,pady=20)
    cmb_cursos.grid(row=1,column=1,padx=20,pady=20)
    lbl_curso2.grid(row=1,column=2,padx=20,pady=20)
    txt_curso2.grid(row=1,column=3,padx=20,pady=20)
    lbl_num_creditos.grid(row=2,column=0,padx=20,pady=20)
    txt_num_creditos.grid(row=2,column=1,padx=20,pady=20)
    lbl_h_lectivas.grid(row=2,column=2,padx=20,pady=20)
    txt_h_lectivas.grid(row=2,column=3,padx=20,pady=20)
    lbl_f_inicio.grid(row=3,column=0,padx=20,pady=20)
    txt_f_inicio.grid(row=3,column=1,padx=20,pady=20)
    lbl_f_final.grid(row=3,column=2,padx=20,pady=20)
    txt_f_final.grid(row=3,column=3,padx=20,pady=20)
    lbl_carreras_asoc.grid(row=5,column=0,padx=20,pady=20)
    c1.grid(row=5,column=1,padx=20,pady=20)
    c2.grid(row=5,column=2,padx=20,pady=20)
    c3.grid(row=5,column=3,padx=20,pady=20)
    c4.grid(row=6,column=1,padx=20,pady=20)
    c5.grid(row=6,column=2,padx=20,pady=20)
    btn_modificar.grid(row=6,column=3,padx=20,pady=20)

    f.grid_propagate(False)

def f_modificar_carrera(v,fo):
    global lista_carreras
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Modificar Carrera")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")
    v_nueva_carrera = StringVar()

    # +++++++++++++++ Widgets de este frame ++++++++++++++++++
    carreras=lista_carreras.listar_carreras()
    lbl_carrera1 = Label(f,text="Carrera A Modificar")
    cmb_carrera1 = Combobox(f, state="readonly", width=30)
    cmb_carrera1["values"] = carreras
    cmb_carrera1.set("Elige una opci??n")
    lbl_carrera2 = Label(f,text="Nueva Carrera")
    txt_carrera2 = Entry(f, textvariable=v_nueva_carrera)
    btn_modificar = Button(f,text="Modificar",command=lambda: [lista_carreras.modificar_carrera(cmb_carrera1.get(),v_nueva_carrera.get()), borrar_texto()]) ####
    # ++++++++++++++++ Posicion en grid ++++++++++++++++++
    lbl_carrera1.grid(row=1,column=0,padx=20,pady=20,sticky="e")
    cmb_carrera1.grid(row=1,column=1,padx=20,pady=20)
    lbl_carrera2.grid(row=2,column=0,padx=20,pady=20,sticky="e")
    txt_carrera2.grid(row=2,column=1,padx=20,pady=20)
    btn_modificar.grid(row=3,column=1,padx=20,pady=20)



    def borrar_texto():
        v_nueva_carrera.set('')


    f.grid_propagate(False)

def f_agregar_carrera(v,fo):
    contenido_frame = frame(v,"Usuario Administrador","#ffffff","900","500")
    fo.destroy()
    f = contenido_frame.f
    menu_administrador(v,f)
    lbl_titulo = Label(f,text="Agregar Carrera")
    lbl_titulo.config(font=("Times New Roman",30),fg="#4ca2f8",bg="#ffffff")
    lbl_titulo.grid(row=0, column=0, columnspan=6, sticky="nwse")

    v_nueva_carrera = StringVar()
    

    # ++++++++++++++++ Widgets de este frame ++++++++++++++
    lbl_carrera = Label(f,text="Nombre Carrera")
    txt_carrera = Entry(f, textvariable=v_nueva_carrera)
    btn_agregar = Button(f,text="Agregar",command=lambda: [lista_carreras.insertar(c.Carrera(v_nueva_carrera.get())),borrar_texto(),carrera_autoguardado_adm()])

    # +++++++++++++ Posicion en grid +++++++++++++
    lbl_carrera.grid(row=1,column=0,padx=20,pady=20,sticky="e")
    txt_carrera.grid(row=1,column=1,padx=20,pady=20)
    btn_agregar.grid(row=2,column=1,padx=20,pady=20)
    f.grid_propagate(False)

    def borrar_texto():
        v_nueva_carrera.set('')

"""
def carrera_autoguardado_est():
    global autoguardado_est
    if autoguardado_est == 1:
        guardar_lista_carreras()
        
"""

def carrera_autoguardado_adm():
    global autoguardado_adm
    if autoguardado_adm.get() == 1:
        guardar_lista_carreras()

def carrera_autoguardado_est():
    global autoguardado_est
    if autoguardado_est.get() == 1:
        guardar_lista_carreras()

def cursos_autoguardado_adm():
    global autoguardado_adm
    if autoguardado_adm.get() == 1:
        guardar_lista_cursos()

def actividad_autoguardado_est():
    global autoguardado_est
    if autoguardado_est.get() == 1:
        guardar_lista_actividades()
        
def curso_est_autoguardado_est():
    global autoguardado_est
    if autoguardado_est.get()==1:
        guardar_cursos_estudiante
    

f_login(v,f)
v.mainloop()