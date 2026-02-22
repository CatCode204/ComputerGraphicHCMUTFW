from LinearAlg import Vector,Matrix,Quaternion

class Transform:
    def __init__(self, position : Vector, rotation : Vector, scale : Vector):
        self._position = position
        self._rotation = rotation
        self._scale = scale

    @property
    def TransformMatrix(self) -> Matrix:
        posX,poxY,posZ = self._position.NumpyVector
        translateMatrix = Matrix.CreateTranslateMatrix(posX,poxY,posZ)

        scaleX,scaleY,scaleZ = self._scale.NumpyVector
        scaleMatrix = Matrix.CreateScaleMatrix(scaleX,scaleY,scaleZ)

        yawDegree,pitchDegree,rollDegree = self._rotation.NumpyVector
        rotateMatrix = Quaternion.CreateQuaternionFromEuler(yawDegree,pitchDegree,rollDegree).ToMatrix

        return translateMatrix * rotateMatrix * scaleMatrix