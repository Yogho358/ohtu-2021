class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        

    def miinus(self, arvo):
        self._edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self._edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self._edellinen = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

   
