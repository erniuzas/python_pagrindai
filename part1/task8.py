                                                    #  1 uzduotis



# sakiniai = ["Laba diena", "Kaip sekasi?", "Viskas gerai?", "Kaip jautiesi?"]

# nauji_sakiniai = map(lambda x: x.replace("?", "") + "!", sakiniai)

# for i in nauji_sakiniai:
#     print(i)

# print("*" * 50)

# sakiniai = ["Laba diena", "Kaip sekasi?", "Viskas gerai?", "Kaip jautiesi?"]

# nauji_sakiniai = map(lambda x: x.replace("?", "") + "!", sakiniai)

# tekstas = " ".join(nauji_sakiniai)
# print(tekstas)



                                                    # 2 uzduotis

# from statistics import mean
# from statistics import median

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
#     19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
#     39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# naujas_sarasas = list(map(lambda x: x * 10, sarasas))
# print(naujas_sarasas)

# print("*" * 50)


# dalyba = filter(lambda x: x % 7 == 0, sarasas)
# print(list(dalyba))
# print("*" * 50)


# kvadratai = list(map(lambda x: x ** 2, sarasas))
# print(list(kvadratai))

# print("*" * 50)
# kvadratu_suma = sum(kvadratai)
# print(kvadratu_suma)

# print("*" * 50)
# maziausias = min(kvadratai)
# didziausias = max(kvadratai)
# print(f"Min: {maziausias}, Max: {didziausias}")

# print("*" * 50)
# vidurkis = mean(kvadratai)
# print(vidurkis)

# print("*" * 50)
# mediana = median(kvadratai)
# print(mediana)

# print("*" * 50)

# atbulai = sorted(kvadratai, reverse=True)
# print(atbulai)

                                                      #3 uzduotis


# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# skaiciu_suma = sum(x for x in sarasas if isinstance(x, (int, float)))
# print(skaiciu_suma)

# print("*" * 50)


# zodziai = ' '.join(x for x in sarasas if isinstance(x, str))
# print(zodziai)
# print("*" * 50)


# kintamieji = sum(1 for x in sarasas if isinstance(x, bool) and x)
# print(kintamieji)

                                                #  4 uzduotis


# class Zmogus:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius

#     def __repr__(self):
#         return f"{self.vardas}, amzius: {self.amzius}"    


# zmogus1 = Zmogus("Tomas", 30)
# zmogus2 = Zmogus("Rokas", 25)
# zmogus3 = Zmogus("Ernestas", 30)
# zmogus4 = Zmogus("Ignas", 32)
# zmogus5 = Zmogus("Karolis", 35)
# zmogus6 = Zmogus("Andrius", 40)
# zmogus7 = Zmogus("Antanas", 60)

# from operator import attrgetter
# zmones = [zmogus1, zmogus2, zmogus3, zmogus4, zmogus5, zmogus6, zmogus7]

# sorted_zmones = sorted(zmones, key=attrgetter("amzius", "vardas"), reverse=True)

# for zmogus in sorted_zmones:
#     print(zmogus)






