from sys import argv
opposites_hash = {'N': 'S','S': 'N','E': 'W','W': 'E'}

def main():
    if len(argv) != 2:
        raise Exception("ERROR: We want 1. the function file and 2. the input file")

    file_path = argv[1]
    f = open(file_path, 'r')
    lines_taken_in = f.readlines()

    for each_line in lines_taken_in:
        tokens = each_line.split()

        if tokens[0] == "SOURCE":
            source_x = int(tokens[1])
            source_y = int(tokens[2])
            facing = tokens[3]

        elif tokens[0] == "DESTINATION":
            destination_x = int(tokens[1])
            destination_y = int(tokens[2])

        else:
            print ("POWER",(200-calculate_cost(source_x, source_y, facing, destination_x, destination_y)))

def calculate_cost(starting_x, starting_y, starting_direction, ending_x, ending_y):
    overall_direction = ""
    if ending_y - starting_y >0:
        overall_direction += "N"
    elif ending_y - starting_y <0:
        overall_direction += "S"
    else:
        overall_direction += "Z"

    if ending_x - starting_x >0:
        overall_direction += "E"
    elif ending_y - starting_y <0:
        overall_direction += "W"
    else:
        overall_direction += "Z"

    turns = 0

    if starting_direction == "N" or starting_direction == "S":
        if overall_direction[0] == opposites_hash[starting_direction]:
            turns = 2
        elif overall_direction[0] == "Z":
            turns == 1
        else:
            if overall_direction[1] == "Z":
                turns = 0
            else:
                turns = 1

    else:
        if starting_direction == "W" or starting_direction == "E":
            if overall_direction[1] == opposites_hash[starting_direction]:
                turns = 2
            elif overall_direction[1] == "Z":
                turns == 1
            else:
                if overall_direction[0] == "Z":
                    turns = 0
                else:
                    turns = 1

    return (turns*5) + (10*(abs(ending_y-starting_y)+abs(ending_x-starting_x)))

if __name__ == "__main__":
    main()




    """
    There is an expectation that the user:
    1. will start off in the Command Line
    2. will be in the folder that is housing this
    3. the user will type:

            python -m geektrust sample_input/input1.txt

    4.

    """