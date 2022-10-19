print ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print ("Welcome to treasure island! \n")
print ("Your mission is to find the treasure. \n")
choice1 = input ('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n').lower ()
if choice1 == "left":
    print ("You fell into a hole! Game over! \n")
else:
    choice2 = input ('You\'ve come to a lake. Type "swim" to swim over, type "wait" to wait for a boat. \n').lower ()
    if choice2 == "swim":
        print("You've been eaten by a crocodile! Game over. \n")
    else:
        choice3 = input ('You\'ve arrived at the island unharmed. There is a house with 3 doors. Which one do you choose? "green", "red" or "yellow?" \n')
        if choice3 == "red":
            print ("It's an armpit! You lost! \n")
        elif choice3 == "green":
            print ("Congragulation, you found the treasure box! \n")
        else:
            print ("It's a fire room! You lost! \n")


