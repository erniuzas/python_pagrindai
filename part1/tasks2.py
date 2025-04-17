#  my_list = [1, 2, 3, 5, 9]


# print(my_list[4])

# my_list.pop(3)
# print(my_list)

# my_list[0] = 10
# print(my_list)

# my_list.append(10)
# my_list.append(18)
# my_list.append(20)
# print(my_list)



# my_dict = {
#     "vardas": "Tomas",
#     "pavarde": "Kulikauskas",
#     "amzius": 30
# }


# print(my_dict["vardas"])

# my_dict["miestas"] = "Vilnius"
# print(my_dict)

# del my_dict["amzius"]
# print(my_dict)

# my_dict["vardas"] = "Jonas"
# print(my_dict)


# metai = int(input("Įveskite metus: "))


# if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#     print(f"{metai} yra keliamieji metai.")
# else:
#     print(f"{metai} nėra keliamieji metai.")



# my_list = [1, 2, 3, 4, 2, 3, 5, 6, 6, 7, 8, 9, 1, 2]
# print(my_list)
# my_list = list(set(my_list)) 
# # papaverčia rinkinį atgal į sąrašą, nes rinkiniai nesaugo elementų tvarkos
# # ir negalima tiesiogiai atlikti operacijų su jais kaip su sąrašais.
# print(my_list)

# import time

# tuple_data = tuple(range(10000))
# list_data = list(range(10000))

# start_time = time.time()
# for item in tuple_data:
#     print(item) 
# tuple_time = time.time() - start_time
# print(f"Tuple spausdinimo laikas: {tuple_time} sekundžių")


# start_time = time.time()
# for item in list_data:
#     print(item)  
# list_time = time.time() - start_time
# print(f"List spausdinimo laikas: {list_time} sekundžių")

# ###############################################################################################################

#                                             1 Uzduotis

# i = 0  # isvedame kintamaji


# while True:  # sukuriame begalini cikla
    
#     skaicius = int(input("iveskite skaičiu: "))  # vartotojas iveda skaicius

#     if skaicius < 0:
#         print("Programa baigiama.")
#         break  # jeigu skaicius yra neigiamas, programa yra sustabdyta
#     i = i + skaicius  # pridedame ivestus teigiamus skaicius

# print(f"Visu ivestu teigiamu skaičiu suma: {i}")  # isvedama teigiamu skaiciu suma
# -------------------------------------------------------------------------------------------

#                                             2 Uzduotis


# zodziai = [] #sukuriu tuscia sarasa kuriame bus talpinami ivesti zodziai


# for i in range(5): #ciklas bus atliekas 5 kartus, vartotojas ives 5 zodzius
#     zodis = input(f"Įveskite {i+1}-a žodį: ")
#     zodziai.append(zodis)  #pridedami zodziai i sarasa


# print("\nĮvesti žodžiai ir jų ilgiai:") 
# for i, zodis in enumerate(zodziai, start=1): #enumerate leidzia gauti zodzio indeksa
#     print(f"{i}. Žodis: {zodis}, Ilgis: {len(zodis)}") #len naudojama zodzio ilgio suzinojimui
# ----------------------------------------------------------------------------------------------


#                                                 3 uzduotis

# import random

# numbers = [] #vel susikuriu sarasa kuris talpins parasytus skaicius

# for _ in range(3): 
#     skaicius = random.randint(1, 6) #sugeneruojame 3 random skaicius
#     numbers.append(skaicius)#pridedame i sarasa

#     if skaicius == 5:
#         print('Pralaimejai')  #jei nors vienas skaicius yra 5, nutraukiame cikla
#         break
# else:
#     print('Laimejai') #jeigu nebuvo 5

# print("Sugeneruoti skaiciai", numbers)

# ----------------------------------------------------------------------------------------------------

#                                            4 uzduotis



# i = 1 #indeksa nusistatau kad numeruotu keliamuosius metus nuo 1

# for metai in range(1900, 2101): # sukuriu cikla kuris pereitu per visus metu nuo 1900 iki 2100
    
#      if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0): #keliamuju metu formule
#         print(f'{i}. {metai} metai') #isvedu eiles numeri ir metus
#      i = i + 1 #po kekvieno keliamojo metu isvedimo i bus padidinamas 1. padeda nuosekliai numeruoti seka












#  if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#         print(f"{metai} yra keliamieji metai.")
#     else:
#         print(f"{metai} nėra keliamieji metai.")


# ----------------------------------------------------------------------------------------------------


# Kortos nuo 9 iki A (24 kortos).
# 2 zaidejai
# 6 kortos kekvienam
# kozeriai
# daugiausiai 6 kortos ismestos
# jei zaidejas neturi kaip apsiginti - privalo imti kortos
# jei zaidejas raundo pradzioje neturi 6 kortu - privalo traukti is kalades
# laimi tas kuris pirmas atsikrato visu kortu (jei kalade tuscia)
# zaidejas ginasi didesnia to pacio tipo korta arba kozeriu
# kai apsigina pradedantysis pasikeicia
# puolantis deda pasirinkta korta(kolkas nera dametimo)


# 9, 10, J, Q, K, A
# clubs (♣), diamonds (♦), hearts (♥) and spades (♠).

# import sys
# import random

# deck_sample = {
#     "♣" : ["9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"],
#     "♦" : ["9♦", "10♦", "J♦", "Q♦", "K♦", "A♦"],
#     "♥" : ["9♥", "10♥", "J♥", "Q♥", "K♥", "A♥"],
#     "♠" : ["9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
# }

# player1_deck = []
# player2_deck = []
# trump_card = None # kozeris
# trump_symbol = None # kozerio simbolis

# game_deck = []

# dict_cards_list = list(deck_sample.values())

# game_deck.extend(dict_cards_list[0])
# game_deck.extend(dict_cards_list[1])
# game_deck.extend(dict_cards_list[2])
# game_deck.extend(dict_cards_list[3])

# random.shuffle(game_deck)
# print(game_deck)
# print()
# # išdalinam kortas žaidejams
# for _ in range(6):
#     player1_deck.append(game_deck.pop())
#     player2_deck.append(game_deck.pop())

# trump_card = game_deck[0] # isissaugo kozeri bet jo iš kalades nepašalinam
# trump_symbol = trump_card[-1] # isissaugo kozerio simboli

# print("deck", game_deck)
# print("player1", player1_deck)
# print("player2", player2_deck)
# print("trump_card", trump_card)
# print("trump_symbol", trump_symbol)

# # surandom kas iš žaideju turi mažiausia kozeri
# player_1_index_of_trump = sys.maxsize
# player_2_index_of_trump = sys.maxsize



# for player1_card in player1_deck:
#     try:
#         dict_trump_list = deck_sample[trump_symbol]
#         player_1_index_of_trump_temp = dict_trump_list.index(player1_card)
#         if player_1_index_of_trump_temp < player_1_index_of_trump:
#             player_1_index_of_trump = player_1_index_of_trump_temp
#     except ValueError:
#         pass

# for player2_card in player2_deck:
#     try:
#         dict_trump_list = deck_sample[trump_symbol]
#         player_2_index_of_trump_temp = dict_trump_list.index(player2_card)
#         if player_2_index_of_trump_temp < player_2_index_of_trump:
#             player_2_index_of_trump = player_2_index_of_trump_temp
#     except ValueError:
#         pass

# print("player_1_index_of_trump", player_1_index_of_trump)
# print("player_2_index_of_trump", player_2_index_of_trump)

# if player_1_index_of_trump < player_2_index_of_trump:
#     print("player1 starts")
# else:
#     print("player2 starts")










