from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.kori) == 0:
            return 0

        lkm = 0

        for ostos in self.kori:
            lkm += ostos.lukumaara()
        return lkm
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.kori) == 0:
            return 0
        hinta = 0
        for ostos in self.kori:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        korissa = False
        for ostos in self.kori:
            
            if lisattava.nimi() == ostos.tuotteen_nimi():
                korissa = True
                ostos.muuta_lukumaaraa(1)
        
        if korissa == False:
            print("tuli")
            ostos = Ostos(lisattava)
            self.kori.append(ostos)
        
        
        
    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if self.tavaroita_korissa() == 0:
                    self.kori = []
                break

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
