with open("input4.txt", "r") as f:
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
print(tranzitii)
f = open("teste4.txt", "r")
x = f.readline()[:-1]

while x:
    drumuri = [initiala.copy()]
    for litera in x:
        if not drumuri:
            print(f"{x} nu e acceptat")
            break
        aux = drumuri.copy()
        drumuri = []
        for drum in aux:
            stari = tranzitii[drum[-1]][litera]
            if stari:
                for elem in range(len(stari)):
                    drumuri.append(drum + [stari[elem]])
                    #drumuri[-1].append(stari[elem])
    else:
        ok1 = 1
        for elem in drumuri:
            if elem[-1] in finale:
                string = " ".join(elem)
                print(f"{x} e acceptat cu drumul: {string}")
                ok1 = 0
        if ok1:
            print(f"{x} nu e acceptat")
    print()
    x = f.readline()[:-1]
f.close()
