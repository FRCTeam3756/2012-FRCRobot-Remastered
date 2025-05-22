from wpilib import Timer
from commands2 import Command, InstantCommand
from commands2.button import CommandXboxController

from subsystems.drive_subsystem import DriveSubsystem
from subsystems.intake_subsystem import IntakeSubsystem
from subsystems.shooter_subsystem import ShooterSubsystem

#############################################################

class RobotContainer:
    def __init__(self) -> None:
        self.robotContainer = RobotContainer()
        self.driveSubsystem = DriveSubsystem()
        self.intakeSubsystem = IntakeSubsystem()
        self.shooterSubsystem = ShooterSubsystem()

        self.configureJoysticks()
        self.configureButtonBindings()

    def configureJoysticks(self) -> None:
        controller = CommandXboxController(0)

        self.shooterOuttakeTrigger = controller.rightTrigger()
        self.shooterIntakeTrigger = controller.leftTrigger()
        self.outtakeButton = controller.rightBumper()
        self.intakeButton = controller.leftBumper()

    def configureButtonBindings(self) -> None:
        self.shooterOuttakeTrigger.whileTrue(InstantCommand(self.shooterSubsystem.outtake(), ShooterSubsystem))
        self.shooterIntakeTrigger.whileTrue(InstantCommand(self.shooterSubsystem.intake(), ShooterSubsystem))
        self.outtakeButton.whileTrue(InstantCommand(self.intakeSubsystem.outtake(), ShooterSubsystem))
        self.intakeButton.whileTrue(InstantCommand(self.intakeSubsystem.intake(), ShooterSubsystem))
    
    def getAutonomousCommand(self) -> Command:
        ...