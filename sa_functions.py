#-----------------------------------
# Functions
#-----------------------------------
#---IMPORTS-------------------------
import time
import os
import random
from sa_class import Narrator, Enemy
from sa_class import Hero, Armor, Weapon
#defaults for hero, armor, weapon, enemy
hero = Hero("FunHero", 50, 50, 5)
armor = Armor("Clothes", 0)
weapon = Weapon("Unarmed", 0)
enemy = Enemy("Type", 0, 0)
#-----------------------------------
# Practical Functions
#-----------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_bar():
    print()
    print(f"""
    ┏┓           •      ┏┓       
    ┃┓┏┓┏┓┏┓┏┓┏┓╋┓┏┓┏┓  ┃┃┏┓┏┓┏┓┏
    ┗┛┗ ┛┗┗ ┛ ┗┻┗┗┛┗┗┫  ┣┛┗┻┗┫┗ ┛
                     ┛       ┛   """)
    print(f"[------------------] 0%")
    time.sleep(1)
    print(f"████████████-------] 60%")
    time.sleep(3)
    print(f"██████████████████ 100%")
    time.sleep(0.05)
    clear_screen()

def stats_menu():
    print(f"""
    ███████████████████████████████
    ██   Player Stats      
    ███████████████████████████████
    ██     Name: {hero.name}   
    ██   Max HP: {hero.hp_max}/{hero.hp}     
    ██      AtK: {hero.atk}    
    ███████████████████████████████
    """)

def game_over():
    print(r"""
     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝ 
     """)

def victory():
    print(f"""
    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗    
    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝    
    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝     
    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝      
     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║       
      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝ 
      
        {hero.name}                        Hp: {hero.hp_max}/{hero.hp}
      """)

#-----------------------------------
# Enemy
#-----------------------------------
def random_enemy():
    #list to hold enemy types
    enemy_names = ["Rat", "Hag", "Mimic", "Ogre", "Goblin", "Ooze", "Skeleton", "Pixie", "Shadow", "Ghost"]
    #list for random hps
    enemy_hp = [25, 40, 55]
    #list for random attacks
    enemy_atk = [6, 10, 12]
    #enemy stats are declared
    enemy.name = random.choice(enemy_names)
    enemy.hp = random.choice(enemy_hp)
    enemy.atk = random.choice(enemy_atk)

def random_encounter():
    #calls random enemy
    random_enemy()
    #roll for initiative
    hero_roll = random.randint(1, 20)
    enemy_roll = random.randint(1, 20)
    #if hero begins
    if hero_roll > enemy_roll:
        #while both are alive
        while hero.hp > 0 and enemy.hp > 0:
            #hero rolls for attack
            attack_roll = random.randint(1, 20)
            #if the roll is not 10 or 20
            if attack_roll % 10 != 0:
                #enemy's hp is reduced by hero attack
                enemy.hp -= hero.atk
                print(f"Your attack lands! {enemy.name} loses {hero.atk}.")
                time.sleep(1)
            #if the roll is 10 or 20 the enemy dodges
            else:
                print(f"The {enemy.name.lower()} dodges your attack!")
                time.sleep(1)
            #enemy attacks
            enemy_attack = random.randint(1, 20)
            #enemy hits if not 10 or 20
            if enemy_attack % 10 != 0:
                #players hp is reduced by the attack
                hero.hp -= enemy.atk
                print(f"The enemies attack lands! {hero.name} loses {enemy.atk}")
                time.sleep(1)
           #if a 10 or 20 the player dodges
            else:
                print(f"{hero.name} dodges the enemies attack!")
                time.sleep(1)
        #if either hp drops to zero or below
        if hero.hp <= 0 or enemy.hp <= 0:
            #the player dies
            if hero.hp <= 0:
                game_over()
                time.sleep(5)
            #the player wins the encounter
            else:
                victory()
                time.sleep(5)
    #if the enemy begins - the same logic is followed in all situations
    elif enemy_roll > hero_roll:
        while hero.hp > 0 and enemy.hp > 0:
            #enemy attack
            enemy_attack = random.randint(1, 20)
            if enemy_attack % 10 != 0:
                hero.hp -= enemy.atk
                print(f"The enemies attack lands! {hero.name} loses {enemy.atk}")
                time.sleep(1)
            else:
                print(f"{hero.name} dodges the enemies attack!")
            #player attack
            attack_roll = random.randint(1, 20)
            if attack_roll % 10 != 0:
                enemy.hp -= hero.atk
                print(f"Your attack lands! {enemy.name} loses {hero.atk}.")
                time.sleep(1)
            else:
                print(f"The {enemy.name.lower()} dodges your attack!")
                time.sleep(1)
        #upon death of either
        if hero.hp <= 0 or enemy.hp <= 0:
            #hero dies
            if hero.hp <= 0:
                game_over()
                time.sleep(5)
            #hero wins
            else:
                victory()
                time.sleep(5)
    #if both roll the same number, the player avoids the encounter
    else:
        print(f"You've scared off the enemy! {enemy.name} runs away!")

