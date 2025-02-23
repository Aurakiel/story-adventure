#------------------------------
# Imports from sa_functions.py
#------------------------------
from sa_functions import clear_screen, intro_screen, naming_narration, stats_explained, random_encounter, victory

#------------------------------
# Imports from sa_class.py
#------------------------------
from sa_class import Hero, Armor, Weapon, Enemy
#default for Hero, Armor, Weapon, Enemy
hero = Hero("MainName", 25, 25, 5)
armor = Armor("Clothes",0)
weapon = Weapon("Unarmed",0)
enemy = Enemy("Type", 0, 0)
#------------------------------
# Other Imports
#------------------------------
import time
#------------------------------
# Start Program
#------------------------------
intro_screen()
gameStart = "yes"
while gameStart == 'yes':
    naming_narration()
    stats_explained()
    #random_encounter() - testing
    print("more game")
    time.sleep(3)
#------------------------------
# Kill Switch
#------------------------------
    gameStart = "no"
#------------------------------
# End Program
#-------------------------------
    if gameStart == 'no':
        clear_screen()
        break


