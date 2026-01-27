import math
import random

def random_walk(n=10000, l=1):
    x = [0]
    y = [0]
    for i in range(1, n+1):
        theta = 2 * math.pi * random.uniform(0, 1)
        dx = l * math.cos(theta)
        dy = l * math.sin(theta)
        x.append(x[i-1] + dx)
        y.append(y[i-1] + dy)
    return x, y