import re

def partone(lst):
	maxred = 12
	maxgreen = 13
	maxblue = 14
	total = 0
	for game in lst:
		ugh = game.split(":")
		gameid = re.sub("[^0-9]", "", ugh[0])
		#print(gameid)
		valid = True
		for pull in ugh[1].split(";"):
			blocks = pull.split(",")
			for block in blocks:
				#print(block)
				if "red" in block:
					if int(re.sub("[^0-9]","",block)) > maxred:
						valid = False
						break
				elif "green" in block:
					if int(re.sub("[^0-9]","",block)) > maxgreen:
						valid = False
						break
				elif "blue" in block:
					if int(re.sub("[^0-9]", "", block)) > maxblue:
						valid = False
						break
				else:
					print("unexpected")
		if valid:
			#print(gameid)
			total += int(gameid)					
	return total


def parttwo(lst):
	maxred = 0
	maxgreen = 0
	maxblue = 0
	total = 0
	for game in lst:
		maxred = 0
		maxgreen = 0
		maxblue = 0
		print("game")
		for pull in game.split(":")[1].split(";"):
			blocks = pull.split(",")
			for block in blocks:
				bnum = int(re.sub("[^0-9]","",block))
				print(block)
				if "red" in block:
					if bnum > maxred:
						maxred = bnum
				elif "green" in block:
					if bnum > maxgreen:
						maxgreen = bnum
				elif "blue" in block:
					if bnum > maxblue:
						maxblue = bnum
				else:
					print("unexpected")
		print(str(maxred) + " " + str(maxgreen) + " " + str(maxblue))
		total += maxred * maxgreen * maxblue
	return total

file1 = open("input.txt", "r")
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))

