import datetime
import pickle
import os

def prideti_knyga(pavadinimas, autorius, isleidimo_metai, zanras, kiekis=1):
    pridejimas = f"{pavadinimas} | {autorius} | {isleidimo_metai} | {zanras} | {kiekis}\n"
    with open("biblioteka.txt", "a", encoding="utf-8") as f:
        f.write(pridejimas)
    print(f"Knyga '{pavadinimas}' pridėta į biblioteką.")


def rodyti_knyga():
    try:
        with open("biblioteka.txt", "r", encoding="utf-8") as f:
            knygos = f.readlines()
            if not knygos:
                print("Biblioteka tuščia.")
                return
            print("Visos bibliotekos knygos:")
            for knyga in knygos:
                print(knyga.strip())
    except FileNotFoundError:
        print("Biblioteka nerasta.")


def ieskoti_knyga(pavadinimas):
    try:
        with open("biblioteka.txt", "r", encoding="utf-8") as f:
            knygos = f.readlines()
            for knyga in knygos:
                if pavadinimas.lower() in knyga.lower():
                    print(f"Knyga '{pavadinimas}' rasta: {knyga.strip()}")
                    return
            print(f"Knyga '{pavadinimas}' nerasta.")
    except FileNotFoundError:
        print("Biblioteka nerasta.")


def istrinti_knyga(pavadinimas):
    try:
        with open("biblioteka.txt", "r", encoding="utf-8") as f:
            knygos = f.readlines()
        with open("biblioteka.txt", "w", encoding="utf-8") as f:
            for knyga in knygos:
                if pavadinimas.lower() not in knyga.lower():
                    f.write(knyga)
                else:
                    print(f"Knyga '{pavadinimas}' ištrinta.")
    except FileNotFoundError:
        print("Biblioteka nerasta.")


prideti_knyga("Pietinia kronika", "Rimantas Kmita", 2016, "Romanas", 1)
prideti_knyga("Haris Poteris ir Isminties akmuo", "J.K. Rowling", 1997, "Fantastika", 1)
prideti_knyga("Haris Poteris ir Fenikso brolija", "J.K. Rowling", 2003, "Fantastika", 1)

rodyti_knyga()
ieskoti_knyga("Ananasas")



class Knyga:
    def __init__(self, pavadinimas, autorius, isleidimo_metai, zanras, kiekis=1):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras
        self.kiekis = kiekis

    def __str__(self):
        return f"{self.autorius} - {self.pavadinimas} | {self.isleidimo_metai} | {self.zanras} | Kiekis: {self.kiekis}"





    


























