                                                    #   Uzduotis 1

# 1
# def skaiciu_suma(x, y, z):
#     suma = x + y + z
#     return suma
    
# skaiciu_suma_result = skaiciu_suma(5, 9, 7)
# print(skaiciu_suma_result)

# 2

# def spausdinimas(*args):
#     suma = 0
#     for number in args:
#         print(number)
#         suma += number
#     print(f"Suma: {suma}")

# spausdinimas(5,6,7,2,8,7,2)

# 3
# def spausdinimas(*args):
#     largest_number = max(args)
#     print(f"Didziausias skaicius: {largest_number}")

# spausdinimas(5,6,7,2,8,7,2,8)

# 4

# def spausdinimas(x):
#     reversed = x[::-1]
#     print(reversed)

# spausdinimas("Labas")

# 5

# def teksto_manipuliacija(text: str, to_upper: bool = False, to_lower: bool = False, word_count: bool = False) -> str:
#     words = text.split()
#     word_count_result = len(words) if word_count else None  # skaiciuoja zodzius, jei word_count yra True

#     if to_upper:
#         text = text.upper()
#     if to_lower:
#         text = text.lower()
    
#     if word_count:
#         return text, word_count_result
#     else:
#         return text
# print(teksto_manipuliacija("Labas, kaip jums sekasi?", to_upper=True))
# print(teksto_manipuliacija("Labas. Mano Vardas Ernestas. Kaip Jums Sekasi? Kaip Praejo Jusu Diena?", to_lower=True))
# print(teksto_manipuliacija("Labas, kaip jums sekasi?", word_count=True))

# 6

# def spausdinimas(list):
#     unikalus = [element for element in list if list.count(element) == 1] #sukuriame nauja sarasa, kuriame bus tik unikalus skaiciai
#     print("Unikalus elementai: ", unikalus) 
#     return unikalus
# list = [5, 6, 7, 2, 8, 7, 2, 8, 10, 11, 12]
# spausdinimas(list)

# 7

# def spausdinimas(skaicius):
#     if skaicius <= 1: #skaiciai 1, 0 ir neigiami nera pirminiai
#         return False
#     for i in range(2, int(skaicius ** 0.5) + 1): #sukuria intervalą nuo 2 iki kvadratinės šaknies reikšmės, pridedant 1 prie kvadratinės šaknies (kad apimtų paskutinį sveikąjį skaičių).
#         if skaicius % i == 0:                       
#             return False # jei dalinasi, tai ne pirminis
#         return True # jei nedalinasi, tai pirminis
# print(spausdinimas(7))
# print(spausdinimas(10))
# print(spausdinimas(5))
# print(spausdinimas(13))
# print(spausdinimas(3))

# 8
# def spausdinimas(text):
#     zodziai = text.split() #padalina teksta i zodzius
#     apversti_zodziai = zodziai [::-1] #apvercia zodzius
#     apverstas_tekstas = ' '.join(apversti_zodziai) #sujungia zodzius atgal i teksta
#     return apverstas_tekstas
# text = "Labas, kaip jums sekasi?"
# print(spausdinimas(text))

# 9
# def spausdinimas():
#     metai = int(input("Iveskite metus: ")) 
#     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#         print(f"{metai} keliamieji metai.")
#     else:
#         print(f"{metai} nekeliamieji metai.")
# spausdinimas()

# 10
# import datetime
# def spausdinimas():
#     text = input("Įveskite datą (YYYY-MM-DD): ")
#     my_date = datetime.datetime.strptime(text, "%Y-%m-%d")  # Paverciame teksta i data
#     now = datetime.datetime.now()  # Dabartine data ir laikas
#     my_date_difference = now - my_date  # Skirtumas tarp dabar ir ivestos datos
    
#     #apskaiciuoju metus, menesiui, dienas, valandas, minutes ir sekundes
#     metai = my_date_difference.days // 365 #suskaiciuoju kiek metu praejo nuo ivestos datos
#     menesiai = (my_date_difference.days % 365) // 30 #suskaiciuoju kiek menesiu praejo nuo ivestos datos
#     dienos = (my_date_difference.days % 365) % 30 #% zenklas padalinus paima likusia liekana, taip galima apskaiciuoti tikslesni dienu skaiciu
#     valandos = my_date_difference.seconds // 3600 #3600 sekundziu yra 1 valanda.
#     minutes = (my_date_difference.seconds // 60) % 60 #pirma padaliame is 60, kad gautume minutes, tada su % paimame likusius sekundes
#     sekundes = my_date_difference.seconds % 60 #apskaiciuojama vis sekundziu skirtuma

#     print(f"Nu nuo ivestos datos praejo: {metai} metai, {menesiai} menesiai, {dienos} dienos, {valandos} valandos, {minutes} minutes, {sekundes} sekundes.")

# spausdinimas()
 

#############################################################################################################################################################

                                                 # Uzduotis 2


# def asmens_kodo_validavimas():
#     asmens_kodas = input("Iveskite asmens koda: ")
#     if len(asmens_kodas) != 11:
#         print("Asmens kodas turi buti 11 simboliu ilgio.")
#         return False
#     if not asmens_kodas.isdigit():
#         print("Asmens kodas turi buti sudarytas tik is skaiciu.")
#         return False
#     pirmas_skaicius = int(asmens_kodas[0])
#     if pirmas_skaicius not in [1, 2, 3, 4, 5, 6, 7, 8]:
#         print("Pirmas skaitmuo neteisingas, turėtų būti nuo 1 iki 8.") 
#         return False
    
