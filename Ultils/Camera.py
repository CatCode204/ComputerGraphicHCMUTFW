from Ultils.LinearAlg import Vector,Matrix,Quaternion
from dataclasses import dataclass

import numpy as np

@dataclass
class Camera:
    Position : Vector = Vector(0,0,0)
    Rotation : Vector = Vector(-90,0,0) # Euler
    WorldUpVector : Vector = Vector(0,1,0)

    @property
    def Forward(self):
        yawDeg, pitchDeg, rollDeg = self.Rotation.NumpyVector
        yaw, pitch, roll = np.radians([yawDeg, pitchDeg, rollDeg])

        sin_y, cos_y = np.sin(yaw), np.cos(yaw)
        sin_pitch, cos_pitch = np.sin(pitch), np.cos(pitch)
        cos_roll, sin_roll = np.sin(roll), np.cos(roll)

        forward = np.array([
            cos_y * cos_pitch,
            sin_pitch,
            sin_y * cos_pitch
        ])

        return Vector(forward)

    @property
    def Right(self):
        return Vector.CrossProduct(self.Forward, self.WorldUpVector)

    @property
    def ViewMatrix(self) -> Matrix:
        matrix = Matrix.CreateLookAtMatrix(self.Position, self.Position + self.Forward,self.WorldUpVector)

        return matrix