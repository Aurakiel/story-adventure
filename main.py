#------------------------------
# Imports from sa_functions.py
#------------------------------
from sa_functions import intro_screen, clear_screen, naming_narration

#------------------------------
# Imports from sa_class.py
#------------------------------
from sa_class import Hero
hero = Hero("YourName", 25, 5)
#------------------------------
# Other Imports
#------------------------------
import time
#-----------------------------
# Test Area (remove this)
#------------------------------

#exit()
#------------------------------
# Start Program
#------------------------------
intro_screen()
gameStart = "yes"
while gameStart == 'yes':
    naming_narration()
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


