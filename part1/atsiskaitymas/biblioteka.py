"""
1. Turėtų būti galima pridėti naują į knygą į biblioteką 
(knyga, privalo turėti bent, autorių pavadinimą išleidimo metus ir žanrą . Done
2. Turėtų būti galima pašalinti senas/nebenaudojamas knygas (konkretų kiekį), Done
 galima daryti pagal išleidimo metus, jeigu senesnis nei x išmetam.
3. Skaitytojai turėtų galėti pasiimti knygą išsinešimui (knygų kiekis ribotas)
4. Turėtų būti galimybė ieškoti knygų bibliotekoje, pagal knygos pavadinimą arba autorių. Done
5. Knygos išduodamos tik tam tikram laikui, jeigu knygos negrąžinamos iki išduotos datos,
 jos skaitomos vėluojančiomis (angl. Overdue).
6. Turi būti galima peržiūrėti visas bibliotekos knygas Done
7. Turi būti galima peržiūrėti visas vėluojančias knygas 
8. Turi būti neleidžiama pasiimti knygos, 
jeigu skaitytojas turi vėluojančią knygą ir jis turi būti įspėtas, kad knyga vėluoja
"""
import pickle
import os
from datetime import datetime, timedelta

#failo pavadinimas
failo_pavadinimas = "biblioteka.pkl"
vartotoju_failas = "vartotoju_sarasas.pkl"
# knygu klase
class Knyga:

    def __init__(self, pavadinimas, autorius, isleidimo_metai, zanras, kiekis=1):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras
        self.kiekis = kiekis
        self.pasiemimo_data = None  # data, kada knyga buvo pasiimta
        self.grazinimo_data = None  # data, kada knyga turi buti grazinta

    def pasiemimas(self, data):
        self.pasiemimo_data = data

    def nustatyti_grazinimo_data(self, grazinimo_data):
        self.grazinimo_data = grazinimo_data

    def __str__(self):
        return f"{self.autorius} - {self.pavadinimas} | {self.isleidimo_metai} | {self.zanras} | Kiekis: {self.kiekis}"


class Biblioteka:
    def __init__(self, failo_pavadinimas):
        self.failo_pavadinimas = failo_pavadinimas
        self.knygos = self.ikelti_biblioteka()
        self.vartotojai = []

 
