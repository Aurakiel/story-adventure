#---IMPORTS------------------------------------------------------------------------------------------------------------
from sa_chapter_two import chapter_two_go_forward
from sa_functions import clear_screen, random_encounter, loading_bar, game_over, end_chapter
from sa_class import Narrator, Hero
import random, time
#---Globals------------------------------------------------------------------------------------------------------------
hero = Hero("sa_chapter_one_hero", 30, 30, 5)
#---Header-------------------------------------------------------------------------------------------------------------
def chapter_one_header():
    print("""
████████████████████████████████
╔═╗┬ ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔═╗┌┐┌┌─┐
║  ├─┤├─┤├─┘ │ ├┤ ├┬┘  ║ ║│││├┤ 
╚═╝┴ ┴┴ ┴┴   ┴ └─┘┴└─  ╚═╝┘└┘└─┘
████████████████████████████████""")
#----------------------------------------------------------------------------------------------------------------------
# Chapter One
#----------------------------------------------------------------------------------------------------------------------
def chapter_one():
    narration = Narrator("Chapter 1")
    clear_screen()
    chapter_one_header()
    narration.text = f"""
Narrator: You find yourself walking along a narrow dirt path winding through an ancient forest. The scent of pine and 
damp earth fills your nostrils as towering trees stretch their gnarled branches overhead, casting shifting shadows in 
the fading light. A distant hoot of an owl echoes through the undergrowth, and a faint path veers off to the west, 
disappearing into dense foliage.

The overgrown path to the west appears seldom traveled, with thick brambles creeping over its edges. Faint tracks in 
the soil suggest something—or someone—has recently passed this way. Deeper in the forest, the trees press closer 
together, obscuring whatever lies ahead."""
    print()
    print(f"████████████████████████████████")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......to go [FORWARD]
Type '2' ......to go [WEST]
Make your Selection: """)
    #invaild selection autocorrects with a choice
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    #Initial Choice
    match selection:
        case '1':
            random_encounter()
            go_forward()
        case '2':
            random_encounter()
            go_west()
#----------------------------------------------------------------------------------------------------------------------
# Go Forward
#----------------------------------------------------------------------------------------------------------------------
def go_forward():
    narration = Narrator ("Go Forward")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: The forest grows darker as the canopy thickens overhead, blocking out the last remnants of daylight. The 
scent of damp earth intensifies, and the distant rustling of unseen creatures hints that you're not entirely alone. 
The path ahead is well-trodden, though roots twist through the soil like grasping fingers, demanding careful footing. 

A sudden gust of wind whispers through the trees, carrying with it the faintest hint of something unusual—perhaps the 
trace of smoke, or an unfamiliar, almost metallic scent. The path begins to slope downward, leading toward what sounds 
like a gently flowing stream somewhere ahead."""
    print()
    print(f"████████████████████████████████")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[PRESS ON] toward the source of the sound
Type '2' ......[TURN BACK] and head west
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            random_encounter()
            press_on()
        case '2':
            random_encounter()
            go_west()
#---press_on-----------------------------------------------------------------------------------------------------------
def press_on():
    narration = Narrator("Press On")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: As you press on, the path descends into a shallow ravine where a narrow stream winds its way through 
moss-covered rocks. The gentle babbling of water fills the air, mingling with the rustling of leaves in the growing 
twilight. The scent of damp stone and fresh water is stronger here, but so is that faint, metallic tang from before.

A crude wooden bridge, barely wide enough for one person, spans the stream. It looks old, its planks weathered and 
slick with moisture. Across the bridge, the path continues into the deepening forest, where the trees seem almost 
unnaturally still. A faint flicker of light—perhaps a fire or lantern—glows in the distance, barely visible through 
the dense foliage. 

As you step closer to the bridge, something shifts in the shadows beneath it. The water ripples slightly, though there 
is no breeze."""
    print()
    print(f"████████████████████████████████")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[INVESTIGATE] the disturbance in the water
Type '2' ......[TURN BACK] and head west
Type '3' ......[CROSS] the bridge
Make your Selection: """)
    if selection != '1' and selection != '2' and selection != '3':
        random_selection = random.randint(1, 3)
        selection = str(random_selection)
    match selection:
        case '1':
        #---GAME OVER--------------------------------------------------------------------------------------------------
            clear_screen()
            print(f"████████████████████████████████")
            narration.text = f"""
Narrator: You step cautiously toward the edge of the stream, peering beneath the bridge where the shadows gather 
thickly. The water is dark, its surface reflecting the dimming light in broken, shifting patterns. At first, nothing 
seems out of the ordinary—just the gentle flow of the current and the mossy stones beneath.

Then, a shape moves.

A pair of gleaming eyes snap open beneath the bridge, too large, too deep-set to belong to any ordinary creature. 
Before you can react, a clawed hand—pale and slick with river moss—shoots out of the darkness, grasping your ankle with 
impossible strength.

You stumble, scrambling for footing, but the thing beneath the bridge pulls you in. The cold water rushes over your 
head, muffling your scream. You kick, you claw, but it’s useless—the grip tightens, and the last thing you see before 
the darkness takes you is a row of jagged teeth splitting open into an inhuman grin."""
            print()
            print(f"████████████████████████████████")
            time.sleep(6)
            game_over()
        case '2':
            random_encounter()
            go_west()
        case '3':
            random_encounter()
            cross_bridge()
#---cross_bridge-------------------------------------------------------------------------------------------------------
def cross_bridge():
    narration = Narrator("Cross Bridge")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: You take a cautious step onto the slick, weathered planks. The wood creaks beneath your weight, but it holds. 
