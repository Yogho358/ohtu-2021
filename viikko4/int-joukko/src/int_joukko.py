KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        
        self.kapasiteetti = kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        
        self.kasvatuskoko = kasvatuskoko
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        
        for i in self.ljono:
            if n == i:
                return True

        return False        

        

    def lisaa(self, n):

        if self.kuuluu(n):
            return False
       
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(taulukko_old, self.ljono)

        return True

        

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        kohta = -1
        

        for i in range(0, self.alkioiden_lkm):
            if n == s.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[i] = 0
                break

        
        for j in range(kohta, self.alkioiden_lkm - 1):
             = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu

        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True


    def kopioi_taulukko(self, kopioitava, kopio):
        for i in range(0, len(kopioitava)):
            kopio[i] = kopioitava[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus.poista(b_taulu[i])

        return z

    def __str__(self):



        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
