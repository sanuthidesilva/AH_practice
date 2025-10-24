# creare a program that produces a shape
from shape import Circle
from shape import Box
import math

C1 = Circle(10, 2, "pink", (5, 3))
print(C1)

C1.change_colour("red")
print(C1)

newArea = C1.area()
print(newArea)

r1 = Box(2, 2, 2, "pink", (5, 3))
print(r1)

R_area = r1.areaRec()
print(R_area)
