#from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kpspvp import KPSPvP
#from kps_tekoaly import KPSTekoaly
#from kps_parempi_tekoaly import KPSParempiTekoaly
from kpspvai import KPSPvAI
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = KPSPvP()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            tekoaly = Tekoaly()
            yksinpeli = KPSPvAI(tekoaly)
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            tekoaly = TekoalyParannettu(10)
            haastava_yksinpeli = KPSPvAI(tekoaly)
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
