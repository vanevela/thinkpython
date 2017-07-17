#exercise 6, chapter 5.
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()


def draw(t,length,n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t,length,n-1)
    rt(t, 2*angle)
    draw(t,length,n-1)
    lt(t, angle)
    bk(t, length*n)
draw(bob,9,3)
wait_for_user()
