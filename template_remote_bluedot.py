# Think Create Learn
# www.thinkcreatelearn.co.uk
#
# ROSI template for remote control using Bluedot
#


# ======================================================================================================
# Imports
# ======================================================================================================
from rosi import RosiRobot, RosiException 
from bluedot import BlueDot


# ======================================================================================================
# Global variables
# ======================================================================================================

# Variable to indicate if we are still running
running = True

# ======================================================================================================
# Functions
# ======================================================================================================

# ------------------------------------------------------------------------------------------------------
# Global for Blue Dot.  Is called when we move our finger on the blue dot.
# ------------------------------------------------------------------------------------------------------
def bd_move(pos):
    print("move")

# ------------------------------------------------------------------------------------------------------
# Global for Blue Dot.  Is called when we lift our finger from the blue dot
# ------------------------------------------------------------------------------------------------------
def bd_stop():
    robot.stop()

# ------------------------------------------------------------------------------------------------------
# Global for Blue Dot.  Placeholder for any action we want to take on a double-press on the blue dot.
# ------------------------------------------------------------------------------------------------------
def bd_double_press():
    #robot.stop()
    pass



# ======================================================================================================
# Main program
# ======================================================================================================
try:
    robot = RosiRobot()

    robot.start()

    bd = BlueDot()
    bd.when_pressed = bd_move
    bd.when_moved = bd_move
    bd.when_released = bd_stop 
    bd.when_double_pressed = bd_double_press

    while running:
        robot.wait(0.1)


except RosiException as e:
    print(e.value)

