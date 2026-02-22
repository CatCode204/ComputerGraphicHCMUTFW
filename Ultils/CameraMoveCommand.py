from typing import override

from Ultils.Camera import Camera
from Ultils.ICameraCommand import ICameraCommand
from Ultils.LinearAlg import Vector

from enum import Enum


class CameraMoveCommand(ICameraCommand):
    def __init__(self,velocity : Vector):
        self.__velocity = velocity

    @override
    def Execute(self,camera : Camera, deltaTime : float):
        camera.Position = camera.Position + camera.Right * self.__velocity.ValueAt(0) * deltaTime
        camera.Position = camera.Position + camera.WorldUpVector * self.__velocity.ValueAt(1) * deltaTime
        camera.Position = camera.Position + camera.Forward * self.__velocity.ValueAt(2) * deltaTime