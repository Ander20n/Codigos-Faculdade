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
    
class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, novaR):
        self.raiz = novaR
        
    def Buscar(self,x):
        i = self.raiz
        while i is not None and x != i.getDado():
            if i.getDado() != x:
                if x < i.getDado():
                    i = i.getFilhoLeft()
                else:
                    i = i.getFilhoRight()
            else:
                break
        return i
    
    def Minimo(self,x):
        while x.getFilhoLeft() != None:
            x = x.getFilhoLeft()
        return x
    
    def Maximo(self,x):
        while x.getFilhoRight() != None:
            x = x.getFilhoRight()
        return x
    
    def Sucessor(self,x):
        x = self.Buscar(x)
        if x == None:
            return '0'
        if x.getFilhoRight() != None:
            f=self.Minimo(x.getFilhoRight())
            return str(f.getDado())
        y = x.getPai()
        if y == None:
            return '0'
        elif x == y.getFilhoRight():
            return str(y.getDado())
        else:
            while x == y.ggetFilhoRight():
                x = y
                y = x.getPai()
                if y == None:
                    return '0'
        return str(y.getDado())
    
    def Predecessor(self,x):
        x = self.Buscar(x)
        if x == None:
            return '0'
        if x.getFilhoLeft() != None:
            f=self.Maximo(x.getFilhoLeft())
            return str(f.getDado())
        y = x.getPai()
        if y == None:
            return '0'
        elif x == y.getFilhoRight():
            return str(y.getDado())
        else:
            while x == y.getFilhoLeft():
                x = y
                y = x.getPai()
                if y == None:
                    return '0'
        return str(y.getDado())
    
    def Inserir(self,z):
        z = No(z)
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
                y.setFilhoLeft(z)
            else:
                y.setFilhoRight(z)
    
    def Deletar(self,z):
        x = self.Buscar(z)
        if x is None:
            return False
        else:
            if x.getFilhoLeft() == None or x.getFilhoRight() == None:
                y = x
            else:
                y = self.Sucessor(x.getDado())
            if y.getFilhoLeft() != None:
                h = y.getFilhoLeft()
            else:
                h= y.getFilhoRight()
            if h!= None:
                h.setPai(y.getPai())
            if y.getPai() == None:
                self.setRaiz(h)
            else:
                if y == y.getPai().getFilhoLeft():
                    y.getPai().setFilhoLeft(h)
                else:
                    y.getPai().setFilhoRight(h)
            if y != x:
                x.setDado(y.getDado())
        return y
    
    def Ordem(self, x,resin):
        if x != None:
            self.Ordem(x.getFilhoLeft(),resin)
            resin.append(str(x.getDado()))
            self.Ordem(x.getFilhoRight(),resin)
    
    def PreOrdem(self, x, respre):
        if x != None:
            respre.append(str(x.getDado()))
            self.PreOrdem(x.getFilhoLeft(),respre)
            self.PreOrdem(x.getFilhoRight(),respre)
        
    def PosOrdem(self, x, respos):
        if x != None:
            self.PosOrdem(x.getFilhoLeft(),respos)
            self.PosOrdem(x.getFilhoRight(),respos)
            respos.append(str(x.getDado()))
r = 1

while True:
    try:            
        arv = ArvoreBinaria()
        
        lista = []
        entrada = int(input())
        print("Caso: %d" % (r))
        r += 1
        for v in range(entrada):
            user = input().split(" ")
            
            if user[0] == "A":
                arv.Inserir(int(user[1]))
            elif user[0] == "B":
                arv.Deletar(int(user[1]))
            elif user[0] == "C":
                print(arv.Predecessor(int(user[1])))
                   
            elif user[0] == "PRE":
                lispre = []
                res = ' '
                arv.PreOrdem(arv.getRaiz(),lispre)
                if lispre == []:
                    print(0)
                else:
                    print(res.join(lispre))

            elif user[0] == "IN":
                lisin = []
                res = ' '
                arv.Ordem(arv.getRaiz(),lisin)
                if lisin == []:
                    print(0)
                else:
                    print(res.join(lisin))
                
            elif user[0] == "POST":
                lispost = []
                res = ' '
                arv.PosOrdem(arv.getRaiz(),lispost)
                if lispost == []:
                    print(0)
                else:
                    print(res.join(lispost))
                
    except:
        break