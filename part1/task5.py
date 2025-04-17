
import os
from datetime import datetime


# with open("Tekstas1.txt", "w", encoding="UTF=8") as failas:
#     print(failas.read())

#################################################################################################################
# dabartine_data = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# with open("Tekstas1.txt", "a", encoding="UTF=8") as failas:
#     failas.write("\n" + dabartine_data)

########################################################################################################
# with open("Tekstas1.txt", "r", encoding="UTF=8") as failas:
#     eilutes = failas.readlines()
    
# sunumeruotos_eilutes = [f"{index + 1}: {eilute}" for index, eilute in enumerate(eilutes)]    

# with open("Tekstas1.txt", "w", encoding="UTF=8") as failas:
#     failas.writelines(sunumeruotos_eilutes)

########################################################################################################

# with open("Tekstas1.txt", "r+", encoding="UTF-8") as failas:
#     eilutes = failas.readlines()

# for index, eilute in enumerate(eilutes):
#     if "Beautiful is better than ugly" in eilute:
#         eilutes[index] = eilute.replace("Beautiful is better than ugly", "Gražus yra geriau už bjauru")
# with open("Tekstas1.txt", "w", encoding="UTF-8") as failas:
#     failas.writelines(eilutes)

########################################################################################################

# with open("Tekstas1.txt", "r", encoding="UTF-8") as failas:
#     failo_turinys = failas.read()

#     print(failo_turinys[::-1])

################################################################################################



# def skaiciuoti_failo_turini(failo_pavadinimas):
#     with open(failo_pavadinimas, "r", encoding="UTF-8") as failas:
#         turinys = failas.read()  

#     zodziai = turinys.split()  
  
#     skaiciai = [zodis for zodis in zodziai if zodis.isdigit()]

#     didziosios_raides = sum(1 for simbolis in turinys if simbolis.isupper())  
#     mazosios_raides = sum(1 for simbolis in turinys if simbolis.islower())  

#     return len(zodziai), len(skaiciai), didziosios_raides, mazosios_raides


# failo_pavadinimas = "Tekstas1.txt"  
# zodziu, skaiciu, didziosios, mazosios = skaiciuoti_failo_turini(failo_pavadinimas)

# print(f"Žodžių skaičius: {zodziu}")
# print(f"Skaičių skaičius: {skaiciu}")
# print(f"Didžiųjų raidžių skaičius: {didziosios}")
# print(f"Mažųjų raidžių skaičius: {mazosios}")
  
 
####################################################################################################


# def kopijuoti_didziosiomis(failo_pavadinimas, naujas_failas):

#     with open(failo_pavadinimas, "r", encoding="UTF-8") as failas:
#         turinys = failas.read()

    
#     turinys_didziosiomis = turinys.upper()


#     with open(naujas_failas, "w", encoding="utf-8") as failas:
#         failas.write(turinys_didziosiomis)


# failo_pavadinimas = "Tekstas1.txt" 
# naujas_failas = "Tekstas1_didziosiomis.txt" 
# kopijuoti_didziosiomis(failo_pavadinimas, naujas_failas)

#####################################################################################################
                                                        
                                                        
                                                        
                                                        # 2 uzduotis

##############################################################################################################


# eiluciu_kiekis = int(input("Iveskite kiek eiluciu norite sukurti: "))

# with open("Naujas.txt", "w", encoding="UTF-8") as failas:
#     for i in range(eiluciu_kiekis):
#         eilute = input(f"Iveskite {i + 1} eilute: ")
#         failas.write(eilute + "\n")
        
# ####################################################################################################################
    
# with open("Naujas.txt", "a", encoding="UTF-8") as failas:
#     print("Iveskite teksta, noredami baigti rasykite 'baigti':")
#     while True:
#         eilute = input("Iveskite teksta: ")
#         if eilute.lower() == "baigti":
#             break

#         failas.write(eilute + "\n")
# print("Tekstas irasytas i faila.")        

##################################################################################################################


# def sukurti_faila():
#     # Paprasome vartotojo ivesti failo pavadinima
#     pavadinimas = input("Iveskite failo pavadinima, jeigu pavadinima sudaro keli zodziai, juos reikia atskirti _ zenklu (pvz.: failas.txt, mano_failas.txt): ")

#     # Tikriname, ar pavadinimas baigiasi ".txt"
#     if not pavadinimas.endswith(".txt"):
#         print("Failo pavadinimas turi baigtis '.txt'.")
#         return  # Baigiame funkcija, jei pavadinimas neteisingas

