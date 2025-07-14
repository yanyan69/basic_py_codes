import random
import msvcrt as m

def introduction():
    class_name = ['warrior', 'mage', 'archer', 'tank']
    level = 1
    strength = 0
    agility = 0
    intelligence = 0
    
    print("???: Greetings, Traveler! Welcome to the land of Termina!")
    input("↵ ")
    
    print("Mira: My name is Mira. I am an arch priest in this sacred land.")
    input("↵ ")
    
    print("Mira: ...and am looking for a comrade to help me fight.")
    input("↵ ")
    
    print("Mira: ...and slay the Demon lord that wrecked havoc and slaughtered our family!")
    input("↵ ")
    
    print("Anyway, may I know your name, dear traveler?")
    input("↵ ")
    
    player_name = input("System: Enter player name: ")
    
    print(f"{player_name}: The name is {player_name}. It's a pleasure to meet you!")
    input("↵ ")
    
    print(f"Mira: Ahh! A fierce name it is, {player_name}. The pleasure is mine!")
    input("↵ ")
    
    print("And, what is your class?")
    input("↵ ")
    
    while m.kbhit():
        m.getch()
    class_pick = int(input("Choose a class: 1 = 'warrior', 2 = 'mage', 3 = 'archer', 4 = 'tank': "))
    if class_pick == 1:
        strength = 10
        agility = 10
        intelligence = 5
    elif class_pick == 2:
        strength = 5
        agility = 5
        intelligence = 15
    elif class_pick == 3:
        strength = 6
        agility = 12
        intelligence = 7
    elif class_pick == 4:
        strength = 12
        agility = 8
        intelligence = 5
    else:
        print("Invalid Input. You have been promoted to a Peasant class!")
        class_pick = 'Peasant'
        strength = 3
        agility = 3
        intelligence = 3
    print(f"I am a {class_pick}.")
    input("↵ ")
    
    print(f"Mira: Great! A {class_pick}! Just what I've been looking for!")
    input("↵ ")
    
    print("*An explosion occurred near your location.*")
    input("↵ ")
    
    print("Mira: Oh No! It seems the Goblin King came back for revenge after we wiped out his entire army during our raid!")
    input("↵ ")
    
    print(f"Mira: Let's go slay that monster, {player_name}!")
    input("↵ ")
    
    print(f"{player_name}: Yes.")
    input("↵ ")
    
def battle():
    print(f"{player_name} and Mira vs Goblin King")
    player_decision = int(input("Attack = 1, Block = 2, Heal = 3"))


def chapter_one():
    print()
    
introduction()
battle()
chapter_one()
