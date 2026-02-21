from typing import override, Callable

from Engine.Renderer.RendererAPI import ERendererSpec
from Engine.RendererResource.OpenGL.OpenGLIndexBuffer import OpenGLIndexBuffer
from Engine.RendererResource.OpenGL.OpenGLVertexBuffer import OpenGLVertexBuffer
from Engine.RendererResource.VertexBuffer import VertexBuffer
from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader


class ResourceManager:
    Implementor : "ResourceManager" = None

    @staticmethod
    def OnInit(rendererSpec : ERendererSpec):
        if rendererSpec == ERendererSpec.OpenGL:
            ResourceManager.Implementor = OpenGLResourceManager()

    @staticmethod
    def OnShutdown():
        pass

    @staticmethod
    def CreateVertexBuffer() -> VertexBuffer:
        return ResourceManager.Implementor.CreateVertexBuffer()

    @staticmethod
    def FreeVertexBuffer(vertexBuffer : VertexBuffer):
        pass

    @staticmethod
    def CreateIndexBuffer() -> IndexBuffer:
        pass

    @staticmethod
    def FreeIndexBuffer(indexBuffer : IndexBuffer):
        pass

    @staticmethod
    def CreateShader() -> Shader:
        pass

    @staticmethod
    def FreeShader(shader : Shader):
        pass

    def OnShutdownImpl(self):
        pass

    def CreateVertexBufferImpl(self) -> VertexBuffer:
        pass

    def FreeVertexBufferImpl(self, vertexBuffer : VertexBuffer):
        pass

    def CreateIndexBufferImpl(self) -> IndexBuffer:
        pass

    def FreeIndexBufferImpl(self, indexBuffer : IndexBuffer):
        pass

    def CreateShaderImpl(self) -> Shader:
        pass

    def FreeShaderImpl(self):
        pass

class OpenGLResourceManager(ResourceManager):
    def OnShutdownImpl(self):
        pass

    def CreateVertexBufferImpl(self) -> VertexBuffer:
        return OpenGLVertexBuffer()

    def FreeVertexBufferImpl(self, vertexBuffer : VertexBuffer):
        vertexBuffer.Delete()

    def CreateIndexBufferImpl(self) -> IndexBuffer:
        return OpenGLIndexBuffer()

    def FreeIndexBufferImpl(self, indexBuffer : IndexBuffer):
        indexBuffer.Delete()

    def CreateShaderImpl(self) -> Shader:
        pass

    def FreeShaderImpl(self):
        pass