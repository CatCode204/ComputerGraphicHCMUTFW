from Engine.Core.EventSystem.EventDispatcher import EventDispatcher
from Engine.Core.InputSystem.InputState import InputState
from Engine.Core.Window.NativeWindow import NativeWindow
from Engine.Core.EventSystem.WindowResizeEvent import WindowResizeEvent

class Application:
    def __init__(self,window : NativeWindow, eventDispatcher : EventDispatcher):
        self._window = window
        self._eventDispatcher = eventDispatcher
        self._inputState : InputState = None

    def _OnWindowResized(self, windowResizeEvent: WindowResizeEvent) -> bool:
        print(f"Application Window Resized [{windowResizeEvent.NewSize[0]},{windowResizeEvent.NewSize[1]}]")
        return False

    def __ServerInit(self):
        self._window.Init()
        self._eventDispatcher.AddEventListener("WindowResizeEvent", self._OnWindowResized)
        self._inputState = self._window.GetInputState()

    def __ServerLoop(self):
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
            self._ClientLoop()
            self.__ServerLoop()

        self._ClientShutdown()
        self.__ServerShutdown()