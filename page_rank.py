import random

def page_rank(outboundLinks, firstNum, lastNum, dampingFactor=0.85, n=10000):
    currentNum = random.randint(firstNum, lastNum)
    count = {currentNum: 1}

    for i in range(n):
        damp = random.randint(1,100)
        if damp > dampingFactor * 100:
            currentNum = random.randint(firstNum, lastNum)
            count[currentNum] = count.get(currentNum, 0) + 1
        else:
            currentNum = random.choice(outboundLinks[currentNum])
            count[currentNum] = count.get(currentNum, 0) + 1
    for key in count.keys():
        count[key] = round(count[key] / n * 100, 3)
    return count


outboundLinks = {1: [2, 3], 2: [1], 3: [1], 4: [5, 6], 5: [4], 6: [4]}
count = page_rank(outboundLinks, 1, 6)
print(count)