#---IMPORTS------------------------------------------------------------------------------------------------------------
import time
#---CLASS for HERO-----------------------------------------------------------------------------------------------------
class Hero:
    def __init__(self, name, hp, hp_max, atk):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.atk = atk
#---CLASS for Armor----------------------------------------------------------------------------------------------------
class Armor:
    def __init__(self, name, hp):
        self.name = name
        self.add_hp = hp
#---CLASS for Weapon---------------------------------------------------------------------------------------------------
class Weapon:
    def __init__(self, name, atk):
        self.name = name
        self.add_atk = atk
#---Class for Enemy----------------------------------------------------------------------------------------------------
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
#---CLASS for NARRATOR-------------------------------------------------------------------------------------------------
class Narrator:
    def __init__(self, text):
        #eneter text to store
        self._text = text

    #defines .text
    @property
    def text(self):
        return self._text

    #controls display speed
    @text.setter
    def text(self, new_text):
        self._text = new_text
        for char in self._text:
            print(char, end='', flush=True)
            time.sleep(0.04)
        print()