class No:

    def __init__(self, dado):
        self.dado = dado
        self.filesquerdo = None
        self.fildireito = None
        self.pai = None
    
    def getDado(self):
        return self.dado
    
    def setDado(self,novo):
        self.dado = novo
    
    def getFilhoLeft(self):
        return self.filesquerdo
    
    def setFilhoLeft(self,esquerdo):
        self.filesquerdo = esquerdo
        
    def getFilhoRight(self):
        return self.fildireito
    
    def setFilhoRight(self,direito):
        self.fildireito = direito
    
    def getPai(self):
        return self.pai
    
    def setPai(self,pai):
        self.pai = pai

    def __str__(self):
        return str(self.getDado())
    
class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, novaR):
        self.raiz = novaR
        
    def Buscar(self,x,k):
        if x == None or x.getDado() == k:
            return x
        if k < x.getDado():
            return self.Buscar(x.getFilhoRight(),k)
        else:
            return self.Buscar(x.getFilhoLeft(),k)
    
    def Minimo(self,x):
        while x.getFilhoLeft() != None:
            x = x.getFilhoLeft()
        return x
    
    def Maximo(self,x):
        while x.getraiz.getFilhoRight() != None:
            x = x.getFilhoRight()
        return x
    
    def Sucessor(self,x):
        if x.getFilhoRight() != None:
            return self.Minimo(x.getFilhoRight())
        y = x.getPai()
        while y != None and x is y.getFilhoRight():
            x = y
            y = y.getPai()
        return y
    
    def Predecessor(self,x):
        if x.getFilhoLeft() != None:
            return self.Maximo(x.getFilhoLeft())
        y = x.getPai()
        while y != None and x is y.getFilhoLeft():
            x = y
            y = y.getPai()
        return y
    
    def Inserir(self,z):
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if z.getDado() < x.getDado():
                x = x.getFilhoLeft()
            else:
                x = x.getFilhoRight()
        z.setPai(y)        
        if y == None:
            self.setRaiz(z)
        else:
            if z.getDado() < y.getDado():
                y.getFilhoLeft(z)
            else:
                y.getFilhoRight(z)
    
    def Deletar(self,z):
        if z.getFilhoLeft() == None or z.getFilhoRight() == None:
            y = z
        else:
            y = self.Sucessor(z)
        if y.getFilhoLeft() != None:
            x = y.getFilhoLeft()
        else:
            x = y.getFilhoRight()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(z)
        else:
            if y == y.getPai().getFilhoLeft():
                y.getPai().setFilhoLeft(z)
            else:
                y.getPai().setFilhoRight(z)
        if y != z:
            z.setDado(y.getDado)
    
    def Ordem(self, x):
        if x != None:
            self.Ordem(x.getFilhoLeft())
            print (x.getDado())
            self.Ordem(x.getFilhoRight())
    
    def PreOrdem(self, x):
        if x != None:
            print (x.getDado())
            self.Ordem(x.getFilhoLeft())
            self.Ordem(x.getFilhoRight())
    
    def PosOrdem(self, x):
        if x != None:
            self.Ordem(x.getFilhoLeft())
            self.Ordem(x.getFilhoRight())
            print (x.getDado())

arv = ArvoreBinaria()

entrada = int(input())

for v in range(entrada):
    user = input().split(" ")
    
    if user[0] == "A":
        arv.Inserir(user[1])
    elif user[0] == "B":
        arv.Deletar(user[1])
    elif user[0] == "C":
        print(arv.Predecessor(user[1]))
    elif user[0] == "PRE":
        print(arv.PreOrdem(arv.getRaiz()))
    elif user[0] == "IN":
        print(arv.Ordem(arv.getRaiz()))
    elif user[0] == "POST":
        print(arv.PosOrdem(arv.getRaiz()))