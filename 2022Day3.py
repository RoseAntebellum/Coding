def main():
    global inventory
    inventory = []
    tempList = []
    global count
    count = 0
    bagNum = 0
    global dupeList
    dupeList = []


    f = open("D3input.txt", "r")
    for line in f:
        bagNum += 1
        if bagNum > 0:
            if bagNum == 3:
                bagNum = 0
                tempList.append(line)
                inventory.append(tempList)
                tempList = []
                count += 1
                continue
            else:
                tempList.append(line)
        elif bagNum == 0:
            tempList.append(line)
    f.close    

    findDupes()
    calculateScore()
        
        
    



def findDupes():
    tempCount = 0
    tempbagOne = []
    tempbagTwo = []
    tempbagThree = []
    appended = False

    while tempCount < count:
        tempbagOne = []
        tempbagTwo = []
        tempbagThree = []
        tempbagOne.extend(inventory[tempCount][0])
        tempbagTwo.extend(inventory[tempCount] [1])
        tempbagThree.extend(inventory[tempCount] [2])
        tempCount += 1 
        appended = False
        for x in tempbagOne:
            #if appended == True:
                #break
            for y in tempbagTwo:
                if appended == True:
                    break
                for z in tempbagThree:
                    if x == y == z:
                        dupeList.append(x)
                        appended = True 
                        break
                

        
    print(dupeList)
    return


def calculateScore():
    priority = 0
    prioritySum = 0
    for a in dupeList:
        if a.islower():
            priority = ord(a) - ord('a') + 1
        elif a.isupper():
            priority = ord(a) - ord('A') + 27
        prioritySum = prioritySum + priority
    print(prioritySum)












main()