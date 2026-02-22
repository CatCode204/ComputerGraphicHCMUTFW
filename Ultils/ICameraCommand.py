from abc import ABC, abstractmethod
from Ultils.Camera import Camera

class ICameraCommand(ABC):
    @abstractmethod
    def Execute(self,camera : Camera, deltaTime : float):
        pass