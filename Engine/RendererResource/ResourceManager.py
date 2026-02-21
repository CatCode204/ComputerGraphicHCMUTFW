from Engine.Renderer.RendererAPI import ERendererSpec
from Engine.RendererResource.OpenGL.OpenGLIndexBuffer import OpenGLIndexBuffer
from Engine.RendererResource.OpenGL.OpenGLShader import OpenGLShader
from Engine.RendererResource.OpenGL.OpenGLVertexBuffer import OpenGLVertexBuffer
from Engine.RendererResource.VertexBuffer import VertexBuffer
from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader


class ResourceManager:
    Implementor : "ResourceManager" = None

    @staticmethod
    def OnInit(rendererSpec : ERendererSpec):
        if rendererSpec == ERendererSpec.OpenGL:
            print("[RESOURCE MANAGER] INIT WITH OPENGL")
            ResourceManager.Implementor = OpenGLResourceManager()

    @staticmethod
    def OnShutdown():
        ResourceManager.Implementor.OnShutdownImpl()

    @staticmethod
    def CreateVertexBuffer() -> VertexBuffer:
        return ResourceManager.Implementor.CreateVertexBufferImpl()

    @staticmethod
    def FreeVertexBuffer(vertexBuffer : VertexBuffer):
        ResourceManager.Implementor.FreeVertexBufferImpl(vertexBuffer)

    @staticmethod
    def CreateIndexBuffer() -> IndexBuffer:
        return ResourceManager.Implementor.CreateIndexBufferImpl()

    @staticmethod
    def FreeIndexBuffer(indexBuffer : IndexBuffer):
        ResourceManager.Implementor.FreeIndexBufferImpl(indexBuffer)

    @staticmethod
    def CreateShader(vertexSource : str, fragmentSource : str) -> Shader:
        return ResourceManager.Implementor.CreateShaderImpl(vertexSource,fragmentSource)

    @staticmethod
    def FreeShader(shader : Shader):
        ResourceManager.Implementor.FreeShaderImpl(shader)

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

    def CreateShaderImpl(self, vertexSource : str, fragmentSource) -> Shader:
        pass

    def FreeShaderImpl(self, shader : Shader):
        pass

class OpenGLResourceManager(ResourceManager):
    def OnShutdownImpl(self): #DEFAULT
        pass

    def CreateVertexBufferImpl(self) -> VertexBuffer:
        return OpenGLVertexBuffer()

    def FreeVertexBufferImpl(self, vertexBuffer : VertexBuffer):
        vertexBuffer.Delete()

    def CreateIndexBufferImpl(self) -> IndexBuffer:
        return OpenGLIndexBuffer()

    def FreeIndexBufferImpl(self, indexBuffer : IndexBuffer):
        indexBuffer.Delete()

    def CreateShaderImpl(self,vertexSource : str, fragmentSource) -> Shader:
        return OpenGLShader(vertexSource,fragmentSource)

    def FreeShaderImpl(self, shader : Shader):
        shader.Delete()