def partone(lst):
    races = []
    total = 1
    for idx, time in enumerate(lst[0].split()):
        if time.isdigit():
            races.append([int(time)])
    for idx, dst in enumerate(lst[1].split()):
        if dst.isdigit():
            races[idx-1].append(int(dst))

    for race in races:
        record = 0
        for i in range(0, race[0]+1):
            move_time = race[0]-i
            speed = i

            distance = move_time * speed
            if distance > race[1]:
                record += 1

        total *= record
        record = 0
    return total

def parttwo(lst):
    races = [49979494,263153213781851] #i'm not parsing this lol
    total = 1

    record = 0
    for i in range(0,races[0]+1):
        move_time = races[0]-i
        speed = i

        distance = move_time*speed
        if distance > races[1]:
            record += 1

    return record


file1 = open("input.txt","r")
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
