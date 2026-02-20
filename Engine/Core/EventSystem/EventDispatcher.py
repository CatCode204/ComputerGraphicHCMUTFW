from typing import Callable

from Engine.Core.EventSystem.EventAction import EventAction
from Engine.Core.EventSystem.EventContext import EventContext

class EventDispatcher:
    def __init__(self):
        self._eventMapping : dict[str,list[EventAction]] = {}

    def AddEventListener(self,eventContextName : str,eventCallBack : Callable[[EventContext],bool]):
        if eventContextName not in self._eventMapping:
            self._eventMapping[eventContextName] = []

        eventAction = EventAction(eventCallBack)
        self._eventMapping[eventContextName].append(eventAction)

    def EventDispatch(self, eventContextName : str, eventContext : EventContext):
        if eventContextName not in self._eventMapping:
            return

        for eventAction in self._eventMapping[eventContextName]:
            if eventAction.Execute(eventContext):
                break