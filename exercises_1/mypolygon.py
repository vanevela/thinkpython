#square
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
"""
fd(bob,100)
lt(bob)

fd(bob,100)
lt(bob)

fd(bob,100)
lt(bob)

fd(bob,100)

wait_for_user()

#example: For statements
for i in range(4):
    print 'Helo!'
"""
for i in range(4):
    fd(bob,100)
    lt(bob)
wait_for_user()
