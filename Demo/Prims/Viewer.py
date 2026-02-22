import numpy as np

from Engine.Core.Application import Application, ApplicationConfiguration
from Engine.Core.EventSystem.EventContexts.MouseEvents import MouseMovedEvent
from Engine.Core.InputSystem.EKeycode import EKeycode
from Engine.Renderer.EBufferModeSpec import EBufferModeSpec
from Engine.Renderer.ERenderPrimitives import ERenderPrimitives
from Engine.Renderer.Renderer import Renderer
from Engine.RendererResource.IndexBuffer import IndexBuffer
from Engine.RendererResource.Shader import Shader
from Engine.RendererResource.VertexBuffer import VertexBuffer
from Ultils.Camera import Camera
from Ultils.CameraController import CameraController
from Ultils.CameraMoveCommand import CameraMoveCommand
from Ultils.CameraRotateCommand import CameraRotateCommand
from Ultils.LinearAlg import Vector, Matrix


class Viewer(Application):
    def __init__(self,appConfig : ApplicationConfiguration):
        super().__init__(appConfig)
        self.camera : Camera = Camera()
        self.cameraController : CameraController = CameraController(self.camera)

        # vertex format: position(3) + color(3) + uv(2) + normal(3)
        self.vertices = np.array([
            # ===== FRONT (+Z) - Red =====
            [-1, -1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, -1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [-1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],

            # ===== BACK (-Z) - Green =====
            [1, -1, -1, 0, 1, 0, 0, 0, 0, 0, -1],
            [-1, -1, -1, 0, 1, 0, 1, 0, 0, 0, -1],
            [-1, 1, -1, 0, 1, 0, 1, 1, 0, 0, -1],
            [1, 1, -1, 0, 1, 0, 0, 1, 0, 0, -1],

            # ===== LEFT (-X) - Blue =====
            [-1, -1, -1, 0, 0, 1, 0, 0, -1, 0, 0],
            [-1, -1, 1, 0, 0, 1, 1, 0, -1, 0, 0],
            [-1, 1, 1, 0, 0, 1, 1, 1, -1, 0, 0],
            [-1, 1, -1, 0, 0, 1, 0, 1, -1, 0, 0],

            # ===== RIGHT (+X) - Yellow =====
            [1, -1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, -1, -1, 1, 1, 0, 1, 0, 1, 0, 0],
            [1, 1, -1, 1, 1, 0, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],

            # ===== TOP (+Y) - Magenta =====
            [-1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
            [1, 1, -1, 1, 0, 1, 1, 1, 0, 1, 0],
            [-1, 1, -1, 1, 0, 1, 0, 1, 0, 1, 0],

            # ===== BOTTOM (-Y) - Cyan =====
            [-1, -1, -1, 0, 1, 1, 0, 0, 0, -1, 0],
            [1, -1, -1, 0, 1, 1, 1, 0, 0, -1, 0],
            [1, -1, 1, 0, 1, 1, 1, 1, 0, -1, 0],
            [-1, -1, 1, 0, 1, 1, 0, 1, 0, -1, 0],
        ], dtype=np.float32)

        self.indices = np.array([
            0, 1, 2, 0, 2, 3,  # Front
            4, 5, 6, 4, 6, 7,  # Back
            8, 9, 10, 8, 10, 11,  # Left
            12, 13, 14, 12, 14, 15,  # Right
            16, 17, 18, 16, 18, 19,  # Top
            20, 21, 22, 20, 22, 23  # Bottom
        ], dtype=np.uint32)

        self.vertexBuffer = None
        self.shader = None
        self._indexBuffer = None

    def _ClientInit(self):
        Renderer.EnableBufferMode(EBufferModeSpec.Depth)
        self._eventDispatcher.AddEventListener("MouseMovedEvent",self.__OnMouseMove)
        self.vertexBuffer = VertexBuffer.Create()
        self.vertexBuffer.SetData(self.vertices,self.vertices.nbytes)

        self._indexBuffer = IndexBuffer.Create()
        self._indexBuffer.SetData(self.indices,self.indices.nbytes)

        self.shader = Shader.Create("color_interp.vert","color_interp.frag")

    def _ClientLoop(self, deltaTime : float):
        self.__ProcessInput()
        self.cameraController.Execute(deltaTime)
        self.shader.Bind()

        projection = Matrix.CreatePerspectiveMatrix(45,4 / 3,.1,100).ToNumpy.astype(np.float32)
        modelView = self.camera.ViewMatrix.ToNumpy.astype(np.float32)

        self.shader.SetMatrix4("projection",projection)
        self.shader.SetMatrix4("modelview", modelView)
        self.vertexBuffer.Bind()
        self._indexBuffer.Bind()
        Renderer.DrawElement(ERenderPrimitives.TRIANGLES,0,36)


    def __OnMouseMove(self, eventCtx : MouseMovedEvent):
        yaw,pitch = eventCtx.Offset
        self.cameraController.EnqueueCommand(CameraRotateCommand(Vector(yaw,-pitch,0) * 100))

    def __ProcessInput(self):
        moveVector : Vector = Vector(0,0,0)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_W):
            moveVector += Vector(0,0,1)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_S):
            moveVector += Vector(0,0,-1)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_A):
            moveVector += Vector(-1,0,0)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_D):
            moveVector += Vector(1,0,0)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_SPACE):
            moveVector += Vector(0,1,0)
        if self._inputState.KeyBoardInput.GetKeyValue(EKeycode.KEY_LEFT_SHIFT):
            moveVector += Vector(0,-1,0)

        self.cameraController.EnqueueCommand(CameraMoveCommand(moveVector))

config = ApplicationConfiguration()
config.WindowTitle = "An Truong"
view = Viewer(config).Run()