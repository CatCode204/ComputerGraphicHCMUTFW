from enum import Enum

class EBufferModeSpec(Enum):
    Depth = 0

class EDepthFuncSpec(Enum):
    Always = 0
    Never = 1
    Less = 2
    Equal = 3
    LessEqual = 4
    Greater = 5
    GreaterEqual = 6
    NotEqual = 7