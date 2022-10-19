
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def get_card (cards, card):
  card.append (random.choice (cards))

def cal_score (card = []):
  return sum (card)

def end (card1, card2):
  print (f"Your final hand: {card1}, final score: {cal_score (card1)}")
  print (f"Computer's final hand: {card2}, final score: {cal_score (card2)}")
  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_done = False
while True :
  start = input ("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower ()
  if start == 'n':
    exit ()
  else:
    is_done = False
    print (logo)
    user_cards = []
    get_card (cards, user_cards)
    get_card (cards, user_cards)
    user_score = cal_score (user_cards)
    computer_cards = []
    get_card (cards, computer_cards)
    get_card (cards, computer_cards)
    computer_score = cal_score (computer_cards)
    print (f"Your cards: {user_cards}, current score: {user_score}")
    print (f"Computer's first card: {computer_cards [0]}")
    if user_score == 21:
      if computer_score != 21:
        print ("You got Blackjack! You win")
        continue      
      else:
        print ("Computer got Blackjack! You lose")
        continue
    if computer_score == 21:
      print ("Computer got Blackjack! You lose")
      continue
    while input ("Type 'y' to get another card, type 'n' to pass ").lower () == 'y':
      get_card (cards, user_cards)
      print (f"Your cards: {user_cards}, current score: {cal_score (user_cards)}")
      print (f"Computer's first card: {computer_cards [0]}")
      if cal_score (user_cards) > 21:
        end (user_cards, computer_cards)
        print ("You went over. You lose")
        is_done = True
        break
        
    while cal_score (computer_cards) <= 16 and not is_done:
      get_card (cards, computer_cards)
      cal_score (computer_cards)
      if cal_score (computer_cards) > 21:
        end (user_cards, computer_cards)
        print ("Computer went over. You win")
        is_done = True
        break

    if not is_done:
      user_score = cal_score (user_cards)
      computer_score = cal_score (computer_cards)
      if user_score > computer_score:
        end (user_cards, computer_cards)
        print ("You win")
      elif user_score < computer_score:
        end (user_cards, computer_cards)
        print ("You lose")
      else:
        end (user_cards, computer_cards)
        print ("Draw")