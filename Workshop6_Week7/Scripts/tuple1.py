# script: tuple1.py
# A function that returns a tuple

from math import sin, cos

def polarToRect(r, theta):
   """Convert the polar coordinates (r, theta (rad)) to
      rectangular coordinates (x, y)."""
   return (r * cos(theta), r * sin(theta)) 
