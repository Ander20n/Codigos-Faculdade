class No:

    def __init__(self, dado):
        self._dado = dado
        self._ant = None
        self._prox = None

    def getDado(self):
        return self._dado

    def getProx(self):
        return self._prox

    def getAnt(self):
        return self._ant

    def setDado(self, dado):
        self._dado = dado

    def setProx(self, prox):
        self._prox = prox

    def setAnt(self, ant):
        self._ant = ant