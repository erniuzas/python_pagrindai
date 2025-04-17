
                                                 # 1 uzduotis

#1

# class Sakinys:
#     def __init__(self, tekstas="default"):
#         self.tekstas = tekstas 
#         """
#         Tai yra konsturktorius, kuris priima argumenta (tekstas) ir priskiria klases (tekstas) savybei.
#         Sukurus klases objekta yra privaloma nurodyti kazkokia tekstine reiksme,
#         kuri bus priskirta klases savybei (tekstas).
#         """
        
#     def atbulai(self):
#         return self.tekstas[::-1] #grazina teksta atbulai

# sakinys = Sakinys("Sveiki, kaip sekasi?") 
# print(sakinys.atbulai())


# #2

# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas 
        
#     def mazosiomis(self):
#         return self.tekstas.lower()

# sakinys = Sakinys("SveiKi, kaiP sEkasI?")
# print(sakinys.mazosiomis())


# #3

# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas 
    
#     def gauti_didziosiomis(self):
#         return self.tekstas.upper()

# sakinys = Sakinys("sveiki, kaip sekasi?")
# print(sakinys.gauti_didziosiomis())


# #4

# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas  # Savybe, kuri laiko teksta
    
#     def eil_numeri(self, numeris):
#         sakiniai = self.tekstas.split('. ')  # Suskaido teksta i sakinius pagal taska ir tarpa
#         if 0 < numeris <= len(sakiniai):  # Patikrina, ar numeris yra teisingas
#             return sakiniai[numeris - 1]  # Grazina sakini pagal numeri (numeris - 1, nes indeksai prasideda nuo 0)

# tekstas = "labas ate. kaip sekasi?. viskas gerai. o kaip tau?."
# sakinys = Sakinys(tekstas)  # Sukuria Sakinys objekta su pateiktu tekstu
# print(sakinys.eil_numeri(2))  # Isveda antra sakini (numeris 2)
# print(sakinys.eil_numeri(3))  # Isveda trecia sakini (numeris 3)
# print(sakinys.eil_numeri(4))  # Isveda ketvirta sakini (numeris 4)
# print(sakinys.eil_numeri(1))  # Isveda penkta sakini (numeris 5)


# #5
# import re
# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas  
    
#     def simboliai(self, simbolis):
#         return self.tekstas.count(simbolis)  # Skaiciuoja, kiek tekste pasikartoja nurodytas simbolis
    
#     def zodziai(self, zodis):
#         zodziai = self.tekstas.split()  # Suskaido teksta i zodzius
#         zodziai = re.findall(r'\b\w+\b', self.tekstas) # Naudojame regex, kad gautume tik zodzius.
#         # \b\w+\b - zodzio ribos, zodis, zodzio ribos.
#         # Tinka tik zodziams su raidemis ir skaiciais
#         return zodziai.count(zodis)  # Skaiciuoja, kiek pasikartoja nurodytas zodis
    
# sakinys = Sakinys("labas, labas, labas. kaip sekasi? viskas gerai. o kaip tau?")
# print(sakinys.simboliai("a"))  # Isveda, kiek tekste yra simbolio "a"
# print(sakinys.zodziai("labas"))  # Isveda, kiek tekste yra zodzio "labas"

# #6

# import re

# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas

#     def pakeisti_simboli(self, senas_simbolis, naujas_simbolis):
#         # Pakeičia simboli visame tekste
#         self.tekstas = self.tekstas.replace(senas_simbolis, naujas_simbolis)
#         return self.tekstas

#     def pakeisti_zodi(self, senas_zodis, naujas_zodis):
#         # Pakeičia žodį visame tekste
#         self.tekstas = re.sub(r'\b' + re.escape(senas_zodis) + r'\b', naujas_zodis, self.tekstas)
#         """
#         re.sub() - iesko visu atitikmenu tekste, kurie atitinka zodi
#         \b - zodzio ribos, re.escape() - specialius simbolius(,./?) pavercia i paprastus simbolius.
#         """
#         return self.tekstas

# sakinys = Sakinys("labas, labas, labas. kaip sekasi? viskas gerai. o kaip tau?")
# #print(sakinys.pakeisti_simboli("a", "?"))  # Pakeičia visus "a" į "?"
# print(sakinys.pakeisti_zodi("labas", "sveikas"))  # Pakeičia visus "labas" į "sveikas"

# #7
# import re
# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas  
    
#     def zodziai(self):
#         zodziai = self.tekstas.split()  # Suskaido tekstą į žodžius pagal tarpus
#         return len(zodziai)  # Grąžina žodžių skaičių
    
