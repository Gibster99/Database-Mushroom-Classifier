import pandas as pd
import sqlite3 as db
import os
import time

clear = lambda: os.system('cls')

mush = db.connect('db.sqlite')

cur = mush.cursor()
#data = pd.read_csv('mushrooms.csv')
#data.to_sql('test', mush)

def menu():
    print('Welcome to the mushroom classifier database please select from the following:\n1. Lookup via ID.\n2. Add a mushroom to the database.\n3. Lookup a mushrooms probability of being edible/poisonous')
    print('\nInput: ')
    choice = input()
    clear()
    handler(choice)

def handler(choice):
    choice = str(choice)
    if(choice == '1'):
        query = 'SELECT max(id) from mushrooms'
        cur.execute(query)
        maxnum = cur.fetchone()
        print('Please input an ID number no greater than: ' + str(maxnum[0]))
        choice = input()
        if (int(choice) < 0 or int(choice) > int(maxnum[0])):
            input("Invalid number entered try again...")
            clear()
            handler(1)
        else:
            lookup(choice)
    elif(choice == '2'):
        clear()
        dbInsert()
    elif (choice == '3'):
        clear()
        dbCheck()
    else:
        clear()
        input('Input not recognized please try again...')
        clear()
        menu()

def catConverter(attribute, key):
    if attribute == 1:
        if key == 'e':
            return('Edible')
        elif key == 'p':
            return('Poisonous')
        else:
            return('Unknown')
    elif attribute == 2:
        if key == 'b':
            return('Bell')
        elif key == 'c':
            return('Conical')
        elif key == 'x':
            return('Convex')
        elif key == 'f':
            return('Flat')
        elif key == 'k':
            return('Knobbed')
        elif key == 's':
            return('Sunken')
        else:
            return('Unknown')
    elif attribute == 3:
        if key == 'f':
            return('Fibrous')
        elif key == 'g':
            return('Grooves')
        elif key == 'y':
            return('Scaly')
        elif key == 's':
            return('Smooth')
        else:
            return('Unknown')
    elif attribute == 4:
        if key == 'n':
            return('Brown')
        elif key == 'b':
            return('Buff')
        elif key == 'c':
            return('cinnamon')
        elif key == 'g':
            return('Gray')
        elif key == 'r':
            return('Green')
        elif key == 'p':
            return('Pink')
        elif key == 'u':
            return('Purple')
        elif key == 'e':
            return('Red')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 5:
        if key == 't':
            return('Bruises')
        elif key == 'f':
            return('No')
        else:
            return('Unknown')
    elif attribute == 6:
        if key == 'a':
            return('Almond')
        elif key == 'l':
            return('Anise')
        elif key == 'c':
            return('Creosote')
        elif key == 'y':
            return('Fishy')
        elif key == 'f':
            return('Foul')
        elif key == 'm':
            return('Musty')
        elif key == 'n':
            return('None')
        elif key == 's':
            return('Spicy')
        elif key == 'p':
            return('Pungent')
        else:
            return('Unknown')
    elif attribute == 7:
        if key == 'a':
            return('Attached')
        elif key == 'd':
            return('Descending')
        elif key == 'f':
            return('Notched')
        else:
            return('Unknown')
    elif attribute == 8:
        if key == 'c':
            return('Close')
        elif key == 'w':
            return('Crowded')
        elif key == 'd':
            return('Distant')
        else:
            return('Unknown')
    elif attribute == 9:
        if key == 'b':
            return('Broad')
        elif key == 'n':
            return('Narrow')
        else:
            return('Unknown')
    elif attribute == 10:
        if key == 'k':
            return('Black')
        elif key == 'n':
            return('Brown')
        elif key == 'b':
            return('Buff')
        elif key == 'h':
            return('Chocolate')
        elif key == 'g':
            return('Gray')
        elif key == 'r':
            return('Green')
        elif key == 'o':
            return('Orange')
        elif key == 'p':
            return('Pink')
        elif key == 'u':
            return('Purple')
        elif key == 'e':
            return('Red')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 11:
        if key == 'e':
            return('Enlarging')
        elif key == 't':
            return('Tapering')
        else:
            return('Unknown')
    elif attribute == 12:
        if key == 'b':
            return('Bulbous')
        elif key == 'c':
            return('Club')
        elif key == 'u':
            return('Cup')
        elif key == 'e':
            return('Equal')
        elif key == 'z':
            return('Rhizomorphs')
        elif key == 'r':
            return('Rooted')
        else:
            return('Unknown')
    elif attribute == 13:
        if key == 'f':
            return('Fibrous')
        elif key == 'y':
            return('Scaly')
        elif key == 'k':
            return('Silky')
        elif key == 's':
            return('Smooth')
        else:
            return('Unknown')
    elif attribute == 14:
        if key == 'f':
            return('Fibrous')
        elif key == 'y':
            return('Scaly')
        elif key == 'k':
            return('Silky')
        elif key == 's':
            return('Smooth')
        else:
            return('Unknown')
    elif attribute == 15:
        if key == 'n':
            return('Brown')
        elif key == 'b':
            return('Buff')
        elif key == 'c':
            return('Cinnamon')
        elif key == 'g':
            return('Gray')
        elif key == 'o':
            return('Orange')
        elif key == 'p':
            return('Pink')
        elif key == 'e':
            return('Red')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 16:
        if key == 'n':
            return('Brown')
        elif key == 'b':
            return('Buff')
        elif key == 'c':
            return('Cinnamon')
        elif key == 'g':
            return('Gray')
        elif key == 'o':
            return('Orange')
        elif key == 'p':
            return('Pink')
        elif key == 'e':
            return('Red')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 17:
        if key == 'p':
            return('Partial')
        elif key == 'u':
            return('Universal')
        else:
            return('Unknown')
    elif attribute == 18:
        if key == 'b':
            return('Brown')
        elif key == 'o':
            return('Orange')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 19:
        if key == 'n':
            return('None')
        elif key == 'o':
            return('One')
        elif key == 't':
            return('Two')
        else:
            return('Unknown')
    elif attribute == 20:
        if key == 'c':
            return('Cobwebby')
        elif key == 'e':
            return('Evanescent')
        elif key == 'f':
            return('Flaring')
        elif key == 'l':
            return('Large')
        elif key == 'n':
            return('None')
        elif key == 'p':
            return('Pendant')
        elif key == 's':
            return('Sheathing')
        elif key == 'z':
            return('Zone')
        else:
            return('Unknown')
    elif attribute == 21:
        if key == 'k':
            return('Black')
        elif key == 'n':
            return('Brown')
        elif key == 'b':
            return('Buff')
        elif key == 'h':
            return('Chocolate')
        elif key == 'g':
            return('Gray')
        elif key == 'r':
            return('Green')
        elif key == 'o':
            return('Orange')
        elif key == 'p':
            return('Pink')
        elif key == 'u':
            return('Purple')
        elif key == 'e':
            return('Red')
        elif key == 'w':
            return('White')
        elif key == 'y':
            return('Yellow')
        else:
            return('Unknown')
    elif attribute == 22:
        if key == 'a':
            return('Abundant')
        elif key == 'c':
            return('Clustered')
        elif key == 'n':
            return('Numerous')
        elif key == 's':
            return('Scattered')
        elif key == 'v':
            return('Several')
        elif key == 'y':
            return('Solitary')
        else:
            return('Unknown')
    elif attribute == 23:
        if key == 'g':
            return('Grasses')
        elif key == 'l':
            return('Leaves')
        elif key == 'm':
            return('Meadows')
        elif key == 'p':
            return('Paths')
        elif key == 'u':
            return('Urban')
        elif key == 'w':
            return('Waste')
        elif key == 'd':
            return('Woods')
        else:
            return('Unknown')

