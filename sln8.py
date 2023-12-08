import re
import math

def partone(lst):

    instructions = []
    nodes = {}
    cur = "AAA"
    steps = 0

    for idx,node in enumerate(lst):
        if "(" not in node and node != "\n":
            instructions = [*node]
            lst.remove(node)
            for idx,i in enumerate(instructions):
                if i == "L":
                    instructions[idx] = 0
                else:
                    instructions[idx] = 1
        else:
            temp = node.split("=")
            base = temp[0].strip()
            elements = [re.sub('[^a-zA-Z]','',x) for x in temp[1].strip().split(",")]
            nodes[base] = elements

    while cur != "ZZZ":
        cur = nodes[cur][instructions[steps%len(instructions)]]
        steps += 1

    return steps

def parttwo(lst):
    instructions = []
    nodes = {}
    cur = []
    steps = 0
    for idx,node in enumerate(lst):
        if "(" not in node and node != "\n":
            instructions = [*node]
            lst.remove(node)
            for idx,i in enumerate(instructions):
                if i == "L":
                    instructions[idx] = 0
                else:
                    instructions[idx] = 1
        else:
            temp = node.split("=")
            base = temp[0].strip()
            elements = [re.sub('[^a-zA-Z]','',x) for x in temp[1].strip().split(",")]
            nodes[base]=elements

            if base[-1] == 'A':
                cur.append(base)
    slns = []
    for node in cur:
        while not node.endswith("Z"):
            node = nodes[node][instructions[steps%len(instructions)]]
            steps += 1
        slns.append(steps)
        steps = 0

    result = 1
    for x in slns:
        result = result*x//math.gcd(result,x)
    return result

file1 = open("input.txt","r")
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