#     def skaiciai(self):
#         skaiciai = re.findall(r'\d+', self.tekstas)  # Suranda visus skaitmenis
#         # \d+ - suranda skaitmenis, + - bent vienas skaitmuo
#         # re.findall() - grazina visus atitikmenis kaip sarasa
#         return len(skaiciai)  # Grąžina skaičių skaičių
    
#     def didziosios(self):
#         return sum(1 for simbolis in self.tekstas if simbolis.isupper())  # Skaičiuoja didžiąsias raides
    
#     def mazosios(self):
#         return sum(1 for simbolis in self.tekstas if simbolis.islower())  # Skaičiuoja mažąsias raides



# sakinys = Sakinys("Labas, kaip sekasi 1 23? Viskas gerai, ačiū! O kaip Tau?")

# print(f"Zodziai: {sakinys.zodziai()}")
# print(f"Skaiciai: {sakinys.skaiciai()}")
# print(f"Didziosios raides: {sakinys.didziosios()}")
# print(f"Mazosios raides: {sakinys.mazosios()}")

#################################################################################################################################################3

                                                # 2 uzduotis

##########################################################################################################################################################

# from datetime import datetime, timedelta

# class Sukaktis:
#     def __init__(self, metai, menuo, diena, valanda=0, minute=0, sekunde=0):
#         # Sukuriama data pagal ivestus parametrus
#         self.sukakties_data = datetime(metai, menuo, diena, valanda, minute, sekunde)

#     def praejo_metai(self):
#         # Apskaiciuojama, kiek metu praejo nuo sukakties
#         dabar = datetime.now()
#         return dabar.year - self.sukakties_data.year - ((dabar.month, dabar.day) < (self.sukakties_data.month, self.sukakties_data.day))

#     def praejo_savaites(self):
#         # Apskaiciuojama, kiek savaiciu praejo nuo sukakties
#         dabar = datetime.now()
#         skirtumas = dabar - self.sukakties_data
#         return skirtumas.days // 7

#     def praejo_dienos(self):
#         # Apskaiciuojama, kiek dienu praejo nuo sukakties
#         dabar = datetime.now()
#         skirtumas = dabar - self.sukakties_data
#         return skirtumas.days

#     def praejo_valandos(self):
#         # Apskaiciuojama, kiek valandu praejo nuo sukakties
#         dabar = datetime.now()
#         skirtumas = dabar - self.sukakties_data
#         return skirtumas.total_seconds() // 3600

#     def praejo_minutes(self):
#         # Apskaiciuojama, kiek minuciu praejo nuo sukakties
#         dabar = datetime.now()
#         skirtumas = dabar - self.sukakties_data
#         return skirtumas.total_seconds() // 60

#     def praejo_sekundes(self):
#         # Apskaiciuojama, kiek sekundziu praejo nuo sukakties
#         dabar = datetime.now()
#         skirtumas = dabar - self.sukakties_data
#         return skirtumas.total_seconds()
    
#     def ar_keliamieji(self):
#         # Patikrinama, ar metai buvo keliamieji
#         metai = self.sukakties_data.year
#         # Jei metai dalijasi iš 4, tačiau nesidalija iš 100 arba dalijasi iš 400, tai keliamieji metai
#         if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#             return True
#         else:
#             return False
        
#     def atnaujinta_data(self, dienos):
#         # Atnaujina sukakties datą pagal nurodytą dienų skaičių
#         nauja_data = self.sukakties_data + timedelta(days=dienos)
#         return nauja_data


# def ivesti_sukakti():
#     print("Įveskite sukaktį (datą ir laiką):")
#     metai = int(input("Metai: "))
#     menuo = int(input("Mėnuo (1-12): "))
#     diena = int(input("Diena (1-31): "))
#     # Sukuriamas Sukakties objektas su ivestais duomenimis
#     return Sukaktis(metai, menuo, diena)
# # Pavyzdys, kaip naudoti programa
# sukaktis = ivesti_sukakti()

# # Kvieciame metodus is objekto
# print(f"Praėjo metų: {sukaktis.praejo_metai()}")
# print(f"Praėjo savaičių: {sukaktis.praejo_savaites()}")
# print(f"Praėjo dienų: {sukaktis.praejo_dienos()}")
# print(f"Praėjo valandų: {sukaktis.praejo_valandos()}")
# print(f"Praėjo minučių: {sukaktis.praejo_minutes()}")
# print(f"Praėjo sekundžių: {sukaktis.praejo_sekundes()}")

# if sukaktis.ar_keliamieji():
#     print("Metai buvo keliamieji.")
# else:
#     print("Metai nebuvo keliamieji.")

# dienos = int(input("Iveskite kiek dienu norite prideti(neigiamas skaicius atims): "))

# nauja_data = sukaktis.atnaujinta_data(dienos)

# print(f"Naujas data: {nauja_data}")

################################################################################################################################################################################################################























