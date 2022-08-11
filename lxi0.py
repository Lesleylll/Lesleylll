from operator import mul
def square(x) :
    return mul(x, x)
square(square(3))
print(square(square(3)))
