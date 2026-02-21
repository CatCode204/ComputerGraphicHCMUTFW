from typing import override

from ..ERenderMode import ERenderMode
from ..VertexBuffer import VertexBuffer

import ctypes

import OpenGL.GL as GL

from ...Renderer.Renderer import Renderer


class OpenGLVertexBuffer(VertexBuffer):
    def __init__(self):
        super().__init__()
        Renderer.Submit(self.__Init)

    def __Init(self):
        self._id = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._id)
        GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,44,ctypes.c_voidp(0))
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(1,3,GL.GL_FLOAT,GL.GL_FLOAT,44,ctypes.c_voidp(3 * 4))
        GL.glEnableVertexAttribArray(1)
        GL.glVertexAttribPointer(2,2,GL.GL_FLOAT,GL.GL_FLOAT,44,ctypes.c_voidp(6 * 4))
        GL.glEnableVertexAttribArray(2)
        GL.glVertexAttribPointer(3,3,GL.GL_FLOAT,GL.GL_FLOAT,44,ctypes.c_voidp(8 * 4))
        GL.glEnableVertexAttribArray(3)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER,0)

    @override
    def Bind(self):
        Renderer.Submit(lambda: GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._id))

    @override
    def Unbind(self):
        Renderer.Submit(lambda: GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0))

    @override
    def Delete(self):
        Renderer.Submit(self.__DeleteCallback)

    def __DeleteCallback(self):
        GL.glDeleteBuffers(1, [self._id])
        self._size = 0
        self._id = 0

    @override
    def SetData(self, data, size: int, renderMode: ERenderMode = ERenderMode.Static):
        Renderer.Submit(lambda : self.__SetDataCallback(data, size, renderMode))

    def __SetDataCallback(self, data, size: int, renderMode: ERenderMode = ERenderMode.Static):
        self._size = size
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self._id)
        if renderMode == ERenderMode.Static:
            GL.glBufferData(GL.GL_ARRAY_BUFFER, size, data, GL.GL_STATIC_DRAW)
        elif renderMode == ERenderMode.Dynamic:
            GL.glBufferData(GL.GL_ARRAY_BUFFER, size, data, GL.GL_DYNAMIC_DRAW)
        elif renderMode == ERenderMode.Stream:
            GL.glBufferData(GL.GL_ARRAY_BUFFER, size, data, GL.GL_STREAM_DRAW)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)