# This program contains functions that evaluate formulas used in geometry.
#
# Emma Waldthausen
# August 31, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

# area of a parallelogram
def parallelogram_area(b, h):
    a = b * h
    return a

print(parallelogram_area(5, 6))

# area of a trapezoid
def trapezoid_area(c, b, h):
    a = ((c + b) / 2) * h
    return a

print(trapezoid_area(5, 3, 2))

# volume of a rectangular prism
def rectangular_p_volume(l, w, h):
    v = w * h * l
    return v

print(rectangular_p_volume(2, 4, 6))

# volume of a cone
def cone_volume(r, h):
    v = math.pi * r**2 *(h/3)
    return v

print(cone_volume(2, 4))

# volume of a sphere
def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v

print(sphere_volume(2))
    
# surface area of a rectangular prism
def rect_prism_surface_area(w, l, h):
    a = 2 * ((w * l) + (h * l) + (h * w))
    return a

print(rect_prism_surface_area(3, 2, 4))

# surface area of a sphere
def sphere_surface_area(r):
    a = 4 * math.pi * r**2
    return a

print(sphere_surface_area(2))

import Triangle

im = triangle.jpg("triangle")
im.show()
