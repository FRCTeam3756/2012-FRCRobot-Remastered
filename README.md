# 2012 FRC Robot Code Remastered

## Description

This robotpy project controls a six motor tank drivetrain, an over the bumper intake mechanism and an elevated shooter.

## Prequisites

### On Robot
- roboRIO Version 2025_v2.0
    - Update a roboRIO 1 through using the roboRIO Imaging Tool
    - Update a roboRIO 2 through flashing the microSD card


## Installation

### Connected to the Internet:

Clone this codebase from GitHub:
```bash
git clone https://github.com/FRCTeam3756/2012-FRCRobot-Remastered.git
cd 2012-FRCRobot-Remastered
```

### Connected to the Robot:

Download and sync libraries:

```bash
python -m robotpy sync
```

Deploy the codebase to the robot:

```bash
python -m robotpy deploy --skip-tests
```

## Running the Robot

- Verify the controller is connected to the computer and initialized to port 0.
- Using the FRC Driver Station, enable the robot to your desired mode (tele-op, autonomous, etc.).
- Drive to your heart's content!

## Authors
- Gabe Lynch
- Nicholas Nyhoff