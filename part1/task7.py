#########################################################################################################################################
                                            #1 uzduotis
##########################################################################################################################################

# class Automobiliai:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas
#     def vaziuoti(self):
#         print(f"Automobilis {self.modelis} ({self.metai}) vaziuoja.")
#     def stoveti(self):
#         print(f"Automobilis {self.modelis} ({self.metai}) priparkuotas.")
#     def pildyti_degalus(self):
#         print(f"Automobilis {self.modelis} ({self.metai}) degalai ipilti.")
#     def __str__(self):
#         return f"Automobilis {self.modelis} ({self.metai}) - {self.kuro_tipas}"
# class Elektromobiliai(Automobiliai):
#     def __init__(self, metai, modelis, kuro_tipas, akumuliatorius):
#         super().__init__(metai, modelis, kuro_tipas)
#         self.akumuliatorius = akumuliatorius
#     def pildyti_degalus(self):
#         print(f"Elektromobilis {self.modelis} ({self.metai}) baterija ikrauta.")
#     def vaziuoti_automatiskai(self):
#         print(f"Elektromobilis {self.modelis} ({self.metai}) vaziuoja automatiskai.")
#     def __str__(self):
#         return f"Elektromobilis {self.modelis} ({self.metai}) - {self.kuro_tipas}, akumuliatorius: {self.akumuliatorius}"

# Automobiliai1 = Automobiliai(2013, "Audi A6", "dyzelinas")

# Elektromobiliai1 = Elektromobiliai(2022, "Tesla Model S", "elektra", "100 kWh")


# print("*"*50)
# Automobiliai1.vaziuoti()

# print("*"*50)
# Automobiliai1.stoveti()

# print("*"*50)
# Automobiliai1.pildyti_degalus()

# print("*"*50)
# Elektromobiliai1.vaziuoti()

# print("*"*50)
# Elektromobiliai1.stoveti()

# print("*"*50)
# Elektromobiliai1.pildyti_degalus()

# print("*"*50)
# Elektromobiliai1.vaziuoti_automatiskai()


##################################################################################################################################################3
                                            #2 uzduotis
##################################################################################################################################################3
from datetime import datetime
class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = float(valandos_ikainis)
        self.dirba_nuo = datetime.strptime(dirba_nuo, "%Y-%m-%d")
    def darbo_dienos(self):
        siandien = datetime.today()
        skirtumas = siandien - self.dirba_nuo
        return skirtumas.days + 1 # +1, kad įtraukti ir šiandieną(dirba_nuo yra jau iskaiciuotas)
    def paskaiciuoti_atlyginima(self):
        darbo_dienos = self.darbo_dienos()
        return darbo_dienos * self.valandos_ikainis * 8
    
class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)
    def paskaiciuoti_atlyginima(self):
        darbo_dienos = self.darbo_dienos()
        darbo_savaites = darbo_dienos // 7 #kiek savaičių
        # = pilnu savaiciu skaicius * 5 darbo dienos * isdirbtos valandos 
        darbo_valandos = darbo_savaites * 5 * 8
        return darbo_valandos * self.valandos_ikainis
        
    
darbuotojas1 = Darbuotojas("Ernestas", 7.80, "2018-05-14")
darbuotojas2 = NormalusDarbuotojas("Tomas", 8.50, "2020-01-01")
print("*"*50)
print(f"Darbuotojas {darbuotojas1.vardas} isdirbo {darbuotojas1.darbo_dienos()} dienų.")
print(f"Darbuotojas {darbuotojas1.vardas} uždirbo {darbuotojas1.paskaiciuoti_atlyginima()} eurų.")
print("*"*50)
print(f"Darbuotojas {darbuotojas2.vardas} isdirbo {darbuotojas2.darbo_dienos()} dienų.")
print(f"Darbuotojas {darbuotojas2.vardas} uždirbo {darbuotojas2.paskaiciuoti_atlyginima()} eurų.")

#################################################################################################################################################





































