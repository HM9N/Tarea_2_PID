#--------------------------------------------------------------------------
#------- PLANTILLA DE CÓDIGO ----------------------------------------------
#------- Juego PDI-------------------------------------------
#------- Por: Jhon Vásquez  y Alejandro -----------------------------------
#------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
#------- Marzo de 2022--------------------------------------------------
#--------------------------------------------------------------------------

import faceDetectionManager # Se importa la clase FaceDetectionManager
import videoManager # Se importa la clase VideoManager

# Se instancia la clase VideoManager
videoManager = videoManager.VideoManager()
# Se instancia la clase FaceDetectionManager
faceDetectionManager = faceDetectionManager.FaceDetectionManager(videoManager)
# Se ejecuta el método encargado de hacer la detección de rostros
faceDetectionManager.detectFace()
