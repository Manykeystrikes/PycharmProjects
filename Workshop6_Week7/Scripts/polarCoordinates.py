#convert cartesian coordinate to polar coordinates
#x = r * cos(angle)
#y = r * sin(angle)

from math import sin, cos
def polarToCartesian(r, theta):
    """Convert the polar coordinates (r, theta)
    to Cartesian coordinates (x, y)

    r is the radius
    theta is the angle"""
    return (r*cos(theta), r*sin(theta))

print(polarToCartesian(13, 25))