from typing import Optional

from wpilib import Timer
from commands2 import Command, InstantCommand, Command
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
        self.armUpButton = controller.rightBumper()
        self.armDownButton = controller.leftBumper()
        self.bandOuttakeButton = controller.b()
        self.bandIntakeButton = controller.a()

    def configureButtonBindings(self) -> None:
        self.shooterOuttakeTrigger.whileTrue(
            InstantCommand(self.shooterSubsystem.shooterOuttake, ShooterSubsystem)
        )
        self.shooterIntakeTrigger.whileTrue(
            InstantCommand(self.shooterSubsystem.shooterIntake, ShooterSubsystem)
        )
        self.bandOuttakeButton.whileTrue(
            InstantCommand(self.intakeSubsystem.outtakeBand, ShooterSubsystem)
        ).onFalse(InstantCommand(self.intakeSubsystem.stopBand, IntakeSubsystem))
        self.bandIntakeButton.whileTrue(
            InstantCommand(self.intakeSubsystem.intakeBand, ShooterSubsystem)
        ).onFalse(InstantCommand(self.intakeSubsystem.stopBand, IntakeSubsystem))
        self.armUpButton.whileTrue(
            InstantCommand(self.intakeSubsystem.armUp, IntakeSubsystem)
        ).onFalse(InstantCommand(self.intakeSubsystem.armStop, IntakeSubsystem))
        self.armDownButton.whileTrue(
            InstantCommand(self.intakeSubsystem.armDown)
        ).onFalse(InstantCommand(self.intakeSubsystem.armStop, IntakeSubsystem))

    def getAutonomousCommand(self) -> Optional[Command]:
        return None
