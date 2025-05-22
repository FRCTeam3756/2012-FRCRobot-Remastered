# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import TimedRobot

from robot_container import RobotContainer
from camera import Camera

#############################################################

class MyRobot(TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.robotContainer = RobotContainer()
        self.camera = Camera()

    def robotInit(self) -> None:
        pass

    def robotPeriodic(self) -> None:
        self.camera.updateFeed()

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.robotContainer.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        self.driveSubsystem.drive(
            self.controller.getLeftX(),
            self.controller.getLeftY()
        )