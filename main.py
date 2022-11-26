#import random module
from random import choice
from game_data import data
#random.choice to the game_data data set
game_stop = False
score = 0
#assign to A and B a random data put it in a function
a = choice(data)  
b = choice(data)
print(f"{a['name']}, {a['follower_count']}, from {a['country']}")
print(f"{b['name']}, {b['follower_count']}, from {b['country']}")


#create a function that compares followers size. A to B
def compare(a_,b_):
  #getting user choice
  global game_stop
  global score
  global a
  global b
  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  if user_choice == 'A':
    user_choice = a_
    if user_choice['follower_count'] > b_['follower_count']:
      score += 1
      print('you are right')
    else:
      game_stop = True
      print(f"Sorry, that's wrong. Final score: {score}")
      return
  else:
    user_choice = b_
    if user_choice['follower_count'] > a_['follower_count']:
      score += 1
      print('you are right')
    else:
      game_stop = True
      print(f"Sorry, that's wrong. Final score: {score}")
      return
  a = b_
  b = choice(data)
  
    

#B becomes A and generate another random data to B, continue until made a mistake  


while not game_stop:
  compare(a,b)
  print(f"{a['name']}, {a['follower_count']}, from {a['country']}")
  print(f"{b['name']}, {b['follower_count']}, from {b['country']}")