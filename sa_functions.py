#-----------------------------------
# Functions
#-----------------------------------
#---IMPORTS-------------------------
import time
import os
import random
from sa_class import Narrator
from sa_class import Hero
hero = Hero("YourName", 25, 5)

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