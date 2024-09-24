"""
Author : Carter Wells
Student Number: 756118
Revison date : 24 September 2024
Program : Three-Part Python Output with Math
Description : A program that computes the area of a rectangle, area of circle,
    surface area and volume of a cylinder, and the period of a pendulum
VARIABLE DICTIONARY :
    rect_length (float) = length of the rectangle (user input)
    rect_width (float) = width of the rectangle (user input)
    rect_area(float) = result of the area forumla
    circ_radius(float) = radius of the circle (user input)
    circ_area(float) = result of the area formula
    cyli_height(float) = height of the cylinder (user input)
    cyli_radius(float) = radius of the cylinder (user input)
    cyli_volume(float) = result of the volume formula
    cyli_surface_area(float) = result of the surface area formula
    pend_length(float) = length of the pendulum (user input)
    pend_gravity(float) = the value of gravity
    pend_period(float) = result of the period formula
"""

import math

#Area of Rectangle
# Asks the user for length of rectangle and will be stored as type float
rect_length: float = float(input("Enter the length of the rectangle: "))
# Asks the user for width of rectangle and will be stored as type float
rect_width: float = float(input("Enter the width of the rectangle: "))
# Calcualtes area and stores result as type float
rect_area: float = rect_length * rect_width
# Prints the area of the rectangle to 2 decimal places
print("The area of the rectangle is %.2f units squared \n" % rect_area)

# Area of circle
# Asks the user for radius of circle and will be stored as type float
circ_radius: float = float(input("Enter the radius of the circle: "))
# Calcualtes area and stores result as type float
circ_area: float = math.pi * math.pow(circ_radius, 2)
# Prints the area of the circle to 2 decimal places
print("The area of the circle is %.2f units squared \n" % circ_area)

# Surface area and volume of cylinder
# Asks the user for height of cylinder and will be stored as type float
cyli_height: float = float(input("Enter the height of the cylinder: "))
# Asks the user for radius of cylinder and will be stored as type float
cyli_radius: float = float(input("Enter the radius of the cylinder: "))
# Calcualtes volume and stores result as type float
cyli_volume: float = math.pi * math.pow(cyli_radius, 2) * cyli_height
# Calcualtes surface area and stores result as type float
cyli_surface_area: float = (2 * math.pi * cyli_radius * cyli_height) + (2 * math.pi * math.pow(cyli_radius, 2))
# Prints the surface area and volume of the cylinder to 2 decimal places
print("The surface area is %.2f units squared and volume is %.2f units cubed \n" % (cyli_surface_area, cyli_volume))

# Period of pendulum
# Asks the user for length of pendulum and will be stored as type float
pend_length: float = float(input("Enter the length of the pendulum (meters): "))
# The value of gravity stored as type float
pend_gravity: float = 9.8
# Calcualtes period and stores result as type float
pend_period: float = 2 * math.pi * (math.sqrt(pend_length/pend_gravity))
print("The period of the pendulum is %.2f seconds \n" % pend_period)
# Prints the period of the pundulum to 2 decimal places