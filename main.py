with open("input1.txt", "r") as f:
    tranzitii = {x: {} for x in f.readline().strip().split()}
    alfabet = [x for x in f.readline().split()]
    initiala = [f.readline().strip()]
    finale = [x for x in f.readline().strip().split()]
    x = f.readline().split()
    while x:
        tranzitii[x[0]][x[1]] = [elem for elem in x[2:]]
        x = f.readline().split()
    for x in tranzitii.keys():
        for lit in alfabet:
            if lit not in tranzitii[x].keys():
                tranzitii[x][lit] = []
#print(tranzitii)
f = open("teste1.txt", "r")
x = f.readline()[:-1]

while x:
    drumuri = [initiala.copy()]
    for litera in x:
        aux = drumuri.copy()
        drumuri = []
        for drum in aux:
            stari = list(set(tranzitii[drum[-1]][litera]))
            if stari:
                for elem in stari:
                    drumuri.append(drum)
                    drumuri[-1].append(elem)
    for elem in drumuri:
        if elem[-1] in finale:
            string = " ".join(elem)
            print(f"Acceptat cu drumul: {string}")
            break
    else:
        print("Nu e acceptat")
    x = f.readline()[:-1]
f.close()
