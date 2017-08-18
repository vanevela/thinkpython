from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

import math
#archimedian spiral : r = a+b*tetha
def spiral(t,n,length=3,a=0.1,b=0.0002):
    theta = 0.0
    for i in range(n):
        fd(t,length)
        dtheta = 1/(a+b*theta)

        lt(t,dtheta)
        theta += dtheta
spiral(bob,n=1000)        
wait_for_user()