#     metai = int(asmens_kodas[1:3])
#     if metai < 1 or metai > 99:
#         print("Gimimo metai neteisingi.") #metai
#         return False
    
#     menesis = int(asmens_kodas[3:5])
#     if menesis < 1 or menesis > 12:
#         print("Gimimo mėnuo neteisingas.") #menesis
#         return False
    
#     diena = int(asmens_kodas[5:7])
#     if diena < 1 or diena > 31:
#         print("Gimimo diena neteisinga.") #diena
#         return False
    
#     eiles_numeris = int(asmens_kodas[7:10])
#     if eiles_numeris < 0 or eiles_numeris > 999: #eiles numeris
#         print("Eilės numeris neteisingas.")
#         return False
    
#     tikrinimo_skaicius = int(asmens_kodas[10])
#     if tikrinimo_skaicius < 0 or tikrinimo_skaicius > 9: #patikrina tikrinimo skaiciu
#         print("Tikrinimo skaitmuo neteisingas.")
#         return False    
#     return True

# asmens_kodo_validavimas()


# def asmens_kodo_generavvimas():
#     import random
#     pirmas_skaicius = random.randint(1, 8) #pirmas skaitmuo gali buti nuo 1 iki 8
#     metai = random.randint(1, 99) #metai
#     menesis = random.randint(1, 12) #menesis
#     diena = random.randint(1, 31) #diena
#     eiles_numeris = random.randint(0, 999) #eiles numeris
#     tikrinimo_skaicius = random.randint(0, 9) #tikrinimo skaicius

#     asmens_kodas = f"{pirmas_skaicius:01}{metai:02}{menesis:02}{diena:02}{eiles_numeris:03}{tikrinimo_skaicius:01}"
#     return asmens_kodas

# print(asmens_kodo_generavvimas())

                                                #   uzduotis 3


# def spausdinimas(skaicius):
#     skaicius_str = str(skaicius) #paverciame skaiciu i string
#     if len(skaicius_str) % 2 != 0: #jei skaicius nelyginis, tai pridedame 0 prie pradzios
#         skaicius_str = '0' + skaicius_str #pridedame 0 prie pradzios
#     pirmas_skaicius = skaicius_str[0:len(skaicius_str)//2] #pirmas skaicius
#     antras_skaicius = skaicius_str[len(skaicius_str)//2:] #antras skaicius
#     return pirmas_skaicius == antras_skaicius #jei pirmas skaicius lygus antram, tai graziname True, kitu atveju graziname False


# print(spausdinimas(1212))
# print(spausdinimas(1313))
# print(spausdinimas(1234))
# print(spausdinimas(123321))
###################################################################################################################################################


                                                     #pradinis lygis 1

# def spausdinimas(*args):
#     spausdinimas = " ".join(args)
#     print(spausdinimas)

# spausdinimas("Jonas", "Petras", "Antanas", "Tomas", "Ernestas", "Rokas", "Andrius", "Marius", "Tomas")    
                                                    

                                                     #pradinis lygis 2

# def spausdinimas(**kwargs):
#     vardas = kwargs.get("vardas", "Nenurodytas vardas")
#     pavarde = kwargs.get("pavarde", "Nenurodyta pavarde") 
#     amzius = kwargs.get("amzius", "Nenurodytas amzius")

#     print(f"Vardas: {vardas}, Pavarde: {pavarde}, amžius: {amzius}")

# spausdinimas(vardas="Jonas", pavarde="Jonaitis", amzius=30)      
# spausdinimas(vardas="Jonas", pavarde="Jonaitis")
# spausdinimas(vardas="Jonas")



# def create_profile(**kwargs):
#     user_profile = {}
#     for elem in kwargs:
#         if elem == "name":
#             user_profile["name"] = kwargs[elem]
#         if elem == "age":
#             user_profile["age"] = kwargs[elem]
#         if elem == "location":
#             user_profile["location"] = kwargs[elem]    

#     return user_profile

# user = create_profile(name="Saulius", age=30, location="Kaunas")
# print(user)        




                                                    #pradinis lygis 3


# my_list = ["Labas", "Pasauli", "Kaip", "Sekasi", "Ernestas", "Rokas", "Andrius", "Marius", "Tomas"]

# my_list_new = sorted(my_list, key=lambda x: len(x)) #rusiuojame sarasa pagal kekvieno vardo simboliu skaiciu

# for i in my_list_new:
#     print(i)


                                                    #pradinis lygis 4

# sarasas = [x**2 for x in range(1, 11)]

# print(sarasas)


                                                    # Vidutinis lygis 5

# def spausdinimas(*args):
#     bendri = set(args[0])
#     for i in args[1:]:
#         bendri.intersection_update(i) #sujungia sarasus ir palieka tik tuos elementus, kurie yra visuose sarasuose
#     return list(bendri) #sugrazina sarasa su bendrais elementais

# sarasas1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# sarasas2 = [3, 4, 5, 2, 7, 5, 4, 3, 4, 5]
# sarasas3 = [5, 6, 7, 8, 9, 3, 4, 5, 2, 7]
# sarasas4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(spausdinimas(sarasas1, sarasas2, sarasas3, sarasas4)) #sugrazina sarasa su bendrais elementais


                                                   # Vidutinis lygis 6
                                                   
                                                            


