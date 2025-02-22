#-----------------------------------
# Class File
#-----------------------------------
#---IMPORTS-------------------------
import time
#-----------------------------------

#---CLASS for HERO------------------
class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

#---CLASS for Armor-----------------
class Armor:
    def __init__(self, hp):
        self.add_hp = hp

#---CLASS for Weapon-----------------
class Weapon:
    def __init__(self, atk):
        self.add_atk = atk

#---CLASS for NARRATOR---------------
class Narrator:
    def __init__(self, text):
        #eneter text to store
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text
        for char in self._text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()