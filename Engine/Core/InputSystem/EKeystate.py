from enum import Enum

class EKeyState(Enum):
    NoneState = 0,
    Pressed = 1,
    Released = 2,
    Held = 3