The faint glow in the distance flickers, almost beckoning, as you move further across.

Halfway over, the air grows unnaturally still. The forest around you seems to hush, as if holding its breath. Beneath 
the bridge, the water shifts again, but this time—nothing reaches for you.

With a final step, you reach the other side. The path continues ahead, winding deeper into the dark forest. That 
strange glow pulses softly through the trees, too steady to be firelight, too warm to be moonlight. Whatever lies 
ahead, it promises answers—or danger."""
    print()
    print(f"████████████████████████████████")
    time.sleep(10)
    end_chapter()
    loading_bar()
#---Chapter Two Begins-------------------------------------------------------------------------------------------------
    chapter_two_go_forward()
#----------------------------------------------------------------------------------------------------------------------
# Go West
#----------------------------------------------------------------------------------------------------------------------
def go_west():
    narration = Narrator("Go West")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: You push through the thick brambles, their thorny tendrils grasping at your clothes as you step onto the 
overgrown path. The air feels different here—heavier, charged with an eerie stillness. The fading light struggles to 
penetrate the dense canopy above, casting the forest floor in deep, shifting shadows.

As you move forward, the tracks in the soil become more distinct—larger than a human’s, yet not quite animal. A 
strange, musky scent lingers in the air, and the silence is broken by the distant rustling of unseen movement.

Then, up ahead, you spot it—a weathered stone archway half-buried in creeping ivy. The carvings along its surface are 
ancient, their meaning lost to time. Beyond the arch, the path continues into darkness, swallowed by the depths of the 
forest."""
    print()
    print(f"████████████████████████████████")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[GO BACK] and continue on the main path
Type '2' ......[STEP THROUGH] the archway
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            random_encounter()
            go_forward()
        case '2':
            random_encounter()
            step_through()
#---step_through-------------------------------------------------------------------------------------------------------
def step_through():
    narration = Narrator("Step Through")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: As you step through the ancient archway, a sudden chill washes over you, raising goosebumps along your arms. 
The forest beyond feels different—older, untouched by time. The air hums with an unnatural stillness, and the scent of 
damp earth is tinged with something metallic, almost like iron. The path beneath your feet is no longer dirt but worn, 
moss-covered stone, as if this place was once part of something greater.

Fireflies flicker between the trees, their glow revealing glimpses of strange symbols carved into the trunks. 
The wind carries a whisper, though whether it’s the trees or something unseen, you cannot tell. To the right, the path 
slopes downward into mist, where shadowed shapes shift at the edges of your vision. To the left, a faint golden glow 
pulses from deep within the woods, beckoning with a soft warmth."""
    print()
    print(f"████████████████████████████████")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[RIGHT] into the mist
Type '2' ......[GO BACK] through the archway to the main path
Type '3' ......[LEFT] toward the golden glow
Make your Selection: """)
    if selection != '1' and selection != '2' and selection != '3':
        random_selection = random.randint(1, 3)
        selection = str(random_selection)
    match selection:
        case '1':
            random_encounter()
            go_right()
        case '2':
            random_encounter()
            go_forward()
        case '3':
        #---GAME OVER--------------------------------------------------------------------------------------------------
            clear_screen()
            print(f"████████████████████████████████")
            narration.text = f"""
Narrator: You turn left, drawn toward the soft golden glow pulsing through the trees. The warmth is inviting, almost 
comforting, like the flickering light of a hearth on a winter’s night. As you step closer, the air grows thick, cloying 
with the scent of honey and wildflowers.

The source of the glow reveals itself—a ring of ancient stones, their surfaces engraved with shifting runes that pulse 
in time with an unseen heartbeat. At the center, a shimmering golden pool swirls, its depths reflecting nothing but 
endless light. A strange lull washes over you, a soothing voice at the edge of your thoughts whispering of rest, of 
peace, of letting go.

Your legs grow heavy. Your eyelids droop. The warmth cradles you, urging you forward.

You take another step.

The moment your foot touches the liquid surface, the glow surges. Pain, searing and absolute, floods through your body. 
The golden light turns to fire, consuming flesh, bone, thought. Your scream never leaves your throat. The warmth was 
never meant to comfort—it was meant to lure.

As the glow fades, the runes dim, waiting patiently for the next traveler."""
            print()
            print(f"████████████████████████████████")
            time.sleep(6)
            game_over()
#---go_right-----------------------------------------------------------------------------------------------------------
def go_right():
    narration = Narrator("Go Right")
    clear_screen()
    print(f"████████████████████████████████")
    narration.text = f"""
Narrator: You take the path to the right, descending into the swirling mist. The air grows colder with each step, and 
the trees around you loom like silent sentinels, their twisted branches reaching out as if to pull you back. The shapes 
shifting at the edges of your vision never fully form, always just beyond sight—watching, waiting.

The ground beneath your feet softens, the moss thick and damp. The mist coils around your legs, whispering against your 
skin like unseen fingers. But you press on.

Then, suddenly, the fog parts.

You find yourself standing before a massive stone doorway embedded in the hillside, its surface cracked with age yet 
thrumming with a quiet power. Strange symbols—similar to those carved into the trees—glow faintly along its edges. A 
sense of finality settles over you.

This is it.

As your fingers brush the cold stone, the runes flare to life, the air vibrating with unseen energy. The door groans 
open, revealing only darkness beyond."""
    print()
    print(f"████████████████████████████████")
    time.sleep(10)
    end_chapter()
    loading_bar()