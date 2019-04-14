user = int(input())
mesa = []
players = []

for x in range(user):
    players.append([])
    parar = 0
    cm = input().split(" ")
    cml = [int(c) for c in cm]
    mesa.append(cml)
    if parar != -1:
        cp = input().split(" ")
        if cp[0] == "-1":
            parar = -1
        else:
            cpl = [int(p) for p in cp]
            players[x].append(cpl)
            cp = []

print(mesa)
print(players[0])