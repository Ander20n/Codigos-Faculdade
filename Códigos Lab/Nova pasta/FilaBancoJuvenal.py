class No:

    def __init__(self, dado):
        self.dado = dado
        self.ProxNo = None
    
    def getDado(self):
        return self.dado
    
    def setDado(self,dado):
        self.dado = dado
    
    def getProximoNo(self):
        return self.ProxNo
        
    def setProximoNo(self,NovoNo):
        self.ProxNo = NovoNo;
    
    
class Lista:
    def __init__(self):
        self.PrimeiroNo = None
        self.UltimoNo = None
            
    def __str__(self):
        if self.isEmpty():
            return '0'
        else:
            string = str(self.PrimeiroNo.getDado())
            return string
        
    def inserircomeco(self, value):
        NovoNo = No (value)
        if self.isEmpty():
            self.PrimeiroNo = self.UltimoNo = NovoNo
        else:
            NovoNo.setProximoNo(self.PrimeiroNo)
            self.PrimeiroNo = NovoNo
    
    def inserirfinal(self, value):
        
        NovoNo = No(value)
        
        if self.isEmpty():
            self.PrimeiroNo = self.UltimoNo = NovoNo
        else:
            self.UltimoNo.setProximoNo(NovoNo)
            self.UltimoNo = NovoNo
            
    def removerinicio(self):
        
        if self.isEmpty():
            raise IndexError
        PrimeiroValorNo = self.PrimeiroNo.getDado()
        if self.PrimeiroNo is self.UltimoNo:
            self.PrimeiroNo = self.lastNode = None
        else:
            self.PrimeiroNo = self.PrimeiroNo.getProximoNo()
        return PrimeiroValorNo
        
    def removerfinal(self):
        
        if self.isEmpty():
            raise IndexError
        UltimoValorNo = self.UltimoNo.getDado()
        if self.PrimeiroNo is self.UltimoNo:
            self.PrimeiroNo = self.UltimoNo = None
        else:
            AtualNo = self.PrimeiroNo
            while AtualNo.getProximoNo() is not self.UltimoNo:
                AtualNo = AtualNo.getProximoNo()
            AtualNo.setProximoNo(None)
            self.lastNode = AtualNo
        return UltimoValorNo
    
    def isEmpty(self):
        return self.PrimeiroNo is None

user = int(input())

juvenal = ""

for x in range(user):
    filnormal = Lista()
    filprefen = Lista()
    coman = int(input())
    for p in range(coman):
        info = input().split()
        if info[0] == "f":
            filnormal.inserirfinal(info[1])
        elif info[0] == "p":
            filprefen.inserirfinal(info[1])
        elif info[0] == "A":
            if filnormal.isEmpty():
                filprefen.removerinicio()
            else:
                filnormal.removerinicio()
        elif info[0] == "B":
            if filprefen.isEmpty():
                filnormal.removerinicio()
            else:
                filprefen.removerinicio()
        elif info[0] == "I":
            juvenal += ("Caso %d:" % (x+1))
            juvenal += ('\n' + filnormal.__str__() + " " + filprefen.__str__())
            
print(juvenal)