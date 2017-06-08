#Write a function that draws a grid
plus = '+'
minus = '- '*4
pipe = '|'
spaces = ' '*8

def do_four(arg):
    print arg
    print arg
    print arg
    print arg

def do_plus_minus():
    line1= plus + minus + plus + minus + plus
    print line1

def do_pipe_space():
    line2= pipe + spaces + pipe + spaces + pipe
    do_four(line2)

def grid(f,t):
    f()
    t()
    f()
    t()
    f()


grid(do_plus_minus,do_pipe_space)