def lookup(choice):
    choice = str(choice)
    query = 'SELECT * FROM (SELECT * FROM mushrooms WHERE id = ' + choice + ' GROUP BY id) q1 JOIN (SELECT * FROM cap WHERE id = ' + choice + ' GROUP BY id) q2 ON q1.id = q2.id JOIN (SELECT * FROM gill WHERE id = ' + choice + ' GROUP BY id) q3 ON q2.id = q3.id JOIN (SELECT * FROM stalk WHERE id = ' + choice +  ' GROUP BY id) q4 ON q3.id = q4.id JOIN (SELECT * FROM "veil-ring" WHERE id = ' + choice + ' GROUP BY id) q5 ON q4.id = q5.id'
    cur.execute(query)
    result = cur.fetchone()
    print(result)
    print('Information for Mushroom ID: ' + choice)
    print('Edibility: ' + catConverter(1,result[1]))
    print('Bruises: ' + catConverter(5, result[2]))
    print('Odor: ' + catConverter(6, result[3]))
    print('Spore-print-color: ' + catConverter(21, result[4]))
    print('Population: ' + catConverter(22, result[5]))
    print('Habitat: ' + catConverter(23, result[6]))
    print('Cap-shape: ' + catConverter(2, result[7]))
    print('Cap-surface: ' + catConverter(3, result[8]))
    print('Cap-color: ' + catConverter(4, result[9]))
    print('Gill-attachment: ' + catConverter(7, result[11]))
    print('Gill-spacing: ' + catConverter(8, result[12]))
    print('Gill-size: ' + catConverter(9, result[13]))
    print('Gill-color: ' + catConverter(10, result[14]))
    print('Stalk-shape: ' + catConverter(11, result[16]))
    print('Stalk-root: ' + catConverter(12, result[17]))
    print('Stalk-surface-above-ring: ' + catConverter(13, result[18]))
    print('Stalk-surface-below-ring: ' + catConverter(14, result[19]))
    print('Stalk-color-above-ring: ' + catConverter(15, result[20]))
    print('Stalk-color-below-ring: ' + catConverter(16, result[21]))
    print('Veil-type: ' + catConverter(17, result[23]))
    print('Veil-color: ' + catConverter(18, result[24]))
    print('Ring-number: ' + catConverter(19, result[25]))
    print('Ring-type: ' + catConverter(20, result[26]))
    print('')
    input('Press any button to continue...')
    clear()
    menu()

