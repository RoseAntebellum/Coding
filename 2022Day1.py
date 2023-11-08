
calCount = 0
calTotals= []
maxCal = 0


f = open(r"C:\Users\allison.cooper\OneDrive - Radford College\Documents\Coding\D1input.txt", "r")
for line in f:
    if line != '\n':
        calCount = int(calCount) + int(line)
    else:
        calTotals.append(calCount)
        calCount = 0

calTotals.sort(reverse = True)

maxCal = calTotals[0] + calTotals[1] + calTotals[2]


#print(calTotals[0])
#print(calTotals[1])
print(maxCal)
f.close
