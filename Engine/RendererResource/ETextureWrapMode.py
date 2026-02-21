from enum import Enum

class ETextureWrapMode(Enum):
    Repeat = 0,
    MirroredRepeat = 1,
    ClampToEdge = 2,
    ClampToBorder = 3,