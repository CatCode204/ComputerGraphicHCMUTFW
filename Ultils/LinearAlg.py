import numpy as np
import math
from numbers import Number
import operator

class Vector:
    def __init__(self,*values):
        self.__v = np.array(values, dtype=float).flatten()

    @property
    def x(self):
        return self.__v[0]

    @property
    def y(self):
        return self.__v[1]

    @property
    def z(self):
        return self.__v[2]

    @property
    def NumpyVector(self):
        return self.__v.copy()

    def ValueAt(self,idx):
        return self.__v[idx]

    @property
    def Length(self):
        return np.sqrt(np.sum(self.__v ** 2))

    @property
    def Dimension(self):
        return len(self.__v)

    @staticmethod
    def Normalized(vector : "Vector") -> "Vector":
        length = vector.Length
        return vector / length

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.NumpyVector + other.NumpyVector)
        else:
            raise ArithmeticError("Cannot Add Vector with a Scalar")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.NumpyVector - other.NumpyVector)
        else:
            raise ArithmeticError("Cannot Subtract Vector with a Scalar")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector(self.NumpyVector * other)
        else:
            raise ArithmeticError("Cannot Mul Vector with a Vector")

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Vector(self.NumpyVector / other)
        else:
            raise ArithmeticError("Cannot Divide Vector with a type not a scalar")

    def __neg__(self):
        return Vector(-self.NumpyVector)

    @staticmethod
    def DotProduct(v1 : "Vector", v2 : "Vector") -> float:
        return np.dot(v1.NumpyVector, v2.NumpyVector)

    @staticmethod
    def CrossProduct(v1 : "Vector", v2 : "Vector") -> "Vector":
        if len(v1.NumpyVector) != 3 or len(v2.NumpyVector) != 3:
            raise ArithmeticError("Cannot compute cross product with two Vectors because one of two (or both) dimension is not equal to 3")
        return Vector(np.cross(v1.NumpyVector, v2.NumpyVector))

class Matrix:
    def __init__(self,data):
        self._m = np.array(data, dtype=float)

        if self._m.ndim != 2:
            raise ArithmeticError("Matrix must have 2 dimensions")

    @property
    def Shape(self):
        return self._m.shape

    @property
    def Transpose(self):
        return self._m.T

    # =========================
    # Basic Operations
    # =========================
    def _elementwise(self, other, op):
        if isinstance(other, Matrix):
            if self.Shape != other.Shape:
                raise ValueError("Matrix shape mismatch")
            return Matrix(op(self._m, other._m))
        elif isinstance(other, (int, float)):
            return Matrix(op(self._m, other))
        return NotImplemented

    def __add__(self, other):
        return self._elementwise(other, operator.add)

    def __sub__(self, other):
        return self._elementwise(other, operator.sub)

    # =========================
    # Multiplication
    # =========================
    def __mul__(self, other):
        # Matrix * Matrix
        if isinstance(other, Matrix):
            if self.Shape[1] != other.Shape[0]:
                raise ValueError("Matrix multiplication shape mismatch")
            return Matrix(self._m @ other._m)

        # Matrix * scalar
        if isinstance(other, (int, float)):
            return Matrix(self._m * other)

        # Matrix * Vector (giả sử Vector có _v)
        if isinstance(other, Vector):
            if self.Shape[1] != len(other.NumpyVector):
                raise ValueError("Matrix-Vector shape mismatch")
            return Vector(*(self._m @ other.NumpyVector))

        raise ArithmeticError("Can't find suitable mul op with that value type")

    def __rmul__(self, other):
        # scalar * Matrix
        if isinstance(other, Number):
            return Matrix(other * self._m)

        raise ArithmeticError("Can't find suitable mul op with that value type")

    # =========================
    # Advanced Operations
    # =========================
    def Inverse(self):
        if self.Shape[0] != self.Shape[1]:
            raise ValueError("Only square matrix can be inverted")
        return Matrix(np.linalg.inv(self._m))

    def Determinant(self):
        if self.Shape[0] != self.Shape[1]:
            raise ValueError("Only square matrix has determinant")
        return float(np.linalg.det(self._m))

    @property
    def ToNumpy(self):
        return self._m.copy()

    @staticmethod
    def CreateIdentityMatrix(size : int) -> "Matrix":
        return Matrix(np.identity(size))

    @staticmethod
    def CreateOrthoMatrix(left : float, right : float, bot : float, top : float, near : float, far : float) -> "Matrix":
        dx, dy, dz = right - left, top - bot, far - near
        rx, ry, rz = -(right + left) / dx, -(top + bot) / dy, -(far + near) / dz

        return Matrix(np.array([[2 / dx, 0, 0, rx],
                         [0, 2 / dy, 0, ry],
                         [0, 0, -2 / dz, rz],
                         [0, 0, 0, 1]], 'f'))

    @staticmethod
    def CreatePerspectiveMatrix(fovy : float, aspect : float, near : float, far : float) -> "Matrix":
        _scale = 1.0 / math.tan(math.radians(fovy) / 2.0)
        sx, sy = _scale / aspect, _scale
        zz = (far + near) / (near - far)
        zw = 2 * far * near / (near - far)
        return Matrix(np.array([[sx, 0, 0, 0],
                         [0, sy, 0, 0],
                         [0, 0, zz, zw],
                         [0, 0, -1, 0]], 'f'))

    @staticmethod
    def CreateFrustumMatrix(xmin : float, xmax : float, ymin : float, ymax : float, zmin : float, zmax : float) -> "Matrix":
        a = (xmax + xmin) / (xmax - xmin)
        b = (ymax + ymin) / (ymax - ymin)
        c = -(zmax + zmin) / (zmax - zmin)
        d = -2 * zmax * zmin / (zmax - zmin)
        sx = 2 * zmin / (xmax - xmin)
        sy = 2 * zmin / (ymax - ymin)
        return Matrix(np.array([[sx, 0, a, 0],
                         [0, sy, b, 0],
                         [0, 0, c, d],
                         [0, 0, -1, 0]], 'f'))

    @staticmethod
    def CreateTranslateMatrix(x = 0,y = 0,z = 0) -> "Matrix":
        matrix = np.identity(4, 'f')
        matrix[:3, 3] = np.array((x, y, z),dtype=float)
        return Matrix(matrix)

    @staticmethod
    def CreateScaleMatrix(scaleX = 1, scaleY = 1, scaleZ = 1) -> "Matrix":
        return Matrix(np.diag([scaleX, scaleY, scaleZ,1]))

    @staticmethod
    def CreateRotateMatrix(axis : Vector = Vector([1,0,0]), angleInDegrees = 0) -> "Matrix":
        """ 4x4 rotation matrix around 'axis' with 'angle' degrees or 'radians' """
        if axis.Dimension != 3:
            raise Exception("Current Axis Dimension is not supported")

        x, y, z = Vector.Normalized(axis).NumpyVector
        radian = math.radians(angleInDegrees)
        s, c = math.sin(radian), math.cos(radian)

        nc = 1 - c
        return Matrix(np.array([[x * x * nc + c, x * y * nc - z * s, x * z * nc + y * s, 0],
                         [y * x * nc + z * s, y * y * nc + c, y * z * nc - x * s, 0],
                         [x * z * nc - y * s, y * z * nc + x * s, z * z * nc + c, 0],
                         [0, 0, 0, 1]], 'f'))

    @staticmethod
    def CreateLookAtMatrix(eye : Vector, target : Vector, up : Vector) -> "Matrix":
        if eye.Dimension != 3 or target.Dimension != 3 or up.Dimension != 3:
            raise Exception("Current Dimension is not supported")

        view = Vector.Normalized(target - eye)
        up = Vector.Normalized(up)
        right = Vector.CrossProduct(view, up)
        up = Vector.CrossProduct(right, view)
        rotation = np.identity(4)
        rotation[:3, :3] = np.vstack([right.NumpyVector, up.NumpyVector, (-view).NumpyVector])

        eyeX, eyeY, eyeZ = (-eye).NumpyVector
        return Matrix(rotation) * Matrix.CreateTranslateMatrix(eyeX,eyeY,eyeZ)

