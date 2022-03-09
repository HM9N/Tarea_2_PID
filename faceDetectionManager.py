import cv2
import mediapipe as mp
import imutils


class FaceDetectionManager:

    def __init__(self, videoManager):
        self.mp_face_detection = mp.solutions.face_detection # Solución de MediaPipe para detección de rostros
        self.mp_drawing = mp.solutions.drawing_utils # Para poder visualizar rectangulo que rodea el rostro y los 6 puntos claves
        self.videoManager = videoManager # Se usa la clase VideoManager

    # El método tiene toda la lógica para hacer la detección de rostros
    def detectFace(self):

        # Se inicia la captura por medio de la camara
        cap = self.videoManager.beginVideoCapture()

        # Se empieza a hacer la detección
        with self.mp_face_detection.FaceDetection(
                min_detection_confidence=0.5) as face_detection: # Min_detection_confidence: el valor minimo de confianza para que una detección sea considerada exitosa

            while True:
                ret, frame = cap.read() # Se lee el vídeo streaming
                if ret == False: 
                    break
                frame = imutils.resize(frame, width=720) # Función que nos ayuda a darle el tamaño que queremos a la imagen manteniendo su relación de aspecto
                frame = cv2.flip(frame, 1) # Se voltea la imagen
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Como openCV por defecto lee las imagenes en BGR, se transforman a RGB

                results = face_detection.process(frame_rgb) #El resultado de la detección 

                if results.detections is not None: # Se verifica que si se haya detectado un rostro
                    for detection in results.detections:
                        #Se dibuja el recuadro y los puntos de referencia
                        self.mp_drawing.draw_detection(frame, detection,
                                                       self.mp_drawing.DrawingSpec(
                                                           color=(0, 255, 255), circle_radius=2),
                                                       self.mp_drawing.DrawingSpec(color=(255, 0, 255)))
                
                #Se muestra el vídeo
                cv2.imshow("Deteccion de Rostros", frame)
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()
