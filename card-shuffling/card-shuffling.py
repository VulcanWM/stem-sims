import random
import math

def card_shuffle(n):
    total = 52

    probs = {}
    for i in range(0, total+1):
        prob = math.comb(total, i) * 0.5**total
        probs[i] = prob

    suits = ["H", "D", "C", "S"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
    for _ in range(n):
        left = random.choices(list(probs.keys()), weights=list(probs.values()), k=1)[0]
        right = total - left
        leftArr = deck[:left]
        rightArr = deck[left:]

        newDeck = []
        for _ in range(total):
            num = random.randint(1, left + right)
            if num > left:
                newDeck.append(rightArr[0])
                rightArr.pop(0)
                right -= 1
            else:
                newDeck.append(leftArr[0])
                leftArr.pop(0)
                left -= 1

        deck = newDeck
    return deck

def example():
    print(card_shuffle(10))

if __name__ == "__main__":
    example()