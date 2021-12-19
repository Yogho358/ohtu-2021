from kps import KPS

class KPSPvAI(KPS):
    def __init__(self, tekoaly):
        self._ai = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self._ai.anna_siirto()

    