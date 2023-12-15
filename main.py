def lentele(lenta):
    for eil in lenta:
        print(" | ".join(eil))
        print("---------")


def ar_pilna(lenta):
    for eil in lenta:
        if " " in eil:
            return False
    return True


def pergales_tikrinimas(lenta):
    for i in range(3):
        if lenta[0][i] == lenta[1][i] == lenta[2][i] != " ":
            return lenta[0][i]
        if lenta[i][0] == lenta[i][1] == lenta[i][2] != " ":
            return lenta[i][0]
        if lenta[0][0] == lenta[1][1] == lenta[2][2] != " ":
            return lenta[0][0]
        if lenta[0][2] == lenta[1][1] == lenta[2][0] != " ":
            return lenta[0][2]


def zaidimas(x, o):
    lentenas = ([" ", " ", " "], [" ", " ", " "], [" ", " ", " "])
    zaidejas = "X"
    x_pergales = x
    o_pergales = o

    while True:
        lentele(lentenas)
        print(f'Žaidėjo {zaidejas} eilė:')
        eil = int(input(f'Įveskite eilutę (0-2): '))
        stulp = int(input(f'Įveskite stulpelį (0-2): '))

        if lentenas[eil][stulp] == " ":
            lentenas[eil][stulp] = zaidejas
        else:
            print("Šis langelis jau užimtas!")
            continue
        laimetojas = pergales_tikrinimas(lentenas)
        if laimetojas:
            lentele(lentenas)
            print(f'Žaidėjas {laimetojas} laimėjo!')
            if laimetojas == "X":
                x_pergales += 1
            if laimetojas == "O":
                o_pergales += 1
            print(f'Žaidėjas X laimėjo {x_pergales} kartų(-us)')
            print(f'Žaidėjas O laimėjo {o_pergales} kartų(-us)')
            dar_viena = str(input("Ar norite žaisti dar partiją? (Y/N)"))
            if dar_viena == "Y":
                zaidimas(x_pergales, o_pergales)
            if dar_viena == "N":
                print(f'Viso gero! : )')
                break
            else:
                print("Įvedėte netinkamą pasirinkimą!")
                break

        if ar_pilna(lentenas):
            lentele(lentenas)
            print("Lygiosios!")
            print(f'Žaidėjas X laimėjo {x_pergales} kartų(-us)')
            print(f'Žaidėjas O laimėjo {o_pergales} kartų(-us)')
            dar_viena = str(input("Ar norite žaisti dar partiją? (Y/N)"))
            if dar_viena == "Y":
                zaidimas(x_pergales, o_pergales)
            if dar_viena == "N":
                print(f'Viso gero! : )')
                break
            else:
                print("Įvedėte netinkamą pasirinkimą!")
                break

        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"


zaidimas(0, 0)