def dbInsert():
    query = 'SELECT max(id) from mushrooms'
    cur.execute(query)
    maxnum = cur.fetchone()
    id = (int(maxnum[0]) + 1)
    ident = input('Please enter the classification of the mushroom:\n1. Edible.\n2. Poisonous')
    if(int(ident) < 1 or int(ident) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    identkey = ['e','p']
    ident = identkey[int(ident)-1]
    bruises = input('Are there bruises?:\n1. Yes.\n2. No.')
    if (int(bruises) < 1 or int(bruises) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    bruiseskey = ['t', 'f']
    bruises = bruiseskey[int(bruises) - 1]
    odor = input('What does it smell like?:\n 1. Almond.\n2. Anise.\n3. Creosote.\n4. Fishy.\n5. Foul.\n6. Musty\n7. None\n8. Pungent.\n9. Spicy')
    if (int(odor) < 1 or int(odor) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    odorkey = ['a','l','c','y','f','m','n','p','s']
    odor = odorkey[int(odor) - 1]
    sporePrintColor = input('What color is the spore print?:\n1. Black.\n2. Brown\n3. Buff.\n4. Chocolate.\n5. Green.\n6. Orange.\n7. Purple.\n8. White.\n9. Yellow')
    if (int(sporePrintColor) < 1 or int(sporePrintColor) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    sporePrintColorkey = ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y']
    sporePrintColor = sporePrintColorkey[int(sporePrintColor) - 1]
    population = input('What is the population?:\n1. Abundant.\n2. Clustered.\n3. Numerous.\n4. Scattered.\n5. Several.\n6. Solitary.')
    if (int(population) < 1 or int(population) > 6):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    populationkey = ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y']
    population = populationkey[int(population) - 1]
    habitat = input('What is the habitat?:\n1. Grasses.\n2. Leaves.\n3. Meadows.\n4. Paths.\n5. Urban.\n6. Waste.\n7. Woods.')
    if (int(habitat) < 1 or int(habitat) > 7):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    habitatkey = ['g', 'l', 'm', 'p', 'u', 'w', 'd']
    habitat = habitatkey[int(habitat) - 1]
    capShape = input('What is the cap-shape?:\n1. Bell.\n2. Conical.\n3. Convex.\n4. Flat.\n5. Knobbed.\n6. Sunken.')
    if (int(capShape) < 1 or int(capShape) > 6):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    capShapekey = ['b', 'c', 'x', 'f', 'k', 's']
    capShape = capShapekey[int(capShape) - 1]
    capSurface = input('What is the cap-surface?:\n1. Fibrous.\n2. Grooves.\n3. Scaly.\n4. Smooth')
    if (int(capSurface) < 1 or int(capSurface) > 6):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    capSurfacekey = ['f', 'g', 'y', 's']
    capSurface = capSurfacekey[int(capSurface) - 1]
    capColor = input('What is the cap-color?:\n1. Brown.\n2. Buff.\n3. Cinnamon.\n4. Gray.\n5. Green.\n6. Pink.\n7. Purple.\n8. Red.\n9. White.\n10. Yellow.')
    if (int(capColor) < 1 or int(capColor) > 10):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    capColorkey = ['n', 'b', 'c', 'g','r','p','u','e','w','y']
    capColor = capColorkey[int(capColor) - 1]
    gillAttach = input('What is the gill-attachment?:\n1. Attached.\n2. Descending.\n3. Free.\n4. Notched.')
    if (int(gillAttach) < 1 or int(gillAttach) > 4):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    gillAttachkey = ['a', 'd', 'f', 'n']
    gillAttach = gillAttachkey[int(gillAttach) - 1]
    gillSpace = input('What is the gill-spacing?:\n1. Close.\n2. Crowded.\n3. Distant.')
    if (int(gillSpace) < 1 or int(gillSpace) > 3):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    gillSpacekey = ['c', 'w', 'd']
    gillSpace = gillSpacekey[int(gillSpace) - 1]
    gillSize = input('What is the gill-size?:\n1. Broad.\n2. Narrow.')
    if (int(gillSize) < 1 or int(gillSize) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    gillSizekey = ['b', 'n']
    gillSize = gillSizekey[int(gillSize) - 1]
    gillColor = input('What is the gill-color?:\n1. Black.\n2. Brown\n3. Buff.\n4. Chocolate.\n5. Green.\n6. Orange.\n7. Pink.\n8. Purple.\n9. Red.\n10. White.\n11. Yellow.')
    if (int(gillColor) < 1 or int(gillColor) > 11):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    gillColorkey = ['k', 'n','b','h','g','r','o','p','u','e','w','y']
    gillColor = gillColorkey[int(gillColor) - 1]
    stalkShape = input('What is the stalk-shape?:\n1. Enlarging.\n2. Tapering.')
    if (int(stalkShape) < 1 or int(stalkShape) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkShapekey = ['e', 't']
    stalkShape = stalkShapekey[int(stalkShape) - 1]
    stalkRoot = input('What is the stalk-root?:\n1. Bulbous.\n2. Club.\n3. Cup.\n4. Equal.\n5. Rhizomorphs.\n6. Rooted.\n7. Missing.')
    if (int(stalkRoot) < 1 or int(stalkRoot) > 7):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkRootkey = ['b', 'c','u','e','z','r','?']
    stalkRoot = stalkRootkey[int(stalkRoot) - 1]
    stalkSAR = input('What is the stalk-surface-above-ring.\n1. Fibrous.\n2. Scaly.\n3. Silky.\n4. Smooth.')
    if (int(stalkSAR) < 1 or int(stalkSAR) > 4):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkSARkey = ['f', 'y', 'k', 's']
    stalkSAR = stalkSARkey[int(stalkSAR) - 1]
    stalkSBR = input('What is the stalk-surface-below-ring.\n1. Fibrous.\n2. Scaly.\n3. Silky.\n4. Smooth.')
    if (int(stalkSBR) < 1 or int(stalkSBR) > 4):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkSBRkey = ['f', 'y', 'k', 's']
    stalkSBR = stalkSBRkey[int(stalkSBR) - 1]
    stalkCAR = input('What is the stalk-surface-above-ring?:\n1. Brown.\n2. Buff\n3. Cinnamon.\n4. Gray.\n5. Orange.\n6. Pink.\n7. Red.\n8. White.\n9. Yellow.')
    if (int(stalkCAR) < 1 or int(stalkCAR) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkCARkey = ['n', 'b', 'c', 'g','o','p','e','w','y']
    stalkCAR = stalkCARkey[int(stalkCAR) - 1]
    stalkCBR = input('What is the stalk-surface-below-ring?:\n1. Brown.\n2. Buff\n3. Cinnamon.\n4. Gray.\n5. Orange.\n6. Pink.\n7. Red.\n8. White.\n9. Yellow.')
    if (int(stalkCBR) < 1 or int(stalkCBR) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    stalkCBRkey = ['n', 'b', 'c', 'g','o','p','e','w','y']
    stalkCBR = stalkCBRkey[int(stalkCBR) - 1]
    veilType = input('What is the veil-type?:\n1. Partial.\n2. Universal.')
    if (int(veilType) < 1 or int(veilType) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    veilTypekey = ['p', 'u']
    veilType = veilTypekey[int(veilType) - 1]
    veilColor = input('What is the veil-color?:\n1. Brown.\n2. Orange.\n3. White.\n4. Yellow.')
    if (int(veilColor) < 1 or int(veilColor) > 4):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    veilColorkey = ['n', 'o','w','y']
    veilColor = veilColorkey[int(veilColor) - 1]
    ringNumber = input('How many rings?:\n1. None.\n2. One.\n3. Two.')
    if (int(ringNumber) < 1 or int(ringNumber) > 3):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    ringNumberkey = ['n', 'o', 't']
    ringNumber = ringNumberkey[int(ringNumber) - 1]
    ringType = input('What type of rings?:\n1. Cobwebby.\n2. Evanescent.\n3. Flaring.\n4. Large.\n5. None.\n6. Pendant.\n7. Sheathing.\n8. Zone.\n')
    if (int(ringType) < 1 or int(ringType) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    ringTypekey = ['c', 'e', 'f','l','n','p','s','z']
    ringType = ringTypekey[int(ringType) - 1]
    query = 'BEGIN TRANSACTION; INSERT INTO mushrooms(id, class, bruises, odor, "spore-print-color", population, habitat) VALUES (' + str(id) + ',"' + ident + '","' + bruises + '","' + odor + '","' + sporePrintColor + '","' + population + '","' + habitat + '"); INSERT INTO cap ("cap-shape", "cap-surface", "cap-color", id) VALUES ("' + capShape + '","' + capSurface + '","' + capColor + '",' + str(id) + '); INSERT INTO gill ("gill-attachment", "gill-spacing", "gill-size", "gill-color", id) VALUES ("' + gillAttach + '","' + gillSpace + '","' + gillSize + '","' + gillColor + '",' + str(id) + '); INSERT INTO stalk ("stalk-shape", "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", id) VALUES ("' + stalkShape + '","' + stalkRoot + '","' + stalkSAR + '","' + stalkSBR + '","' + stalkCAR + '","' + stalkCBR + '",' + str(id) + '); INSERT INTO "veil-ring" ("veil-type", "veil-color", "ring-number", "ring-type", id) VALUES ("' + veilType + '","' + veilColor + '","' + ringNumber + '","' + ringType + '",' + str(id) + '); COMMIT;'
    cur.executescript(query)
    print(query)
    input('Transaction complete press any key to return to the menu...')
    clear()
    menu()

def dbCheck():
    bruises = input('Are there bruises?:\n1. Yes.\n2. No.')
    if (int(bruises) < 1 or int(bruises) > 2):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    bruiseskey = ['t', 'f']
    bruises = bruiseskey[int(bruises) - 1]
    odor = input(
        'What does it smell like?:\n 1. Almond.\n2. Anise.\n3. Creosote.\n4. Fishy.\n5. Foul.\n6. Musty\n7. None\n8. Pungent.\n9. Spicy')
    if (int(odor) < 1 or int(odor) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    odorkey = ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's']
    odor = odorkey[int(odor) - 1]
    sporePrintColor = input(
        'What color is the spore print?:\n1. Black.\n2. Brown\n3. Buff.\n4. Chocolate.\n5. Green.\n6. Orange.\n7. Purple.\n8. White.\n9. Yellow')
    if (int(sporePrintColor) < 1 or int(sporePrintColor) > 9):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    sporePrintColorkey = ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y']
    sporePrintColor = sporePrintColorkey[int(sporePrintColor) - 1]
    population = input(
        'What is the population?:\n1. Abundant.\n2. Clustered.\n3. Numerous.\n4. Scattered.\n5. Several.\n6. Solitary.')
    if (int(population) < 1 or int(population) > 6):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    populationkey = ['a', 'c', 'n', 's', 'v', 'y']
    population = populationkey[int(population) - 1]
    habitat = input(
        'What is the habitat?:\n1. Grasses.\n2. Leaves.\n3. Meadows.\n4. Paths.\n5. Urban.\n6. Waste.\n7. Woods.')
    if (int(habitat) < 1 or int(habitat) > 7):
        input('Incorrect input please try again')
        clear()
        dbInsert()
    clear()
    habitatkey = ['g', 'l', 'm', 'p', 'u', 'w', 'd']
    habitat = habitatkey[int(habitat) - 1]
    query = 'SELECT ((Q1*1.0)/((Q1+Q2)*1.0)*100) FROM (SELECT count(*) AS Q1 FROM mushrooms WHERE class = "p" AND bruises = "' + bruises + '" AND odor = "' + odor + '" AND "spore-print-color" = "' + sporePrintColor +'" AND population = "' + population +'" AND habitat = "' + habitat +'"),(SELECT count(*) AS Q2 FROM mushrooms WHERE class = "e" AND bruises = "' + bruises + '" AND odor = "' + odor + '" AND "spore-print-color" = "' + sporePrintColor + '" AND population = "' + population + '" AND habitat = "' + habitat + '");'
    cur.execute(query)
    result = cur.fetchone()
    print(query)
    if (result[0] == None):
        print('No cases exist for poisonous or edible with the supplied combination')
    else:
        print('From the provided information the probability of: ',result[0],'% of being poisonous and a ',(100 - float(result[0])),'% chance of being edible.')
    input('Press any key to return to the main menu...')
    clear()
    menu()
    
menu()



