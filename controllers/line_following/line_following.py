"""line_following controller."""
from controller import Robot
import numpy as np

# instantiate robot
robot = Robot()
# get timestep
timestep = int(robot.getBasicTimeStep())
delta_t = timestep / 1000.0

# handle to e-puck wheels
motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')

# set to velocity mode
motor_left.setPosition(float('Inf'))
motor_right.setPosition(float('Inf'))
# zero-out velocity for consistency
motor_left.setVelocity(0)
motor_right.setVelocity(0)



# initialize ground sensors
gs = []
for i in range(3):
    gs.append(robot.getDevice(f'gs{i}'))
    gs[-1].enable(timestep)

MAX_SPEED = np.pi / 2

# wheel velocities
phildot = 0
phirdot = 0

# odometry
r = 0.0201
d = 0.052
delta_x = 0
delta_w = 0

while robot.step(timestep) != -1:
    # read ground sensors
    gs_values = []
    for gs_val in gs:
        gs_values.append(gs_val.getValue())

    # print(gs_values)

    # go straight
    if gs_values[0] > 500 and gs_values[1] < 350 and gs_values[2] > 500:
        phildot = MAX_SPEED
        phirdot = MAX_SPEED
    # if left sensor is hitting the line, turn left
    elif gs_values[0] < 350:
        phildot = MAX_SPEED * -0.1
        phirdot = MAX_SPEED * 0.25
    # if right sensor is hitting the line, turn right
    elif gs_values[2] < 350:
        phildot = MAX_SPEED * 0.25
        phirdot = MAX_SPEED * -0.1

    # perform odometry
    delta_x += r * delta_t * (phildot + phirdot) / 2.0
    delta_w += r * delta_t * (phirdot - phildot) / d

    print (delta_x, delta_w)

    # set actuator
    motor_left.setVelocity(phildot)
    motor_right.setVelocity(phirdot)

    

    

