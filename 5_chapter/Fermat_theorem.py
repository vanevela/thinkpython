# no positive integers a,b,c such as: a^n + b^n = c^n
# for any values of n greater than 2
def check_fermat(a,b,c,n):
    if c**n==a**n+b**n and n > 2:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No,that doesn't work"
check_fermat(1,2,3,4)
#function that prompts the user to input values
#for a,b,c and n
def prompt():
    a = int(raw_input('type a value for a\n'))
    b = int(raw_input('type a value for b\n'))
    c = int(raw_input('type a value for c\n'))
    n = int(raw_input('type a value for n\n'))
    return check_fermat(a,b,c,n)
prompt()
