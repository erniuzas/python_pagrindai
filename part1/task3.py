#                                                         Uzduotis 1


# my_list = ['Ernestas', 'Tomas', 5, 6, 4, 10, True, False, 1.5, 2.5, 3.6]

# my_sum = 0


# for item in my_list:
#     if isinstance (item, bool):
#         continue
#     if isinstance(item, (int, float)): #patikrina ar sarase yra int arba float elementai
#         my_sum += item #sudeda int ir float tipo elementus

# print(f"int ir float skaiciu suma yra: {my_sum}")

# # #kodel 1 variante yra gaunama 33.6 o 2 variante 32.6?

# my_list = ['Ernestas', 'Tomas', 5, 6, 4, 10, True, False, 1.5, 2.5, 3.6]

# suma = 0
# for item in my_list:
#     if type(item) == int or type(item) == float:
#         suma += item
# print(f"int ir float skaiciu suma yra: {suma}")


                                                        # Uzduotis 1, 2 dalis

# import traceback


# try:
#     number = input("Iveskite skaiciu: ")
#     number = float(number)

#     ar_skaicius_teigiamas = number > 0

#     print(f"Skaicius {number} yra teigiamas: {ar_skaicius_teigiamas}")
# except ValueError:
#     print("Ivestas netinkamas skaicius")



    
                                                        # Uzduotis 3

# import datetime

# text = input("Jusu gimtadienis(YYYY-MM-DD): ")

# my_date = datetime.datetime.strptime(text, "%Y-%m-%d")
# my_date_difference = datetime.datetime.now() - my_date
# metai = my_date_difference.days // 365 #suskaiciuoju kiek metu praejo nuo ivestos datos
# dienos = my_date_difference.days % 365 #% zenklas padalinus paima likusia liekana, taip galima apskaiciuoti tikslesni dienu skaiciu
# valandos = my_date_difference.seconds // 3600 #3600 sekundziu yra 1 valanda.
# minutes = (my_date_difference.seconds // 60) % 60 #pirma padaliame is 60, kad gautume minutes, tada su % paimame likusius sekundes
# sukundes = my_date_difference.seconds % 60 #
# print(f"nuo gimtadienio praejo: {metai} metu-ai, {dienos} dienu-os, {valandos} valandu-os, {minutes} minutes-ciu, {sukundes} sekundes-ziu")


                                                        















