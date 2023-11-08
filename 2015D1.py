f = open("2015D1input", "r")


z = f.read()

level = 0
count = 0

for char in z:
    
    #print (char)
    match char:
        case '(':
            level = level + 1
        case ')':
            level = level - 1
    count = count + 1
    if level == -1:
        print(count)

print(level)

print("Hi can this please update")
