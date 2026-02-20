from Engine.Core.EventSystem.EventContext import EventContext
from dataclasses import dataclass

from Engine.Core.InputSystem.EMouseButton import EMouseButton


@dataclass
class MouseMovedEvent(EventContext):
    Position : tuple[float,float] = (0,0)
    Offset : tuple[float,float] = (0,0)

@dataclass
class MouseButtonPressedEvent(EventContext):
    Button : EMouseButton = EMouseButton.BUTTON_LEFT

@dataclass
class MouseButtonReleasedEvent(EventContext):
    Button : EMouseButton = EMouseButton.BUTTON_LEFT