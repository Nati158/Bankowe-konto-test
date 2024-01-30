class KontoBankowe:
    def __init__(self, imie, nazwisko, saldo=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        print(f"Wpłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")

    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f"Wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
        else:
            print("Brak wystarczających środków na koncie.")

    def sprawdz_saldo(self):
        print(f"Aktualne saldo dla {self.imie} {self.nazwisko}: {self.saldo} PLN")


class KontoOsobiste(KontoBankowe):
    def __init__(self, imie, nazwisko, saldo=0, kredyt=0):
        super().__init__(imie, nazwisko, saldo)
        self.kredyt = kredyt

    def wyplac_z_kredytu(self, kwota):
        if kwota <= self.saldo + self.kredyt:
            self.saldo -= kwota
            print(f"Wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN. Kredyt pozostały: {self.kredyt} PLN")
        else:
            print("Brak wystarczających środków (również kredytowych).")


if __name__ == "__main__":
    konto1 = KontoBankowe("Jan", "Kowalski", 1000)
    konto1.wplac(500)
    konto1.wyplac(300)
    konto1.sprawdz_saldo()

    konto2 = KontoOsobiste("Anna", "Nowak", 2000, 1000)
    konto2.wplac(800)
    konto2.wyplac_z_kredytu(3000)
    konto2.sprawdz_saldo()
