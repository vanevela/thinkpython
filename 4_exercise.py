#A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and
#calls it twice:
#Type this example into a script and test it.
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'
#test
do_twice(print_spam)
#Modify do_twice so that it takes two arguments, a function object and a value,
#and calls the function twice, passing the value as an argument.
def do_twice(f,v):
    f(v)
    f(v)
#test
def print_name(name):
    print name
do_twice(print_name,'vane')
#Write a more general version of print_spam, called print_twice, that takes
#a string as a parameter and prints it twice.
def print_twice(v):
    print v
    print v
#test
do_twice(print_twice,'caro')
#Define a new function called do_four that takes a function object and a value
#and calls the function four times, passing the value as a parameter.
# There should be only two statements in the body of this function, not four.
def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)
#test
do_four(print_name,'emma'
