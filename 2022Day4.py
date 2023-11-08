def main():

    tempList = []
    global jobList
    global x
    global size
    global count
    jobList = []
    testingList = []
    count = 0
    size = 0
    x = 0

    f = open("D4input.txt", "r")
    for line in f:
        tempList = []
        tempList = line.split(",")
        tempList[1] = tempList[1].split("-")
        tempList[0] = tempList[0].split("-")
        size += 1
        jobList.append(tempList)
    

    inRange()
    #print(jobList)
    #while x < size:
    #    if (int(jobList[x][0][0]) <= int(jobList[x][1][0]) and int(jobList[x][0][1])>= int(jobList[x][1][1])) or int(jobList[x][1][0]) <= int(jobList[x][0][0]) and int(jobList[x][1][1])>= int(jobList[x][0][1]) or (int(jobList[x][0][0]) == int(jobList[x][1][0]) and int(jobList[x][0][1]) == int(jobList[x][1][1])):
    #       count = count + 1
    #        testingList.append(jobList[x])
    #    x += 1
    #print(testingList)
    print(count)
    
def inRange():
    tempCount = False
    x = 0
    count = 0

    while x < size:
        tempCount = False
        
        if int(jobList[x][0][0]) <= int(jobList[x][1][0]) <= int(jobList[x][0][1]) and tempCount == False:
            count += 1
            print(jobList[x])
            tempCount = True
        if int(jobList[x][0][0]) <= int(jobList[x][1][1]) <= int(jobList[x][0][1]) and tempCount == False:
            tempCount = True
            print(jobList[x])
            count += 1
        if int(jobList[x][1][0]) <= int(jobList[x][0][0]) <= int(jobList[x][1][1]) and tempCount == False:
            tempCount = True
            print(jobList[x])
            count += 1
        if int(jobList[x][1][0]) <= int(jobList[x][0][1]) <= int(jobList[x][1][1]) and tempCount == False:
            tempCount = True
            count += 1
            print(jobList[x])
        
        #if tempCount == False:
            
        x += 1
    print(count)


main()