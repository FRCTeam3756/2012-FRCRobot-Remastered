#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import phoenix5

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.leftDriveLeader = phoenix5.TalonSRX(6)
        self.leftDriveFront = phoenix5.TalonSRX(5)
        self.leftDriveBack = phoenix5.TalonSRX(4)

        self.rightDriveLeader = phoenix5.TalonSRX(1)
        self.rightDriveFront = phoenix5.TalonSRX(2)
        self.rightDriveBack = phoenix5.TalonSRX(3)

        self.leftDriveFront.follow(self.leftDriveLeader)
        self.leftDriveBack.follow(self.leftDriveLeader)

        self.rightDriveFront.follow(self.rightDriveLeader)
        self.rightDriveBack.follow(self.rightDriveLeader)

        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

        self.rightDriveLeader.setInverted(True)

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
            self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
        else:
            self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.0)
            self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
        self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)

if __name__ == "__main__":
    wpilib.run(MyRobot)