
import datetime
import pickle
import os

# Knygos klasė
class Knyga:
    def __init__(self, pavadinimas, autorius, isleidimo_metai, zanras, kiekis=1):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras
        self.kiekis = kiekis

    def __str__(self):
        return f"{self.autorius} - {self.pavadinimas} | {self.isleidimo_metai} | {self.zanras} | Kiekis: {self.kiekis}"

# Vartotojo klasė
class Vartotojas:
    def __init__(self, vardas, korteles_numeris):
        self.vardas = vardas
        self.korteles_numeris = korteles_numeris
        self.paskolintos_knygos = []  # [{"pavadinimas":..., "gražinti_iki": ...}]

    def __str__(self):
        return f"{self.vardas} - {self.korteles_numeris}"

# Bibliotekos klasė
class Biblioteka:
    def __init__(self):
        self.knygos = []  # Saugo knygas
        self.vartotojai = {}  # Saugo vartotojus
        self.load_data()

    def load_data(self):
        """Užkrauna knygas ir vartotojus iš failų."""
        if os.path.exists("knygos.pkl"):
            with open("knygos.pkl", "rb") as f:
                self.knygos = pickle.load(f)
        if os.path.exists("vartotojai.pkl"):
            with open("vartotojai.pkl", "rb") as f:
                self.vartotojai = pickle.load(f)

    def save_data(self):
        """Išsaugo knygas ir vartotojus į failus."""
        with open("knygos.pkl", "wb") as f:
            pickle.dump(self.knygos, f)
        with open("vartotojai.pkl", "wb") as f:
            pickle.dump(self.vartotojai, f)

    def prideti_knyga(self, knyga):
        """Pridėti knygą į biblioteką."""
        self.knygos.append(knyga)
        self.save_data()
        print(f"Knyga '{knyga.pavadinimas}' pridėta į biblioteką.")

    def pasalinti_senas_knygas(self, iki_metai):
        """Pašalina senas knygas, kurių išleidimo metai mažesni nei nurodyti."""
        self.knygos = [k for k in self.knygos if k.isleidimo_metai >= iki_metai]
        self.save_data()
        print(f"Pašalintos knygos, išleistos iki {iki_metai} metų.")

    def uzsakyti_knyga(self, vartotojas, pavadinimas):
        """Leidžia vartotojui pasiimti knygą, jei jos yra ir jei nėra vėluojančių knygų."""
        today = datetime.date.today()
        if vartotojas.korteles_numeris in self.vartotojai:
            for knyga in self.vartotojai[vartotojas.korteles_numeris]:
                if datetime.date.fromisoformat(knyga["gražinti_iki"]) < today:
                    print(f"Negalite pasiimti knygos, nes turite vėluojančią knygą: {knyga['pavadinimas']}")
                    return

        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas and knyga.kiekis > 0:
                knyga.kiekis -= 1
                grazinti_iki = today + datetime.timedelta(days=14)
                if vartotojas.korteles_numeris not in self.vartotojai:
                    self.vartotojai[vartotojas.korteles_numeris] = []
                self.vartotojai[vartotojas.korteles_numeris].append({
                    "pavadinimas": pavadinimas,
                    "gražinti_iki": grazinti_iki.isoformat()
                })
                self.save_data()
                print(f"Knyga '{pavadinimas}' išduota '{vartotojas.vardas}' iki {grazinti_iki}")
                return

        print(f"Negalima pasiimti knygos '{pavadinimas}'. Nėra jos ar nepakanka kiekio.")

    def rodyti_knygas(self):
        """Parodo visas bibliotekoje esančias knygas."""
        if not self.knygos:
            print("Biblioteka tuščia.")
        else:
            for knyga in self.knygos:
                print(knyga)

    def ieskoti_knygos(self, paieska):
        """Ieško knygų pagal pavadinimą arba autorių."""
        rezultatai = [k for k in self.knygos if paieska.lower() in k.pavadinimas.lower() or paieska.lower() in k.autorius.lower()]
        if rezultatai:
            for k in rezultatai:
                print(k)
        else:
            print("Nerasta tokių knygų.")

    def rodyti_veluojancias(self):
        """Parodo vėluojančias knygas."""
        today = datetime.date.today()
        vėluojančios = False
        for kortele, knygos in self.vartotojai.items():
            for kn in knygos:
                data = datetime.date.fromisoformat(kn["gražinti_iki"])
                if data < today:
                    print(f"Vartotojas {kortele} vėluoja grąžinti knygą: {kn['pavadinimas']} (gražinti iki {kn['gražinti_iki']})")
                    vėluojančios = True
        if not vėluojančios:
            print("Nėra vėluojančių knygų.")

# Prisijungimo sistema
def prisijungti_bibliotekininkas():
    """Bibliotekininko prisijungimo funkcija."""
    username = input("Įveskite naudotojo vardą: ")
    password = input("Įveskite slaptažodį: ")
    if username == "bibliotekininkas" and password == "slaptas":
        return True
    print("Netinkamas vardas arba slaptažodis.")
    return False

# Testavimas
if __name__ == "__main__":
    biblioteka = Biblioteka()

    while True:
        pasirinkimas = input("\n1. Pridėti knygą\n2. Pašalinti senas knygas\n3. Užsakyti knygą\n4. Ieškoti knygos\n5. Rodyti knygas\n6. Rodyti vėluojančias knygas\n7. Išeiti\nPasirinkite: ")

        if pasirinkimas == "1":
            if prisijungti_bibliotekininkas():
                pavadinimas = input("Įveskite knygos pavadinimą: ")
                autorius = input("Įveskite knygos autorių: ")
                isleidimo_metai = int(input("Įveskite knygos išleidimo metus: "))
                zanras = input("Įveskite knygos žanrą: ")
                knyga = Knyga(pavadinimas, autorius, isleidimo_metai, zanras)
                biblioteka.prideti_knyga(knyga)

        elif pasirinkimas == "2":
            if prisijungti_bibliotekininkas():
                iki_metai = int(input("Įveskite metus, iki kurių norite pašalinti knygas: "))
                biblioteka.pasalinti_senas_knygas(iki_metai)

        elif pasirinkimas == "3":
            korteles_numeris = input("Įveskite savo skaitytojo kortelės numerį: ")
            vartotojas = Vartotojas("Skaitytojas", korteles_numeris)
            pavadinimas = input("Įveskite knygos pavadinimą, kurią norite pasiimti: ")
            biblioteka.uzsakyti_knyga(vartotojas, pavadinimas)

        elif pasirinkimas == "4":
            paieska = input("Įveskite knygos pavadinimą arba autorių: ")
            biblioteka.ieskoti_knygos(paieska)

        elif pasirinkimas == "5":
            biblioteka.rodyti_knygas()

        elif pasirinkimas == "6":
            biblioteka.rodyti_veluojancias()

        elif pasirinkimas == "7":
            print("Išeinate iš programos.")
            break



































