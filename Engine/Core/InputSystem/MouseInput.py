from .EMouseButton import EMouseButton
from .EKeystate import EKeyState

from Engine.Core.EventSystem.EventContexts.MouseEvents import MouseMovedEvent

from abc import ABC, abstractmethod

from ..EventSystem.EventDispatcher import EventDispatcher


class MouseInput(ABC):
    def __init__(self,position : tuple[int,int], offset : tuple[int,int], scroll : tuple[int,int]):
        self._position : tuple[float,float] = position
        self._scroll : tuple[float,float] = scroll
        self._eventDispatcher : EventDispatcher = None

    def SetEventDispatcher(self,eventDispatcher : EventDispatcher):
        self._eventDispatcher = eventDispatcher
        eventDispatcher.AddEventListener("MouseMovedEvent",self.__OnMouseCursorMove)

    def GetPosition(self) -> tuple[float,float]:
        return self._position

    def GetScroll(self) -> tuple[float,float]:
        return self._scroll

    def SetPosition(self,position : tuple[float,float]):
        self._position = position

    def SetScroll(self,scroll: tuple[float,float]):
        self._scroll = scroll

    def GetKeyValue(self, button : EMouseButton) -> bool:
        return self.IsPressed(button) or self.IsHeld(button)

    def __OnMouseCursorMove(self, eventCtx : MouseMovedEvent):
        self._position = eventCtx.Position

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