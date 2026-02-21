from abc import ABC,abstractmethod

from Engine.Core.EventSystem.EventContexts.KeyboardEvents import KeyboardPressedEvent, KeyboardReleasedEvent
from Engine.Core.EventSystem.EventContexts.MouseEvents import MouseMovedEvent, MouseButtonPressedEvent, \
    MouseButtonReleasedEvent
from Engine.Core.EventSystem.EventDispatcher import EventDispatcher
from Engine.Core.EventSystem.WindowResizeEvent import WindowResizeEvent
from Engine.Core.InputSystem.EKeycode import EKeycode
from Engine.Core.InputSystem.EKeystate import EKeyState
from Engine.Core.InputSystem.EMouseButton import EMouseButton
from Engine.Core.InputSystem.InputState import InputState


class NativeWindow(ABC):
    def __init__(self, windowSize : tuple[int,int], title : str):
        self._windowSize = windowSize
        self._title = title
        self._eventDispatcher : EventDispatcher = None
        self._inputState : InputState = None

    def SetWindowSize(self, windowSize : tuple[int,int]):
        self._windowSize = windowSize

    def SetTitle(self, title : str):
        self._title = title

    def SetInputState(self,inputState : InputState):
        self._inputState = inputState

    def GetInputState(self):
        return self._inputState

    def SetEventDispatcher(self, eventDispatcher : EventDispatcher):
        self._eventDispatcher = eventDispatcher

    def _OnKeyCallback(self, keyCode : EKeycode, keyState : EKeyState):
        if keyState == EKeyState.Pressed:
            eventCtx : KeyboardPressedEvent = KeyboardPressedEvent()
            eventCtx.KeyCode = keyCode
            self._eventDispatcher.EventDispatch("KeyboardPressedEvent",eventCtx)

        if keyState == EKeyState.Released:
            eventCtx : KeyboardReleasedEvent = KeyboardReleasedEvent()
            eventCtx.KeyCode = keyCode
            self._eventDispatcher.EventDispatch("KeyboardReleasedEvent",eventCtx)

    def _OnChangeSize(self, newWidth : int, newHeight : int):
        eventCtx : WindowResizeEvent = WindowResizeEvent()
        eventCtx.NewSize = (newWidth,newHeight)
        self._eventDispatcher.EventDispatch("WindowResizeEvent",eventCtx)

    def _OnMouseMoved(self,position: tuple[float,float], offset: tuple[float,float]):
        eventCtx : MouseMovedEvent = MouseMovedEvent()
        eventCtx.Position = position
        eventCtx.Offset = offset
        self._eventDispatcher.EventDispatch("MouseMovedEvent",eventCtx)

    def _OnMouseButtonCallback(self,button : EMouseButton, btnState : EKeyState):
        if btnState == EKeyState.Pressed:
            eventCtx : MouseButtonPressedEvent = MouseButtonPressedEvent()
            eventCtx.Button = button
            self._eventDispatcher.EventDispatch("MouseButtonPressedEvent",eventCtx)

        if btnState == EKeyState.Released:
            eventCtx : MouseButtonReleasedEvent = MouseButtonReleasedEvent()
            eventCtx.Button = button
            self._eventDispatcher.EventDispatch("MouseButtonReleasedEvent",eventCtx)

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def ShouldClose(self):
        pass

    @abstractmethod
    def PollEvents(self):
        pass

    @abstractmethod
    def SwapBuffer(self):
        pass

    @abstractmethod
    def Shutdown(self):
        pass