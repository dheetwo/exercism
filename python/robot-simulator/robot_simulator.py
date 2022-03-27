# Globals for the directions
# Change the values as you see fit
EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        while len(instructions) > 0:
            if instructions[0] == "A":
                self.advance()
            elif instructions[0] == "L":
                self.turn_left()
            elif instructions[0] == "R":
                self.turn_right()
            print(self.coordinates)
            instructions = instructions[1:]

    def advance(self):
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        elif self.direction == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == EAST:
            self.direction = NORTH
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST

    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()

