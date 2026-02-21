from typing import Callable

from .RenderCommandCallback import RenderCommandCallBack, IRenderCommandCallBack

from collections import deque

class RenderCommandQueue:
    def __init__(self):
        self.__commandQueue = deque()

    def EnqueueCommandCallback(self,callback : Callable):
        renderCommandCallback : IRenderCommandCallBack = RenderCommandCallBack(callback)
        self.__commandQueue.append(renderCommandCallback)

    def ProcessAndRender(self):
        while True:
            try:
                renderCommandCallBack : IRenderCommandCallBack = self.__commandQueue.popleft()
                renderCommandCallBack.Execute()
            except IndexError:
                break
        self.__commandQueue.clear()