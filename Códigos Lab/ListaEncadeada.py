class No():
    def __init__(self,dado=None):
        self._dado = dado
        self._prox = None
    def setDado(self,dado):
        self._dado = dado
    def getDado(self):
        return self._dado
    def getProx(self):
        return self._prox
    def setProx(self,prox):
        self._prox = prox
        
class ListaEncadeada():
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def isVazia(self):
        return self._inicio == None
    
    def __str__(self):
        i = self.inicio
        string = ''
        while i != None:
            str += str(i.getDado())
            i = i.getProx()
        return string
    
    def inserirNoInicio(self,dado):
        no = No(dado)
        no.setProx(self._inicio)
        self._inicio = no
        if self.isVazia():
            self._fim = no

    def removerDoInicio(self):
        if self.isVazia():
            return None
        no = self._inicio
        self._inicio = no.getProx()
        if self.isVazia():
            self._fim = None
        return no.getDado()
    
    def inserirNoFim(self,dado):
        no = No(dado)
        if self.isVazia():
            self._inicio = no
        ultimo = self._fim
        ultimo.setProx(no)
        self._fim = no
        
class Pilha(ListaEncadeada):
    def push(self,dado):
        self.inserirNoInicio(dado)
    
    def pop(self):
        return self.removerDoInicio()

dad = 7    
a = ListaEncadeada()
a.inserirNoFim(dad)
print(a)