"""line_following controller."""
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

# initialize ground sensors
gs = []
for i in range(3):
    gs.append(robot.getDevice(f'gs{i}'))
    gs[-1].enable(timestep)



while robot.step(timestep) != -1:

    # read ground sensors
    gs_values = []
    for gs_val in gs:
        gs_values.append(gs_val.getValue())

    

    

