import itertools
import copy

f = open("2015D3Input", "r")

path = f.read()

roboTurn = False
location = [0, 0]
visited = []
roboSanta = [0, 0]

for char in path:
    repeat = False
    if roboTurn == False:
        match char:
            case "<":
                location[0] = location[0] - 1
            case ">":
                location[0] = location[0] + 1
            case "^":
                location[1] = location[1] + 1
            case "v":
                location[1] = location[1] - 1
        for i in range(len(visited)):
            if visited[i] == location:
                repeat = True
        if repeat == False:
            visited.append(copy.deepcopy(location))
        roboTurn = True
    
    
    else:
        match char:
            case "<":
                roboSanta[0] = roboSanta[0] - 1
            case ">":
                roboSanta[0] = roboSanta[0] + 1
            case "^":
                roboSanta[1] = roboSanta[1] + 1
            case "v":
                roboSanta[1] = roboSanta[1] - 1
        for i in range(len(visited)):
            if visited[i] == roboSanta:
                repeat = True
        if repeat == False:
            visited.append(copy.deepcopy(roboSanta))
        roboTurn = False
    
    

    


    #if repeat == False:
        #visited.append(copy.deepcopy(a))


print(len(visited))
