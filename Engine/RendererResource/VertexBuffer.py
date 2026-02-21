from abc import ABC, abstractmethod

import numpy as np

from .ERenderMode import ERenderMode
from .ResourceManager import ResourceManager

from dataclasses import dataclass

@dataclass
class VertexData:
    Position : tuple[float,float,float] = (0,0,0)
    Color : tuple[float,float,float] = (1,1,1)
    TextureCoordinate : tuple[float,float] = (0,0)
    Normal : tuple[float,float,float] = (0,1,0)

class VertexBuffer(ABC):
    def __init__(self):
        self._id = 0
        self._size = 0

    @staticmethod
    def Create() -> "VertexBuffer":
        return ResourceManager.CreateVertexBuffer()

    def __del__(self):
        self.Delete()

    def GetID(self):
        return self._id

    def GetSize(self):
        return self._size

    @abstractmethod
    def Bind(self):
        pass

    @abstractmethod
    def Unbind(self):
        pass

    @abstractmethod
    def SetData(self, data, size : int, renderMode : ERenderMode = ERenderMode.Static):
        pass

    @abstractmethod
    def Delete(self):
        pass