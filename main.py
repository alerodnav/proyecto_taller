import funciones.funciones as func

#Lista de los estudiantes registrados
estudiantes = [
    {
    'nombre_completo':'Jose Alejandro Rodriguez Navarro',
    'carreras': [],
    'cursos':[],
    'usuario': 'arodri',
    'contrasena': func.cifrar_contrasena('ar123')
    },
    {
    'nombre_completo':'Deivid Matute Guerrero',
    'carreras': [],
    'cursos':[],
    'usuario': 'dmatute',
    'contrasena': func.cifrar_contrasena('dmcr7')
    },
    {
    'nombre_completo':'Andres Dinarte Castro',
    'carreras': [],
    'cursos':[],
    'usuario': 'dini',
    'contrasena': func.cifrar_contrasena('adin69')
    },
    {
    'nombre_completo':'Leonardo Alpizar',
    'carreras': [],
    'cursos':[],
    'usuario': 'leoalp',
    'contrasena': func.cifrar_contrasena('lp7178')
    }

]

administradores = [
    {
    'nombre_completo':'Gabriel Alfonso Blanco Ruiz',
    'telefono': '87657890',
    'usuario': 'gblanco',
    'contrasena': func.cifrar_contrasena('192Gabriel_168')
    },
    {
    'nombre_completo':'Jorge José Hernandez Pérez',
    'telefono': '87604152',
    'usuario': 'jquiros',
    'contrasena': func.cifrar_contrasena('jorginho0777')
    },
    {
    'nombre_completo':'Daniel Josué Quirós Ampieé',
    'telefono': '88024367',
    'usuario': 'dquiros',
    'contrasena': func.cifrar_contrasena('daniTurtle00')
    },
    {
    'nombre_completo':'Sofía Jimena Alfaro Jiménez',
    'telefono': '89076444',
    'usuario': 'salfaro',
    'contrasena': func.cifrar_contrasena('minny02x02')
    }
]

actividades = ['Estudiar','Repasar','Hacer ejercicio','Practicar deporte','Leer un libro','Actividad física','Reunión con amigos','Salir al aire libre']

# actividades = [
#     {
#         'descripcion': EL USUARIO LA ELIGE,
#         'curso_asociado': '',
#         'fecha_inicio': '',
#         'fecha_conclusión': ''
#     }
# ] #Después...

cursos = [
    {
        'nombre': 'Comunicación Escrita',
        'creditos': 2,
        'horas lectivas': 3,
        'fecha_inicio': '07-02-2022',
        'fecha_final': '03-06-2022',
        'horario_clases': ['L: 5:05pm - 7:45pm'],
        'carreras':['Administración de Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Matemática General',
        'creditos': 2,
        'horas lectivas': 5,
        'fecha_inicio': '07-02-2022',
        'fecha_final': '03-06-2022',
        'horario_clases': ['K: 12:30pm - 2:15pm','M: 12:30pm - 3:15pm'],
        'carreras':['Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería En Agronomía''Ingeniería Electrónica']
    },
    {
        'nombre': 'Actividad Cultural I',
        'creditos': 0,
        'horas lectivas': 2,
        'fecha_inicio': '07-02-2022',
        'fecha_final': '03-06-2022',
        'horario_clases': 'J: 07:00am - 9:00am',
        'carreras':['Administración de Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Química Básica I',
        'creditos': 3,
        'horas lectivas': 4,
        'fecha_inicio': '07-02-2022',
        'fecha_final': '10-06-2022',
        'horario_clases': 'L: 12:30 - 4:30',
        'carreras':['Administración de Empresas','Ingeniería En Producción Industrial','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Cálculo Diferencial E Integral',
        'creditos': 4,
        'horas lectivas': 5,
        'fecha_inicio': '25-07-2022',
        'fecha_final': '11-11-2022',
        'horario_clases': ['J: 12:30pm - 2:15pm','V: 7:55am - 9:40am'],
        'carreras':['Gestión del Turismo Rural Sostenible','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Inglés I',
        'creditos': 2,
        'horas lectivas': 3,
        'fecha_inicio': '25-07-2022',
        'fecha_final': '11-11-2022',
        'horario_clases': 'K 1:20 - 4:30',
        'carreras':['Administración de Empresas','Gestión del Turismo Rural Sostenible','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    }
]

carreras = ['Administración de Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']

# PRUEBAS DE LAS FUNCIONES

#Agregar curso
# print(func.agregar_curso(cursos,"Deivid Curso",3,4,'02,03,2022','03,09,2022',['M: 7:55pm - 9:40pm'],["Administración De Empresas",'Ingeniería En Computación']))


#Modificar Curso
# print(func.modificar_curso(cursos,"Matemática General","Deivid Curso",3,4,'02,03,2022','03,09,2022',['M: 7:55pm - 9:40pm'],["Administración De Empresas",'Ingeniería En Computación']))

#Agregar Carrera
# print(func.agregar_carrera(carreras,"Diseño Industrial"))

#Modificar Carrera
# print(func.modificar_carrera(carreras,"Ingeniería En Computación","Desarrollo De Software")) 

#Agregar actividad
# print(func.agregar_actividad(actividades,"Ver Documental"))

#Modificar Actividad
# print(func.modificar_actividad(actividades,"Practicar deporte","Practicar Matemáticas"))