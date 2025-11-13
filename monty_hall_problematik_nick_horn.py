# @Author: Nick Horn
# @Date: 13-11-2025 
# @Description: Monty Hall Problem 

import random

# play or simulate
wahl_modus = input("Willst du selbst spielen (s) oder die Simulation starten (x)? ")

türen = ["ziege", "ziege", "auto"]

if wahl_modus == "s":
    random.shuffle(türen)
    print("Es gibt 3 Türen: 0, 1, 2")
    wahl = int(input("Welche Tür wählst du? (0-2): "))

    # opens a goat door
    ziege_türen = [i for i in range(3) if türen[i] == "ziege"]
    if wahl in ziege_türen:
        geöffnete_tür = random.choice([z for z in ziege_türen if z != wahl])
    else:
        geöffnete_tür = random.choice(ziege_türen)

    print("Tür", geöffnete_tür, "war eine Ziege.")
    wechsel = input("Willst du wechseln? (j/n): ")

    # switch 
    if wechsel == "j":
        neue_wahl = [0,1,2]
        neue_wahl.remove(wahl)
        neue_wahl.remove(geöffnete_tür)
        wahl = neue_wahl[0]

    if türen[wahl] == "auto":
        print("Du hast GEWONNEN!")
    else:
        print("Leider verloren.")
        
else:
    durchläufe = 1000

    # keep same door
    gewinne = 0
    for i in range(durchläufe):
        random.shuffle(türen)
        wahl = random.randint(0,2)
        ziege_türen = [j for j in range(3) if türen[j] == "ziege"]
        if wahl in ziege_türen:
            geöffnete_tür = random.choice([z for z in ziege_türen if z != wahl])
        else:
            geöffnete_tür = random.choice(ziege_türen)
        if türen[wahl] == "auto":
            gewinne += 1
    print("Beibehalten:", (gewinne/durchläufe)*100, "%")

    # switch door
    gewinne = 0
    for i in range(durchläufe):
        random.shuffle(türen)
        wahl = random.randint(0,2)
        ziege_türen = [j for j in range(3) if türen[j] == "ziege"]
        if wahl in ziege_türen:
            geöffnete_tür = random.choice([z for z in ziege_türen if z != wahl])
        else:
            geöffnete_tür = random.choice(ziege_türen)
        alle_türen = [0,1,2]
        alle_türen.remove(wahl)
        alle_türen.remove(geöffnete_tür)
        neue_wahl = alle_türen[0]
        if türen[neue_wahl] == "auto":
            gewinne += 1
    print("Wechseln:", (gewinne/durchläufe)*100, "%")

# I used help from this video: https://youtu.be/YNysEWzeseg?si=GB6IXgd_18UzlIRs
