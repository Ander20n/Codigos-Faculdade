def pasto(i,j,T):
    global ovelha_pasto
    global lobo_pasto
    global linha
    global coluna
    if T[i][j] == '.':
        T[i][j] = 'x'
    elif T[i][j] == '#':
        pass    
    elif T[i][j] == 'x':
        pass
    elif T[i][j] == 'k':
        ovelha_pasto += 1
        T[i][j] = 'x'
    elif T[i][j] == 'v':
        lobo_pasto += 1
        T[i][j] = 'x'
    if i-1 >= 0:
        pasto(i-1,j,T)
    if i+1 < linha:
        pasto(i+1,j,T)
    if j+1 < coluna:
        pasto(i,j+1,T)
    if j-1 >= 0:
        pasto(i,j-1,T)
    return lobo_pasto, ovelha_pasto
    
def matriz(l,c,caract):
    matr = []
    ovelha = 0
    lobo = 0
    for i in range(l):
        lista = []
        for j in range(c):
            if caract[i][j] == 'k':
                ovelha += 1
            if caract[i][j] == 'v':
                lobo += 1
            lista.append(caract[i][j])
        matr.append(lista)
    return matr, lobo, ovelha

lincol = input().split(" ")
col = [int(c) for c in lincol[1]]

caracteres = []

for d in range(int(lincol[0])):
    dados = input()
    caracteres.append(dados)

linha = int(lincol[0])
coluna = col[0]

p,lobo_inicial,ovelha_inicial= matriz(linha,coluna,caracteres)

ovelha_pasto = 0
lobo_pasto = 0

for i in range(linha):
    for j in range(col[0]):
        total_lobo,total_ovelha = pasto(i,j,p)
        if total_lobo >= total_ovelha:
            ovelha = ovelha_inicial - total_ovelha
            lobo = total_lobo
        else:
            lobo = lobo_inicial - total_lobo
            ovelha = total_ovelha
        total_lobo = 0
        total_ovelha = 0
            
print('%d %d' %(ovelha,lobo))