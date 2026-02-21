from Engine.Core.EventSystem.EventDispatcher import EventDispatcher
from Engine.Core.InputSystem.InputState import InputState
from Engine.Core.Window.NativeWindow import NativeWindow
from Engine.Core.EventSystem.WindowResizeEvent import WindowResizeEvent
from Engine.Core.Window.WindowFactory import WindowFactory
from Engine.Core.ApplicationCofiguration import ApplicationConfiguration
from Engine.Renderer.Renderer import Renderer
from Engine.RendererResource.ResourceManager import ResourceManager


class Application:
    def __init__(self,appConfig : ApplicationConfiguration = ApplicationConfiguration()):
        self._window : NativeWindow = None
        self._eventDispatcher : EventDispatcher = EventDispatcher()
        self._inputState : InputState = None
        self.__appConfig = appConfig # THIS PYTHON OOP IS SO BAD
        self.SetConfig(appConfig)

    def SetConfig(self,appConfig : ApplicationConfiguration):
        self.__appConfig = appConfig
        self._window = WindowFactory.CreateInstance(appConfig.WindowFlatformSpec)
        self._window.SetEventDispatcher(self._eventDispatcher)
        self._window.SetWindowSize(appConfig.WindowInitSize)
        self._window.SetTitle(appConfig.WindowTitle)

    def GetAppConfig(self):
        return self.__appConfig

    def SetWindow(self, window : NativeWindow):
        self._window = window

    def SetEventDispatcher(self, eventDispatcher : EventDispatcher):
        self._eventDispatcher = eventDispatcher

    def _OnWindowResized(self, windowResizeEvent: WindowResizeEvent) -> bool:
        print(f"Application Window Resized [{windowResizeEvent.NewSize[0]},{windowResizeEvent.NewSize[1]}]")
        return False

    def __ServerInit(self):
        self._window.Init()
        self._inputState = self._window.GetInputState()
        self._eventDispatcher.AddEventListener("WindowResizeEvent", self._OnWindowResized)
        self._inputState = self._window.GetInputState()

        Renderer.OnInit(self.__appConfig.RendererApiSpec)
        ResourceManager.OnInit(self.__appConfig.RendererApiSpec)

    def __ServerBeginLoop(self):
        Renderer.ClearColor(1,1,1,1)

    def __ServerEndLoop(self):
        Renderer.OnDraw()
        self._window.SwapBuffer()
        self._window.PollEvents()

    def __ServerShutdown(self):
        self._window.Shutdown()

    def _ClientInit(self):
        print("Application Client Default Init (Nothing to do)")

    def _ClientLoop(self):
        print("Application Client Default Loop (Nothing to do)")

    def _ClientShutdown(self):
        print("Application Client Shutdown (Nothing to do)")

    def Run(self):
        self.__ServerInit()
        self._ClientInit()

        while not self._window.ShouldClose():
            self.__ServerBeginLoop()
            self._ClientLoop()
            self.__ServerEndLoop()

        self._ClientShutdown()
        self.__ServerShutdown()