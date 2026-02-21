from Engine.Core.Application import Application,ApplicationConfiguration
from Engine.Renderer.ERenderPrimitives import ERenderPrimitives
from Engine.Renderer.Renderer import Renderer
from Engine.RendererResource import ResourceManager
from Engine.RendererResource.Shader import Shader
from Engine.RendererResource.VertexBuffer import VertexBuffer

import numpy as np
import OpenGL.GL as GL

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

        self.__triangleData = np.array([
            [-1,-1,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0],
            [1,-1,0,0,0,0,0,0,0,0,0]
        ],dtype=np.float32)

        self.shader : Shader = None
        self.vertexBuffer : VertexBuffer = None

    def _ClientInit(self):
        self.shader = Shader.Create("./SimpleTriangle/triangle.vert","./SimpleTriangle/triangle.frag")
        self.vertexBuffer = VertexBuffer.Create()
        self.vertexBuffer.SetData(self.__triangleData,33 * 4)

    def _ClientLoop(self):
        self.shader.Bind()
        self.vertexBuffer.Bind()
        Renderer.DrawArray(ERenderPrimitives.TRIANGLES,0,3)