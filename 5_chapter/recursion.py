"""
#recursion
def countdown(n):
    if n <= 0:
        print 'Blastoff'
    else:
        print n
        countdown(n-1)
countdown(3)
"""
#

def print_n(s,n):
    if n <= 0:
        return
    print s
    print_n(s,n-1)
print_n('no',1)

#function that takes a function object and number as arguments
def song():
    print 'hola como estas'
def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)
do_n(song,3)
