
from Biudzetas.klases.irasas import Irasas




class Islaidos(Irasas):
    def __init__(self, suma, atsiskaitymo_budas=None, isigyta_preke_paslauga=None):
        super().__init__("Islaidos", suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def papildoma_informacija(self):
        if not self.atsiskaitymo_budas:
            self.atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą (pvz., grynaisiais, kortele): ")
        if not self.isigyta_preke_paslauga:
            self.isigyta_preke_paslauga = input("Įveskite įsigytą prekę ar paslaugą: ")

    def __str__(self):
        return f"{self.pajamos}: {self.suma} EUR, Atsiskaitymo būdas: {self.atsiskaitymo_budas if self.atsiskaitymo_budas else 'Nenurodyta'}, Įsigyta prekė/paslauga: {self.isigyta_preke_paslauga if self.isigyta_preke_paslauga else 'Nenurodyta'}"