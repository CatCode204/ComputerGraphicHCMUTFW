from Engine.Core.InputSystem.EKeycode import EKeycode
from Engine.Core.InputSystem.EKeystate import EKeyState
from Engine.Core.InputSystem.EMouseButton import EMouseButton
from Engine.Core.InputSystem.GLFW.GLFWKeyboard import GLFWKeyboard
from Engine.Core.InputSystem.GLFW.GLFWMouse import GLFWMouseInput
from Engine.Core.InputSystem.InputState import InputState
from Engine.Core.Window.NativeWindow import NativeWindow
import glfw

class GlfwWindow(NativeWindow):
    def __init__(self, windowSize : tuple[int,int] = (800,600),title : str = "GlfwWindow"):
        super().__init__(windowSize,title)
        self.__window = None

        self._lastFrameX : float = 0
        self._lastFrameY : float = 0
        self._firstInit : bool = False

    def Init(self):
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.__window = glfw.create_window(self._windowSize[0], self._windowSize[1], self._title, None, None)
        glfw.make_context_current(self.__window)

        glfw.set_window_size_callback(self.__window,lambda window,width,height : self._OnChangeSize(width, height))
        self._inputState = InputState()
        self._inputState.MouseInput = GLFWMouseInput(self.__window)
        self._inputState.KeyBoardInput = GLFWKeyboard(self.__window)

        glfw.set_key_callback(self.__window, self._OnKeyCallbackGLFW)
        glfw.set_cursor_pos_callback(self.__window,self._OnMouseMovedGLFW)
        glfw.set_mouse_button_callback(self.__window,self._OnMouseButtonGLFW)

    def ShouldClose(self):
        return glfw.window_should_close(self.__window)

    def PollEvents(self):
        glfw.poll_events()

    def SwapBuffer(self):
        glfw.swap_buffers(self.__window)

    def Shutdown(self):
        glfw.destroy_window(self.__window)
        self.__window = None
        glfw.terminate()

    def _OnKeyCallbackGLFW(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self._OnKeyCallback(EKeycode(key),EKeyState.Pressed)
        if action == glfw.RELEASE:
            self._OnKeyCallback(EKeycode(key),EKeyState.Released)

    def _OnMouseMovedGLFW(self,window,x : float, y : float):
        if self._firstInit:
            self._lastFrameX = x
            self._lastFrameY = y
            self._firstInit = False

        offset : tuple[float,float] = (x - self._lastFrameX, y - self._lastFrameY)
        self._OnMouseMoved((x,y),offset)

        self._lastFrameX = x
        self._lastFrameY = y

    def _OnMouseButtonGLFW(self,window,button,action,mod):
        if action == glfw.PRESS:
            self._OnMouseButtonCallback(EMouseButton(button),EKeyState.Pressed)

        if action == glfw.RELEASE:
            self._OnMouseButtonCallback(EMouseButton(button),EKeyState.Released)