#     # Sukuriame ir atidarome faila rasymui
#     try:
#         with open(pavadinimas, 'w') as failas:
#             failas.write("Sveikinu, susikuriai savo nuosava faila!!!")  # Irašome teksta i faila
#         print(f"Failas '{pavadinimas}' buvo sukurtas su tekstu.")
#     except Exception as e:
#         print(f"Ivyko klaida kuriant faila: {e}")

# # Iskvieciame funkcija
# sukurti_faila()

###################################################################################################################################


                                                       # 3 uzduotis


import os
from datetime import datetime

# def katalogas():
#     # Darbalaukyje sukuriame folderi "Naujas Katalogas"
#     katalogas = os.path.join(os.path.expanduser("~"), "Desktop", "Naujas Katalogas")

#     if not os.path.exists(katalogas):
#         os.makedirs(katalogas)
#         print(f"Katalogas '{katalogas}' buvo sukurtas.")           
#     else:
#         print(f"Katalogas '{katalogas}' jau egzistuoja.")

#     return katalogas  # Graziname katalogo kelia, kad toliau galetume jame sukurti faila

# def sukurti_faila(katalogas):
#     # siandienos data
#     siandienos_data = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
#     # sukuriame failo pilna kelia
#     failo_pavadinimas = "failas.txt"
#     failo_kelias = os.path.join(katalogas, failo_pavadinimas)

#     try:
#         # Patikriname, ar failas jau egzistuoja
#         os.stat(failo_kelias)
#         print(f"Failas '{failo_kelias}' jau egzistuoja.")
#     except FileNotFoundError:
#         # sukuriame faila, jei jis dar neegzistuoja
#         with open(failo_kelias, "w") as failas:
#             failas.write("Failas buvo sukurtas\n")
#             failas.write(siandienos_data + "\n")
#             print(f"Failas '{failo_kelias}' buvo sukurtas.")

# # funkcijos iskvietimas
# katalogas_kelias = katalogas()  # sukuriame kataloga ir graziname jo kelia
# sukurti_faila(katalogas_kelias)  # sukuriame faila kataloge

###########################################################################################################


# failo_pavadinimas = "failas.txt"
# failo_kelias = os.path.join(os.path.expanduser("~"), "Desktop/Naujas Katalogas", failo_pavadinimas)

# # Atspausdinkite tikrinamą kelią
# print(f"Bandome rasti failą šiame kelyje: {failo_kelias}")

# # Patikriname, ar failas egzistuoja
# if os.path.exists(failo_kelias):
#     # Gauti failo informaciją
#     failo_info = os.stat(failo_kelias)
    
#     # Gauti failo dydį baitais
#     failo_dydis = failo_info.st_size
    
#     # Gauti failo sukūrimo laiką (st_ctime) ir konvertuoti į žmogui skaitomą datą
#     sukurimo_data_timestamp = failo_info.st_ctime
#     sukurimo_data = datetime.fromtimestamp(sukurimo_data_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
#     # Išvedame failo sukūrimo datą ir dydį baitais
#     print(f"Failo sukūrimo data: {sukurimo_data}")
#     print(f"Failo dydis: {failo_dydis} baitai")
# else:
#     print(f"Failas '{failo_kelias}' neegzistuoja.")

############################################################################################################################################    
                                                 
                                                 
                                                 #uzduotis 4


#########################################################################################################################


import pickle

# Funkcija, kuri nuskaito vartotoju duomenis is failo
def nuskaityti_vartotojus():
    try:
        with open('vartotojai.pkl', 'rb') as f:  # Nuskaitome vartotoju duomenis iš Pickle failo
            vartotojai = pickle.load(f)
        return vartotojai
    except FileNotFoundError:
        return {}  # Jei failo nera, graziname tuscia zodyna

# Funkcija, kuri issaugos vartotoju duomenis i faila
def issaugoti_vartotojus(vartotojai):
    with open('vartotojai.pkl', 'wb') as f:
        pickle.dump(vartotojai, f)
#-----------------------------------------------------------------------------------------------------------------
# Funkcija, kuri leidzia vartotojui uzsiregistruoti
def registracija():
    vartotojai = nuskaityti_vartotojus()

    while True:
        vardas = input("Iveskite vartotojo varda: ")
        if vardas in vartotojai:
            print("Vartotojas su tokiu vardu jau egzistuoja.")
        else:
            slapta = input("Iveskite slaptazodi: ")
            vartotojai[vardas] = {"password": slapta, "name": vardas}
            issaugoti_vartotojus(vartotojai)
            print(f"Vartotojas {vardas} buvo sukurtas.")
            break