# pagalbines funkcijos
    def issaugoti_biblioteka(self, knygu_sarasas):
        try:
            with open(self.failo_pavadinimas, "wb") as f:
                pickle.dump(knygu_sarasas, f)
            print("Biblioteka issaugota.")
        except Exception as e:
            print(f"Klaida issaugant biblioteka: {e}")

    def ikelti_biblioteka(self):
        try:
            if os.path.exists(failo_pavadinimas):
                with open(self.failo_pavadinimas, "rb") as f:
                    knygu_sarasas = pickle.load(f)
                return knygu_sarasas
            else:
                print(f"failas '{failo_pavadinimas}' nerastas. Sukuriamas naujas.")
                return []
        except Exception as e:
            print(f"Klaida ikeliant biblioteka: {e}")
            return []
        
    def rodyti_bibliotekos_knygas(self):
        if not self.bibliotekos_objektas or not self.bibliotekos_objektas.knygos:
            print("Biblioteka nera nustatyta.")
            return
        print(f"Bibliotekos knygos:")
        for knyga in self.bibliotekos_objektas.knygos:
            print(knyga)
    # funkcijos, skirtos knygu valdymui



    def prideti_knyga(self, knyga):
        knygos = self.ikelti_biblioteka()
        knygos.append(knyga)
        self.knygos = knygos
        self.issaugoti_biblioteka(knygos)
        print(f"Knyga '{knyga.pavadinimas}' prideta i biblioteka.")

    def rodyti_knygas(self):
        knygos = self.ikelti_biblioteka()
        if not knygos:
            print("Biblioteka tuscia.")
            return
        print("Visos bibliotekos knygos:")
        for knyga in knygos:
            print(knyga)

    def ieskoti_knyga(self, pavadinimas):
        knygos = self.ikelti_biblioteka()
        rasta = False
        for knyga in knygos:
            if pavadinimas.lower() in knyga.pavadinimas.lower():
                print(f"Rasta: {knyga}")
                rasta = True
        if not rasta:
            print(f"Knyga '{pavadinimas}' nerasta.")

    def istrinti_knyga(self, pavadinimas, kieki_pasalinti):
        knygos = self.ikelti_biblioteka()
        for knyga in knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower():
                if knyga.kiekis >= kieki_pasalinti:
                    knyga.kiekis -= kieki_pasalinti
                    if knyga.kiekis == 0:
                        knygos.remove(knyga)
                    self.issaugoti_biblioteka(knygos)
                    print(f"Istrinta {kieki_pasalinti} knygos '{pavadinimas}'.")
                else:
                    print(f"Nera tiek knygu '{pavadinimas}'.")
                return

    def istrinti_knygas_pagal_metus(self, metai):
        knygos = self.ikelti_biblioteka()
        pries = len(knygos)
        knygos = [k for k in knygos if int(k.isleidimo_metai) >= metai]
        istrintos = pries - len(knygos)
        if istrintos > 0:
            self.knygos = knygos
            self.issaugoti_biblioteka(knygos)
            print(f"Istrintos {istrintos} knygos, isleistos iki {metai}.")
        else:
            print(f"Nerasta knygu, isleistu iki {metai}.")

    def rodyti_vartotoju_knygas(self, vartotojai):
        if not vartotojai:
            print("Nera uzregistruotu vartotoju.")
            return
        print("\n Vartotoju pasiimtos knygos:")
        for vartotojas in vartotojai:
            print(f"{vartotojas.vardas} {vartotojas.pavarde}:")
            if vartotojas.pasiimtos_knygos:
                for info in vartotojas.pasiimtos_knygos.values():
                    knyga = info['knyga']
                    kiekis = info['kiekis']
                    print(f" {knyga.autorius} - {knyga.pavadinimas} | {knyga.isleidimo_metai} | {knyga.zanras} | Kiekis: {kiekis}")
            else:
                print("  Nera pasiimtu knygu.")


