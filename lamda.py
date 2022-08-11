"""lambda"""
def composel(f,g):
    def composed(x):
        return f(g(x))
    return composed
    #return lambda x: f(g(x))

def square(x):
    return x * x

def add_one(x):
    return x + 1

h = composel(square, add_one)
#h = composel(lambda x : x * x, lambda y : y + 1)
result = h(12) 