# Funkcija, kuri leidzia vartotojui prisijungti
def prisijungimas():
    vartotojai = nuskaityti_vartotojus()

    while True:
        vardas = input("Iveskite vartotojo varda: ")
        if vardas in vartotojai:
            slapta = input("Iveskite slaptazodi: ")
            if slapta == vartotojai[vardas]["password"]:
                print(f"Vartotojas {vardas} prisijunge sekmingai.")
                return vardas  # Graziname prisijungusi vartotoja
            else:
                print("Neteisingas slaptazodis.")
        else:
            print("Vartotojas nerastas.")

# Funkcija, kuri leidzia vartotojui pasirinkti, ar registruotis, ar prisijungti
def prisijungimo_meniu():
    while True:
        pasirinkimas = input("Pasirinkite veiksma: 1. Registracija, 2. Prisijungimas, 3. Iseiti: ")
        if pasirinkimas == '1':
            registracija()
        elif pasirinkimas == '2':
            return prisijungimas()
        elif pasirinkimas == '3':
            print("Programa baigta.")
            break
        else:
            print("Netinkamas pasirinkimas. Prasome pasirinkti 1-3.")
#--------------------------------------------------------------------------------------------------------------------------
# Funkcija, kuri nuskaito biudzeto duomenis pagal vartotojo varda
def nuskaitymas(vartotojas):
    try:
        failo_pavadinimas = f'biudzetas_{vartotojas}.pkl'
        with open(failo_pavadinimas, 'rb') as f:
            duomenys = pickle.load(f)
        return duomenys
    except FileNotFoundError:
        return []  # Jei failas neegzistuoja, grazina tuscia sarasa

# Funkcija, kuri issaugos biudzeto duomenis pagal vartotojo varda
def issaugoti(vartotojas, duomenys):
    failo_pavadinimas = f'biudzetas_{vartotojas}.pkl'
    with open(failo_pavadinimas, 'wb') as f:
        pickle.dump(duomenys, f)
#--------------------------------------------------------------------------------------------------------------------------
# Biudzeto funkcija
def biudzetas(vartotojas):
    duomenys = nuskaitymas(vartotojas)  # Paimame duomenis pagal vartotojo varda

    while True:
        print("\nPasirinkite veiksma:")
        print("1. Ivesti pajamas ar islaidas")
        print("2. Rodyti biudzeto balansa")
        print("3. Rodyti biudzeto ataskaita")
        print("4. Iseiti iš programos")

        pasirinkimas = input("Pasirinkite veiksma (1-4): ")

        if pasirinkimas == '1':
            ivestis = input("Iveskite pajamas ar islaidas (pvz.: 500 arba -100): ")
            if ivestis.lower() == 'baigti':
                break

            try:
                suma = float(ivestis)  # Bandome konvertuoti ivesti i skaiciu
                duomenys.append(suma)  # Irasome i sarasa
                issaugoti(vartotojas, duomenys)  # Issaugome duomenis i Pickle faila pagal vartotojo varda
                balansas = sum(duomenys)  # Apskaiciuojame balansa
                print(f"\nAtnaujintas biudzetas: {balansas:.2f} EUR")
            except ValueError:
                print("Neteisinga ivestis. Prasome ivesti skaiciu.")

        elif pasirinkimas == '2':
            balansas = sum(duomenys)
            print(f"\nBendras biudzetas: {balansas:.2f} EUR")
        elif pasirinkimas == '3':
            print("\nBiudzeto ataskaita:")
            if duomenys:
                for suma in duomenys:
                    tipas = "Pajamos" if suma > 0 else "Islaidos"
                    print(f"{tipas}: {suma:.2f} EUR")
            else:
                print("Nera ivestu duomenu.")
        elif pasirinkimas == '4':
            print("Programa baigta.")
            break
        else:
            print("Neteisingas pasirinkimas. Prasome pasirinkti 1-4.")

# Pagrindine programa
def main():
    vartotojas = prisijungimo_meniu()  # Vartotojas pasirinks registracija arba prisijungima
    biudzetas(vartotojas)  # Pereiname i biudzeto valdyma po prisijungimo

if __name__ == '__main__':
    main()

    

            




































