import pickle

# Funkcija, kuri nuskaito vartotojų duomenis iš failo
def nuskaityti_vartotojus():
    try:
        with open('vartotojai.pkl', 'rb') as f:
            vartotojai = pickle.load(f)
        return vartotojai
    except FileNotFoundError:
        return {}

# Funkcija, kuri išsaugo vartotojų duomenis į failą
def issaugoti_vartotojus(vartotojai):
    with open('vartotojai.pkl', 'wb') as f:
        pickle.dump(vartotojai, f)

# Funkcija registracijai2
def registracija():
    vartotojai = nuskaityti_vartotojus()

    while True:
        vardas = input("Įveskite vartotojo vardą: ")
        if vardas in vartotojai:
            print("Vartotojas su tokiu vardu jau egzistuoja.")
        else:
            slapta = input("Įveskite slaptažodį: ")
            vartotojai[vardas] = {"password": slapta, "name": vardas}
            issaugoti_vartotojus(vartotojai)
            print(f"Vartotojas {vardas} buvo sukurtas.")
            break

# Funkcija prisijungimui
def prisijungimas():
    vartotojai = nuskaityti_vartotojus()

    while True:
        vardas = input("Įveskite vartotojo vardą: ")
        if vardas in vartotojai:
            slapta = input("Įveskite slaptažodį: ")
            if slapta == vartotojai[vardas]["password"]:
                print(f"Vartotojas {vardas} prisijungė sėkmingai.")
                return vardas  # Grąžina prisijungusį vartotoją
            else:
                print("Neteisingas slaptažodis.")
        else:
            print("Vartotojas nerastas.")

# Meniu pasirinkimų funkcija
def prisijungimo_meniu():
    while True:
        pasirinkimas = input("Pasirinkite veiksmą: 1. Registracija, 2. Prisijungimas, 3. Išeiti: ")
        if pasirinkimas == '1':
            registracija()
        elif pasirinkimas == '2':
            return prisijungimas()
        elif pasirinkimas == '3':
            print("Programa baigta.")
            break
        else:
            print("Netinkamas pasirinkimas. Prašome pasirinkti 1-3.")

# Funkcija, kuri nuskaito biudžeto duomenis
def nuskaitymas(vartotojas):
    try:
        failo_pavadinimas = f'biudzetas_{vartotojas}.pkl'
        with open(failo_pavadinimas, 'rb') as f:
            duomenys = pickle.load(f)
        return duomenys
    except FileNotFoundError:
        return []  # Jei failas neegzistuoja, grąžina tuščią sąrašą

# Funkcija, kuri išsaugos biudžeto duomenis
def issaugoti(vartotojas, duomenys):
    failo_pavadinimas = f'biudzetas_{vartotojas}.pkl'
    with open(failo_pavadinimas, 'wb') as f:
        pickle.dump(duomenys, f)

# Klasių definicijos

class Irasas:
    def __init__(self, pajamos, suma):
        self.pajamos = pajamos
        self.suma = suma

    def __str__(self):
        return f"{self.pajamos}: {self.suma} EUR"

class Pajamos(Irasas):
    def __init__(self, suma, siuntejas=None):
        super().__init__("Pajamos", suma)
        self.siuntejas = siuntejas

    def papildoma_informacija(self):
        if not self.siuntejas:
            self.siuntejas = input("Įveskite papildomą informaciją apie siuntėją: ")

    def __str__(self):
        return f"{self.pajamos}: {self.suma} EUR, Siuntėjas: {self.siuntejas if self.siuntejas else 'Nenurodyta'}"

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

# Biudžeto klasė
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

# Programos pradžia
def run():
    vartotojas = prisijungimo_meniu()  # Prisijungimas arba registracija
    biudzetas = Biudzetas()

    # Nuskaitome vartotojo biudžeto duomenis
    biudzetas_duomenys = nuskaitymas(vartotojas)
    biudzetas.zurnalas = biudzetas_duomenys

    while True:
        print("\n--------Biudžeto valdymo programa-----------")
        print("1. Pridėti pajamas")
        print("2. Pridėti išlaidas")
        print("3. Gauti balansą")
        print("4. Parodyti ataskaitą")
        print("5. Išeiti")

        pasirinkimas = input("Pasirinkite veiksmą (1-5): ")
        
        try:
            if pasirinkimas == "1":
                suma = float(input("Įveskite pajamų sumą: "))
                biudzetas.prideti_pajamu_irasa(suma)
                print(f"Pajamos {suma:.2f} EUR buvo pridėtos.")
            elif pasirinkimas == "2":
                suma = float(input("Įveskite išlaidų sumą: "))
                biudzetas.prideti_islaidu_irasa(suma)
                print(f"Išlaidos {suma:.2f} EUR buvo pridėtos.")
            elif pasirinkimas == "3":
                balansas = biudzetas.gauti_balansa()
                print(f"Balansas: {balansas:.2f} EUR")
            elif pasirinkimas == "4":
                biudzetas.parodyti_ataskaita()
            elif pasirinkimas == "5":
                # Išsaugome vartotojo biudžeto duomenis
                issaugoti(vartotojas, biudzetas.zurnalas)
                print("Išeinate iš programos. Iki pasimatymo!")
                break
            else:
                print("Neteisingas pasirinkimas. Prašome pasirinkti skaičių nuo 1 iki 5.")
        except ValueError:
            print("Klaida: Prašome įvesti teisingą skaičių.")


run()




