from ..EShaderTypes import EShaderTypes
from ..Shader import Shader

import OpenGL.GL as gl
import os

from ...Renderer.Renderer import Renderer

class OpenGLShader(Shader):
    def __init__(self, vertexSource : str, fragmentSource : str):
        super().__init__(vertexSource, fragmentSource)
        self._vertexShaderID = 0
        self._fragmentShaderID = 0
        Renderer.Submit(self.__Init)

    def __Init(self):
        self._CompileShader(EShaderTypes.VERTEX_SHADER)
        self._CompileShader(EShaderTypes.FRAGMENT_SHADER)
        self._CompileShader(EShaderTypes.PROGRAM_SHADER)

    def _CompileShader(self, shaderType: EShaderTypes):
        if shaderType == EShaderTypes.PROGRAM_SHADER:
            self._id = gl.glCreateProgram()
            gl.glAttachShader(self._id,self._vertexShaderID)
            gl.glAttachShader(self._id,self._fragmentShaderID)
            gl.glLinkProgram(self._id)
            gl.glDeleteShader(self._vertexShaderID)
            gl.glDeleteShader(self._fragmentShaderID)
            status = gl.glGetProgramiv(self._id, gl.GL_LINK_STATUS)
            if not status:
                log = gl.glGetProgramInfoLog(self._id).decode('ascii')
                gl.glDeleteProgram(self._id)
                raise Exception(f"Shader linking failed: {log}")

        if shaderType == EShaderTypes.VERTEX_SHADER:
            if os.path.exists(self._vertexSrc):
                self._vertexSrc = open(self._vertexSrc, 'r').read()
            else:
                raise FileNotFoundError(f"Vertex shader file not found: {self._vertexSrc}")
            self._vertexShaderID = gl.glCreateShader(gl.GL_VERTEX_SHADER)
            gl.glShaderSource(self._vertexShaderID, self._vertexSrc)
            gl.glCompileShader(self._vertexShaderID)
            status = gl.glGetShaderiv(self._vertexShaderID, gl.GL_COMPILE_STATUS)
            if not status:
                log = gl.glGetShaderInfoLog(self._vertexShaderID).decode('ascii')
                gl.glDeleteShader(self._vertexShaderID)
                raise Exception(f"Vertex Shader compilation failed: {log}")

        if shaderType == EShaderTypes.FRAGMENT_SHADER:
            if os.path.exists(self._fragmentSrc):
                self._fragmentSrc = open(self._fragmentSrc, 'r').read()
            else:
                raise FileNotFoundError(f"Fragment shader file not found: {self._fragmentSrcSrc}")
            self._fragmentShaderID = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
            gl.glShaderSource(self._fragmentShaderID, self._fragmentSrc)
            gl.glCompileShader(self._fragmentShaderID)
            status = gl.glGetShaderiv(self._fragmentShaderID, gl.GL_COMPILE_STATUS)
            if not status:
                log = gl.glGetShaderInfoLog(self._fragmentShaderID).decode('ascii')
                gl.glDeleteShader(self._fragmentShaderID)
                raise Exception(f"Vertex Shader compilation failed: {log}")

    def Delete(self):
        Renderer.Submit(lambda : gl.glDeleteProgram(self._id))

    def Bind(self):
        Renderer.Submit(lambda : gl.glUseProgram(self._id))

    def Unbind(self):
        Renderer.Submit(lambda : gl.glUseProgram(0))

    def SetBool(self, name: str, value: bool):
        Renderer.Submit(lambda : gl.glUniform1i(self.__FindUniformLocation(name),int(value)))

    def SetInt(self, name: str, value: int):
        Renderer.Submit(lambda : gl.glUniform1i(self.__FindUniformLocation(name),value))

    def SetFloat(self, name: str, value: float):
        Renderer.Submit(lambda : gl.glUniform1f(self.__FindUniformLocation(name),value))

    def SetVector2(self, name: str, x: float, y: float):
        Renderer.Submit(lambda : gl.glUniform2f(self.__FindUniformLocation(name),x,y))

    def SetVector3(self, name: str, x: float, y: float, z: float):
        Renderer.Submit(lambda : gl.glUniform3f(self.__FindUniformLocation(name),x,y,z))

    def SetMatrix2(self, name: str, pValue):
        Renderer.Submit(lambda : gl.glUniformMatrix2fv(self.__FindUniformLocation(name),1,gl.GL_TRUE,pValue))

    def SetMatrix3(self, name: str, pValue):
        Renderer.Submit(lambda : gl.glUniformMatrix3fv(self.__FindUniformLocation(name),1,gl.GL_TRUE,pValue))

    def SetMatrix4(self, name: str, pValue):
        Renderer.Submit(lambda : gl.glUniformMatrix4fv(self.__FindUniformLocation(name),1,gl.GL_TRUE,pValue))

    def __FindUniformLocation(self, name : str):
        return gl.glGetUniformLocation(self._id, name)