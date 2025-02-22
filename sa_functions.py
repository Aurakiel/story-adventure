#-----------------------------------
# Functions
#-----------------------------------
#---IMPORTS-------------------------
import time
import os
from sa_class import Narrator

#-----------------------------------
# Practical Functions
#-----------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#-----------------------------------
# NARRATION
#-----------------------------------
def intro_screen():
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
    print()
    print(f"Generating Pages...")
    print(f"<----------> 0%")
    time.sleep(1)
    print(f"<====------> 40%")
    time.sleep(3)
    print(f"<=========> 100%")
    time.sleep(1)
    clear_screen()