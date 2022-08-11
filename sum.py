"""Generalization."""

def identify(k) :
    return k


def cube(k) :
    return pow(k, 3)

def summation(n, term) :
    """Sum the first N terms of a sequence.
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n :
        total, k = total + term(k), k
    return total

def sum_naturals(n) :
    """Sum the first N natural numbers
    >>> sum_naturals(5）
     15
     """
    return summation(n, identity)

def sum_cubes(n) :
    """Sum the first N cubes of naturals.
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

from operator import mul
def pi_term(k) :
    return 8 / mul(4 * k - 3, 4* k - 1)
summation(1000000, pi_term)


