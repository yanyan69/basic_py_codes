# Write code below 💖

from random import choice as ch
import datetime as dt

bday_messages = ['Hope you have a very Happy Birthday! 🎈',
'It\'s your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞']

random_message = ch(bday_messages)

today = dt.date.today()
next_birthday = dt.date(2025, 7, 15)

time_difference = next_birthday - today 

if today == next_birthday:
    print(random_message)
else:
    print(f'My birthday is {time_difference} away!')