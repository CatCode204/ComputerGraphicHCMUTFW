from enum import Enum

class ETextureFilterMode(Enum):
    Nearest = 0,
    Bilinear = 1,
    Trilinear = 2 # CURRENTLY NOT SUPPORT

    # MIPMAP SUPPORT
    NearestMipmapNearest = 3,
    NearestMipmapBilinear = 4,
    BilinearMipmapNearest = 5,
    BilinearMipmapBilinear = 6
