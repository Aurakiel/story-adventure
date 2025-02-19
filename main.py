#------------------------------
# Imports from sa_functions.py
#------------------------------
from sa_functions import intro_narration

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
intro_narration()
gameStart = "yes"
while gameStart == 'yes':
    print(f"Game has started")
    time.sleep(2)
    gameStart = "no"
#------------------------------
# End Program
#-------------------------------
    if gameStart == 'no':
        break


