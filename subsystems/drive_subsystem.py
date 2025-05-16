import math

from commands2 import Subsystem
from phoenix5 import TalonSRX, TalonSRXControlMode

from constants.drive_constants import DriveConstants

class DriveSubsystem(Subsystem):
    def __init__(self):
        super().__init__()

        self.leftDriveLeader = TalonSRX(1)
        self.leftDriveFront = TalonSRX(2)
        self.leftDriveBack = TalonSRX(3)

        self.rightDriveLeader = TalonSRX(4)
        self.rightDriveFront = TalonSRX(5)
        self.rightDriveBack = TalonSRX(6)

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
        return (math.sin((xInput if isLeft else -xInput * math.pi) / 2) + 1) / 2