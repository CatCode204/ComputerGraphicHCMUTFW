from Engine.RendererResource.ERenderMode import ERenderMode
from Engine.RendererResource.IndexBuffer import IndexBuffer

import OpenGL.GL as GL

from ...Renderer.Renderer import Renderer


class OpenGLIndexBuffer(IndexBuffer):
    def __init__(self):
        super().__init__()
        Renderer.Submit(self.__Init)

    def __Init(self):
        self._id = GL.glGenBuffers(1)


    def Bind(self):
        Renderer.Submit(lambda : GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self._id))

    def UnBind(self):
        Renderer.Submit(lambda : GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, 0))

    def Delete(self):
        Renderer.Submit(self.__Delete)

    def __Delete(self):
        GL.glDeleteBuffers(1, [self._id])

    def SetData(self, data,size,renderMode : ERenderMode = ERenderMode.Static):
        Renderer.Submit(lambda : self.__SetDataCallback(data,size,renderMode))

    def __SetDataCallback(self,data,size,renderMode : ERenderMode = ERenderMode.Static):
        self._size = size
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self._id)
        if renderMode == ERenderMode.Static:
            GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER,size,data,GL.GL_STATIC_DRAW)
        elif renderMode == ERenderMode.Dynamic:
            GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER,size,data,GL.GL_DYNAMIC_DRAW)
        elif renderMode == ERenderMode.Stream:
            GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER,size,data,GL.GL_STREAM_DRAW)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER,0)