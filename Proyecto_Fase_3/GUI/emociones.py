"""
pip3 install opencv-python
pip3 install google-api-python-client
pip3 install google-cloud
pip3 install google-cloud-vision

"""
import os, io
from pprint import pprint
from time import sleep, time
from tkinter.messagebox import showerror,showwarning
from urllib.response import addinfo
import cv2 as cv
import threading
from google.cloud import vision
from playsound import playsound
from time import sleep

estar_concentrado = True
respuesta_sonido = ""
cont = 0

#Diccionario de emociones predominantes
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
    """ Clase Rostro
    """
    
    def __init__(self) -> None:
        pass

    def capturar_imagen(self,vista,cuenta_regresiva):
        """"Esta se encarga de capturar una imagen
        args:
        vista(bool): Mostrar foto 
        cuenta_regresica(bool): Activar contador    
  
        """

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
    """Esta funcion determina si la tarea paralela debe de seguir ejecutandose
    args:
        estado (bool): Estado de la tarea 
    """
    mi_rostro=rostro()
    while estado[0]:
        print("Toma de imagen: ",mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False))
        sleep(5)


def usuario_concentrado():
    """Devuelve el valor de la variable global estar_concentrado
    """
    global estar_concentrado
    return estar_concentrado

def detectar_emociones(imagen,concentracion,emocion):
    """Esta funcion detecta las emociones de la caputra
    args:
        imagen (instancia): Captura
        concentracion(bool): Detectar concentracion
        emocion(bool): Detectar emociones    
    """

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
        global cont
        #dicccionario con los angulos asociados a la detecci??n de la cara
        face_angles=dict(roll_angle=face.roll_angle,pan_angle=face.pan_angle,tilt_angle=face.tilt_angle)
        angulos_rostro = face_angles

        #confianza de detecci??n (tipo float)
        detection_confidence=face.detection_confidence

        #Probabilidad de Expresiones
        #Emociones: Alegr??a, pena, ira, sorpresa
        face_expressions=dict(  joy_likelihood=likelihood_name[face.joy_likelihood],
                                sorrow_likelihood=likelihood_name[face.sorrow_likelihood],
                                anger_likelihood=likelihood_name[face.anger_likelihood],
                                surprise_likelihood=likelihood_name[face.surprise_likelihood],
                                under_exposed_likelihood=likelihood_name[face.under_exposed_likelihood],
                                blurred_likelihood=likelihood_name[face.blurred_likelihood],
                                headwear_likelihood=likelihood_name[face.headwear_likelihood])

        #pol??gono de marco de cara
        vertices=[]
        for vertex in face.bounding_poly.vertices:
            vertices.append (dict (x=vertex.x, y=vertex.y))

        face_dict=dict( face_angles=face_angles,
                        detection_confidence=detection_confidence,
                        face_expressions=face_expressions,
                        vertices=vertices
                        )
        faces_list.append(face_dict)

    if concentracion:
        try:
            if angulos_rostro!=None:
                parametros = [angulos_rostro]
                proceso2=threading.Thread(target=detectar_concentracion,args=parametros)
                proceso2.start()
        except:
            print("No se completaron correctamente los analisis de la foto")
        
        
    if (len(faces_list) == 0) or (len(faces_list) > 1) :
        showerror(message='No se detect?? ning??n rostro o se detect?? m??s de un rostro en la imagen')

    else:
        if emocion:
            for k,v in face_expressions.items():
            #======================== No es posible reconocer
                if v == "UNKNOWN":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 0
                        print("No es posible reconocer si est?? alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 0
                        print("No es posible reconocer si est?? triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 0
                        print("No es posible reconocer si est?? enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 0
                        print("No es posible reconocer si est?? sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 0
                        print("No es posible reconocer si est?? bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 0
                        print("No es posible reconocer si est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 0
                        print("No es posible reconocer si tiene un sombrero")

            #======================= Muy poco probable         
                if v == "VERY_UNLIKELY":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 0
                        print("Es muy poco probable que est??s alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 0
                        print("Es muy poco probable que est??s triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 0
                        print("Es muy poco probable que est??s enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 0
                        print("Es muy poco probable que est??s sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 0
                        print("Es muy poco probable que est??s bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 0
                        print("Es muy poco probable que est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 0
                        print("Es muy poco probable que lleve sombrero")

                #=====================Es poco probable 

                if v == "UNLIKELY":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 0
                        print("Es poco probable que est??s alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 0
                        print("Es poco probable que est??s triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 0
                        print("Es poco probable que est??s enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 0
                        print("Es poco probable que est??s sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 0
                        print("Es poco probable que est??s bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 0
                        print("Es poco probable que est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 0
                        print("Es poco probable que lleve sombrero")

                #=====================Es posible 

                if v == "POSIBLE":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 1
                        print("Es posible que est??s alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 1
                        print("Es posible que est??s triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 1
                        print("Es posible que est??s enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 1
                        print("Es posible que est??s sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 1
                        print("Es posible que est??s bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 1
                        print("Es posible que est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 1
                        print("Es posible que lleve sombrero")

                #==================Es probable

                if v == "LIKELY":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 2
                        print("Es probable que est??s alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 2
                        print("Es probable que est??s triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 2
                        print("Es probable que est??s enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 2
                        print("Es probable que est??s sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 2
                        print("Es probable que est??s bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 2
                        print("Es probable que est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 2
                        print("Es probable que lleve sombrero")

            #===================Muy probable
                    
                if v == "VERY_LIKELY":
                    if k == "joy_likelihood":
                        emocion_dominante['Alegre'] += 3
                        print("Es muy probable que est??s alegre")
                    elif k == "sorrow_likelihood":
                        emocion_dominante['Triste'] += 3
                        print("Es muy probable que est??s triste")
                    elif k == "anger_likelihood":
                        emocion_dominante['Enfadado'] += 3
                        print("Es muy probable que est??s enfadado")
                    elif k == "surprise_likelihood":
                        emocion_dominante['Sorprendido'] += 3
                        print("Es muy probable que est??s sorprendido")
                    elif k == "under_exposed_likelihood":
                        emocion_dominante['Bajo Expuesto'] += 3
                        print("Es muy probable que est??s bajo expuesto")
                    elif k == "blurred_likelihood":
                        emocion_dominante['Borroso'] += 3
                        print("Es muy probable que est?? borroso")
                    elif k == "headwear_likelihood":
                        emocion_dominante['Sombrero'] += 3
                        print("Es muy probable que lleve sombrero")


def enciclar_sonido():
    """Esta funcion reproduce un sonido hasta que el usuario presione el boton de detener
    """
    global respuesta_sonido
    while respuesta_sonido!="ok":
        playsound('./Proyecto_Fase_3/GUI/sonido.mp3')
    
def fotos_frecuentes():
    """Esta funcion permita tomar capturas con mayor frecuencia     
    """
    global estar_concentrado
    mi_rostro= rostro()
    estar_concentrado = False
    sleep(5)
    print('Tomando foto mas frecuente:')
    imagen = mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False)
    detectar_emociones(imagen,True,False)

def detectar_concentracion(dict):
    """funcion que detecta cambios en la inclinacion o giro de la cabeza
    args
    dict (diccionario) Recibe el diccionario con los angulos del rostro
    """
    global respuesta_sonido,cont,estar_concentrado
    if (not(-20<dict['pan_angle']<20)) | (not(-20<dict['tilt_angle']<20)):
        cont += 1
    else:
        cont = 0
        estar_concentrado = True
       
    if (cont >0 ) & (cont < 7):
        fotos_frecuentes()    
        
    if cont == 7:
        proceso3=threading.Thread(target=enciclar_sonido)
        proceso3.start()
        if cont == 7:
            #cont+=1
            cont = 0
            estar_concentrado = True
            respuesta_sonido = showwarning(message='Mant??n tu cabeza frente al monitor, no te distraigas!')
# Retorna True, False o None.
