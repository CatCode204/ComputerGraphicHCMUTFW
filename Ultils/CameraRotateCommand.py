from Ultils.LinearAlg import Vector
from Ultils.Camera import Camera
from Ultils.ICameraCommand import ICameraCommand


class CameraRotateCommand(ICameraCommand):
    def __init__(self, rotate : Vector): # vector of (pitch,yaw,roll)
        self.__rotate = rotate

    def Execute(self,camera : Camera, deltaTime : float):
        newRotation = camera.Rotation + self.__rotate * deltaTime
        if newRotation.y < -89: newRotation = Vector(newRotation.x,-89,newRotation.z)
        if newRotation.y > 89: newRotation = Vector(newRotation.x, 89, newRotation.z)
        camera.Rotation = newRotation