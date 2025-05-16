# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import XboxController, Timer, TimedRobot

from subsystems.drive_subsystem import DriveSubsystem
from subsystems.camera_subsystem import CameraSubsystem
from robot_container import RobotContainer

class MyRobot(TimedRobot):
    def __init__(self):
        super().__init__()

        self.robotContainer = RobotContainer()
        self.driveSubsystem = DriveSubsystem()

    def robotInit(self):        
        self.controller = XboxController(0)
        self.timer = Timer()
        self.camera = CameraSubsystem()

    def robotPeriodic(self):
        self.camera.update_feed()

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        self.driveSubsystem.drive(0.0, 1.0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.driveSubsystem.drive(
            self.controller.getLeftX(),
            self.controller.getLeftY()
        )