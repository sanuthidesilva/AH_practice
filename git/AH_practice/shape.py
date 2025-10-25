# 1. create the super class/parent class which holds all the basic attributes required to create a shape
import math


class shape:
    def __init__(self, boarder_thickness, boarder_colour, location):
        self.boarder_thickness = boarder_thickness
        self.boarder_colour = boarder_colour
        self.location = location

    def __str__(self):  # YOU DON'T NEED TO PUT THE ARGUMENTS HERE AGAIN, BECAUSE ITS ALREADY INSIDE THE CLASS!! IT'LL ONLY CONFUSE THE PROGRAM WHICH WILL BE LOOKING FOR MORE ATTRIBUTES TO BE FILLED
        return f"Shape {self.boarder_thickness}, {self.boarder_colour}, {self.location}"

    # change the boarder colour
    def change_colour(self, colour):
        self.boarder_colour = colour

# 2. create a child class that inherits those attributes in addition


class Circle(shape):
    # The code will print 'Shape' Instead of 'Circle'
    def __init__(self, radius, boarder_thickness, boarder_colour, location):
        super().__init__(boarder_thickness, boarder_colour, location)
        self.radius = radius
    # Over-rides the inherited method (POLYMORPHISM)

    def __str__(self):
        return f"Circle {self.boarder_thickness}, {self.boarder_colour}, {self.location}"

# 3. add own attributes of the child class
    def area(self):
        return math.pi * self.radius ** 2


class Box(shape):
    def __init__(self, breath, lenght, boarder_thickness, boarder_colour, location):
        super().__init__(boarder_thickness, boarder_colour, location)
        self.breath = breath
        self.lenght = lenght

    def __str__(self):
        return f"Rectangle{self.boarder_thickness}, {self.boarder_colour}, {self.location}"

    def areaRec(self):
        return self.breath * self.lenght
