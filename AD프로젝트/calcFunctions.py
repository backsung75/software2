import random

def roll():
    a = random.randint(1, 6) 
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    e = random.randint(1, 6)
    return [a, b, c, d, e]

def reroll(checkList, diceList):
    for i in range(5):
        if checkList[i].isChecked():
            diceList[i] = random.randint(1, 6)
    return diceList

def aces(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 1:
            value += 1
    return str(value)

def twos(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 2:
            value += 2
    return str(value)

def threes(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 3:
            value += 3
    return str(value)

def fours(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 4:
            value += 4
    return str(value)

def fives(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 5:
            value += 5
    return str(value)

def sixes(diceNumList):
    value = 0
    for i in diceNumList:
        if i == 6:
            value += 6
    return str(value)

def choice(diceNumList):
    value = sum(diceNumList)
    return str(value)

def tcard(diceNumList):
    value = 0
    for i in diceNumList:
        if diceNumList.count(i) == 3:
            value = sum(diceNumList)
            break
    return str(value)

def fcard(diceNumList):
    value = 0
    for i in diceNumList:
        if diceNumList.count(i) >= 4:
            value = sum(diceNumList)
            break
    return str(value)

def fhouse(diceNumList):
    value = 0
    diceNumList.sort()
    if (diceNumList[0] == diceNumList[1] and (diceNumList[2] == diceNumList[3] or diceNumList[2] == diceNumList[1]) and diceNumList[3] == diceNumList[4]):
        value = sum(diceNumList)
    return str(value)

def s_straight(diceNumList):
    value = 0
    diceNumList.sort()
    checkList = []
    for i in range(4):
        checkList.append(diceNumList[i+1] - diceNumList[i])
    if checkList.count(1) > 2:
        value = 30
    return str(value)

def l_straight(diceNumList):
    l_ = [int(i) for i in diceNumList]
    l_ = sorted(l_)
    ll_ = []
    lll_ = {}
    value = 0
    for i in range(4):
        ll_.append(l_[i+1] - l_[i])
    for i in sorted(ll_):
        if i not in lll_:
            lll_[i] = 1
        else:
            lll_[i] += 1
    if len(lll_) == 1 and (l_[0] != l_[1]):
        value = 40
    return str(value)

def yatcht(diceNumList):
    l_ = [int(i) for i in diceNumList]
    value = 0
    if len(set(l_)) == 1:
        value = 50
    return str(value)

def score(a, b, c, d, e, f, g, h, i ,j , k, l, m):
    l_ = [a, b, c, d, e, f, g, h, i ,j , k, l, m]
    c = 0
    for i in l_:
        if i == '':
            l_[c] = 0
            c += 1
        else:
            l_[c] = int(i)
            c += 1
    return str(sum(l_))

if __name__ == '__main__':
    a = score('1', '', '', '', '', '', '', '', '', '', '', '', '',)
    print(a)