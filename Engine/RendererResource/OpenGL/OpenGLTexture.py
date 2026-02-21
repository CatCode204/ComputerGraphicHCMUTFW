from OpenGL.raw.GL.VERSION.GL_1_1 import glBindTexture

from ..ETextureFilterMode import ETextureFilterMode
from ..ETextureWrapMode import ETextureWrapMode
from ..Texture import Texture
from ...Renderer.Renderer import Renderer

import OpenGL.GL as gl

from PIL import Image
import os

class OpenGLTexture(Texture):
    def __init__(self, textureSrc : str,useMipmap : bool = True):
        super().__init__(textureSrc,useMipmap)
        Renderer.Submit(self.__Init)

    def __Init(self):
        self._id = gl.glGenTextures(1)
        pixelData, (width, height), channels = self.__ReadImage(self._textureSrc)

        dataFormat = gl.GL_RGB
        if channels == 3:
            dataFormat = gl.GL_RGB
        elif channels == 4:
            dataFormat = gl.GL_RGBA
        else:
            raise Exception(f"Unsupported channels: {channels}")

        gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)

        gl.glTexImage2D(
            gl.GL_TEXTURE_2D,
            0,
            gl.GL_RGBA,
            width,
            height,
            0,
            dataFormat,
            gl.GL_UNSIGNED_BYTE,
            pixelData
        )

        if self._useMipmap:
            gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)


    def __ReadImage(self, imageFile : str) -> tuple[bytes,tuple[int,int],int]:
        """
            FROM CHATGPT IDK :V
            Read Image file and return:
            - pixelData
            - (width, height)
            - numChannel
        """

        if not os.path.isfile(imageFile):
            raise Exception(f"File {imageFile} does not exist or not image file")

        img = Image.open(imageFile)

        if img.mode in ("RGBA", "LA"): # IF IMAGE IS RGBA (has alpha value)
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")

        width, height = img.size
        pixelData = img.tobytes()

        channels = 4 if img.mode == "RGBA" else 3

        return pixelData, (width,height) ,channels


    def SetWrapSMode(self, wrapMode : ETextureWrapMode, color = None):
        def callback():
            self._wrapS = wrapMode
            gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)
            if wrapMode == ETextureWrapMode.Repeat:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
            elif wrapMode == ETextureWrapMode.ClampToEdge:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
            elif wrapMode == ETextureWrapMode.MirroredRepeat:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_MIRRORED_REPEAT)
            elif wrapMode == ETextureWrapMode.ClampToBorder:
                if color is not None:
                    gl.glTextureParameterfv(gl.GL_TEXTURE_2D,gl.GL_TEXTURE_BORDER_COLOR, color)
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_BORDER)
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        Renderer.Submit(callback)


    def SetWrapTMode(self, wrapMode : ETextureWrapMode, color = None):
        def callback():
            self._wrapT = wrapMode
            gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)
            if wrapMode == ETextureWrapMode.Repeat:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
            elif wrapMode == ETextureWrapMode.ClampToEdge:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
            elif wrapMode == ETextureWrapMode.MirroredRepeat:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_MIRRORED_REPEAT)
            elif wrapMode == ETextureWrapMode.ClampToBorder:
                if color is not None:
                    gl.glTextureParameterfv(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_BORDER_COLOR, color)
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_BORDER)
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        Renderer.Submit(callback)

    def SetMagFilterMode(self, filterMode : ETextureFilterMode):
        def callback():
            self._magFilter = filterMode
            gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)
            if filterMode == ETextureFilterMode.Bilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
            elif filterMode == ETextureFilterMode.Nearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
            elif filterMode == ETextureFilterMode.BilinearMipmapBilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR_MIPMAP_LINEAR)
            elif filterMode == ETextureFilterMode.BilinearMipmapNearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR_MIPMAP_NEAREST)
            elif filterMode == ETextureFilterMode.NearestMipmapBilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST_MIPMAP_LINEAR)
            elif filterMode == ETextureFilterMode.NearestMipmapNearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST_MIPMAP_NEAREST)
            else:
                raise Exception("FilterMode not supported")
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        Renderer.Submit(callback)

    def SetMinFilterMode(self, filterMode : ETextureFilterMode):
        def callback():
            self._magFilter = filterMode
            gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)
            if filterMode == ETextureFilterMode.Bilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
            elif filterMode == ETextureFilterMode.Nearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
            elif filterMode == ETextureFilterMode.BilinearMipmapBilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR_MIPMAP_LINEAR)
            elif filterMode == ETextureFilterMode.BilinearMipmapNearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR_MIPMAP_NEAREST)
            elif filterMode == ETextureFilterMode.NearestMipmapBilinear:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST_MIPMAP_LINEAR)
            elif filterMode == ETextureFilterMode.NearestMipmapNearest:
                gl.glTextureParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST_MIPMAP_NEAREST)
            else:
                raise Exception("FilterMode not supported")
            gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        Renderer.Submit(callback)

    def Delete(self):
        Renderer.Submit(lambda : gl.glDeleteTextures(1,[self._id]))

    def Bind(self, textureIndex: int):
        def callback():
            gl.glActiveTexture(gl.GL_TEXTURE0 + textureIndex)
            gl.glBindTexture(gl.GL_TEXTURE_2D, self._id)

        Renderer.Submit(callback)