import glfw

from Engine.Core.InputSystem.EKeystate import EKeyState
from Engine.Core.InputSystem.EMouseButton import EMouseButton
from Engine.Core.InputSystem.MouseInput import MouseInput

class GLFWMouseInput(MouseInput):
    def __init__(self,window = None ,position : tuple[int,int] = (0,0), offset : tuple[int,int] = (0,0), scroll : tuple[int,int] = (0,0)):
        super().__init__(position,offset,scroll)
        self._window = window

    def SetWindow(self,windowObj):
        self._window = windowObj

    def IsPressed(self, button: EMouseButton) -> bool:
        return self.GetState(button) == EKeyState.Pressed

    def IsReleased(self, button: EMouseButton) -> bool:
        return self.GetState(button) == EKeyState.Released

    def IsHeld(self, button: EMouseButton) -> bool:
        return self.GetState(button) == EKeyState.Held

    def GetState(self, button: EMouseButton) -> EKeyState:
        if glfw.get_mouse_button(self._window, button.value) == glfw.PRESS: return EKeyState.Pressed
        if glfw.get_mouse_button(self._window, button.value) == glfw.RELEASE: return EKeyState.Released
        if glfw.get_mouse_button(self._window, button.value) == glfw.REPEAT: return EKeyState.Held
        return EKeyState.NoneState