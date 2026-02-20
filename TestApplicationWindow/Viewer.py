from TestApplicationWindow.SimpleApp import SimpleApp

from Engine.Core.Window.WindowFactory import WindowFactory
from Engine.Core.Window.WindowPlatforms import WindowPlatforms
from Engine.Core.EventSystem.EventDispatcher import EventDispatcher

eventDispatcher = EventDispatcher()
window = WindowFactory.CreateInstance(WindowPlatforms.GLFW)
window.SetEventDispatcher(eventDispatcher)

myApp = SimpleApp(window,eventDispatcher)