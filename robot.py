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
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
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
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
            self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
        else:
            self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.0)
            self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.0)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.leftDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)
        self.rightDriveLeader.set(phoenix5.TalonSRXControlMode.MotionMagic, 0.5)

if __name__ == "__main__":
    wpilib.run(MyRobot)