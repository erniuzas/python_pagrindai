
# my_variable = True
#my_variable2 = False

# print(my_variable)

# my_variable = 5 < 10 and 10 > 15

# print(my_variable)

# if my_variable:
#     print("yes")
# else:
#     print("no")


#####################################################################


# my_int = 5
# my_float = 5.0
# my_string = "5"
# my_bool = True
# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)
# my_dict = {"key": "value"}
# my_set = {1, 2, 3}

# print(type(my_int))
# print(type(my_float))
# print(type(my_string))
# print(type(my_bool))
# print(type(my_list))
# print(type(my_tuple))
# print(type(my_dict))
# print(type(my_set))

# new_list = [1, 2, "string", 4.5, True, 5.0, (1, 2), {1, 2}, {"key": "value"}]


# # if (my_int) == (my_float):
# #     print("same type")

# my_sum = 0

# for item in new_list:
#     print(item, type(item))
#     if type(item) == int or type(item) == float:
#         my_sum += item
#     if type(item) == tuple:
#         my_sum += sum(item)
#         for number in item:
#             if type(number) == int or type(number) == float:
#                 sum += number
    

        
         

# print(my_sum)        


########################################################################

# import datetime

# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.today().time())

# x_date = datetime.datetime.now()

# my_date = datetime.datetime(2025, 1, 25)

# print(type(x_date))
# print(x_date)

# print(type(my_date))
# print(my_date)

# if x_date < my_date:
#     print("X maziau")
# else:
#     print("daugiau")


################################################################3


# my_date = datetime.datetime.now()



# # my_date = datetime.timedelta(days = 1)

# print(my_date)



# print(my_date.strftime("%Y * %m * %d - %H : %M : %S : %f"))

# print(my_date.strftime("%Y * %m * %d - %H : %M : %S : %f : %A"))
# print(my_date.strftime("%Y * %B * %d - %H : %M : %S : %f"))

# my_date_diference = my_date - datetime.datetime(2000, 1, 1 )

# print(my_date_diference)
# print(f"{my_date_diference.days // 7} weeks") 


################################################################################


# text = input("iveskite data(YYYY-MM-DD H:M:S): ")
# print(text)
# print(type(text))
# my_date = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")


# print(my_date)
# print(type(my_date))

# my_date_diference = datetime.datetime.now() - my_date
# print(f"nuo datos praejo: {my_date_diference.days} dienu")

#########################################################################################################

"""""
Vartotojas gali įvesti statybos metus ir programa pasako, ar tai senos statybos namas ar ne, ar visiškai nauja.
(pilna data su dienomis)


senos statybos 21 metai 
pusiau nauja nuo 21 iki 3
nuo 3  nauja
"""

# import datetime

# text = input("Iveskite pastato pastatymo metus(YYYY-MM-DD): ")
# my_date = datetime.datetime.strptime(text, "%Y-%m-%d")

# my_date_difference = datetime.datetime.now() - my_date 
# metai = my_date_difference.days // 365 #suskaiciuoju kiek metu praejo nuo ivestos datos
# dienos = my_date_difference.days  #parodo kiek dienu praejo nuo ivestos datos
# if metai > 21:
#         print('Senos statybos')
# elif 3 <= metai <= 21:
#         print('Vidutinio amziaus')
# else:
#         print('Naujos statybos')
                                
# print(f"nuo pastatymo praejo: {metai} metu ir apytiksliai {dienos} dienos")


#################################################################################################################

# import datetime
# import traceback
# try:
#     number = int(input("Ivesk skaiciu su kuriuo dalinsim 5: "))
#     my_number = 5 / number
#     datetime.datetime.strptime(number, "%Y-%m-%d")
# except ZeroDivisionError:
#     print("Ups ivyko klaida dalybos is 0, dalyti is 0 negalima..... Sorry. Prasome isvesti skaiciu kuris nera 0")
# except ValueError:
#     print("jus ivedete ne skaiciu, prasome ivesti skaiciu")
# except Exception as ex:
#     print(ex)
#     tb = traceback.extract_tb(ex.__traceback__)
#     for x in tb:
#         print(f"Eilutes nr {x.lineno}")
#     print("sorry, ivyko nenumatyta klaida, praneskite administratoriui")
# print("Baigta")

# number = None
# while True:
#     try:
#         number = int(input("iveskite skaiciu:"))
#         if number < 0:
#             raise ValueError("skaičius negali būti neigiamas")

#         if number > 100:    
#             raise ValueError("skaicius yra daugiau nei 100")
#         break

#     except Exception as ex:
#         print("klaida yra: ", ex)
  
# finally:
#     print("vykdomas finally blokas")   

























