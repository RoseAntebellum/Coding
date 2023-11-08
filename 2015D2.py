f = open("2015D2input", "r")

totalPaper = 0
y = []
#puzInput = f.read()

#print(puzInput)
for x in f:


    paper = 0
    l, w, h, = x.split('x')
    l, w, h = int(l), int(w), int(h)

    paper =  2*l*w + 2*w*h + 2*l*h
    slack = min(l+w, w+h, h+l)
    totalPaper += slack*2 + l*w*h
    

    
print(totalPaper)
        
