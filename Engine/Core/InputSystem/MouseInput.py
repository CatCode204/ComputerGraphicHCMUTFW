from .EMouseButton import EMouseButton
from .EKeystate import EKeyState

from abc import ABC, abstractmethod

class MouseInput(ABC):
    def __init__(self,position : tuple[int,int], offset : tuple[int,int], scroll : tuple[int,int]):
        self._position : tuple[float,float] = position
        self._offset : tuple[float,float] = offset
        self._scroll : tuple[float,float] = scroll

    def GetPosition(self) -> tuple[float,float]:
        return self._position

    def GetOffset(self) -> tuple[float,float]:
        return self._offset

    def GetScroll(self) -> tuple[float,float]:
        return self._scroll

    def SetPosition(self,position : tuple[float,float]):
        self._position = position

    def SetOffset(self,offset: tuple[float,float]):
        self._offset = offset

    def SetScroll(self,scroll: tuple[float,float]):
        self._scroll = scroll

    def GetKeyValue(self, button : EMouseButton) -> bool:
        return self.IsPressed(button) or self.IsHeld(button)

    @abstractmethod
    def IsPressed(self,button : EMouseButton) -> bool:
        pass

    @abstractmethod
    def IsReleased(self,button : EMouseButton) -> bool:
        pass

    @abstractmethod
    def IsHeld(self,button : EMouseButton) -> bool:
        pass

    @abstractmethod
    def GetState(self, button : EMouseButton) -> EKeyState:
        pass