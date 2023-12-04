import re

def partone(lst):
    total = 0
    for ticket in lst:
        first = ticket.split(":")
        cardid = first[0]
        nums = first[1].split("|")
        mine = [int(num.strip()) for num in nums[1].split()]
        wins = [int(num.strip()) for num in nums[0].split()]
        mywins = set(mine) & set(wins)
        if len(mywins) > 0:
            total += 2**(len(mywins)-1)
    return total

def parttwo(lst):
    thing = {}
    for i in range(0, len(lst)):
        thing[i+1] = 1
    for ticket in lst:
        first = ticket.split(":")
        cardid = int(re.search(r'\d+', first[0]).group())
        nums = first[1].split("|")
        mine = [int(num.strip()) for num in nums[1].split()]
        wins = [int(num.strip()) for num in nums[0].split()]
        mywins = set(mine) & set(wins)

        for i in range(cardid+1, cardid+1+len(mywins)):
            thing[i] += thing[cardid]
    return sum(thing.values())

file1 = open("input.txt", "r")
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
