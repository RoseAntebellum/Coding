f = open("2015D5Input", "r")

PuzIn = f.read()
PuzIn = PuzIn.split("\n")
goodList = 0

for x in PuzIn:
    niceList = True
    
    """vowel = x.count("a") + x.count("e") + x.count("i") + x.count("o") + x.count("u")
    if vowel < 3:
        niceList = False
    
    badSub = x.count("ab") + x.count("cd") + x.count("pq") + x.count("xy")
    if badSub >= 1:
        niceList = False
    
    xLength = len(x)
    y = 0
    letterRepeat = False
    while y < len(x) - 1:
        z = list(x)
        if z[y] == z[y+1]:
            letterRepeat = True
        y += 1
        
    if letterRepeat == False:
        niceList = False"""
    
    xLength = len(x)
    y = 0
    letterRepeat = False
    while y < len(x) - 2:
        z = list(x)
        if z[y] == z[y+2]:
            letterRepeat = True
        y += 1

    if niceList == True:
        goodList += 1

print(goodList)

