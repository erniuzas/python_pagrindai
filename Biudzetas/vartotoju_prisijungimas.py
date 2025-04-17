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