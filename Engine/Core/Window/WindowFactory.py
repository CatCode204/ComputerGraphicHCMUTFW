from Engine.Core.Window.NativeWindow import NativeWindow
from Engine.Core.Window.WindowPlatforms import WindowPlatforms

from Engine.Core.Window.GLFW.GlfwWindow import GlfwWindow

class WindowFactory:
    @staticmethod
    def CreateInstance(windowPlatform : WindowPlatforms) -> NativeWindow:
        if windowPlatform == WindowPlatforms.GLFW:
            return GlfwWindow()
        raise Exception("Window platform not supported")