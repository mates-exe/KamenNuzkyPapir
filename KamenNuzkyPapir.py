import random

intro = input('''
=========================================
|     000    |    \   /    |  ________  |
|    00000   |     \ /     | |        | |
|    00000   |      o      | |        | |
|   000000   |     / \     | |________| |
|     00     |    0   0    |            |
=========================================
Zahrajeme si kamen, nuzky, papir.\n- Pro zobrazeni aktualnich vysledku \"V\"\n- Pro ukonceni hry vyber \"Q\" \nStiskni Enter pro zacatek hry!''')

score = 0
vyhry = 0
prohry = 0
remizy = 0
hrac = input("\n\n\n\nVyber si Kamen [R], Nuzky [S], Papir [P] ")
hrac = hrac.lower()
vyber = ["r", "p", "s"]

while True:

    pocitac = random.choice(vyber)

    if(pocitac == hrac):
        print("Remiza! Zkus to znovu!")
        remizy += 1
    elif(hrac == "r"):
        if(pocitac == "s"):
            score += 1
            vyhry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|   \   /    |     000     |
|    \ /     |    00000    |
|     o      |    00000    |
|    / \     |   000000    |
|   0   0    |     00      |
============================
Vyhral jsi! Score: {score}''')
        else:
            score -= 1
            prohry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|  ________  |     000     |
| |        | |    00000    |
| |        | |    00000    |
| |________| |   000000    |
|            |     00      |
============================
Prohral jsi :/ Score: {score} ''')
    elif(hrac == "p"):
        if(pocitac == "r"):
            score += 1
            vyhry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|     000    |  ________   |
|    00000   | |        |  |
|    00000   | |        |  |
|   000000   | |________|  |
|     00     |             |
============================
Vyhral jsi! Score: {score}''')
        else:
            score -= 1
            prohry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|   \   /    |  ________   |
|    \ /     | |        |  |
|     o      | |        |  |
|    / \     | |________|  |
|   0   0    |             |
============================
Prohral jsi :/ Score: {score}''')
    elif(hrac == "s"):
        if(pocitac == "p"):
            score += 1
            vyhry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|  ________  |    \   /    |
| |        | |     \ /     |
| |        | |      o      |
| |________| |     / \     |
|            |    0   0    |
============================
Vyhral jsi! Score: {score}''')
        else:
            score -= 1
            prohry += 1
            print(f'''
============================
|   Pocitac  |      Ty     |
============================
|     000    |    \   /    |
|    00000   |     \ /     |
|    00000   |      o      |
|   000000   |     / \     |
|     00     |    0   0    |
============================
Prohral jsi :/ Score: {score}''')

    elif(hrac == "q"):
        if(score >= 0):
            scoreline = f"| Score  |    {score}    |"
        else:
            scoreline = f"| Score  |    {score}   |"
        print(f'''
Hra skoncila! Vysledky:
====================
{scoreline}
| Vyhry  |    {vyhry}    |
| Prohry |    {prohry}    |
| Remizy |    {remizy}    |
====================
        ''')
        break

    elif(hrac == "v"):
        if(score >= 0):
            scoreline = f"| Score  |    {score}    |"
        else:
            scoreline = f"| Score  |    {score}   |"
        print(f'''
Aktualni vysledky:
====================
{scoreline}
| Vyhry  |    {vyhry}    |
| Prohry |    {prohry}    |
| Remizy |    {remizy}    |
====================
        ''')

    else:
        print("Neplatny vyber!")
    
    hrac = input("\nVyber si Kamen [R], Nuzky [S], Papir [P] ")
    hrac = hrac.lower()

end = input("\n\nPro ukonceni programu stiskni Enter")