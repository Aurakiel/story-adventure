#---IMPORTS--------------------------
from sa_functions import clear_screen, random_encounter, loading_bar, game_over
from sa_class import Narrator, Hero
hero = Hero("Chpt One", 50, 50, 20)
import random, time
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
    narration.text = (f"""You find yourself walking along a narrow dirt path winding through an ancient forest. 
The scent of pine and damp earth fills your nostrils as towering trees stretch their gnarled branches 
overhead, casting shifting shadows in the fading light. A distant hoot of an owl echoes through the 
undergrowth, and a faint path veers off to the west, disappearing into dense foliage. 

The overgrown path to the west appears seldom traveled, with thick brambles creeping over its edges. 
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
    narration = Narrator("Go Forward")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = (f"""You follow the main path, the trees whispering with the evening breeze. The undergrowth rustles, 
and suddenly, a low growl reverberates from the shadows. A pair of glowing yellow eyes peer at you from behind 
a moss-covered log.""")
    random_encounter()
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = ("""You continue down the main path, the trees gradually thinning as you walk. The air grows cooler, and 
the faint sound of running water reaches your ears. Soon, you arrive at the edge of a gently flowing river, its 
surface shimmering under the moonlight. 

A wooden bridge, aged but sturdy, spans the water. A small wooden signpost stands at the entrance of the bridge, 
its text barely legible from years of exposure to the elements. You step closer and make out the faded inscription: 
"Cross with caution. The waters hold secrets." The cryptic message leaves you uneasy, but the bridge appears solid 
enough to cross.""")
    print(f"████████████████████████████████")
    narration.text = f"Narrator: Will you cross the bridge or turn around and go west?"
    selection = input("""Type 1 ......[CROSS] the bridge
Type 2 ......turn around and go [WEST]
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            cross_bridge()
        case '2':
            go_west()

def cross_bridge():
    narration = Narrator("Cross Bridge")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = ("""You step onto the bridge, its wooden planks creaking beneath your weight. As you reach the midpoint, 
the river below churns violently, and an eerie blue glow begins to emanate from the depths. 

Suddenly, a spectral figure rises from the water, its translucent form hovering before you. Its hollow eyes fixate on 
you as a whispering voice fills the air: 'Only those who answer truthfully may pass.' 

The spirit's voice echoes in your mind: 'I have no life, but I can die. I don't breathe, but I need air. What am I?'""")
    print(f"████████████████████████████████")
    narration.text = f"Narrator: Choose your answer {hero.name}."
    selection = input("""Type 1 ......[THE WIND]
Type 2 ......[A FIRE]
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            clear_screen()
            print(f"████████████████████████████████")
            narration.text = ("""The spirit's eyes glow brighter, and the river begins to churn violently. "You have answered 
falsely," it intones, its voice like the rustling of dead leaves. Without warning, spectral hands shoot up from the 
water, grasping at your legs.

Before you can react, the world tilts, and you are pulled down into the river’s depths. The cold water engulfs you, 
and your vision darkens as eerie whispers fill your mind. Just before unconsciousness takes hold, you feel yourself 
being dragged somewhere deep below...""")
            time.sleep(2)
            game_over()
        case '2':
            clear_screen()
            print(f"████████████████████████████████")
            narration.text = ("""The spirit's hollow gaze lingers on you for a moment, then it nods slowly. 'You have answered 
wisely. The path is open to you.' The spectral figure fades back into the depths, and the river's surface calms. 

You take a deep breath and step forward, crossing the remainder of the bridge. On the far side, the path continues 
toward a distant flickering light. What awaits you beyond the river remains unknown. """)
            time.sleep(2)
            loading_bar()

def go_west():
    narration = Narrator("Go West")
    clear_screen()
    print(f"████████████████████████████████")
    print("""You step cautiously onto the westward path, pushing aside brambles as you go. The air grows thick with 
the scent of moss and decay. Shafts of pale moonlight filter through the dense canopy, illuminating a small clearing 
up ahead. At the center of the clearing, you see an ancient stone well, its edges worn smooth by time. The ground 
around it is scattered with strange, broken symbols, and a faint humming sound seems to rise from its depths.

You peer into the well. The darkness below seems deeper than it should be, an abyss untouched by light. A soft, 
whispering voice drifts upward, forming words you cannot quite understand. The stones surrounding the well vibrate 
slightly beneath your fingers.""")
    print(f"████████████████████████████████")
    narration.text = f"Narrator: Do you dare reach inside {hero.name}?"
    selection = input("""Type 1 ......[NO]
Type 2 ......[YES]
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            no_do_nothing()
        case '2':
            yes_reach_in()

def no_do_nothing():
    narration = Narrator("No")
    clear_screen()
    print(f"████████████████████████████████")
    print("""You hesitate, uncertain of what to do next. The humming from the well grows louder, pulsing in time with 
your heartbeat. The whispering voice intensifies, but the words remain unintelligible.  A strange sensation prickles 
at the back of your neck, as if unseen eyes are watching. 
    
Moments pass. The forest is unnaturally still. 
    
Then, without warning, the whispering ceases, and the well falls silent. Whatever presence lingered here has either 
lost interest—or is waiting for you to act.""")
    time.sleep(12)
    print()
    print("""You remain where you are, unmoving. The silence around you deepens, pressing in like an unseen force. The well, once 
vibrating with energy, now feels like a gaping maw of endless darkness. 

Minutes stretch into eternity. The trees seem to close in, their twisted branches reaching toward you. A shiver runs 
down your spine as the temperature plummets. Shadows begin to stir at the edges of your vision, forming indistinct 
shapes that slither through the undergrowth.

The whispering returns, softer this time, almost pleading. You feel the weight of unseen eyes upon you, waiting. """)
    print(f"████████████████████████████████")
    narration.text = f"Narrator: Will you stay or flee to the main path?"
    selection = input("""Type 1 ......[STAY]
Type 2 ......[FLEE]
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            yes_reach_in()
        case '2':
            go_forward()

def yes_reach_in():
    clear_screen()
    print(f"████████████████████████████████")
    print(f"""You take a deep breath and slowly extend your hand into the darkness of the well. The moment your fingers 
breach the surface, an icy chill shoots up your arm, and the whispering grows into an eerie chorus of voices. A sudden 
force grips your wrist, pulling you downward.

Before you can react, your vision warps, and the world around you distorts. You feel weightless, as if falling through 
an endless void. The well’s edge vanishes, replaced by swirling shadows and flickering blue lights. The voices whisper 
secrets too ancient to comprehend, their meaning slipping through your mind like water through your fingers. 

Then, just as abruptly, the sensation ceases. You find yourself standing in a vast underground chamber, the walls lined 
with glowing runes. The air is thick with the scent of damp stone and something unfamiliar—something old. 

In the center of the chamber, a hooded figure watches you silently. Its voice echoes without sound: 'You have crossed 
the threshold. Now, you must prove yourself.'""")
    time.sleep(15)
    loading_bar()