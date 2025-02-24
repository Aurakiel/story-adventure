#---IMPORTS--------------------------
from sa_functions import clear_screen, random_encounter
from sa_class import Narrator
import random
#------------------------------------
# Chapter One
#------------------------------------
def chapter_one():
    narration = Narrator("Chapter 1")
    print("""
████████████████████████████████
╔═╗┬ ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔═╗┌┐┌┌─┐
║  ├─┤├─┤├─┘ │ ├┤ ├┬┘  ║ ║│││├┤ 
╚═╝┴ ┴┴ ┴┴   ┴ └─┘┴└─  ╚═╝┘└┘└─┘
████████████████████████████████""")
    print(f"""You find yourself walking along a narrow dirt path winding through an ancient forest. 
The scent of pine and damp earth fills your nostrils as towering trees stretch their gnarled branches 
overhead, casting shifting shadows in the fading light. A distant hoot of an owl echoes through the 
undergrowth, and a faint path veers off to the [WEST], disappearing into dense foliage. 

The overgrown path to the [WEST] appears seldom traveled, with thick brambles creeping over its edges. 
Faint tracks in the soil suggest something—or someone—has recently passed this way. Deeper in the forest, 
the trees press closer together, obscuring whatever lies ahead.""")
    print(f"████████████████████████████████")
    narration.text = (f"Narrator: Will you continue forward or go west? Friendly reminder, I choose when you cannot "
                      f"follow instructions.")
    selection = input("""Type 1 ......to go [FORWARD]
Type 2 ......to go [WEST]
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            go_forward()
        case '2':
            go_west()

#---Chapter One Selections------------
def go_forward():
    clear_screen()
    print(f"████████████████████████████████")
    print(f"""You follow the main path, the trees whispering with the evening breeze. The undergrowth rustles, 
and suddenly, a low growl reverberates from the shadows. A pair of glowing yellow eyes peer at you from behind 
a moss-covered log.""")
    random_encounter()

def go_west():
    clear_screen()
    print(f"████████████████████████████████")
    print("""You step cautiously onto the westward path, pushing aside brambles as you go. The air grows thick with 
the scent of moss and decay. Shafts of pale moonlight filter through the dense canopy, illuminating a small clearing 
up ahead. At the center of the clearing, you see an ancient stone well, its edges worn smooth by time. The ground 
around it is scattered with strange, broken symbols, and a faint humming sound seems to rise from its depths.""")