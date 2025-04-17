
# funkcijos aprasymas
# def greeting(name):
#     print("hello!")
#     print(f"      {name},")
# #funkcijos iskvietimas
# vardas = input("Iveskite savo varda: ")
# greeting(vardas)

##########################################################

# def pakelk_kvadratu(number):
#     kvadratas = number * number
#     print(f"kvadratas skaiciaus {number} yra: {kvadratas}")

# def daugyba(x, y):
#     result = x * y
#     return result


# a = 5
# b = 2

# daaugyba_result = daugyba(a, b)

# print(daaugyba_result*99)

# while True:
#     number = int(input("Iveskite skaiciu: "))

#     pakelk_kvadratu(number)


################################################################3


# def skaiciuokle(x, y, z, j = 0):
#     result = x * y
#     result = result + z + j
#     return result

# skaiciuokle_result = skaiciuokle( 5, 9, 7,)

# print(skaiciuokle_result)


#####################################################################3

# def teksto_manipuliacija(text:str, to_upper = False, to_lower = False):
#     """sita funkcija keicia teksta ir grazina ji pakeista
#     Args:
#         text: Tai yra teksto kintamasis, kuris bus manipoliuojamas
#         to_upper: Jei True, tekstas bus paverstas didziosiomis raidemis
#         to_lower: Jei True, tekstas bus paverstas mazosiosiomis raidemis
    
#     Returns:
#         Si funkcija grazina pakeista teksta
#     """
#     if to_upper:
#         text = text.upper()
#     if to_lower:
#         text = text.lower()

#     return text

# def run():
#     text = input()
#     naujas_textas = teksto_manipuliacija(text, to_upper=True)
#     print(naujas_textas)





# my_list = []
# my_list.sort()

# naujas_textas = teksto_manipuliacija("Labas", to_lower=True)

# print(naujas_textas)


################################################################################

# def spausdinimas(name, *args):
#     for number in args:
#         print(name, number)


# spausdinimas("Rokas", 5,5,6,7,5,4,4,3,4,6,7,8,67,6)   



# def spausdinimas(start, **kwargs):
#     for key, value in kwargs.items():
#         print(start, key, " ", value)

# spausdinimas(1, Rokas = 5, Tomas = 6, Ernestas = 7, Marius = 8, Andrius = 9)        


######################################################################################################3

# def get_initial_coordonates():
#     x = 0
#     y = 0
#     return x, y

# x, y = get_initial_coordonates()

# print("x: ", x)
# print("y: ", y)


# globalus = 10

# def skaiciavimas(localus):
#     return localus + globalus


# localus = 20
# print(skaiciavimas(localus))



# def run_task_1_1():
#     x = 0
#     print("hello")

# def skaiciavimas(x):
#     return x * 2



# run_task_1_1()


# def run_lambda_example():
#     # dalyba_is_2 = lambda x: x / 2
#     # result = dalyba_is_2(10)
#     # print(result)
#     my_list = [1, 2, 3, 4, 5]
    
#     my_list_new = map()
# run_lambda_example()


# my_list = ["Ernestas", "Tomas", "Rokas", "Marius", "Andrius"]

# my_list_new = map(lambda x: x.upper(), my_list)

# for i in my_list_new:
#     print(i)


# def run_inline_loop():
#     my_list_lambda = [lambda x = i: x / 2 for i in range(1,10) if i % 2 == 0]
#     my_list = [i / 2 for i in range(1,10) if i % 2 == 0]

#     for i in my_list:
#         print(i)

#     print("#########################")

#     for i in my_list_lambda:
#         print(i())

# run_inline_loop()












































































