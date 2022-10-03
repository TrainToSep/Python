rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
import random
print ("Welcome to rock, paper, scissors!")
player = int (input ("What do you choose? Type 1 for rock, 2 for paper, 3 for scissors: "))
if player == 1:
    print (rock)
elif player == 2:
    print(paper)
else:
    print (scissors)
print ("The computer chose:")
computer = random.randint (1, 3)
if computer == 1:
    print (rock)
    if player == 1:
        print ("It's a draw.")
    elif player == 3:
        print ("You lost!")
    elif player == 2:
        print ("You won!")
elif computer == 2:
    print(paper)
    if player == 2:
        print ("It's a draw.")
    elif player == 1:
        print ("You lost!")
    elif player == 3:
        print ("You won!")
else:
    print (scissors)
    if player == 3:
        print ("It's a draw.")
    elif player == 2:
        print ("You lost!")
    elif player == 1:
        print ("You won!")
