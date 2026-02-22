from Engine.Core.InputSystem.EKeycode import EKeycode
from Engine.Core.InputSystem.EKeystate import EKeyState
from Engine.Core.InputSystem.KeyboardInput import KeyboardInput

import glfw

class GLFWKeyboard(KeyboardInput):
    def __init__(self, window = None):
        self._window = window

    def SetWindow(self,objWindow):
        self._window = objWindow

    def IsHeld(self, keycode: EKeycode) -> bool:
        return self.GetState(keycode) == EKeyState.Held

    def IsPressed(self, keycode: EKeycode) -> bool:
        return self.GetState(keycode) == EKeyState.Pressed

    def IsReleased(self, keycode: EKeycode) -> bool:
        return self.GetState(keycode) == EKeyState.Released

    def GetState(self, keyCode : EKeycode) -> EKeyState:
        if glfw.get_key(self._window, keyCode.value) == glfw.PRESS: return EKeyState.Pressed
        if glfw.get_key(self._window, keyCode.value) == glfw.RELEASE: return EKeyState.Released
        if glfw.get_key(self._window, keyCode.value) == glfw.REPEAT: return EKeyState.Released
        return EKeyState.NoneState

    # Actually now don't need the adapter pattern because We use the enum value according to keycode glfw