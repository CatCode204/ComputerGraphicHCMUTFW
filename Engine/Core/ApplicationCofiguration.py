from dataclasses import dataclass

from Engine.Core.Window.WindowPlatforms import WindowPlatforms
from Engine.Renderer.RendererAPI import ERendererSpec

@dataclass
class ApplicationConfiguration:
    WindowInitSize : tuple[int,int] = (800,600)
    WindowTitle : str = "HCMUT_COMPUTER_GRAPHIC_LTS_FW"
    WindowFlatformSpec : WindowPlatforms = WindowPlatforms.GLFW

    RendererApiSpec : ERendererSpec = ERendererSpec.OpenGL