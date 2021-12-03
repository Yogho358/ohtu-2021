from enum import Enum
from tkinter import ttk, constants, StringVar



class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovellus, lue):
        self._sovellus = sovellus
        self._lue = lue
        self._edellinen = 0

    def suorita(self):
        try:
            self._edellinen = self._sovellus.tulos
            self._sovellus.plus(int(self._lue()))
        except Exception:
            pass

    def kumoa(self):
        self._sovellus.tulos = self._edellinen

class Erotus:
    def __init__(self, sovellus, lue):
        self._sovellus = sovellus
        self._lue = lue
        self._edellinen = 0

    def suorita(self):
        try:
            self._edellinen = self._sovellus.tulos
            self._sovellus.miinus(int(self._lue()))
        except Exception:
            pass

    def kumoa(self):
        self._sovellus.tulos = self._edellinen

class Nollaa:
    def __init__(self, sovellus, lue):
        self._sovellus = sovellus
        self._edellinen = 0

    def suorita(self):
        self._edellinen = self._sovellus.tulos
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.tulos = self._edellinen

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._edellinen_komento = Erotus

        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(self._sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaa(self._sovellus, self._lue_syote),
            Komento.KUMOA: self._edellinen_komento(self._sovellus, self._lue_syote)
        }

    def _lue_syote(self):
        return self._syote_kentta.get()

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            #state=constants.DISABLED,
            command=lambda: self._kumoa()
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def nayta_tulos_ja_nollaa_kentta(self):
        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)

    def _kumoa(self):
        komento_olio = self._edellinen_komento
        komento_olio.kumoa()
        self.nayta_tulos_ja_nollaa_kentta()

    def _suorita_komento(self, komento):

        komento_olio = self._komennot[komento]
        self._edellinen_komento = komento_olio
        komento_olio.suorita()
        

        # arvo = 0

        # try:
        #     arvo = int(self._syote_kentta.get())
        # except Exception:
        #     pass

        # if komento == Komento.SUMMA:
        #     self._sovellus.plus(arvo)
        # elif komento == Komento.EROTUS:
        #     self._sovellus.miinus(arvo)
        # elif komento == Komento.NOLLAUS:
        #     self._sovellus.nollaa()
        # elif komento == Komento.KUMOA:
        #     pass

        # self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
           self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self.nayta_tulos_ja_nollaa_kentta()       
