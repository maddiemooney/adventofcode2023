
def get_fit(lst):
    diffs = [p2 - p1 for p1,p2 in zip(lst,lst[1:])]
    if lst:
        return lst[-1] +  get_fit(diffs)
    else:
        return 0

def partone(lst):
    result = 0
    for eqn in lst:
        result += get_fit(eqn)
    return result
    
def parttwo(lst):
    result = 0
    for eqn in lst:
        eqn.reverse()
        result += get_fit(eqn)
    return result
            

file1 = open("./input.txt","r")
lst = [list(map(int,line.split())) for line in file1.readlines()]
print(partone(lst))
print(parttwo(lst))
