user = int(input())
resposta = []
juv = ""

for x in range(user):
    cont = 0
    stop = 0
    players = []
    mesa = []
    parar = 0
    cm = input().split(" ")
    cml = [int(c) for c in cm]
    mesa += cml
    while parar != -1:
        cp = input().split(" ")
        if cp[0] == "-1":
            parar = -1
        else:
            cpl = [int(p) for p in cp]
            players.append(cpl)
            cp = []

    while cont < 1000:
        if cont == 999:
            resposta.append(str(0))
            cont = 1000
            break
        else:
            for lc in players:
                if lc == []:
                    indi = players.index(lc)
                    resposta.append(str(indi+1))
                    stop = "parar"
            if stop != "parar":
                for lc in players:
                    if lc[0] == mesa[0]:
                        lc.remove(lc[0])
                    else:
                        lc.append(lc[0])
                        lc.remove(lc[0])
                mesa.append(mesa[0])
                mesa.remove(mesa[0])
                cont += 1
            else:
                cont = 1000
                
for res in range(len(resposta)):
    print(resposta[res])