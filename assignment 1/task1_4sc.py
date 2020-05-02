'''4.
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3'''

import math

pi=math.pi
diameter=12
radius=diameter/2

volume=(4/3)*pi*(radius**3)
print("Volume of the sphere is:",round(volume,2))
