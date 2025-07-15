import random

class Role:
    def __init__(self, player_name, level, attributes, role):
        self.player_name = player_name
        self.level = level
        self.attributes = attributes
        self.role = role
    
    def player_role(self):
        #to be updated
        print('')
    def player_attributes(self):
        #to be updated
        print('')
    def player_experience(self):
        #to be updated
        print('')
    def boss(self, enemy):
        print('')
    def introduction(self):
        self.role = ['warrior', 'mage', 'archer', 'tank']
        self.level = 1
        self.attributes = [1,1,1]  #strength, agility, intelligence
        
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
        
        self.player_name = input("System: Enter player name: ")
        
        print(f"{self.player_name}: The name is {self.player_name}. It's a pleasure to meet you!")
        input("↵ ")
        
        print(f"Mira: Ahh! A fierce name it is, {self.player_name}. The pleasure is mine!")
        input("↵ ")
        
        print("Mira: And, what is your class?")
        input("↵ ")
        
        class_pick = int(input("Choose a class: 1 = 'warrior', 2 = 'mage', 3 = 'archer', 4 = 'tank': "))
        
        if class_pick == 1:
            self.role = 'Warrior'
            self.attributes = [10,10,5]
        elif class_pick == 2:
            self.role = 'Mage'
            self.attributes = [5,5,15]
        elif class_pick == 3:
            self.role = 'Archer'
            self.attributes = [6,12,7]
        elif class_pick == 4:
            self.role = 'Tank'
            self.attributes = [12,8,5]
        else:
            print("System: Invalid Input. You have been promoted to a Peasant class!")
            self.role = 'Peasant'
            self.attributes = [3,3,3]

        print(f"{self.player_name}: I am a {self.role}.")
        input("↵ ")
        
        print(f"Mira: Great! A {self.role}! Just what I've been looking for!")
        input("↵ ")
        
        print("Narrator: *An explosion occurred near your location.*")
        input("↵ ")
        
        print("Mira: Oh No! It seems the Goblin King came back for revenge after we wiped out his entire army during our raid!")
        input("↵ ")
        
        print(f"Mira: Let's go slay that monster, {self.player_name}!")
        input("↵ ")
        
        print(f"{self.player_name}: Yes.")
        input("↵ ")
        print("Narrator: You and Mira set out to face the Goblin King.")
        input("↵ ")
        
    def battle(self):
        player_health = 50
        goblin_king_health = 20
        
        print(f"The enemy is approaching...")
        input("↵ ")
        print(f"{self.player_name} and Mira vs Goblin King")
        while player_health > 0 and goblin_king_health > 0:
            player_decision = int(input("1 = Attack, 2 = Skill, 3 = Retreat: "))
            if player_decision == 1:
                player_attack_roll = random.randint(1,6)
                goblin_king_health -= player_attack_roll
                print(f"{self.player_name} dealt {player_attack_roll} to Goblin King")
                enemy_attack_roll = random.randint(1,6)
                player_health -= enemy_attack_roll
                print(f"Goblin King dealt {enemy_attack_roll} to {self.player_name}")
                print(f"Player health: {player_health} and Enemy: {goblin_king_health}")
            elif player_decision == 2:
                player_attack_roll = random.randint(6,12)
                goblin_king_health -= player_attack_roll
                enemy_attack_roll = random.randint(1,6)
                player_health -= enemy_attack_roll
            elif player_decision == 3:
                print(f"Narrator: You turned around and fled to the scene...")
                input("↵ ")
                print(f"...leaving everyone and Mira suffering")
                input("↵ ")
                print(f'Suddenly...')
                input("↵ ")
                print(f"You stopped moving, and looked down your limbs was cut off")
                input("↵ ")
                print("The goblin king grabbed you are tore you to pieces")
                input("↵ ")
                print("You Died")
                break
            else:
                print('invalid')
                continue
        if player_health <= 0:
            print(f"{self.player_name} has been defeated!")
            input("↵ ")
            print("Game Over")
            input("↵ ")
        else:
            print(f"{self.player_name} has defeated the Goblin King!")
            input("↵ ")
            print("Mira: We did it! We defeated the Goblin King!")
            input("↵ ")
            print(f"{self.player_name}: Yes, we did it together, Mira.")
            input("↵ ")
            print("Mira: Let's head back to the village and report our victory!")
            input("↵ ")
            print(f"{self.player_name}: Agreed. Let's go.")
            input("↵ ")
            print("Narrator: You and Mira returned to the village as heroes.")
            input("↵ ")
            print("Narrator: The villagers celebrated your victory and praised your bravery.")
            input("↵ ")
            print("Narrator: You and Mira became close friends and continued to fight together against the forces of evil.")
            input("↵ ")
            print("Narrator: The end.")

player = Role('', 0, [0,0,0], '')
player.introduction()
player.battle()