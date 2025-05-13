# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import XboxController, Timer, TimedRobot

from subsystems.drive_subsystem import DriveSubsystem
from robot_container import RobotContainer

class MyRobot(TimedRobot):
    def __init__(self):
        self.robotContainer = RobotContainer()
        self.driveSubsystem = DriveSubsystem()

    def robotInit(self):        
        self.controller = XboxController(0)
        self.timer = Timer()

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        self.driveSubsystem.drive(1.0, 0.0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.driveSubsystem.drive(
            self.controller.getLeftX(),
            self.controller.getLeftY()
        )