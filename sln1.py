import re

def partone(lst):
    values = []
    for item in lst:
        nums = []
        for ch in item:
            if ch.isdigit():
                nums.append(ch)
        values.append(int(nums[0] + nums[-1]))
    return sum(values)

def parttwo(lst):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    values = []

    for item in lst:
        nums = []
        newitem = item

        to_insert = []
        # this is so inefficient but i'm [redacted] so
        for d in digits:
            idx_list = [m.start() for m in re.finditer(d, item)]
            for idx in idx_list:
                to_insert.append((idx, str(digits.index(d)+1)))
        to_insert = sorted(to_insert)

        for i in to_insert:
            newitem = newitem[:i[0]+to_insert.index(i)] + i[1]+ newitem[i[0]+to_insert.index(i):]

        for ch in newitem:
            if ch.isdigit():
                nums.append(ch)
        values.append(int(nums[0]+nums[-1]))
    return sum(values)


file1 = open("input.txt", "r")

lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
