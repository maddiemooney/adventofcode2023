import re
from itertools import chain

def partone(lst):
    # destination range start, source range start, range length
    # all other numbers are the same except for
    # source[srs] -> source[srs+rl] maps to destination[drs] -> destination[drs+rl]

    sections = []
    temp = []
    for item in lst:
        if item == '':
            sections.append(temp)
            temp = []
        else:
            if "map" not in item:
                if "seeds" not in item:
                    temp.append(list(map(int, item.split(" "))))
                else:
                    temp.append(item) # do more parsing here
    sections.append(temp)

    seeds = []
    ranges = []
    for sec in sections:
        if "seeds" in sec[0]:
            seeds = list(map(int, re.findall(r'\d+', sec[0])))
            #print(seeds)
        else:
            ranges_sec = []
            for x in sec:
                dest_range = (x[0], x[0]+x[2])
                source_range = (x[1], x[1]+x[2])
                ranges_sec.append([source_range, dest_range])
            ranges.append(ranges_sec)

    # f word
    final_seeds = []
    for seed in seeds:
        final = seed
        for sec in ranges:
            for rng in sec:
                #print(str(rng[0][0]) + "-" + str(rng[0][1]))
                if rng[0][0] < final < rng[0][1]:
                    #print("seed "+str(final)+" in range "+str(rng[0][0])+" "+str(rng[0][1]))
                    seed_offset = final - rng[0][0]
                    final = rng[1][0] + seed_offset
                    break
        #print("---")
        final_seeds.append(final)
    #print(final_seeds)
    return min(final_seeds)

def parttwo(lst):
    sections = []
    temp = []
    for item in lst:
        if item == '':
            sections.append(temp)
            temp = []
        else:
            if "map" not in item:
                if "seeds" not in item:
                    temp.append(list(map(int, item.split(" "))))
                else:
                    temp.append(item)
    sections.append(temp)

    seeds = []
    ranges = []
    for sec in sections:
        if "seeds" in sec[0]:
            nums = list(map(int, re.findall(r'\d+', sec[0])))
            seeds = chain(range(nums[0],nums[0]+nums[1]), range(nums[2],nums[2]+nums[3]))
        else:
            ranges_sec = []
            for x in sec:
                dest_range = (x[0],x[0]+x[2])
                source_range = (x[1],x[1]+x[2])
                ranges_sec.append([source_range, dest_range])
            ranges.append(ranges_sec)

    final_seeds = []
    for seed in seeds:
        final = seed
        for sec in ranges:
            for rng in sec:
                if rng[0][0] < final < rng[0][1]:
                    seed_offset = final - rng[0][0]
                    final = rng[1][0] + seed_offset
                    break
        final_seeds.append(final)

    return min(final_seeds)

file1 = open("test.txt", "r")
lst = [line.strip() for line in file1.readlines()]
print(partone(lst))
print(parttwo(lst))
