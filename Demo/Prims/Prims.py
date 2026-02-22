from Engine.Core.Application import Application,ApplicationConfiguration
import numpy as np

from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader
from Engine.RendererResource.VertexBuffer import VertexBuffer


class Prims:
    def __init__(self):
        self.vertices = np.array(
            [
                [+1, -1, +1],  # A <= Bottom:
                [+1, +1, +1],  # B
                [-1, -1, +1],  # C
                [-1, +1, +1],  # D
                [-0.5, -1, -1],  # E
                [-0.5, +1, -1],  # F
            ],
            dtype=np.float32
        )
        self.indices = np.array(
            [0, 1, 2, 3, 4, 5, 0, 1, 1, 0, 0, 2, 4, 4, 1, 1, 5, 3],
            dtype=np.int32
        )

        self.normals = self.vertices.copy()
        self.normals = self.normals / np.linalg.norm(self.normals, axis=1, keepdims=True)

        # colors: RGB format
        self.colors = np.array(
            [  # R    G    B
                [1.0, 0.0, 0.0],  # A <= Bottom:
                [1.0, 0.0, 1.0],  # B
                [0.0, 0.0, 1.0],  # C
                [0.0, 1.0, 0.0],  # D
                [1.0, 1.0, 0.0],  # E
                [1.0, 1.0, 1.0]  # F
            ],
            dtype=np.float32
        )

        #tmp uv
        uvs = np.zeros((self.vertices.shape[0], 2), dtype=np.float32)

        self.vertexData = np.concatenate(
            [
                self.vertices,  # 3
                self.colors,  # 3
                uvs,  # 2
                self.normals  # 3
            ],
            axis=1
        ).astype(np.float32)

        self.indices = np.array(
            [0, 1, 2, 3, 4, 5, 0, 1, 1, 0, 0, 2, 4, 4, 1, 1, 5, 3],
            dtype=np.int32
        )

        self.vertexBuffer = None
        self.indexBuffer = None
        self.shader = None
