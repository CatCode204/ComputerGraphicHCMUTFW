from Engine.Core.Application import Application,ApplicationConfiguration

import numpy as np

from Engine.Core.InputSystem.EKeycode import EKeycode
from Engine.Renderer.ERenderPrimitives import ERenderPrimitives
from Engine.Renderer.Renderer import Renderer
from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader
from Engine.RendererResource.VertexBuffer import VertexBuffer


class Viewer(Application):
    def __init__(self,config : ApplicationConfiguration):
        super().__init__(config)

        # pos(x,y,z) + color(r,g,b) + uv(u,v)
        self.vertices = np.array([
            # pos               # color              # uv        # normal
            [-1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, -1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [-1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0],
        ], dtype=np.float32)

        self.indices = np.array([
            [0, 1, 2],
            [2, 3, 1]
        ],dtype=np.uint32)

        self.indexBuffer = None
        self.vertexBuffer = None
        self.shader = None

    def _ClientInit(self):
        self.shader = Shader.Create("rect.vert","rect.frag")

        self.indexBuffer = IndexBuffer.Create()
        self.indexBuffer.SetData(self.indices,self.indices.nbytes)

        self.vertexBuffer = VertexBuffer.Create()
        self.vertexBuffer.SetData(self.vertices,self.vertices.nbytes)

    def _ClientLoop(self, deltaTime : float):
        self.shader.Bind()
        self.vertexBuffer.Bind()
        self.indexBuffer.Bind()

        Renderer.DrawArray(ERenderPrimitives.TRIANGLE_STRIP,0,4)

config = ApplicationConfiguration()
config.WindowTitle = "Interpolate Rectangle"

app = Viewer(config).Run()