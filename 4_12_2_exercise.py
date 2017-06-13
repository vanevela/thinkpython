#flowers
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

from math import pi

def polyline(t,n,length, angle):
    """draw n line segments

    t: Turtle
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t,length)
        lt(t,angle)

def arc(t,r,angle):
    """draws an arc with the given radius and angle
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = (2 * pi * r * abs(angle))/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t,r,angle):
    """draws a petal using two arcs
    t: Turtle
    r: radius
    angle: angle that subtended the arcs
    """
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,r,n,angle):
    """draw a flower whit n petals
    t: Turtle
    r: radius
    n: number of petals
    angle: angle that subtended the arcs
    """
    for i in range(n):
        petal(t,r,angle)
        lt(t,360.0/n)
def moved(t,length):
    """leaves turtle (t) forwad (length) units without leaving a trail.
    """
    pu(t)
    fd(t,length)
    pd(t)

moved(bob,-100)
flower(bob,60.0,7,60.0)

moved(bob,100)
flower(bob,40.0,10,80.0)

moved(bob,100)
flower(bob,140.0,20,20.0)

die(bob)

wait_for_user()
