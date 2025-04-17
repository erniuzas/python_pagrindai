

import os
import datetime
# file_info = os.stat("lecture7.py")
# print(file_info.st_mtime)
# print(file_info.st_size)

# print(datetime.datetime.fromtimestamp(file_info.st_mtime))
# print(file_info.st_size / 1024, "KB")
# print(file_info.st_size / 1024 / 1024, "MB")

# failo atidarimo tipai
# r - read (default) - failas tik skaitomas
# w - write - failas tik rasomas, jei failas egzistuoja, jis bus perrasytas
# a - append - failas tik rasomas, jei failas egzistuoja, jis bus papildytas

# r+ - read and write - failas skaitomas ir rasomas, jei failas neegzistuoja, bus sukurta
# w+ - write and read - failas skaitomas ir rasomas, jei failas egzistuoja, jis bus perrasytas
# a+ - append and read - failas skaitomas ir rasomas, jei failas egzistuoja, jis bus papildytas

# wb - write binary - failas rasomas binariniu formatu, jei failas egzistuoja, jis bus perrasytas
# ab - append binary - failas rasomas binariniu formatu, jei failas egzistuoja, jis bus papildytas
# rb - read binary - failas skaitomas binariniu formatu, jei failas neegzistuoja, bus sukurta


# with open("test.txt", "w") as failas:
#     failas.write("Labas\n")
#     failas.write("Pasauli\n")
#     failas.write("Kaip sekasi?\n")

# failas = open("test.txt", "w")
# failas.write("Labas\n")
# failas.write("Pasauli\n")
# failas.write("Kaip sekasi?\n")

# failas.close()

# with open("test.txt", "w") as failas:
#     failas.write("Labas\n")
#     failas.write("Pasauli\n")
#     failas.write("Kaip sekasi?\n")


# with open("test.txt", "a", encoding="UTF-8") as failas:
   
#    failas.seek(0)
#    failas.write("cio\n")
#    failas.write("Pasauli\n")


# with open ("test.txt", "r", encoding="UTF-8") as failas:
#     for line in failas:
#         if line.find("Labas") is -1:
#             print(line, end="")


# with open ("test.txt", "r", encoding="UTF-8") as failas:
#     print(failas.read(1))
#     print(failas.read(1))
#     print(failas.read(1))
#     print(failas.read(1))

# with open ("test.txt", "r", encoding="UTF-8") as failas:
#     with open ("poetry_copy.txt", "w", encoding="UTF-8") as kopija:
#         for line in failas:
#             kopija.write(line)

# import pickle

# def save_to_file(filename, variable):
#     with open("variable_a.pkl", "wb") as failas:
#         pickle.dump(variable, failas)

# def load_from_file(filename):
#     with open("variable_a.pkl", "rb") as failas:
#         variable = pickle.load(failas)
    
# a = 9999999999
# with open("variable_a.pkl", "wb") as failas:
#     pickle.dump(a, failas)


# with open("variable_a.pkl", "rb") as failas:
#     result = pickle.load(failas)

# print(result)

# user = {"name": "Tomas", "surname": "Tomas", "age": 25, "height": 1.85, "weight": 80}
# save_to_file("variable_a.pkl", user)

# print(load_from_file("variable_a.pkl"))






