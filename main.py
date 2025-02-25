from sa_chapter_one import chapter_one
#---Imports from sa_functions.py-------------------------------------------------------------------------------------
from sa_functions import clear_screen, intro_screen, naming_narration, stats_explained
#---Imports from sa_class.py------------------------------------------------------------------------------------------
from sa_class import Hero, Armor, Weapon, Enemy
#default for Hero, Armor, Weapon, Enemy
hero = Hero("MainName", 30, 30, 5)
armor = Armor("Clothes",0)
weapon = Weapon("Unarmed",0)
enemy = Enemy("Type", 0, 0)
#---Other Imports----------------------------------------------------------------------------------------------------
import time
#---Imports from sa_chapter(s).py-----------------------------------------------------------------------------------

#---TEST AREA-------------------------------------------------------------------------------------------------------

#time.sleep(3)
#exit()
#------------------------------
# Start Program
#------------------------------
intro_screen()
gameStart = "yes"
while gameStart == 'yes':
    naming_narration()
    stats_explained()
    chapter_one()
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


