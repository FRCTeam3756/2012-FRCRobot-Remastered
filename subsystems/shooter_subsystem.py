from commands2 import Subsystem
from phoenix5 import TalonSRX, TalonSRXControlMode

#############################################################

class ShooterSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.enterWheel = TalonSRX(7)
        self.exitWheel = TalonSRX(8)

    def intake(self, speed: float) -> None:
        self.exitWheel.set(TalonSRXControlMode.PercentOutput, -speed)
        self.enterWheel.set(TalonSRXControlMode.PercentOutput, -speed)

    def outtake(self, speed: float) -> None:
        self.exitWheel.set(TalonSRXControlMode.PercentOutput, speed)
        self.enterWheel.set(TalonSRXControlMode.PercentOutput, speed)