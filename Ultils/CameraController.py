from Ultils.Camera import Camera
from Ultils.CameraMoveCommand import CameraMoveCommand
from Ultils.ICameraCommand import ICameraCommand


class CameraController:
    def __init__(self, camera : Camera):
        self.__camera = camera
        self.__commands : list[ICameraCommand] = []

    def EnqueueCommand(self, command : ICameraCommand):
        self.__commands.append(command)

    def Execute(self, deltaTime : float):
        for command in self.__commands:
            command.Execute(self.__camera,deltaTime)

        self.__commands.clear()