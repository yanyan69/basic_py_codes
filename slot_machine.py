# Write code below 💖

import random

def play():
  symbol = ['🍒',' 🍇', '🍉', '7️⃣']

  result = random.choices(symbol, k=3)
  for k in result:
    print(k, end =' | ')

  if result[0] == symbol[3] and result[1] == symbol[3] and result[2] == symbol[3]:
    print('Jackpot')
  else:
    print('Thanks for playing')

user = ''
while True:
  user = input("Play? Y or N: ")
  if user == 'Y':
    play()
  elif user == 'N':
    print('Bye')
    break
  else:
    print('Invalid')