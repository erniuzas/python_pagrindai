from Biudzetas.klases.irasas import Irasas



class Pajamos(Irasas):
    def __init__(self, suma, siuntejas=None):
        super().__init__("Pajamos", suma)
        self.siuntejas = siuntejas

    def papildoma_informacija(self):
        if not self.siuntejas:
            self.siuntejas = input("Įveskite papildomą informaciją apie siuntėją: ")

    def __str__(self):
        return f"{self.pajamos}: {self.suma} EUR, Siuntėjas: {self.siuntejas if self.siuntejas else 'Nenurodyta'}"
