
from klases import Pajamos, Islaidos





class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        pajamos = Pajamos(suma)
        pajamos.papildoma_informacija()
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Islaidos(suma)
        islaidos.papildoma_informacija()
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, Pajamos):
                balansas += irasas.suma
            elif isinstance(irasas, Islaidos):
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        print("\nBiudžeto ataskaita:")
        if not self.zurnalas:
            print("Nėra įrašų.")
        else:
            for irasas in self.zurnalas:
                print(irasas)











