"""
pip3 install opencv-python
pip3 install google-api-python-client
pip3 install google-cloud
pip3 install google-cloud-vision

"""
import os, io
from pprint import pprint
from time import sleep
from tkinter.messagebox import showerror
from urllib.response import addinfo
import cv2 as cv
import threading
from google.cloud import vision
from playsound import playsound

#Variables

emocion_dominante = {
    'Alegre': 0 ,
    'Triste': 0 ,
    'Enfadado': 0 ,
    'Sorprendido': 0 ,
    'Bajo Expuesto': 0 ,
    'Borroso': 0 ,
    'Sombrero': 0 ,
}

class rostro ():
    
    def __init__(self) -> None:
        pass

    def capturar_imagen(self,vista,cuenta_regresiva):

        if cuenta_regresiva:
            cont=5
            while cont>0:
                print (f'Captura en {cont} segundos...')
                sleep(1)
                cont-=1

        camara = cv.VideoCapture(0)
        leido, imagen = camara.read()
        camara.release()

        if leido == True:
            cv.imwrite("foto.png", imagen)
            if vista:
                cv.imshow('Toma de fotografia',imagen)
                cv.waitKey(0)
        else:
            showerror(
                title='Error en la toma de imagen', 
                message='No fue posible capturar la imagen con esta dispositivo!')
        return imagen


def tarea_paralela(estado):
    mi_rostro=rostro()
    while estado[0]:
        print("Toma de imagen: ",mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False))
        sleep(5)

"""
def menu():
    estado=[True]
    parametros=[estado]
    proceso=threading.Thread(target=tarea_paralela,args=parametros)
    proceso.start()

    while True:
        print ("1) Saludar\n2) Salir")
        if (input ('Selección: ')=='1'):
            lectura=input("Tu nombre: ")
            print (f"Hola como estas, {lectura}")
        else:
            estado[0]=False
            exit()
            #break
"""

#menu()

#mi_rostro=rostro()
#imagen=mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=True)


