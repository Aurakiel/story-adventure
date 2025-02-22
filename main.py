#------------------------------
# Imports from sa_functions.py
#------------------------------
from sa_functions import intro_screen, clear_screen

#------------------------------
# Imports from sa_class.py
#------------------------------

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
    print(f"Game has started")
    time.sleep(6)
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


