from Engine.Core.Application import Application,ApplicationConfiguration
from Engine.Renderer.ERenderPrimitives import ERenderPrimitives
from Engine.Renderer.Renderer import Renderer
from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader
from Engine.RendererResource.VertexBuffer import VertexBuffer

import OpenGL.GL as GL

import numpy as np

class TriangleApp(Application):
    def __init__(self,config : ApplicationConfiguration):
        super().__init__(config)

        """
        VertexArrayDataOnFormat = [
            [vertPos.x, vertPos.y, vertPos.z, vertColor.r, vertColor.g, vertColor.b, vertUV.u, vertUV.v, vertNorm.x, vertNorm.y, vertNorm.z],
            .
            .
            .
        ]
        """

        self.__triangleData1 = np.array([
            [-1,-1,0,1,0,0,0,0,0,0,0],
            [0,1,0,0,1,0,0,0,0,0,0],
            [1,-1,0,0,0,1,0,0,0,0,0]
        ],dtype=np.float32)

        self.__triangleData2 = np.array([
            [-1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ], dtype=np.float32)

        self.__indices = np.array([0,1,2],dtype=np.uint32)

        self.shader : Shader = None
        self.vertexBuffer1 : VertexBuffer = None
        self.vertexBuffer2 : VertexBuffer = None

        self.indexBuffer : IndexBuffer = None

    def _ClientInit(self):
        self.shader = Shader.Create("triangle.vert","triangle.frag")
        self.vertexBuffer1 = VertexBuffer.Create()
        self.vertexBuffer1.SetData(self.__triangleData1,33 * 4)

        self.vertexBuffer2 = VertexBuffer.Create()
        self.vertexBuffer2.SetData(self.__triangleData2,33 * 4)

        self.indexBuffer = IndexBuffer.Create()
        self.indexBuffer.SetData(self.__indices,3 * 4)

    def _ClientLoop(self):
        self.shader.Bind()
        self.vertexBuffer2.Bind()
        self.indexBuffer.Bind()
        Renderer.DrawElement(ERenderPrimitives.TRIANGLES,0,3)
        Renderer.OnDraw()