def detectar_emociones(imagen):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'./Proyecto_Fase_3/GUI/key.json'
    client=vision.ImageAnnotatorClient()

    with io.open('foto.png','rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)

    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')

    faces_list=[]


    angulos_rostro = None
    for face in faces:
        #dicccionario con los angulos asociados a la detección de la cara
        face_angles=dict(roll_angle=face.roll_angle,pan_angle=face.pan_angle,tilt_angle=face.tilt_angle)
        angulos_rostro = face_angles

        #confianza de detección (tipo float)
        detection_confidence=face.detection_confidence

        #Probabilidad de Expresiones
        #Emociones: Alegría, pena, ira, sorpresa
        face_expressions=dict(  joy_likelihood=likelihood_name[face.joy_likelihood],
                                sorrow_likelihood=likelihood_name[face.sorrow_likelihood],
                                anger_likelihood=likelihood_name[face.anger_likelihood],
                                surprise_likelihood=likelihood_name[face.surprise_likelihood],
                                under_exposed_likelihood=likelihood_name[face.under_exposed_likelihood],
                                blurred_likelihood=likelihood_name[face.blurred_likelihood],
                                headwear_likelihood=likelihood_name[face.headwear_likelihood])

        #polígono de marco de cara
        vertices=[]
        for vertex in face.bounding_poly.vertices:
            vertices.append (dict (x=vertex.x, y=vertex.y))

        face_dict=dict( face_angles=face_angles,
                        detection_confidence=detection_confidence,
                        face_expressions=face_expressions,
                        vertices=vertices
                        )
        faces_list.append(face_dict)

    try:
        parametros = [angulos_rostro]
        proceso=threading.Thread(target=detectar_concentracion,args=parametros)
        proceso.start()
    except playsound.PlaysoundException: #No sirve esta vara, necesito que ignore el primer intento aunque sea
        print("No se completaron correctamente los analisis de la foto")
        
        
    if (len(faces_list) == 0) or (len(faces_list) > 1) :
        showerror(message='No se detectó ningún rostro o se detectó más de un rostro en la imagen')

    else:
        for k,v in face_expressions.items():

        #======================== No es posible reconocer
            if v == "UNKNOWN":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 0
                    print("No es posible reconocer si está alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 0
                    print("No es posible reconocer si está triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 0
                    print("No es posible reconocer si está enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 0
                    print("No es posible reconocer si está sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 0
                    print("No es posible reconocer si está bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 0
                    print("No es posible reconocer si está borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 0
                    print("No es posible reconocer si tiene un sombrero")

           #======================= Muy poco probable         
            if v == "VERY_UNLIKELY":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 0
                    print("Es muy poco probable que estés alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 0
                    print("Es muy poco probable que estés triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 0
                    print("Es muy poco probable que estés enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 0
                    print("Es muy poco probable que estés sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 0
                    print("Es muy poco probable que estés bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 0
                    print("Es muy poco probable que esté borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 0
                    print("Es muy poco probable que lleve sombrero")

            #=====================Es poco probable 

            if v == "UNLIKELY":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 0
                    print("Es poco probable que estés alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 0
                    print("Es poco probable que estés triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 0
                    print("Es poco probable que estés enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 0
                    print("Es poco probable que estés sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 0
                    print("Es poco probable que estés bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 0
                    print("Es poco probable que esté borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 0
                    print("Es poco probable que lleve sombrero")

            #=====================Es posible 

            if v == "POSIBLE":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 1
                    print("Es posible que estés alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 1
                    print("Es posible que estés triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 1
                    print("Es posible que estés enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 1
                    print("Es posible que estés sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 1
                    print("Es posible que estés bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 1
                    print("Es posible que esté borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 1
                    print("Es posible que lleve sombrero")

            #==================Es probable

            if v == "LIKELY":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 2
                    print("Es probable que estés alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 2
                    print("Es probable que estés triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 2
                    print("Es probable que estés enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 2
                    print("Es probable que estés sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 2
                    print("Es probable que estés bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 2
                    print("Es probable que esté borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 2
                    print("Es probable que lleve sombrero")

          #===================Muy probable
                  
            if v == "VERY_LIKELY":
                if k == "joy_likelihood":
                    emocion_dominante['Alegre'] += 3
                    print("Es muy probable que estés alegre")
                elif k == "sorrow_likelihood":
                    emocion_dominante['Triste'] += 3
                    print("Es muy probable que estés triste")
                elif k == "anger_likelihood":
                    emocion_dominante['Enfadado'] += 3
                    print("Es muy probable que estés enfadado")
                elif k == "surprise_likelihood":
                    emocion_dominante['Sorprendido'] += 3
                    print("Es muy probable que estés sorprendido")
                elif k == "under_exposed_likelihood":
                    emocion_dominante['Bajo Expuesto'] += 3
                    print("Es muy probable que estés bajo expuesto")
                elif k == "blurred_likelihood":
                    emocion_dominante['Borroso'] += 3
                    print("Es muy probable que esté borroso")
                elif k == "headwear_likelihood":
                    emocion_dominante['Sombrero'] += 3
                    print("Es muy probable que lleve sombrero")



def detectar_concentracion(dict):
    """funcion que detecta cambios en la inclinacion o giro de la cabeza
    args
    dict (diccionario) Recibe el diccionario con los angulos del rostro
    """
    if not(-20<dict['pan_angle']<20):
        playsound("sonido.mp3")
        print("Hombre te me estas desconcetrando, deja de GIRAR LA CABEZA!")
    elif not(-20<dict['tilt_angle']<20):
        playsound("sonido.mp3")
        print("Hombre te me estas desconcetrando, deja de SUBIR Y BAJAR LA CABEZA!")


    
    
"""
    else:
        x1=faces_list[0]['vertices'][0]['x']
        y1=faces_list[0]['vertices'][0]['y']
        x2=faces_list[0]['vertices'][2]['x']
        y2=faces_list[0]['vertices'][2]['y']

        cv.rectangle(imagen,(x1,y1),(x2,y2),(0,255,0),3)
        
        cv.imshow('Toma de fotografia',imagen)

        cv.waitKey(0)

"""