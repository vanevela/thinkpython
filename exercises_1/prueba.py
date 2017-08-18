from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

import math

def isosceles(t, r, angle):
    """Draws an isosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t,2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)

def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)


size = 40
draw_pie(bob,5,size)
draw_pie(bob,6,size)
draw_pie(bob,7,size)

wait_for_user()
