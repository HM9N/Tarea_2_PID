import cv2

class VideoManager:

    def __init__(self):
        pass

    def beginVideoCapture(self):
        print("Voy a ejecutar")
        return cv2.VideoCapture(0, cv2.CAP_DSHOW)