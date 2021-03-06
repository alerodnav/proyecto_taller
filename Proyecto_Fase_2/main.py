import funciones.funciones as func
#Lista de los estudiantes registrados
estudiantes = [
    {
    'nombre_completo':'Jose Alejandro Rodriguez Navarro',
    'carreras': ['Ingeniería En Computación','Administración De Empresas'],
    'cursos':[],
    'usuario': 'arodri',
    'contrasena': func.cifrar_contrasena('ar123'),
    'actividades':
        [
            {
            'nombre':'Realizar tarea ingles',
            'curso_asociado':'Inglés I',
            'horario': ['Lunes','8:00','10:00'],
            'semana': 11,
            'hora_inicio':'9:00',
            'hora_final': '11:00',
            'estado':False  # False = No realizada,  True = Realizada
            }
        ]
    },

    {
    'nombre_completo':'Deivid Matute Guerrero',
    'carreras': [],
    'cursos':[],
    'usuario': 'dmatute',
    'contrasena': func.cifrar_contrasena('dmcr7'),
    'actividades':
        [
        {
            'nombre':'Estudiar materia vista en Matematica General',
            'curso_asociado':'Cálculo Diferencial E Integral',
            'horario': ['Lunes','8:00','10:00'],
            'semana': '11',
            'hora_inicio':'6:00',
            'hora_final': '8:00',
            'estado':False  # False = No realizada,  True = Realizada
        }
        ]
    },

    {
    'nombre_completo':'Andres Dinarte Castro',
    'carreras': [],
    'cursos':[],
    'usuario': 'dini',
    'contrasena': func.cifrar_contrasena('adin69'),
    'actividades':
        [
            {
            'nombre':'Estudiar materia vista en Quimica Basica',
            'curso_asociado':'Química Básica I',
            'horario': ['Lunes','8:00','10:00'],
            'semana': '11',
            'hora_inicio':'13:00',
            'hora_final': '15:00',
            'estado':False  # False = No realizada,  True = Realizada
            }
        ]
    },
    
    {
    'nombre_completo':'Leonardo Alpizar',
    'carreras': [],
    'cursos':[],
    'usuario': 'leoalp',
    'contrasena': func.cifrar_contrasena('lp7178'),
    'actividades':
        [
            {
            'nombre':'Estudiar materia vista en comunicacion escrita',
            'curso_asociado':'Comunicación Escrita',
            'horario': ['Lunes','8:00','10:00'],
            'semana': '11',
            'hora_inicio':'17:05',
            'hora_final': '19:45',
            'estado':False  # False = No realizada,  True = Realizada
            }
        ]
    }

]


administradores = [
    {
    'nombre_completo':'Gabriel Alfonso Blanco Ruiz',
    'telefono': '87657890',
    'usuario': 'gblanco',
    'contrasena': func.cifrar_contrasena('g123')
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

#actividades = ['Estudiar','Repasar','Hacer ejercicio','Practicar deporte','Leer un libro','Actividad física','Reunión con amigos','Salir al aire libre']

# actividades = [
#     {
#         'nombre': EL USUARIO LA ELIGE,
#         'curso_asociado': '',
#         'fecha_inicio': '',
#         'fecha_conclusión': ''
#     }
# ] #Después...

cursos = (
    {
        'nombre': 'Comunicación Escrita',
        'creditos': 2,
        'horas lectivas': 3,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Lunes','17:05','19:45']],
        'carreras':['Administración De Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Matemática General',
        'creditos': 2,
        'horas lectivas': 5,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Martes','12:30','14:15'],['Jueves','12:30','15:15']],
        'carreras':['Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería En Agronomía''Ingeniería Electrónica']
    },
    {
        'nombre': 'Actividad Cultural I',
        'creditos': 0,
        'horas lectivas': 2,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Jueves','7:00','9:00']],
        'carreras':['Administración De Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Química Básica I',
        'creditos': 3,
        'horas lectivas': 4,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Lunes','12:30','16:30']],
        'carreras':['Administración De Empresas','Ingeniería En Producción Industrial','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Cálculo Diferencial E Integral',
        'creditos': 4,
        'horas lectivas': 5,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Jueves','12:30','14:15'],['Viernes','7:55','9:40']],
        'carreras':['Gestión del Turismo Rural Sostenible','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    },
    {
        'nombre': 'Inglés I',
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': '07-02',
        'fecha_final': '03-06',
        'semana': '*',
        'horario': [['Martes','13:20','16:30']],
        'carreras':['Administración De Empresas','Gestión del Turismo Rural Sostenible','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía']
    }
)

carreras = ('Administración De Empresas','Ingeniería En Producción Industrial','Ingeniería En Computación','Ingeniería Electrónica','Ingeniería En Agronomía')

semanas = [
    {
        'numero': 1,
        'inicio': '07-02',
        'fin': '13-02'
    },
    {
        'numero': 2,
        'inicio': '14-02',
        'fin': '20-02'
    },
    {
        'numero': 3,
        'inicio': '21-02',
        'fin': '27-02'
    },
    {
        'numero': 4,
        'inicio': '28-02',
        'fin': '06-03'
    },
    {
        'numero': 5,
        'inicio': '07-03',
        'fin': '13-03'
    },
    {
        'numero': 6,
        'inicio': '14-03',
        'fin': '20-03'
    },
    {
        'numero': 7,
        'inicio': '21-03',
        'fin': '27-03'
    },
    {
        'numero': 8,
        'inicio': '28-03',
        'fin': '03-04'
    },
    {
        'numero': 9,
        'inicio': '04-04',
        'fin': '10-04'
    },
    {
        'numero': 10,
        'inicio': '18-04',
        'fin': '24-04'
    },
    {
        'numero': 11,
        'inicio': '25-04',
        'fin': '01-05'
    },
    {
        'numero': 12,
        'inicio': '02-05',
        'fin': '08-05'
    },
    {
        'numero': 13,
        'inicio': '09-05',
        'fin': '15-05'
    },
    {
        'numero': 14,
        'inicio': '16-05',
        'fin': '22-05'
    },
    {
        'numero': 15,
        'inicio': '23-05',
        'fin': '29-05'
    },
    {
        'numero': 16,
        'inicio': '30-05',
        'fin': '05-06'
    },
    {
        'numero': 17,
        'inicio': '06-06',
        'fin': '12-06'
    }
]

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