from Engine.Core.EventSystem.EventContext import EventContext
from Engine.Core.InputSystem.EKeycode import EKeycode

class KeyboardPressedEvent(EventContext):
    KeyCode : EKeycode

class KeyboardReleasedEvent(EventContext):
    KeyCode : EKeycode