class Quaternion:
    def __init__(self,x = 0.0, y = 0.0, z = 0.0, w = 1.0):
        self._q = np.array((w, x, y, z), 'f')

    @property
    def ToNumpy(self):
        return self._q.copy()

    @staticmethod
    def CreateQuaternionFromAngle(axis : Vector, angleInDegrees = 0) -> "Quaternion":
        angle = math.radians(angleInDegrees)
        sin,cos = math.sin(angle / 2), math.cos(angle / 2)
        x,y,z = (Vector.Normalized(axis) * sin).NumpyVector
        return Quaternion(x,y,z,cos)

    @staticmethod
    def CreateQuaternionFromEuler(yawInDegree=0.0, pitchInDegree=0.0, rollInDegree=0.0):
        yaw, pitch, roll = math.radians(yawInDegree), math.radians(pitchInDegree), math.radians(rollInDegree)
        siy, coy = math.sin(yaw * 0.5), math.cos(yaw * 0.5)
        sir, cor = math.sin(roll * 0.5), math.cos(roll * 0.5)
        sip, cop = math.sin(pitch * 0.5), math.cos(pitch * 0.5)
        return Quaternion(x=coy * sir * cop - siy * cor * sip, y=coy * cor * sip + siy * sir * cop,
                          z=siy * cor * cop - coy * sir * sip, w=coy * cor * cop + siy * sir * sip)

    def __mul__(self, other) -> float:
        if not isinstance(other, Quaternion):
            raise AttributeError("Cannot multiply Quaternion with other type")

        q1,q2 = self.ToNumpy, other.ToNumpy

        return np.dot(np.array([[q1[0], -q1[1], -q1[2], -q1[3]],
                                [q1[1], q1[0], -q1[3], q1[2]],
                                [q1[2], q1[3], q1[0], -q1[1]],
                                [q1[3], -q1[2], q1[1], q1[0]]]), q2)

    def Conjugate(self) -> "Quaternion":
        return Quaternion(x=-self._q[1], y=-self._q[2], z=-self._q[3], w=self._q[0])

    def Inverse(self):
        norm_sq = np.sum(self._q ** 2)
        return Quaternion(
            -self._q[1] / norm_sq,
            -self._q[2] / norm_sq,
            -self._q[3] / norm_sq,
            self._q[0] / norm_sq
        )

    @property
    def ToMatrix(self) -> "Matrix":
        q = Vector.Normalized(Vector(self.ToNumpy)).NumpyVector
        nxx, nyy, nzz = -q[1] * q[1], -q[2] * q[2], -q[3] * q[3]
        qwx, qwy, qwz = q[0] * q[1], q[0] * q[2], q[0] * q[3]
        qxy, qxz, qyz = q[1] * q[2], q[1] * q[3], q[2] * q[3]
        return Matrix(np.array([[2 * (nyy + nzz) + 1, 2 * (qxy - qwz), 2 * (qxz + qwy), 0],
                         [2 * (qxy + qwz), 2 * (nxx + nzz) + 1, 2 * (qyz - qwx), 0],
                         [2 * (qxz - qwy), 2 * (qyz + qwx), 2 * (nxx + nyy) + 1, 0],
                         [0, 0, 0, 1]], 'f'))