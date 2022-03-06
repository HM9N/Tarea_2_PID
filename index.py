import faceDetectionManager
import videoManager

videoManager = videoManager.VideoManager()
faceDetectionManager = faceDetectionManager.FaceDetectionManager(videoManager)
faceDetectionManager.detectFace()
