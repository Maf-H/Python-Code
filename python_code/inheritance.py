#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

import math


class Point:
    """Base class point with attribute of x, y """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Point):
    """Circle is a sub-class of point with attributes of x, y, radius"""

    def __init__(self, x=0, y=0, radius=0.0):
        Point.__init__(self, x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# demonstrate class relationships with built-in function issubclass
print("Point is sub-class of Circle: ", issubclass(Point, Circle))
print("Circle is a sub-class of Point: ", issubclass(Circle, Point))
print()

# if it is derived class, tells it's class
print("medods and attributes of Point: ", Point.__bases__)
print("medods and attributes of Circle: ", Circle.__bases__)
print()

point = Point(10, 20)
circle = Circle(10, 20, 15)

print("members (attributes) of a point: ", point.__dict__)
print("members (attributes) of a circle: ", circle.__dict__)
print()

# demonstrate object relationship with built-in function isinstance syntax == isinstance(object, typre)
print("point is an instance of point: ", isinstance(point, Point))
print("Point is an instance of Circle: ", isinstance(circle, Point))
print("Circle is an instance of Point: ", isinstance(point, Circle))
print()

print("The area of a circle = %.2f" % circle.area())
print()
