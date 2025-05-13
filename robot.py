# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import XboxController, Timer, TimedRobot
from phoenix5 import TalonSRX, TalonSRXControlMode

class MyRobot(TimedRobot):
    def robotInit(self):
        self.enterWheel = TalonSRX(7)
        self.exitWheel = TalonSRX(8)

        self.leftDriveLeader = TalonSRX(6)
        self.leftDriveFront = TalonSRX(5)
        self.leftDriveBack = TalonSRX(4)

        self.rightDriveLeader = TalonSRX(1)
        self.rightDriveFront = TalonSRX(2)
        self.rightDriveBack = TalonSRX(3)

        self.leftDriveLeader.setInverted(True)
        self.leftDriveFront.setInverted(True)
        self.leftDriveBack.setInverted(True)

        self.leftDriveFront.follow(self.leftDriveLeader)
        self.leftDriveBack.follow(self.leftDriveLeader)

        self.rightDriveFront.follow(self.rightDriveLeader)
        self.rightDriveBack.follow(self.rightDriveLeader)
        

        self.controller = XboxController(0)
        self.timer = Timer()

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        self.leftDriveLeader.set(TalonSRXControlMode.PercentOutput, 1.0)
        self.rightDriveLeader.set(TalonSRXControlMode.PercentOutput, 1.0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.leftDriveLeader.set(TalonSRXControlMode.PercentOutput, 1.0)
        self.rightDriveLeader.set(TalonSRXControlMode.PercentOutput, 1.0)