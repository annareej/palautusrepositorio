KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, luku):
        if self.kuuluu(luku):
            kohta = self.ljono.index(luku)
            self.ljono.pop(kohta)
            self.alkioiden_lkm = self.alkioiden_lkm - 1

            return True

        return False

    def kopioi_lista(self, kopioitava_taulu, kohde_taulu):
        for i in range(0, len(kopioitava_taulu)):
            kohde_taulu[i] = kopioitava_taulu[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[i])

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    joukko.lisaa(b_taulu[j])

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.poista(b_taulu[i])

        return joukko

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
