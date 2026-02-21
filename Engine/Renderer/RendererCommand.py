from typing import override
from .RendererAPI import ERendererSpec
import OpenGL.GL as gl

class RendererCommand:
    def __new__(cls):
        if cls.sInstance is None:
            cls.sInstance = super().__new__(cls)
        return cls.sInstance

    @staticmethod
    def ClearColor(r : float, g : float, b : float, a : float):
        RendererCommand.sInstance.ClearColorImplement(r, g, b, a)

    @staticmethod
    def OnInit(rendererSpect : ERendererSpec):
        if rendererSpect == ERendererSpec.OpenGL:
            RendererCommand.sInstance = OpenGLRendererCommand()

    @staticmethod
    def Shutdown():
        RendererCommand.sInstance.ShutdownImplement()

    def ClearColorImplement(self, r : float, g : float, b : float, a : float):
        pass

    def ShutdownImplement(self):
        pass

    sInstance : "RendererCommand" = None

class OpenGLRendererCommand(RendererCommand):
    @override
    def ClearColorImplement(self, r : float, g : float, b : float, a : float):
        gl.glClearColor(r,g,b,a)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    @override
    def ShutdownImplement(self): # DEFAULT OPENGL DO IT BY SELF
        pass