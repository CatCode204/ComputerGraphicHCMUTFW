from .EKeycode import EKeycode
from .EKeystate import EKeyState

from abc import ABC, abstractmethod

class KeyboardInput(ABC):
    def GetKeyValue(self, keyCode : EKeycode) -> bool:
        return self.IsPressed(keyCode) or self.IsHeld(keyCode)

    @abstractmethod
    def IsPressed(self,keycode : EKeycode) -> bool:
        pass

    @abstractmethod
    def IsReleased(self,keycode : EKeycode) -> bool:
        pass

    @abstractmethod
    def IsHeld(self,keycode : EKeycode) -> bool:
        pass

    @abstractmethod
    def GetState(self, keyCode : EKeycode) -> EKeyState:
        pass