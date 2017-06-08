#1.Write a function called square that takes a parameter
#named t, which is a turtle. It should use the turtle to draw a square.
#Write a function call that passes bob as an argument to
#square, and then run the program again.
"""
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)

square(bob)

#Add another parameter, named length, to square. Modify
##the body so length of the sides is length, and then modify
#the function call to provide a second argument. Run the
#program again. Test your program with a range of values for length.
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

square(bob,200)
wait_for_user()
"""
#The functions lt and rt make 90-degree turns by default,
#but you can provide a second argument that specifies the
#number of degrees. For example, lt(bob, 45) turns bob
#45 degrees to the left.
#Make a copy of square and change the name to polygon.
#Add another parameter named n and modify the body so it
#draws an n-sided regular polygon. Hint: The exterior angles
#of an n-sided regular polygon are 360/n degrees.
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)
#polygon(bob,n=30,length=10) #keyword argument,this syntax makes the program more readable
#wait_for_user()

"""
def circle(t,r):
    from math import pi
    circumference = 2*pi*r
    n=50
    length=circumference/n
    polygon(t,n,length)
circle(bob,15)
wait_for_user()
"""
#circle for book
from math import pi
def circle(t,r):
    circumference = 2 * pi * r
    n = int(circumference/3) + 1
    length = circumference /n
    polygon(t, n, length)
circle(bob,15)
wait_for_user()
#Make a more general version of circle called arc that takes an additional parameter angle,
#which determines what fraction of a circle to draw. angle is in units of degrees,
#so when angle=360, arc should draw a complete circle.
