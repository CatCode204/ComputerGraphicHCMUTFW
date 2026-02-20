from .EventContext import EventContext
from dataclasses import dataclass

@dataclass
class WindowResizeEvent(EventContext):
    NewSize : tuple[int,int] = (0,0)