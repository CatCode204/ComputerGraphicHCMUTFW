from typing import Callable, override
from abc import ABC, abstractmethod

class IRenderCommandCallBack(ABC):
    @abstractmethod
    def Execute(self):
        pass

class RenderCommandCallBack(IRenderCommandCallBack):
    def __init__(self, callBack : Callable):
        self.callBack = callBack

    @override
    def Execute(self):
        self.callBack()