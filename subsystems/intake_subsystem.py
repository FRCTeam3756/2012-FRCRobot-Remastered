from commands2 import Subsystem
from wpilib import Solenoid, PneumaticsModuleType, Compressor
from phoenix5 import TalonSRX, TalonSRXControlMode

class IntakeSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.intakeMotor = TalonSRX(9)
        self.solenoid = Solenoid(9, PneumaticsModuleType.CTREPCM)
        self.compressor = Compressor(0, PneumaticsModuleType.CTREPCM)
        self.compressor.enableDigital()

    def intake(self) -> None:
        self.intakeMotor.set(TalonSRXControlMode.PercentOutput, 1.0)

    def outtake(self) -> None:
        self.intakeMotor.set(TalonSRXControlMode.PercentOutput, -1.0)

    def up(self) -> None:
        self.solenoid.set(on=True)

    def down(self) -> None:
        self.solenoid.set(on=False)