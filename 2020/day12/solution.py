from abc import abstractmethod
from enum import Enum

with open("input.txt") as file:
    commands = list(map(lambda x: (x[0], int(x[1:])), file.read().splitlines()))

class Direction(Enum):
    north = 0 
    east = 1
    south = 2
    west = 3

    def turn_left(self, degrees):
        dir = (self.value - degrees / 90) % 4
        return list(Direction)[int(dir)]

    def turn_right(self, degrees):
        dir = (self.value + degrees / 90) % 4
        return list(Direction)[int(dir)]

    def from_str(name):
        names = {"N": Direction.north, "E": Direction.east, "S": Direction.south, "W": Direction.west }
        return names[name]


class Movable:

    def __init__(self) -> None:
        pass

    def move(self, direction, amount):
        if direction == Direction.east:
            self.pos_x += amount
        elif direction == Direction.west:
            self.pos_x -= amount
        elif direction == Direction.north:
            self.pos_y += amount
        elif direction == Direction.south:
            self.pos_y -= amount
        else:
            raise ValueError

    @abstractmethod
    def print_loc(self):
        pass

    @abstractmethod
    def forward(self, amount):
        pass

    @abstractmethod
    def rotate(self, direction, degrees):
        pass

class Ship(Movable):

    def __init__(self) -> None:
        self.direction = Direction.east
        self.pos_x, self.pos_y = 0,0 
        super().__init__()
    
    def print_loc(self):
        print(f"Ship position ({self.pos_x}, {self.pos_y}), facing {self.direction.name}")

    def forward(self, amount):
        self.move(self.direction, amount)
    
    def rotate(self, direction, degrees):
        if direction == "L":
            self.direction = self.direction.turn_left(degrees)
        elif direction == "R":
            self.direction = self.direction.turn_right(degrees)
        else:
            raise ValueError    
           
class Waypoint(Movable):

    def __init__(self, ship: Ship):
        self.ship = ship
        self.pos_x, self.pos_y = 10, 1
        super().__init__()

    def print_loc(self):
        print(f"Waypoint position ({self.pos_x}, {self.pos_y})")
        self.ship.print_loc()
        print("_____________")
    
    def forward(self, amount):
        self.ship.pos_x += amount * self.pos_x
        self.ship.pos_y += amount * self.pos_y

    def rotate(self, direction, degrees):
        times = int(degrees / 90)

        if direction == "L":
            times = 4 - times
            
        for _ in range(0, times):
            self.pos_x, self.pos_y = self.pos_y, -self.pos_x

def execute(movable: Movable, debug: bool):
    for command, amount in commands:
        if debug:
            movable.print_loc()

        if command in ["N", "S", "E", "W"]:
            movable.move(Direction.from_str(command), amount)
        elif command in ["R", "L"]:
            movable.rotate(command, amount)
        elif command == "F":
            movable.forward(amount)
        else:
            raise ValueError(command, amount)


ship = Ship()
execute(ship, False)
print(f"Answer: {abs(ship.pos_x) + abs(ship.pos_y)}")


waypoint = Waypoint(Ship())
execute(waypoint, False)
print(f"Answer: {abs(waypoint.ship.pos_x) + abs(waypoint.ship.pos_y)}")

