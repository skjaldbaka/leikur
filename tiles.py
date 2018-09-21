# Verkefni 8 - Tile Traveler leikur
'''
Við búum til 4 áttir: North, South, East og West. Notandi á að geta slegið inn áttina með stórum eða litlum staf.
X og y tákna reitinn sem notandinn er á.
Notandinn getur ekki alltaf valið 4 áttir því þeir eru lokaðir með vegg. 
Við gefum upp hvaða áttir notandinn getur farið en það er komið að honum að finna réttu leiðina
'''
x = 1
y = 1
north = "(N)orth"
south = "(S)outh"
west = "(W)est"
east = "(E)ast"

while x <= 3 or x >= 1  and y <= 3 or y >= 1:

    if x == 1 and y == 1:
        change_to = north + "."
    elif x == 1 and y == 2:
        change_to = north + " or " + east + " or " + south + "."
    elif x == 1 and y == 3:
        change_to = east + " or " + south + "."
    elif x == 2 and y == 1:
        change_to = north + "."
    elif x == 2 and y == 2:
        change_to = south + " or " + west + "."
    elif x == 2 and y == 3:
        change_to = east + " or " + west + "."
    elif x == 3 and y == 3:
        change_to = south + " or " + west + "."
    elif x == 3 and y == 2:
        change_to = north + " or " + south + "."
    elif x == 3 and y == 1:
        print("Victory!")
        break
    else:
        change_to == 'x'
        print("Not a valid direction!")


    if change_to != 'x':
        print("You can travel:", change_to)
    direction = str(input("Direction: "))
    lower_dir = direction.lower()


    if lower_dir == "n":
        y += 1
    elif lower_dir == "s":
        y -= 1
    elif lower_dir == "w":
        x -= 1
    elif lower_dir == "e":
        x += 1
    else:
        print("Not a valid direction!")