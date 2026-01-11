import random

def page_rank(outbound_links, first_num, last_num, damping_factor=0.85, n=10000):
    current_num = random.randint(first_num, last_num)
    count = {current_num: 1}

    for i in range(n):
        damp = random.randint(1,100)
        if damp > damping_factor * 100:
            current_num = random.randint(first_num, last_num)
            count[current_num] = count.get(current_num, 0) + 1
        else:
            current_num = random.choice(outbound_links[current_num])
            count[current_num] = count.get(current_num, 0) + 1
    for key in count.keys():
        count[key] = round(count[key] / n * 100, 3)
    return count