#-----------------------------------
# NARRATION
#-----------------------------------
def intro_screen():
    #displays title screen and opening dialogue
    print(r"""
    █████████████████████████████████████████████
    ╔═╗┌┬┐┌─┐┬─┐┬ ┬  ╔═╗┌┬┐┬  ┬┌─┐┌┐┌┌┬┐┬ ┬┬─┐┌─┐  
    ╚═╗ │ │ │├┬┘└┬┘  ╠═╣ ││└┐┌┘├┤ │││ │ │ │├┬┘├┤   
    ╚═╝ ┴ └─┘┴└─ ┴   ╩ ╩─┴┘ └┘ └─┘┘└┘ ┴ └─┘┴└─└─┘
    
    ╔═╗  ╦ ╦┌─┐┬─┐┬  ┌┬┐  ┌─┐┌─┐  ╦ ╦┌─┐┬─┐┌┬┐┌─┐
    ╠═╣  ║║║│ │├┬┘│   ││  │ │├┤   ║║║│ │├┬┘ ││└─┐
    ╩ ╩  ╚╩╝└─┘┴└─┴─┘─┴┘  └─┘└    ╚╩╝└─┘┴└──┴┘└─┘
    █████████████████████████████████████████████
""")
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
    #if the user tries to skip ahead
    if hero.name == "":
        narration.text = (f"Narrator: Pressing [ENTER] will not hurry me along, best to practice patience or your tale "
                          f"will be decided by me. ")
        hero.name = input(f">Please type your name as you'd have it appear: ")
    #if the user still refuses to enter a name
    while hero.name == "":
        narration.text = (f"Narrator: You've entered what the programmers call a 'loop'. You'll need to enter a name to "
                          f"escape it.")
        hero.name = input(f">Please type your name as you'd have it appear: ")
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
            hero.hp_max += armor.add_hp
            #displays updates
            print()
            narration.text = (f"Narrator: {armor.name}'s can be fashionable. It's also added +{armor.add_hp} to your "
                              f"hit points.")
        #case 2 & 3 follow the same logic as case 1
        case '2':
            armor.name = "Leather"
            armor.add_hp = armor_bonus[1]
            hero.hp_max += armor.add_hp
            print()
            narration.text = (f"Narrator: {armor.name} huh? We listen and we don't judge. It will add +{armor.add_hp} "
                              f"to your hit points.")
        case '3':
            armor.name = "Plate"
            armor.add_hp = armor_bonus[2]
            hero.hp_max += armor.add_hp
            print()
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
            hero.hp_max += armor.add_hp
            #displays updates
            print()
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
            print()
            narration.text = (f"Narrator: A true hero indeed. Your {weapon.name.lower()} will add +{weapon.add_atk} "
                              f"to your attack.")
        #case 2 follows the same logic as case 1
        case '2':
            weapon.name = "Mace"
            weapon.add_atk = weapon_bonus[1]
            hero.atk += weapon.add_atk
            print()
            narration.text = (f"Narrator: A big hammer never misses the nail. Your {weapon.name.lower()} will add "
                              f"+{weapon.add_atk} to your attack.")
        case '3':
            #updates weapon
            weapon.name = "Staff"
            weapon.add_atk = weapon_bonus[2]
            #updates hero - staff also adds it's bonus to hero hp
            hero.atk += weapon.add_atk
            hero.hp_max += weapon.add_atk
            #displays updates
            print()
            narration.text = (f"Narrator: Not the strongest weapon but the {weapon.name.lower()} adds +{weapon.add_atk} "
                              f"to your attack & hit points.")
        case _:
            #error randomizes the list index
            weapon.add_atk = random.choice(weapon_bonus)
            if weapon.add_atk == weapon_bonus[0]:
                weapon.name = "Sword"
                print()
                narration.text = (f"Narrator: I see I'll be choosing your weapon. Your {weapon.name.lower()} will add "
                                  f"+{weapon.add_atk} to your attack.")
            elif weapon.add_atk == weapon_bonus[1]:
                weapon.name = "Mace"
                print()
                narration.text = (f"Narrator: I see I'll be choosing your weapon. Your {weapon.name.lower()} will add "
                                  f"+{weapon.add_atk} to your attack.")
            else:
                weapon.name = "Staff"
                #staff also adds it's bonus to the hero hp
                hero.hp_max += weapon.add_atk
                print()
                narration.text = f"Narrator: I've added +{weapon.add_atk} to your hit points out of pity."
                narration.text = f"Narrator: Your {weapon.name.lower()} will also add +{weapon.add_atk} to your attack."
            #hero stats are updated
            hero.atk += weapon.add_atk
    #hp is set to max
    hero.hp = hero.hp_max
    #brief pause to read
    time.sleep(3)
    #the screen is cleared to display updated stat menu
    clear_screen()
    stats_menu()
    narration.text = f"Narrator: There your have it. It could be worse, it also could have been better."
    narration.text = f"Narrator: The first chapter is about to be written. Let's begin."
    loading_bar()