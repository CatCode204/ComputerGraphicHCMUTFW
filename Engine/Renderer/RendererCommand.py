from typing import override

from .ERenderPrimitives import ERenderPrimitives
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
            print("[RENDER COMMAND] INIT WITH OPENGL")
            RendererCommand.sInstance = OpenGLRendererCommand()

    @staticmethod
    def Shutdown():
        RendererCommand.sInstance.ShutdownImplement()

    @staticmethod
    def DrawArray(renderPrimitive : ERenderPrimitives, first : int, count : int):
        RendererCommand.sInstance.DrawArrayImplement(renderPrimitive,first,count)

    def ClearColorImplement(self, r : float, g : float, b : float, a : float):
        pass

    def ShutdownImplement(self):
        pass

    def DrawArrayImplement(self, renderPrimitive : ERenderPrimitives,first : int, count : int):
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

    @override
    def DrawArrayImplement(self, renderPrimitive : ERenderPrimitives,first : int, count : int):
        if renderPrimitive == ERenderPrimitives.TRIANGLES:
            gl.glDrawArrays(gl.GL_TRIANGLES, first, count)
        elif renderPrimitive == ERenderPrimitives.TRIANGLE_STRIP:
            gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, first, count)
        elif renderPrimitive == ERenderPrimitives.TRIANGLE_FAN:
            gl.glDrawArrays(gl.GL_TRIANGLE_FAN, first, count)