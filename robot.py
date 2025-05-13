# Copyright (c) FRC Team 3756 RamFerno.
# Open Source Software; you can modify and/or share it under the terms of
# the license viewable in the root directory of this project.

from wpilib import XboxController, Timer, TimedRobot
from phoenix5 import TalonSRX, TalonSRXControlMode

class MyRobot(TimedRobot):
    def robotInit(self):
        self.leftDriveLeader = TalonSRX(6)
        self.leftDriveFront = TalonSRX(5)
        self.leftDriveBack = TalonSRX(4)

        self.rightDriveLeader = TalonSRX(1)
        self.rightDriveFront = TalonSRX(2)
        self.rightDriveBack = TalonSRX(3)

        self.leftDriveFront.follow(self.leftDriveLeader)
        self.leftDriveBack.follow(self.leftDriveLeader)

        self.rightDriveFront.follow(self.rightDriveLeader)
        self.rightDriveBack.follow(self.rightDriveLeader)

        self.controller = XboxController(0)
        self.timer = Timer()

        self.rightDriveLeader.setInverted(True)

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.leftDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.5)
            self.rightDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.5)
        else:
            self.leftDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.0)
            self.rightDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.leftDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.5)
        self.rightDriveLeader.set(TalonSRXControlMode.MotionMagic, 0.5)