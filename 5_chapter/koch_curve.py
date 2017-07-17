#exercise 5, chapter 5.
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

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
##
def Make_fractal():
    length = float(raw_input("type a starting legth >= 3\n"))
    n = int(raw_input("tipe the number of recursions >=3\n"))
    return draw(bob,length,n)


Make_fractal()

wait_for_user()
