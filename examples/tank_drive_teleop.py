from .util.drive import TankDrive
from arc.hardware import *
from arc import *

# You are REQUIRED to have a main() function in your program.
# and you MUST NOT call it yourself.
@Teleop("Tank Drive example")
def main(op: Op):
    op.log("Starting...")

    # Create a tank drive with the left and right motors.
    leftMotor  = op.hardwareMap[DcMotor]("motor0")
    rightMotor = op.hardwareMap[DcMotor]("motor1")
    drive = TankDrive(leftMotor, rightMotor)

    # While the opmode is running...
    while op.running:
        # Get the left and right stick values.
        l = op.gamepad.left_stick.y
        r = op.gamepad.right_stick.y
        movement = TankDrive.calc(l, r)
        op.debug("Left: ", l, "Right: ", r)

        # Drive the robot with the left and right sticks.
        drive.move(movement)

    op.log("Done!")
    return OK
