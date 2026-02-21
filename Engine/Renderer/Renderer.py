from typing import Callable

from Engine.Renderer.ERenderPrimitives import ERenderPrimitives
from Engine.Renderer.RenderCommandQueue import RenderCommandQueue
from Engine.Renderer.RendererAPI import ERendererSpec
from Engine.Renderer.RendererCommand import RendererCommand

class Renderer:
    RenderCommandQueue : RenderCommandQueue = RenderCommandQueue()

    @staticmethod
    def Submit(callback : Callable):
        Renderer.RenderCommandQueue.EnqueueCommandCallback(callback)

    @staticmethod
    def OnInit(renderAPISpec : ERendererSpec):
        renderCallBack : Callable = lambda : RendererCommand.OnInit(renderAPISpec)
        Renderer.RenderCommandQueue.EnqueueCommandCallback(renderCallBack)

    @staticmethod
    def OnDraw():
        Renderer.RenderCommandQueue.ProcessAndRender()

    @staticmethod
    def OnGUIRender(): # UPGRADE LATER
        pass

    @staticmethod
    def BeginScene(): # UPGRADE LATER
        return False

    @staticmethod
    def EndScene(): # UPGRADE LATER
        return False

    @staticmethod
    def DrawArray(renderPrimitive : ERenderPrimitives, first : int, count : int):
        renderCallBack = lambda : RendererCommand.DrawArray(renderPrimitive, first, count)
        Renderer.RenderCommandQueue.EnqueueCommandCallback(renderCallBack)

    @staticmethod
    def ClearColor(r : float,g : float, b : float, a : float):
        renderCallBack : Callable = lambda : RendererCommand.ClearColor(r,g,b,a)
        Renderer.RenderCommandQueue.EnqueueCommandCallback(renderCallBack)

    @staticmethod
    def Shutdown():
        renderCallBack: Callable = lambda: RendererCommand.Shutdown()
        Renderer.RenderCommandQueue.EnqueueCommandCallback(renderCallBack)