from Engine.Core.InputSystem.GLFW.GLFWKeyboard import GLFWKeyboard
from Engine.Core.InputSystem.GLFW.GLFWMouse import GLFWMouseInput
from Engine.Core.InputSystem.InputState import InputState
from Engine.Core.Window.GLFW.GlfwWindow import GlfwWindow
from Engine.Core.Window.NativeWindow import NativeWindow
from Engine.Core.Window.WindowFactory import WindowFactory

class GlfwWindowFactory(WindowFactory):
    def CreateWindow(self) -> NativeWindow:
        return GlfwWindow()

    def CreateInputState(self):
        inputState = InputState()
        inputState.MouseInput = GLFWMouseInput()
        inputState.KeyBoardInput = GLFWKeyboard()
        return inputState