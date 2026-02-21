from typing import override

from Engine.Core.Application import Application
from Engine.Core.ApplicationCofiguration import ApplicationConfiguration
from Engine.Core.EventSystem.EventContexts.KeyboardEvents import KeyboardPressedEvent
from Engine.Core.EventSystem.EventContexts.MouseEvents import MouseMovedEvent, MouseButtonPressedEvent, \
    MouseButtonReleasedEvent
from Engine.Renderer.Renderer import Renderer

class SimpleApp(Application):
    def __init__(self, appConfig : ApplicationConfiguration = ApplicationConfiguration()):
        super().__init__(appConfig)

    @override
    def _ClientInit(self):
        self._eventDispatcher.AddEventListener("KeyboardPressedEvent",self.__OnKeyPressedEvent)
        self._eventDispatcher.AddEventListener("MouseMovedEvent",self.__OnMouseMovedEvent)
        self._eventDispatcher.AddEventListener("MouseButtonPressedEvent",self.__OnMouseButtonPressedEvent)
        self._eventDispatcher.AddEventListener("MouseButtonReleasedEvent",self.__OnMouseButtonReleasedEvent)

    @override
    def _ClientLoop(self):
        Renderer.ClearColor(1,0,1,1)

    @override
    def _ClientShutdown(self):
        pass

    def __OnKeyPressedEvent(self,keyboardPressedEvent : KeyboardPressedEvent) -> bool:
        print(f"Key Event Pressed: {keyboardPressedEvent.KeyCode.name}")
        return False

    def __OnMouseMovedEvent(self,mouseMovedEvent : MouseMovedEvent) -> bool:
        print(f"Mouse Event Moved: FROM {mouseMovedEvent.Position} (dx,dy): {mouseMovedEvent.Offset}")
        return False

    def __OnMouseButtonPressedEvent(self, mouseButtonEvent : MouseButtonPressedEvent):
        print(f"Mouse button pressed: {mouseButtonEvent.Button.name}")
        return False

    def __OnMouseButtonReleasedEvent(self, mouseButtonEvent : MouseButtonReleasedEvent):
        print(f"Mouse button released: {mouseButtonEvent.Button.name}")
        return False