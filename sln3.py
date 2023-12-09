def get(arr, i, j):
    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
        # corners
        new_neighbors = []
        if i != 0:
            new_neighbors.append(arr[i - 1][j])  # top neighbor
        if j != len(arr[i]) - 1:
            new_neighbors.append(arr[i][j + 1])  # right neighbor
        if i != len(arr) - 1:
            new_neighbors.append(arr[i + 1][j])  # bottom neighbor
        if j != 0:
            new_neighbors.append(arr[i][j - 1])  # left neighbor

    else:
        # add neighbors
        new_neighbors = [
            arr[i - 1][j],  # top neighbor
            arr[i][j + 1],  # right neighbor
            arr[i + 1][j],  # bottom neighbor
            arr[i][j - 1]   # left neighbor
        ]
    return new_neighbors

def partone(lst):
    sym = ["*","#","+","$"]
    total = 0
    for i in range(0, len(lst)):
        num = ""
        nbr = []
        for j in range(0, len(lst[i])):
            if lst[i][j].isdigit():
                num += lst[i][j]
                nbr += (get(lst,i,j))
                print(nbr)
            elif lst[i][j] == ".":
                if any(sym) in nbr:
                    print("fuck")
                    total += int(num)
                num = ""
                nbr = []
                pass
            else:
                #is symbol?
                pass
        #print(num)

    return total

def parttwo(lst):
    return 0


file1 = open("./test.txt","r")
lst = [line.strip() for line in file1.readlines()]
print(partone(lst))
print(parttwo(lst))
