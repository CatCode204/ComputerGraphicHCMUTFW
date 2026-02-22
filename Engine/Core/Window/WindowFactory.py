from Engine.Core.Window.NativeWindow import NativeWindow
from Engine.Core.Window.WindowPlatforms import WindowPlatforms

from Engine.Core.Window.GLFW.GlfwWindow import GlfwWindow

from abc import ABC, abstractmethod

class WindowFactory(ABC):
    @abstractmethod
    def CreateWindow(self) -> NativeWindow:
        pass

    @abstractmethod
    def CreateInputState(self):
        pass