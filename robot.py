# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import XboxController, Timer, TimedRobot

from subsystems.drive_subsystem import DriveSubsystem
from subsystems.camera_subsystem import CameraSubsystem
from robot_container import RobotContainer

#############################################################

class MyRobot(TimedRobot):
    def __init__(self) -> None:
        super().__init__()

        self.robotContainer = RobotContainer()
        self.driveSubsystem = DriveSubsystem()

    def robotInit(self) -> None:        
        self.controller = XboxController(0)
        self.timer = Timer()
        self.camera = CameraSubsystem()

    def robotPeriodic(self) -> None:
        self.camera.update_feed()

    def autonomousInit(self) -> None:
        self.timer.restart()

    def autonomousPeriodic(self) -> None:
        self.driveSubsystem.drive(0.0, 1.0)

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        self.driveSubsystem.drive(
            self.controller.getLeftX(),
            self.controller.getLeftY()
        )