from commands2 import Subsystem
from wpilib import DoubleSolenoid, PneumaticsModuleType, Compressor
from phoenix5 import TalonSRX, TalonSRXControlMode

class IntakeSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.intakeMotor = TalonSRX(9)
        self.solenoid = DoubleSolenoid(PneumaticsModuleType.CTREPCM, 0, 1)
        self.compressor = Compressor(PneumaticsModuleType.CTREPCM, 0)
        self.compressor.enableDigital()

    def intakeBand(self) -> None:
        self.intakeMotor.set(TalonSRXControlMode.PercentOutput, 1.0)

    def outtakeBand(self) -> None:
        self.intakeMotor.set(TalonSRXControlMode.PercentOutput, -1.0)

    def stopBand(self) -> None:
        self.intakeMotor

    def armUp(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kReverse)

    def armDown(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kForward)

    def armStop(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kOff)