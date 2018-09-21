# Verkefni 8 - Tile Traveler leikur
'''
Við búum til 4 áttir: North, South, East og West. Notandi á að geta slegið inn áttina með stórum eða litlum staf.
X og y tákna reitinn sem notandinn er á.
Notandinn getur ekki alltaf valið 4 áttir því þeir eru lokaðir með vegg. 
Við gefum upp hvaða áttir notandinn getur farið en það er komið að honum að finna réttu leiðina
'''

for_low = ""
y = 1
x = 1
p = True
n = "(N)orth"
e = "(E)ast"
s = "(S)outh"
w = "(W)est"

while True:


    if y == 1:
        change = n + "."
        for_low = "n"
    if x == 1 and y == 2:
        change = n + " or " + e + " or " + s + "."
        for_low = "nes"
    if x == 2 and y == 2:
        change = s + " or " + w + "."
        for_low = "sw"
    if x == 1 and y == 3:
        change = e + " or " + s + "."
        for_low = "es"
    if x == 2 and y == 3:
        change = e + " or " + w + "."
        for_low = "we"
    if x == 3 and y == 3:
        change = s + " or " + w + "."
        for_low = "sw"
    if x == 3 and y == 2:
        change = n + " or " + s + "."
        for_low = "sn"
    
    
    if p == True:
        print("You can travel: " + change)
    p = False
    direct = str(input("Direction: "))
    low = direct.lower()

    for l in for_low:
        if low == l:
            p = True
    
    if p == False:
        print("Not a valid direction!")   

    if p == True:
        if low == "n":
            y += 1

        if low == "s":
            y -= 1

        if low == "e":
            x += 1
    
        if low == "w":
            x -= 1

    if x == 3 and y == 1:
        break

print("Victory!")