
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
  if sum (card) == 21 and len (card) == 2:
    return 0
  if sum (card) > 21 and 11 in card:
    card.remove (11)
    card.append (1)
  return sum (card)

def compare (computer_score, user_score):
  if computer_score == 0:
    return ("Computer got Blackjack. You lose")
  elif user_score == 0:
    return ("You got Blackjack. You win")
  elif computer_score > 21 and user_score > 21:
    return ("You went over. You lose")
  elif user_score > 21:
    return ("You went over. You lose")
  elif computer_score > 21:
    return ("Computer went over. You lose")
  elif user_score > computer_score:
    return ("You win")
  elif user_score < computer_score:
    return ("You lose")
  elif user_score == computer_score:
    return ("Draw")
  else:
    return 0

def end (user_cards, user_score, computer_cards, computer_score):
  print (f"Your final hand: {user_cards}, final score {user_score}")
  print (f"Computer's final hand: {computer_cards}, final score: {computer_score}")

def play_game ():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  computer_cards = []
  for i in range (2):
    get_card (cards, user_cards)
    get_card (cards, computer_cards)
  computer_score = cal_score (computer_cards)
  user_score = cal_score (user_cards)
  print (f"Your current cards: {user_cards}, current score: {user_score}")
  print (f"Computer's first card: {computer_cards [0]}")
  if compare (computer_score, user_score) != 0:
      end (user_cards, user_score, computer_cards, computer_score)
      print (compare (computer_score, user_score))
      return 
  while input ("Type 'y' to get another card, type 'n' to pass: ") == 'y'.lower ():
    get_card (cards, user_cards)
    computer_score = cal_score (computer_cards)
    user_score = cal_score (user_cards)
    print (f"Your current cards: {user_cards}, current score: {user_score}")
    print (f"Computer's first card: {computer_cards [0]}")
    if compare (computer_score, user_score) != 0:
      end (user_cards, user_score, computer_cards, computer_score)
      print (compare (computer_score, user_score))
      return 
  while computer_score != 0 and computer_score < 17:
    get_card (computer_cards)
    computer_score = cal_score (computer_cards)
  
  print (f"Your current cards: {user_cards}, current score: {user_score}")
  print (f"Computer's first card: {computer_cards [0]}")
  compare (computer_score, user_score)
  end (user_cards, user_score, computer_cards, computer_score)

while input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  print (logo)
  play_game ()

  

