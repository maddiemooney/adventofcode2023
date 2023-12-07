from operator import itemgetter
from collections import Counter

def run(lst, partone):

    five_kind = []
    four_kind = []
    full_house = []
    three_kind = []
    two_pair = []
    one_pair = []
    high = []

    bids_dict = {}

    for idx, hand in enumerate(lst):
        temp = hand.split(" ")
        cards = temp[0]
        bid = int(temp[1])

        bids_dict[cards] = bid

        if "J" in cards and not partone:
            Jcount = cards.count("J")
            if Jcount == 5 or Jcount == 4:
                five_kind.append(cards)
            elif Jcount == 3:
                freq_dict = {}
                for c in cards:
                    freq_dict[c] = freq_dict.setdefault(c,0)+1
                if sorted(list(freq_dict.values())) == [2,3]:
                    five_kind.append(cards)
                else:
                    four_kind.append(cards)
            elif Jcount == 2:
                freq_dict = {}
                for c in cards:
                    freq_dict[c] = freq_dict.setdefault(c,0)+1
                if sorted(list(freq_dict.values())) == [2,3]:
                    five_kind.append(cards)
                elif sorted(list(freq_dict.values())) == [1,2,2]:
                    four_kind.append(cards)
                else:
                    three_kind.append(cards)
            else:
                freq_dict = {}
                for c in cards:
                    freq_dict[c] = freq_dict.setdefault(c,0)+1
                thing = sorted(list(freq_dict.values()))
                if thing == [1,4]:
                    five_kind.append(cards)
                elif thing == [1,1,3]:
                    four_kind.append(cards)
                elif thing == [1,2,2]:
                    full_house.append(cards)
                elif thing == [1,1,1,2]:
                    three_kind.append(cards)
                elif thing == [1,1,1,1,1]:
                    one_pair.append(cards)
                else:
                    print(thing)

        else:

            if all(ch == cards[0] for ch in cards):
                five_kind.append(cards)
            elif any(v==4 for k,v in Counter(ch for ch in cards).items()):
                four_kind.append(cards)
            elif any(v==3 for k,v in Counter(ch for ch in cards).items()):
                freq_dict = {}
                for ch in cards:
                    freq_dict[ch] = freq_dict.setdefault(ch, 0) + 1
                if sorted(list(freq_dict.values())) == [2, 3]:
                    full_house.append(cards)
                else:
                    three_kind.append(cards)
            elif any(v==2 for k,v in Counter(ch for ch in cards).items()):
                freq_dict = {}
                for ch in cards:
                    freq_dict[ch] = freq_dict.setdefault(ch,0)+1
                if sorted(list(freq_dict.values())) == [1,2,2]:
                    two_pair.append(cards)
                else:
                    one_pair.append(cards)
            else:
                high.append(cards)

    if partone:
        ranks = "23456789TJQKA"
    else:
        ranks = "J23456789TQKA"
    total = 0
    final_hands = []

    final_hands+=sorted(high, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(one_pair, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(two_pair, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(three_kind, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(full_house, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(four_kind, key=lambda word: [ranks.index(c) for c in word])
    final_hands+=sorted(five_kind, key=lambda word: [ranks.index(c) for c in word])

    for idx, hand in enumerate(final_hands):
        total += ((idx+1) * bids_dict[hand])

    return total

file1 = open("input.txt","r")
lst = [line.strip() for line in file1.readlines()]
print(run(lst,True))
print(run(lst,False))
