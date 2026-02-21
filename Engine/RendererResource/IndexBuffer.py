from abc import ABC, abstractmethod

from Engine.RendererResource.ERenderMode import ERenderMode
from Engine.RendererResource.ResourceManager import ResourceManager


class IndexBuffer(ABC):
    def __init__(self):
        self._id = 0
        self._size = 0

    def __del__(self):
        self.Delete()

    @staticmethod
    def Create() -> "IndexBuffer":
        return ResourceManager.CreateIndexBuffer()

    @abstractmethod
    def Bind(self):
        pass

    @abstractmethod
    def UnBind(self):
        pass

    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def SetData(self, data,size,renderMode : ERenderMode = ERenderMode.Static):
        pass

    def GetID(self):
        return self._id

    def GetSize(self):
        return self._size