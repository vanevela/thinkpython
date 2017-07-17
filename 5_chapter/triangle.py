def is_triangle(a,b,c):
    if a+b < c or a+c < b or b+c <a:
        print "no, is not a triangle"
    else:
        print "yes, is a triangle"
is_triangle(3,3,3)
###
def prompts():
    a = int(raw_input('type a value for a\n'))
    b = int(raw_input('type a value for b\n'))
    c = int(raw_input('type a value for c\n'))
    return is_triangle(a,b,c)
prompts()
