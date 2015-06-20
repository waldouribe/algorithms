import math

def my_max(x, y):
    return (x+y + my_abs(x-y))/2

def my_abs(x):
    return math.sqrt(x*x)
