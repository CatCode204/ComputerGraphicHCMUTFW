from Engine.Core.ApplicationCofiguration import ApplicationConfiguration
from Engine.Renderer.RendererAPI import ERendererSpec
from TestApplicationWindow.SimpleApp import SimpleApp
from Engine.Core.Window.WindowPlatforms import WindowPlatforms

# applicationConfig = ApplicationConfiguration()
# applicationConfig.WindowInitSize = (800,600)
# applicationConfig.WindowTitle = "SIMPLE APP"
# applicationConfig.WindowFlatformSpec = WindowPlatforms.GLFW
# applicationConfig.RendererApiSpec = ERendererSpec.OpenGL

myApp = SimpleApp()