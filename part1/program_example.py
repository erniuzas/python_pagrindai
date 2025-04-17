
def islaidos():
    print()
    print("islaidos")

def pajamos():
    print()
    print("pajamos")    




def run():
    while True:
        print("pasirinkite veiksmą:")
        print("1 - islaidos")
        print("2 - pajamos")
        print("3 - israsas")
        user_choice = input("iveskite (1 arba 2)")

        match user_choice:
            case "1":
                islaidos()
            case "2":
                pajamos()    












