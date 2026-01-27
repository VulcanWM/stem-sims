import random

def coin_toss(n=10000):
    count = {"H": 0, "T": 0}
    for i in range(10000):
        toss = random.choice(list(count.keys()))
        count[toss] += 1
    return count