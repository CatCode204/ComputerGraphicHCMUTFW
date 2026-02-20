from dataclasses import dataclass
from .KeyboardInput import KeyboardInput
from .MouseInput import MouseInput

@dataclass
class InputState:
    KeyBoardInput : KeyboardInput = None
    MouseInput : MouseInput = None