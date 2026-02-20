from Engine.Core.EventSystem.EventContext import EventContext
from typing import Callable, override

from abc import ABC, abstractmethod

class IEventAction(ABC):
    @abstractmethod
    def Execute(self,eventContext : EventContext) -> bool: # Return True if failed else Success
        pass

class EventAction(IEventAction):
    def __init__(self, eventCallBack : Callable[[EventContext],bool]):
        self._eventCallBack = eventCallBack

    @override
    def Execute(self,eventContext : EventContext) -> bool:
        return self._eventCallBack(eventContext)