from commands2 import Subsystem
from phoenix5 import TalonSRX

#############################################################

class ShooterSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.enterWheel = TalonSRX(7)
        self.exitWheel = TalonSRX(8)