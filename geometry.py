# from distutils.core import setup
# setup(name='geometry',
#       version='1.0',
#       py_modules=['geometry'],
#       )

from math import sqrt
from math import pi as pi


def circle():
    r = float(input("Enter the radius of a circle: "))
    area = (pi * r * r)
    print (f"The area of the circle is {area}")

def hypotenuse():
	print("Input lengths of shorter triangle sides:")
	a = float(input("a: "))
	b = float(input("b: "))

	c = sqrt(a**2 + b**2)

	print (f"The area of the circle is {c}")

