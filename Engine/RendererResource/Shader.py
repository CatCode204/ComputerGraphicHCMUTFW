from abc import ABC, abstractmethod

from Engine.Renderer.RendererAPI import ERendererSpec
from Engine.RendererResource.EShaderTypes import EShaderTypes
from Engine.RendererResource import ResourceManager

class Shader(ABC):
    def __init__(self, vertexSource : str, fragmentSource : str):
        self._vertexSrc = vertexSource
        self._fragmentSrc = fragmentSource
        self._id = 0

    def __del__(self):
        self.Delete()

    @staticmethod
    def Create(vertexSource : str, fragmentSource : str) -> "Shader":
        return ResourceManager.ResourceManager.CreateShader(vertexSource,fragmentSource)

    @staticmethod
    def OnInit(rendererSpec : ERendererSpec):
        pass

    @abstractmethod
    def _CompileShader(self, shaderType : EShaderTypes):
        pass

    def GetID(self):
        return self._id

    @abstractmethod
    def Bind(self):
        pass

    @abstractmethod
    def Unbind(self):
        pass

    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def SetBool(self,name : str, value : bool):
        pass

    @abstractmethod
    def SetInt(self,name : str, value : int):
        pass

    @abstractmethod
    def SetFloat(self,name : str, value : float):
        pass

    @abstractmethod
    def SetVector2(self,name : str, x : float, y : float):
        pass

    @abstractmethod
    def SetVector3(self,name : str, x : float, y : float, z : float):
        pass

    @abstractmethod
    def SetMatrix2(self,name : str, pValue):
        pass

    @abstractmethod
    def SetMatrix3(self,name : str, pValue):
        pass

    @abstractmethod
    def SetMatrix4(self,name : str, pValue):
        pass