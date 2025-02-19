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
def intro_narration():
    narration = Narrator("Intro")
    print("==============================================================================")
    narration.text = (f"Narrator: What have we here? A brave adventurer ready to begin "
                      f"their story?")
    narration.text = f"Narrator: ...or just another bored mortal killing time?"
    narration.text = (f"Narrator: It really makes no difference, we're both here now so "
                      f"we should begin.")
    print("==============================================================================")
    print("           oOo oOo C.R.E.A.T.I.N.G oOo oOo oOo S.T.O.R.Y oOo oOo")
    time.sleep(2)
    clear_screen()




