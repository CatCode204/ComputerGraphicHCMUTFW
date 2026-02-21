from abc import ABC, abstractmethod

from Engine.RendererResource import ResourceManager

from .ETextureWrapMode import ETextureWrapMode
from .ETextureFilterMode import ETextureFilterMode


class Texture(ABC):
    def __init__(self, textureSrc : str, useMipmap : bool = True):
        self._textureSrc = textureSrc
        self._useMipmap = useMipmap
        self._id = 0
        self._wrapS = ETextureWrapMode.Repeat
        self._wrapT = ETextureWrapMode.Repeat
        self._minFilter = ETextureFilterMode.BilinearMipmapBilinear
        self._magFilter = ETextureFilterMode.Bilinear

    def SetWrapSMode(self, wrapMode : ETextureWrapMode, color = None):
        self._wrapS = wrapMode

    def SetWrapTMode(self, wrapMode : ETextureWrapMode, color = None):
        self._wrapT = wrapMode

    def SetMinFilterMode(self, filterMode : ETextureFilterMode):
        self._minFilter = filterMode

    def SetMagFilterMode(self, filterMode : ETextureFilterMode):
        self._magFilter = filterMode

    def __del__(self):
        self.Delete()

    def GetID(self):
        return self._id

    @abstractmethod
    def Delete(self):
        pass

    @abstractmethod
    def Bind(self,textureIndex : int):
        pass

    @staticmethod
    def Create(textureSrc : str):
        return ResourceManager.ResourceManager.CreateTexture(textureSrc)