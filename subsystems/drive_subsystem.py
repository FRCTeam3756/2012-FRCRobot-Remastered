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

    def drive(self, xInput, yInput) -> None:
        """Drive the robot using joystick inputs."""

        left_speed = xInput * (-yInput) * DriveConstants.MAX_SPEED
        right_speed = xInput * yInput * DriveConstants.MAX_SPEED

        self.leftDriveLeader.set(TalonSRXControlMode.PercentOutput, left_speed)
        self.rightDriveLeader.set(TalonSRXControlMode.PercentOutput, right_speed)