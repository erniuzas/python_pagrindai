#  number = int(input("Įveskite dabartinę vandens temperatūrą: "))
# if number > 20:
#     print("Vanduo šiltas")
# else:
#     print("Vanduo vėsus")
# if number > 0:
#             print("daugiau nei 0")
# if number > 10:
#             print("daugiau nei 10")   

# if number < 0 and number > -10:
#       print("maziau negu 0 ir daugiau nei -10")

# if number == 0 or number == 10:
#     print("lygu 0 arba 10")

# print("-"*100)

# number = int(input("Iveskite temperatura: "))

# if number <= 10:
#     print("labai salta")
#     print("negalima maudytis")
# elif number <= 15:
#     print("vesu")
#     print("negalima maudytis")
# elif number <= 25:
#     print("siltas")
#     print("galima maudytis")
# elif number <= 30:
#     print("karsta")
#     print("galima maudytis")
# else:
#     print("labai karsta")
#     print("ideali temperatura maudytis")

# print("-"*100)

# a = input("Įveskite pirmąjį skaičių (a): ")
# a = float(a)
# b = input("Įveskite antrąjį skaičių (b): ")
# b = float(b)
# def palyginti_skaicius(a, b):
#     if a < b:
#         print("a yra mažesnis už b.")
#     elif a == b:
#         print("a yra lygus b.")
#     elif a > b:
#         print("a yra didesnis už b.")
# palyginti_skaicius(a, b)

# print("-"*100)

# amzius = int(input("Įveskite savo amžių: "))
# if amzius < 1:
#         print("Naujagimis")
# elif 1 <= amzius <= 3:
#         print("Kūdikis")
# elif 3 <= amzius <= 13:
#         print("Vaikas")
# elif 13 <= amzius <= 18:
#         print("Paauglys")
# elif 18 <= amzius <= 30:
#         print("Jaunuolis")
# elif 30 <= amzius <= 65:
#         print("Suaugęs")
# elif 65 <= amzius <= 100:
#         print("Senjoras")
# else:
#         print("Šimtametis")

# print("-"*100)

# pirmas_skaicius = int(input("Iveskite pirma skaičiu: "))
# antras_skaicius = int(input("Iveskite antra skaičiu: "))

# print("Pasirinkite veiksma: ")
# print("1 - Suma")
# print("2 - Atimtis")
# print("3 - Daugyba")
# print("4 - Dalyba")

# veiksmas = input("Koki veiskma norite atlikti?")
# if veiksmas == "1":
#     rezultatas = pirmas_skaicius + antras_skaicius
#     print(f"Rezultatas: {pirmas_skaicius} + {antras_skaicius} = {rezultatas}")
# elif veiksmas == "2":
#     rezultatas = pirmas_skaicius - antras_skaicius
#     print(f"Rezultatas: {pirmas_skaicius} - {antras_skaicius} = {rezultatas}")
# elif veiksmas == "3":
#     rezultatas = pirmas_skaicius * antras_skaicius
#     print(f"Rezultatas: {pirmas_skaicius} * {antras_skaicius} = {rezultatas}")
# elif veiksmas == "4":
#     if antras_skaicius != 0:
#         rezultatas = pirmas_skaicius / antras_skaicius
#         print(f"Rezultatas: {pirmas_skaicius} / {antras_skaicius} = {rezultatas}")

# print("-"*100)
# import re

# def patikrinti_slaptazodi(slaptažodis):
    
#     if len(slaptažodis) < 8:
#         return "Silpnas: slaptažodis turi būti bent 8 simbolių ilgio."
    
#     if not re.search(r'[A-Z]', slaptažodis):
#         return "Silpnas: slaptažodyje turi būti bent viena didžioji raidė."
    
#     if not re.search(r'\d', slaptažodis):
#         return "Silpnas: slaptažodyje turi būti bent vienas skaičius."
     
#     if not re.search(r'[^A-Za-z0-9]', slaptažodis):
#         return "Silpnas: slaptažodyje turi būti bent vienas specialus simbolis."
    
#     if len(slaptažodis) >= 12 and re.search(r'[A-Z]', slaptažodis) and re.search(r'\d', slaptažodis) and re.search(r'[^A-Za-z0-9]', slaptažodis):
#         return "Stiprus slaptažodis"
#     else:
#         return "Vidutinis slaptažodis"

# slaptažodis = input("Įveskite slaptažodį: ")
# print(patikrinti_slaptazodi(slaptažodis))


# text = "pirmadienis"
# if text.find("a") == -1 or text.find("e") == -1 or text.find("i") == -1 or text.find("o") == -1 or text.find("u") == -1:
#     print("Nera")