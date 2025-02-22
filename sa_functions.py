#-----------------------------------
# Functions
#-----------------------------------
#---IMPORTS-------------------------
import time
import os
import random
from sa_class import Narrator
from sa_class import Hero, Armor, Weapon
#defaults for hero, armor, weapon
hero = Hero("YourName", 25, 5)
armor = Armor("Clothes", 0)
weapon = Weapon("Unarmed", 0)

#-----------------------------------
# Practical Functions
#-----------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_bar():
    print()
    print(f"Generating Pages...")
    print(f"<----------> 0%")
    time.sleep(1)
    print(f"<====------> 40%")
    time.sleep(3)
    print(f"<=========> 100%")
    time.sleep(1)
    clear_screen()

def stats_menu():
    print(f"""        +----------------------+
        |   Player Stats      |
        +----------------------+
        | Name: {hero.name}   
        |   HP: {hero.hp}     
        |  AtK: {hero.atk}    
        +----------------------+ """)

#-----------------------------------
# NARRATION
#-----------------------------------
def intro_screen():
    #displays title screen and opening dialogue
    print(r"""     _______________________
    ||                     ||
    ||                     ||
    ||   STORY ADVENTURE   ||
    ||   A World of Words  ||
    ||                     ||
    ||                     ||
    ||                     ||
    ||                     ||
    ||                     ||
    ||                     ||
    ||_____________________||
    |_______________________|""")
    time.sleep(2)
    narration = Narrator("Title Screen")
    narration.text = f"Narrator: What have we here? A brave adventurer ready to begin their story?"
    narration.text = f"Narrator: ...or just another bored mortal killing time?"
    narration.text = f"Narrator: It really makes no difference, you're here now so we should begin."
    loading_bar()

def naming_narration():
    #handles naming
    narration = Narrator("Naming Narration")
    narration.text = f"Narrator: Every story has a main character.  In our tale, it's you."
    #prompt for user input
    hero.name = input(f">Please type your name as you'd have it appear: ")
    #displays name given by user
    narration.text = (f"Narrator: {hero.name}, hero of legend! Are you sure this is the name you want echoed through "
                      f"history?")
    #prompt for name confirmation
    user_input = input(">Type 'yes' to confirm your name or 'no' to give another: ")
    #converts input to manage selection
    selection = user_input.lower()
    match selection:
        case 'no':
            narration.text = f"Narrator: Our story hasn't even started yet and you're already making changes."
            narration.text = f"Narrator: Have it your way my insecure friend. What shall we call you?"
            #prompt for new name
            hero.name = input(">For the final time, type your name as you'd have it appear: ")
            #displays new name
            narration.text = f"Narrator: I'm already beginning to question your life choices...{hero.name}."
            narration.text = f"Narrator: The name is officially yours.  Before we begin, we'll go over your stats."
            loading_bar()
        case 'yes':
            narration.text = f"Narrator: The name is officially yours. Before we begin, we'll go over your stats."
            loading_bar()
        case _:
            narration.text = f"Narrator: When given two options, you choose to go rogue."
            narration.text = f"Narrator: Learn, when this happens I'll be making choices for you."
            #list for holding dumb names the narrator chooses for you
            dumb_names = ['Fiddlesticks', 'McSnickerdoodle', 'Wobblebottom', 'Cuddlefluff', 'Snugglepants', 'Twinkletoes']
            #updates hero name
            hero.name = random.choice(dumb_names)
            #displays the dumb name the player is stuck with
            narration.text = f"Narrator: Going forward, following directions is in your best interest...{hero.name}."
            narration.text = f"Narrator: Before we begin, we'll go over your stats."
            loading_bar()
