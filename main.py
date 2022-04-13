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

carreras = {
    'Administración de Empresas':['Computación Para Administración','Contabilidad I',
    'Metodología De La Investigación','Derecho Comercial','Cálculo Para Administración'],

    'Gestión del Turismo Rural Sostenible':['Desarrollo De Emprendedores','Fundamentos De Ecología','Legislación Turística De Costa Rica','Servicios Turísticos Reales','Gestión Ambiental Y Turismo'],

    'Ingeniería En Computación':['Introducción A La Programación','Taller De Programación','Estructura De Datos','Programación Orientada A Objetos','Arquitectura De Computadores'],
    
    'Ingeniería Electrónica':['Elementos De Computación','Introducción A La Ingeniería','Dibujo Técnico','Seguridad Y Salud Ocupacional','Analisis Y Diseño De Algoritmos'],
    
    'Ingeniería En Agronomía':['Introducción A La Agronomía','Agromática I','Botánica General','Introducción A Plagas Agropecuarias','Fisiología Vegetal']
} #Faltaría agregar más si el profe pide más

# PRUEBAS DE LAS FUNCIONES

#Agregar curso
carrera = input("Ingrese la carrera a agregar nuevos cursos: ")
nuevo_curso = input("Ingrese el nuevo curso: ")
print(func.agregar_curso(carrera,carreras,nuevo_curso))


#Modificar Curso
carrera = input("Ingrese la carrera a agregar nuevos cursos: ")
curso_a_modificar = input("Ingrese el curso a modificar: ")
nuevo_curso = input("Ingrese el nuevo curso: ")
print(func.modificar_curso(carrera,carreras,curso_a_modificar,nuevo_curso))

#Agregar Carrera
print(func.agregar_carrera("Biología En Fauna",carreras))

#Modificar Carrera
print(func.modificar_carrera("Ingeniería En Computación","Desarrollo De Software",carreras)) 
