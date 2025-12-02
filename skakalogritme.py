#Kryds og bolle
import random as r


#Jeg lavet en funktion der printer spillepladen. bemærk at hvert element i listen er en plads i spillet fra 0 -> 8.
def spilleplade3x3(spilleplade):
    print('\n')
    print(f"{spilleplade[0]} | {spilleplade[1]} | {spilleplade[2]}")
    print("--+---+--")
    print(f"{spilleplade[3]} | {spilleplade[4]} | {spilleplade[5]}")
    print("--+---+--")
    print(f"{spilleplade[6]} | {spilleplade[7]} | {spilleplade[8]}")
    print("\n")

#jeg indsætter nu et nummer for hvert brik i spillet, Så kan man vælge hvilken brik man vil spille.
spilleplade = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
spilleplade3x3(spilleplade)

############################################################################################################################## vinder funktion
def du_har_vundet_funktionen (spilleplade):
    # den følger samme skema som spilleplade.
    vinderkombinationer = [
        [0, 1, 2],  # række 1
        [3, 4, 5],  # række 2
        [6, 7, 8],  # række 3
        [0, 3, 6],  # kolonne 1
        [1, 4, 7],  # kolonne 2
        [2, 5, 8],  # kolonne 3
        [0, 4, 8],  # skrå 
        [2, 4, 6]   # skrå 
    ]

    # Tjekker om nogen af vinderkombinationerne er opfyldt. hvis 0 = 1 = 2 er der af samme symbol på stribe.
    for kombination in vinderkombinationer:
        if spilleplade[kombination[0]] == spilleplade[kombination[1]] == spilleplade[kombination[2]] != " ":
            return True
    return False
#############################################################################################################################

for tur in range(9):
    spilleplade3x3(spilleplade)
    if tur % 2 == 0:  # Spiller 1's tur
        while True:
            spiller1input = input("Spiller 1, vælg en ledig brik mellem 0-8: ")
            valg = int(spiller1input)  #input skal være integer
            if spilleplade[valg] in ["X", "O"]:
                print("Den brik er allerede taget. Vælg en anden brik.")
            else:
                spilleplade[valg] = "X"
                break

    else:  # Ai spiller tur
        # RANDOM VALG AF LEDIGT FELT
        ledige_felter = [i for i in range(9) if spilleplade[i] not in ["X", "O"]]
        spiller2valg = r.choice(ledige_felter)
        print(f"Spiller 2 valgte brik {spiller2valg}")
        spilleplade[spiller2valg] = "O"

        # AI MED STRATEGI (DEN PRØVER AT BLOKERE MIG)
        """ kan simpelthen ikke få det til at virke, udover hvis jeg laver if else sætninger for hver kombination af 2 X'er."""
        

    # Tjek vinder lige efter hvert træk
    if du_har_vundet_funktionen(spilleplade):
        spilleplade3x3(spilleplade)
        if tur % 2 == 0:
            print("Tillykke! Spiller 1 (X) har vundet!")
        else:
            print("Spiller 2 (O) har vundet!")
        break
else:
    # Kun hvis løkken ikke havde en kombination = uafgjort
    spilleplade3x3(spilleplade)
    print("Det er uafgjort! Ingen har vundet.")