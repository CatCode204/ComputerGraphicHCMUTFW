from enum import Enum

class ECursorMode(Enum):
    Hidden = 0,
    Captured = 1,
    Normal = 2,
    Unavailable = 3,
    Disabled = 4