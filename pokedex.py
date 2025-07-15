class Pokedex:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        if self.is_caught == True:
            print(f"The {self.name} speaks: {self.name} {self.name}!!!")
        else:
            print(f"The wind blows of emptiness as you have not even caught a {self.name} yet.")
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught == True:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")
            
pikachu = Pokedex(25, 'Pikachu', 'Electric', 'When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.', False)
meowth = Pokedex(52, 'Meowth', 'Normal', 'All it does is sleep during the daytime. At night, it patrols its territory with its eyes aglow.', True)
bidoof = Pokedex(399, 'Bidoof', 'Normal', 'With nerves of steel, nothing can perturb it. It is more agile and active than it appears.', True)

pikachu.display_details()
pikachu.speak()
meowth.display_details()
meowth.speak()
bidoof.display_details()
bidoof.speak()