class Vartotojas:
    def __init__(self, vardas, pavarde, knygu_limitas=2, biblioteka=None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pasiimtos_knygos = {}  # knygos, kurias pasieme vartotojas
        self.veluojancios_knygos = []
        self.knygu_limitas = knygu_limitas
        self.bibliotekos_objektas = biblioteka  # biblioteka, kurioje vartotojas registruotas
        
        
    def __str__(self):
        return f"{self.vardas} {self.pavarde} - {len(self.pasiimtos_knygos)} knygos, {len(self.veluojancios_knygos)} vėluojančios knygos"

    def viso_knygu(self):
        return sum(info['kiekis'] for info in self.pasiimtos_knygos.values())
    

    def velavimas(self):
        veluojancios_knygos = []
        dabar = datetime.now()
        for info in self.pasiimtos_knygos.values():
            grazinimo_data = info['knyga'].grazinimo_data
            if grazinimo_data < dabar:
                veluojancios_knygos.append(info['knyga'])
        
        if veluojancios_knygos:
            print(f"\nVėluojančios knygos: {', '.join([knyga.pavadinimas for knyga in veluojancios_knygos])}")
        else:
            print("Nėra vėluojančių knygų.")
    #knygu velavimo testavimas
    def testuoti_velavima(vartotojas):
        if not vartotojas.pasiimtos_knygos:
            print("Vartotojas neturi pasiimtų knygų testavimui.")
            return
        for info in vartotojas.pasiimtos_knygos.values():
            info['knyga'].grazinimo_data = datetime.now() - timedelta(days=3)
        print("Testavimo režimas: visų knygų grąžinimo laikas nustatytas į praeitį (vėlavimas).")



        vartotojas.velavimas()





    def pasiimti_knyga(self, knyga, kiekis=1):
        dabar = datetime.now()
        if self.veluojancios_knygos:
            print(f"Negalite pasiimti knygos, nes turite veluojanciu knygu.")
            for veluojanti_knyga in self.veluojancios_knygos:
                print(f"{veluojanti_knyga.pavadinimas}, turi buti grazinta iki {veluojanti_knyga.grazinimo_data}")
            return
        grazinimo_data = dabar + timedelta(days=14)  # knyga turi buti grazinta po 14 dienu
        knyga.pasiemimas(dabar)
        knyga.nustatyti_grazinimo_data(grazinimo_data)
            
        if self.viso_knygu() + kiekis > self.knygu_limitas:
            print(f"Pasiekta knygu riba. Negalite pasiimti daugiau nei {self.knygu_limitas} knygu.")
            return
        if knyga.kiekis < kiekis:
            print(f"Nera tiek knygu '{knyga.pavadinimas}'.")
            return
        knyga.kiekis -= kiekis
        if knyga.pavadinimas in self.pasiimtos_knygos:
            self.pasiimtos_knygos[knyga.pavadinimas]['kiekis'] += kiekis
        else:
            self.pasiimtos_knygos[knyga.pavadinimas] = {'knyga': knyga, 'kiekis': kiekis}
        print(f"Knyga '{knyga.pavadinimas}' pasiimta {kiekis} vnt.")
        self.bibliotekos_objektas.issaugoti_biblioteka(self.bibliotekos_objektas.knygos)
        issaugoti_vartotojus

    def grazinti_knyga(self, pavadinimas, kiekis=1):
        if pavadinimas in self.pasiimtos_knygos:
            paimtas_kiekis = self.pasiimtos_knygos[pavadinimas]['kiekis']

            for info in self.pasiimtos_knygos.values():
                knyga = info["knyga"]
                if knyga.grazinimo_data and knyga.grazinimo_data < datetime.now():
                    self.veluojancios_knygos.append(knyga)
                    print(f"Jus veluojate su knyga '{knyga.pavadinimas}'. Grazinkite ja greitai.")

            #pasalina is vartotojo
            if paimtas_kiekis <= kiekis:
                del self.pasiimtos_knygos[pavadinimas]
            else:
                self.pasiimtos_knygos[pavadinimas]['kiekis'] -= kiekis
            for knyga in self.bibliotekos_objektas.knygos:
                if knyga.pavadinimas.lower() == pavadinimas.lower():
                    knyga.kiekis += kiekis
                    print(f"Knyga '{pavadinimas}' grazinta {kiekis} vnt.")
                    self.bibliotekos_objektas.issaugoti_biblioteka(self.bibliotekos_objektas.knygos)
                    return
            print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")
        else:
            print(f"Knyga '{pavadinimas}' nerasta pasiimtu knygu sarase.")    
            self.bibliotekos_objektas.issaugoti_biblioteka(self.bibliotekos_objektas.knygos)
            issaugoti_vartotojus(self.bibliotekos_objektas.vartotojai)

            

    def rodyti_knygas(self):
        if not self.pasiimtos_knygos:
            print("Nera pasiimtu knygu.")
            return
        print(f"Pasiimtos knygos:")
        for info in self.pasiimtos_knygos.values():
            print(f"{info['knyga']} | Kiekis: {info['kiekis']}")

    def rodyti_bibliotekos_knygas(self):
        if not self.bibliotekos_objektas or not self.bibliotekos_objektas.knygos:
            print("Biblioteka nera nustatyta.")
            return
        print(f"Bibliotekos knygos:")
        for knyga in self.bibliotekos_objektas.knygos:
            print(knyga)




def issaugoti_vartotojus(vartotojai):
    try:
        with open(vartotoju_failas, "wb") as f:
            pickle.dump(vartotojai, f)
    except Exception as e:
        print(f"Klaida issaugant vartotojus: {e}")
    
def ikelti_vartotojus():
    if os.path.exists(vartotoju_failas):
        with open(vartotoju_failas, "rb") as f:
            return pickle.load(f)
    return []

def registruoti_vartotoja(biblioteka, vartotojai):
    vardas = input("Iveskite varda: ")
    if vardas in vartotojai:
        print("Vartotojas jau egzistuoja.")
        return
    pavarde = input("Iveskite pavarde: ")
    slaptazodis = input("Iveskite slaptazodi: ")
    vartotojas = Vartotojas(vardas, pavarde, biblioteka=biblioteka)
    vartotojas.slaptazodis = slaptazodis
    vartotojai.append(vartotojas)
    issaugoti_vartotojus(vartotojai)
    print(f"Vartotojas '{vardas}' uzregistruotas.")
    

def prisijungti(vartotojai, biblioteka):
    vardas = input("Iveskite varda: ")
    for vartotojas in vartotojai:
        if vartotojas.vardas == vardas:
            slaptazodis = input("Iveskite slaptažodi: ")
            if vartotojas.slaptazodis != slaptazodis:
                print("Neteisingas slaptažodis.")
                return None
            print(f"\nSveiki atvykę, {vardas}!")
            vartotojas.bibliotekos_objektas = biblioteka
            return vartotojas
    print("Vartotojas nerastas.")
    return None

BIBLIOTEKOS_SLAPTAZODIS = "admin123"

def prisijungti_biblioteka():
    slaptazodis = input("Iveskite bibliotekos slaptažodi: ")
    if slaptazodis != BIBLIOTEKOS_SLAPTAZODIS:
        print("Neteisingas slaptažodis.")
        return False
    return True


#vartotojo meniu
def vartotojo_meniu(vartotojas):
    while True:
        print("\nPasirinkite veiksma:")
        print("1. Pasiimti knyga")
        print("2. Grazinti knyga")
        print("3. Rodyti pasiimtas knygas")
        print("4. Rodyti vėluojančias knygas")
        print("5. Rodyti bibliotekos knygas")
        print("6. Testuoti vėlavimą")
        print("7. Iseiti")
        pasirinkimas = input("Pasirinkimas: ")

        if pasirinkimas == "1":
            pavadinimas = input("Iveskite knygos pavadinima:")
            try:
                kiekis = int(input("Iveskite knygos kieki:"))
            except ValueError:
                print("Kiekis turi buti skaicius. Bandykite dar karta.")
                continue
            for knyga in vartotojas.bibliotekos_objektas.knygos:
                if knyga.pavadinimas.lower() == pavadinimas.lower():
                    vartotojas.pasiimti_knyga(knyga, kiekis)
                    break
            else:
                print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")
        elif pasirinkimas == "2":
            pavadinimas = input("Iveskite knygos pavadinima:")
            try: 
                kiekis = int(input("Iveskite knygos kieki:"))
            except ValueError:
                print("Kiekis turi buti skaicius. Bandykite dar karta.")
                continue
            vartotojas.grazinti_knyga(pavadinimas, kiekis)
        elif pasirinkimas == "3":
            vartotojas.rodyti_knygas()
        elif pasirinkimas == "4":
            vartotojas.velavimas()
        elif pasirinkimas == "5":
            vartotojas.rodyti_bibliotekos_knygas()
        elif pasirinkimas == "6":
            vartotojas.testuoti_velavima()
            print("Vėlavimo testavimas atliktas.")
        elif pasirinkimas == "7":
            break
        else:
            print("Neteisingas pasirinkimas, bandykite dar karta.")
        
        

def biblioteka_meniu(biblioteka, vartotojai):

    while True:
        print("\nPasirinkite veiksma:")
        print("1. Prideti knyga")
        print("2. Rodyti visas knygas")
        print("3. Ieskoti knygos")
        print("4. Istrinti knyga")
        print("5. Ivesti metus iki kuriu knygos bus istrintos")
        print("6. Rodyti vartotoju paimtas knygas")
        print("7. Rodyti vėluojančias knygas")
        print("8. Iseiti")

        pasirinkimas = input("Pasirinkimas: ")
        
        if pasirinkimas == "1":
            pavadinimas = input("Knygos pavadinimas: ")
            autorius = input("Autorius: ")
            isleidimo_metai = input("Isleidimo metai: ")
            zanras = input("Zanras: ")
            try:
                kiekis = int(input("Kiekis: "))
            except ValueError:
                print("Kiekis turi buti skaicius. Bandykite dar karta.")
                continue
            knyga = Knyga(pavadinimas, autorius, isleidimo_metai, zanras, kiekis)
            biblioteka.prideti_knyga(knyga)
        elif pasirinkimas == "2":
            biblioteka.rodyti_knygas()
        elif pasirinkimas == "3":
            pavadinimas = input("Ieskoti knygos pavadinimo: ")
            biblioteka.ieskoti_knyga(pavadinimas)
        elif pasirinkimas == "4":
            pavadinimas = input("Istrinti knygos pavadinima: ")
            try:
                kiekis = int(input("Kiekis: "))
            except ValueError:
                print("Kiekis turi buti skaicius. Bandykite dar karta.")
                continue
            biblioteka.istrinti_knyga(pavadinimas, kiekis)
            print(f"Knyga pavadinimu '{pavadinimas}' '{kiekis}' vnt buvo istrinta.")
        elif pasirinkimas == "5":
            try:
                metai = int(input("Iveskite metus iki kuriu knygos bus istrintos: "))
                biblioteka.istrinti_knygas_pagal_metus(metai)
            except ValueError:
                print("Metai turi buti skaicius. Bandykite dar karta.")
                continue
        elif pasirinkimas == "6":
            vartotojai = ikelti_vartotojus()
            biblioteka.rodyti_vartotoju_knygas(vartotojai)
        elif pasirinkimas == "7":
            vartotojai = ikelti_vartotojus()
            for vartotojas in vartotojai:
                vartotojas.velavimas()
        elif pasirinkimas == "8":
            break
        else:
            print("Neteisingas pasirinkimas, bandykite dar karta.")




#pagrindine funkcija
def run():
    biblioteka = Biblioteka("biblioteka.pkl")
    vartotojai = ikelti_vartotojus()

    print(f"\nSveiki atvyke i biblioteka!!!")

    try:
        while True:
            print("\nPasirinkite veiksma:")
            print("1. Registracija")
            print("2. Vartotojo prisijungimas")
            print("3. Bibliotekos prisijungimas")
            print("4. Iseiti")

            pasirinkimas = input("Pasirinkimas: ")
            
            if pasirinkimas == "1":
                registruoti_vartotoja(biblioteka, vartotojai)
            elif pasirinkimas == "2":
                vartotojas = prisijungti(vartotojai, biblioteka)
                if vartotojas:
                    vartotojo_meniu(vartotojas)
                    issaugoti_vartotojus(vartotojai)
            elif pasirinkimas == "3":
                if prisijungti_biblioteka():
                    biblioteka_meniu(biblioteka, vartotojai)
                else:
                    print("Neteisingas slaptažodis.")
            elif pasirinkimas == "4":
                print("Iseinate is programos.")
                break
            else:
                print("Neteisingas pasirinkimas, bandykite dar karta.")
    finally:
        print("Isaugomi duomenys pries iseinant.")
        biblioteka.issaugoti_biblioteka(biblioteka.knygos)
        issaugoti_vartotojus(vartotojai)

run()
        






