import math

from commands2 import Subsystem
from phoenix5 import TalonSRX, TalonSRXControlMode

from constants.drive_constants import DriveConstants

class DriveSubsystem(Subsystem):
    def __init__(self):
        super().__init__()

        self.leftDriveLeader = TalonSRX(6)
        self.leftDriveFront = TalonSRX(5)
        self.leftDriveBack = TalonSRX(4)

        self.rightDriveLeader = TalonSRX(1)
        self.rightDriveFront = TalonSRX(2)
        self.rightDriveBack = TalonSRX(3)

        self.leftDriveLeader.setInverted(True)
        self.leftDriveFront.setInverted(True)
        self.leftDriveBack.setInverted(True)

        self.leftDriveFront.follow(self.leftDriveLeader)
        self.leftDriveBack.follow(self.leftDriveLeader)

        self.rightDriveFront.follow(self.rightDriveLeader)
        self.rightDriveBack.follow(self.rightDriveLeader)

    def drive(self, xInput: float, yInput: float) -> None:
        left_speed = yInput * self.compute_turn(xInput, isLeft=True) * DriveConstants.MAX_SPEED
        right_speed = yInput * self.compute_turn(xInput, isLeft=False) * DriveConstants.MAX_SPEED

        self.leftDriveLeader.set(TalonSRXControlMode.PercentOutput, left_speed)
        self.rightDriveLeader.set(TalonSRXControlMode.PercentOutput, right_speed)
    
    @staticmethod
    def compute_turn(xInput: float, isLeft: bool) -> float:
        return ((math.cos((((0.5 if isLeft else -0.5) * math.pi) * xInput) - (0.5 * math.pi)) + 1) / 2) * DriveConstants.MAX_SPEED