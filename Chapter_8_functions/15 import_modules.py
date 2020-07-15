import math as maths    # import maths module


def area_of_a_circle(radius):
    """finds area of a circle, argument is radius"""
    area = round(pi * radius, 2)
    return area

pi = maths.pi

# call function, which will give me the area of a circle
circle_0 = area_of_a_circle(50)
print(circle_0)
