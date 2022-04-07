import math
#Function to track the directions and distance covered
def robotic_movement():
    directions = 0
    #List of all directions that are considered valid
    valid_directions = ["UP", "DOWN", "RIGHT", "LEFT"]
    try:
        n = int(input("Enter the number of commands: \n"))

        for i in range(0,n):
            command = input("Enter the command: \n")
            #Spliting the direction and distance
            valid_input = command.split(" ")
            if valid_input[0] in valid_directions:
                measurement = command[-1]
                #Adding up all the distances that have been travelled
                directions += int(measurement)
                return math.floor(directions)
            else:
                return "Invalid Instruction\n"

    except:
        return "Invalid Input"


print(robotic_movement())