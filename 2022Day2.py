
score = 0
gameGuide = []
gameScore = 0 



f = open("D2input.txt", "r")
for line in f:
    gameGuide.append(line)
f.close

for game in gameGuide:
    strat = game.split()
    match strat[1]:
        case "X":
            match strat[0]:
                case "A":
                    score = score + 3
                case "B":
                    score = score + 1
                case "C":
                    score = score + 2

        case "Y":
            match strat[0]:
                case "A":
                    score = score + 4
                case "B":
                    score = score + 5
                case "C":
                    score = score + 6

        case "Z":
            match strat[0]:
                case "A":
                    score = score + 8
                case "B":
                    score = score + 9
                case "C":
                    score = score + 7
    

print(score)