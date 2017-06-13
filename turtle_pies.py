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

def polygon(t,n,length):
    """draws a polygon with n sides

    t: Turtle
    n: number of line segments
    length: length of each segment
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def pie(t,n,length):
    """draw a pie whit n pieces
    t: Turtle
    r: radius
    n: number of pieces
    angle: angle that subtended the arcs
    """
    for i in range(n):
        polygon(t,n,length)
        lt(t,360.0/n)




pie(bob,6,60)
wait_for_user()
