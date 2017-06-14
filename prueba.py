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

def trian(t,length):
    """draws a trian with n sides

    t: Turtle
    n: number of line segments
    length: length of each segment
    """
    n=3
    angle = 360.0/n
    polyline(t, n, length, angle)
    
trian(bob,50)
wait_for_user()
