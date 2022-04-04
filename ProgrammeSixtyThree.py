import math
def robotic_movement():
    directions = 0
    n = int(input("Enter the number of commands: \n"))
    for i in range(0,n):
        command = input("Enter the command: \n")
        measurement = command[-1]
        directions += int(measurement)
    return math.floor(directions)
print(robotic_movement())