def stats_explained():
    #calls the stats menu
    stats_menu()
    narration = Narrator("Stats")
    narration.text = f"Narrator: That's what you're working with {hero.name}. At least here in the beginning."
    narration.text = f"Narrator: You'll boost those numbers as your story progresses...or it will end in tears."
    narration.text = f"Narrator: Either way, it'll be an interesting read...what?"
    narration.text = (f"Narrator: Fine, we'll add some equipment if it'll make you feel better. "
                      f"It is dangerous to go alone...or so I'm told.")
    narration.text = f"Narrator: As far as armor goes, you have a few options. Light, medium, or heavy?"
    #list for holding values based on selection
    armor_bonus = [10, 20, 30]
    #gets armor type
    selection = input(""">
    Type: 1 ......to select light armor
    Type: 2 ......to select medium armor
    Type: 3 ......to select heavy armor
    Make your Selection: """)
    match selection:
        case '1':
            #updates armor
            armor.name = "Robe"
            armor.add_hp = armor_bonus[0]
            #adds the armor to hero stats
            hero.hp += armor.add_hp
            #displays updates
            narration.text = (f"Narrator: {armor.name}'s can be fashionable. It's also added +{armor.add_hp} to your "
                              f"hit points.")
        #case 2 & 3 follow the same logic as case 1
        case '2':
            armor.name = "Leather"
            armor.add_hp = armor_bonus[1]
            hero.hp += armor.add_hp
            narration.text = (f"Narrator: {armor.name} huh? We listen and we don't judge. It will add +{armor.add_hp} "
                              f"to your hit points.")
        case '3':
            armor.name = "Plate"
            armor.add_hp = armor_bonus[2]
            hero.hp += armor.add_hp
            narration.text = (f"Narrator: {armor.name}. Better safe than sorry I say. This choice will add "
                              f"+{armor.add_hp} to your hit points.")
        case _:
            #error randomizes the list index
            armor.add_hp = random.choice(armor_bonus)
            #armor name assigned based off random list index
            if armor.add_hp == armor_bonus[0]:
                armor.name = "Robe"
            elif armor.add_hp == armor_bonus[1]:
                armor.name = "Leather"
            else:
                armor.name = "Plate"
            #adds the armor bonus to hero stats
            hero.hp += armor.add_hp
            #displays updates
            narration.text = (f"Narrator: Fine, I'll choose. Your {armor.name.lower()} will add +{armor.add_hp} to "
                              f"your hit points.")
    narration.text = f"Narrator: Now lets add a weapon. Make your selection."
    #list for holding values based on selection
    weapon_bonus = [15, 10, 5]
    #get weapon selection
    selection = input(""">
    Type: 1 ......to wield a sword
    Type: 2 ......to wield a mace
    Type: 3 ......to wield a staff
    Make your Selection: """)
    match selection:
        case '1':
            #updates weapon
            weapon.name = "Sword"
            weapon.add_atk = weapon_bonus[0]
            #adds the weapon to hero stats
            hero.atk += weapon.add_atk
            #displays updates
            narration.text = (f"Narrator: A true hero indeed. Your {weapon.name.lower()} will add +{weapon.add_atk} "
                              f"to your attack.")
        #case 2 follows the same logic as case 1
        case '2':
            weapon.name = "Mace"
            weapon.add_atk = weapon_bonus[1]
            hero.atk += weapon.add_atk
            narration.text = (f"Narrator: A big hammer never misses the nail. Your {weapon.name.lower()} will add "
                              f"+{weapon.add_atk} to your attack.")
        case '3':
            #updates weapon
            weapon.name = "Staff"
            weapon.add_atk = weapon_bonus[2]
            #updates hero - staff also adds it's bonus to hero hp
            hero.atk += weapon.add_atk
            hero.hp += weapon.add_atk
            #displays updates
            narration.text = (f"Narrator: Not the strongest weapon but the {weapon.name.lower()} adds +{weapon.add_atk} "
                              f"to your attack & hit points.")
        case _:
            #error randomizes the list index
            weapon.add_atk = random.choice(weapon_bonus)
            if weapon.add_atk == weapon_bonus[0]:
                weapon.name = "Sword"
            elif weapon.add_atk == weapon_bonus[1]:
                weapon.name = "Mace"
            else:
                weapon.name = "Staff"
                #staff also adds it's bonus to the hero hp
                hero.hp += weapon.add_atk
                narration.text = f"Narrator: I've added +{weapon.add_atk} to your hit points out of pity."
            #hero stats are updated
            hero.atk += weapon.add_atk
            #snarky display
            narration.text = (f"Narrator: I see I'll be choosing your weapon. Your {weapon.name.lower()} will add "
                              f"+{weapon.add_atk} to your attack.")
    #brief pause to read
    time.sleep(3)
    #the screen is cleared to display updated stat menu
    clear_screen()
    stats_menu()
    narration.text = f"Narrator: There your have it. It could be worse, it also could have been better."
    narration.text = f"Narrator: The first chapter is about to be written. Let's begin."
    loading_bar()