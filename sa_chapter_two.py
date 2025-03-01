#---Imports------------------------------------------------------------------------------------------------------------
from sa_functions import clear_screen, random_encounter, loading_bar, game_over, end_chapter
from sa_class import Narrator
import random, time
#---Header-------------------------------------------------------------------------------------------------------------
def chapter_two_header():
    print("""
████████████████████████████████    
╔═╗┬ ┬┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔╦╗┬ ┬┌─┐
║  ├─┤├─┤├─┘ │ ├┤ ├┬┘   ║ ││││ │
╚═╝┴ ┴┴ ┴┴   ┴ └─┘┴└─   ╩ └┴┘└─┘
████████████████████████████████""")
#----------------------------------------------------------------------------------------------------------------------
# Chapter Two - Go Forward
#----------------------------------------------------------------------------------------------------------------------
def chapter_two_go_forward():
    narration = Narrator("Chapter Two - Go Forward")
    clear_screen()
    chapter_two_header()
    narration.text = """
Narrator: Curiosity tugs at you, and you step cautiously toward the pulsing glow. The deeper you go, the more the 
trees seem to bend inward, their gnarled limbs curling like grasping fingers. The glow pulses in time with your 
heartbeat, drawing you forward. As you step into a small clearing, you see its source—a crystalline orb, floating 
just above the ground, humming with energy.

As you reach out, the orb shudders and splits into two—one half glowing with a warm golden hue, the other deep and 
crimson. A whisper drifts through the air, unintelligible at first, until it forms a single, chilling question:

'Choose.'"""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......Touch the [GOLDEN] hued half
Type '2' ......Touch the [CRIMSON] hued half
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            random_encounter()
            golden_orb()
        case '2':
            random_encounter()
            crimson_orb()
#----------------------------------------------------------------------------------------------------------------------
# Go Forward - Golden Orb
#----------------------------------------------------------------------------------------------------------------------
def golden_orb():
    narration = Narrator("Golden Orb")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You reach out, fingers brushing against the golden half of the orb. The instant you make contact, a warmth 
floods through you—not just over your skin, but deep in your chest, sinking into your very bones. The forest around 
you flickers and twists, as if the world itself is shifting.

Then, silence.

When your vision clears, you are no longer in the shadowed clearing. Instead, you stand in a grand hall of white marble 
and gold, the air thick with the scent of old parchment and incense. Rows of towering bookshelves stretch high above, 
their spines etched with symbols you can’t understand. At the center of the room, a figure stands waiting—a woman in 
flowing robes, her face obscured by a golden mask.

"You have chosen the Light of Remembrance," she intones, her voice reverberating through the chamber. "But tell me, 
traveler... what is it that you seek?"

A surge of knowledge fills your mind. You realize that this place, wherever it is, holds answers—secrets lost to time, 
histories untold. But what you ask of this place may come at a price."""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you ask?"""
    selection = input("""Type '1' ......Seek [KNOWLEDGE] of your past
Type '2' ......Ask about the orbs [POWER]
Type '3' ......[DEMAND] to know where you are
Make your Selection: """)
    if selection != '1' and selection != '2' and selection != '3':
        random_selection = random.randint(1, 3)
        selection = str(random_selection)
    match selection:
        case '1':
            knowledge()
        case '2':
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: Your gaze drops to your hands, still tingling from the warmth of the orb. That light was no ordinary glow—it 
changed something inside you. You lift your head, fixing your eyes on the masked woman.

'The orb,' you say. 'What has it done to me?'

For a moment, she does not answer. Then, she raises a single hand. The air grows heavy, pressing against your chest, 
and the sigils lining the bookshelves begin to pulse—first softly, then violently.

'It has awakened something within you.' Her voice is calm, but there is a weight to it, a warning unspoken. 'Something 
that was never meant to wake.'

A dull ache blossoms in your chest. Then—pain.

Your breath hitches as the warmth inside you flares, no longer comforting, but searing. You stagger back, gripping 
your chest as golden light pours from your skin, too bright, too intense. The knowledge—the power—you wanted to 
understand is consuming you.

The masked woman does not move, does not try to stop it. She only watches.

'Power without purpose is a fire without form,' she says, voice distant as your vision blurs. 'And fire consumes all 
it touches.'

You try to scream, but no sound comes. The light overtakes you, and for an instant, you glimpse something beyond—a void 
of formless energy, a force too great for mortal hands to wield.

Then, there is nothing."""
            print()
            print("""████████████████████████████████""")
            time.sleep(6)
            game_over()
        case '3':
        #---GAME OVER--------------------------------------------------------------------------------------------------
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: A flicker of impatience rises in you. You square your shoulders and meet the masked woman’s gaze—or at least 
where her eyes should be.

"Where am I?" you demand. "What is this place?"

For a moment, silence stretches between you. Then, the golden mask tilts slightly.

"You were not ready to ask that question."

Before you can react, the warmth in your body vanishes, replaced by an unbearable cold. Your breath catches, your 
limbs stiffen—your heart stops. The golden light in the hall dims, the towering shelves fading into an abyss. The last 
thing you see is the woman turning away, her voice an echo as the darkness swallows you whole:

"Some knowledge is not meant for the unworthy."

You are dead."""
            print()
            print("""████████████████████████████████""")
            time.sleep(6)
            game_over()
#---Knowledge----------------------------------------------------------------------------------------------------------
def knowledge():
    narration = Narrator("Knowledge")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You steady yourself, feeling the weight of the moment press upon you. If this place holds knowledge, then 
surely it holds the truth of who I am... or who I was.

Taking a deep breath, you meet the masked woman's gaze and say, 'I want to know my past.'

A long silence follows. Then, she lifts a single hand and gestures toward the towering shelves. The books shift, their 
spines glowing with ethereal light, and one volume slides free, floating toward you. The cover bears no title—only an 
insignia that feels... familiar. Your pulse quickens as you take the book into your hands.

'Open it.'

You do. And as the pages turn, memories flood back—flashes of another life. You see yourself standing in a grand city 
of shimmering spires, your hands tracing runes into the air. You were once a scholar... no, more than that. A guardian 
of lost histories, entrusted with secrets long forgotten. But something happened. A betrayal. A fall. And then—darkness.

'You were cast out,' the woman murmurs, as if reading your thoughts. 'But now, the choice remains: will you reclaim 
what was taken, or forge a new path?'

You glance down at the book, heart pounding. You are not just anyone. You were someone of great importance. And now, 
given this second chance..."""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[RECLAIM] your legacy
Type '2' ......[FORGE] a new destiny
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            reclaim()
        case '2':
            forge()
#---Reclaim------------------------------------------------------------------------------------------------------------
def reclaim():
    narration = Narrator("Reclaim")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: Your fingers tighten around the book’s worn cover as the weight of revelation settles over you. You were not 
merely a scholar—you were a guardian of forgotten knowledge, entrusted with wisdom that others sought to erase. Someone 
had taken everything from you. Cast you into oblivion.

And yet, here you stand.

The masked woman watches in silence as you straighten, resolve hardening in your chest. 'I will reclaim what was 
taken,' you declare. The words taste like truth, like power, like a vow that binds itself to your very soul.

She nods, almost imperceptibly. The grand hall shimmers, the golden light flaring brilliantly before fading into a 
swirling abyss of stars. The ground shifts beneath you, the scent of parchment and incense replaced by cool night air. 
When the world steadies, you find yourself elsewhere—standing atop an ancient balcony, overlooking the ruins of a 
once-magnificent city.

Your city.

The towers, now crumbling, still hum with the remnants of old magic. The streets below are choked with vines, the 
echoes of footsteps long gone whispering through the wind. But beyond the ruins, deeper into the heart of this forsaken 
place, you sense something waiting. A presence.

A memory resurfaces—of a name spoken in whispers, of the one who orchestrated your fall.

You are not alone in this return.

As the moon casts its pale glow over the shattered remnants of your past, you take your first step forward, ready to 
reclaim what was lost."""
    print()
    print("""████████████████████████████████""")
    time.sleep(10)
    end_chapter()
    loading_bar()
    #---Chapter 3 - Reclaim--------------------------------------------------------------------------------------------
#---Forge--------------------------------------------------------------------------------------------------------------
def forge():
    narration = Narrator("Forge")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You run your fingers over the book’s worn cover, feeling the weight of the past pressing against you. These 
memories, these truths—they are part of you, but they do not define you. Whoever you once were, whatever was taken 
from you, it no longer holds power over who you can become.

You lift your gaze to the masked woman. 'No,' you say firmly. 'The past is gone. I will not chase ghosts. I will shape 
my own future.'

For a moment, she is silent. Then, slowly, she inclines her head.

'Then your path is your own.'

The golden hall around you begins to dissolve, the towering shelves turning to streaks of light. The ground vanishes 
beneath your feet, and for a breathless moment, you are weightless—adrift in the void between what was and what will be.

Then, the world reforms.

You stand at the edge of an unfamiliar city, its skyline dotted with flickering lanterns and towering spires. The air 
hums with possibility. New faces pass by, unaware of the past you left behind. The road before you is unwritten, 
waiting for your steps to carve its story.

The book in your hands vanishes, replaced by a single golden sigil etched into your palm—proof that you carry the 
wisdom of the past, even as you walk toward the future.

With a deep breath, you take your first step forward."""
    print()
    print("""████████████████████████████████""")
    time.sleep(10)
    end_chapter()
    loading_bar()
    #---Chapter 3 - Forge----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# Go Forward - Crimson Orb
#----------------------------------------------------------------------------------------------------------------------
def crimson_orb():
    narration = Narrator("Crimson Orb")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: Your fingers hesitate for only a moment before closing around the crimson half of the orb. A rush of warmth 
surges up your arm, spreading through your veins like liquid fire. The forest around you twists, the trees shuddering 
as if in protest. The whisper returns, louder now, threading into your thoughts.

'Blood binds, blood calls. Are you prepared to see?'

The world flickers. For a moment, you stand between realities—the clearing dissolving into shadow, replaced by a vision.

Before you, a battlefield stretches to the horizon, warriors clad in tattered crimson banners locked in endless combat. 
The ground is slick with blood, yet they do not fall. Wounds close, bones snap back into place, and the dead rise once 
more, their eyes burning with the same deep red glow as the orb in your grasp.

A figure steps forward from the chaos, cloaked in shadow but unmistakably aware of your presence. Their voice rumbles 
through the void.

'You have taken the path of the Crimson Veil. Blood remembers. Blood obeys. But tell me, traveler—will you wield it, or 
be consumed by it?'"""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[WIELD] the power
Type '2' ......[RESIST] the pull
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            wield()
        case '2':
        #---GAME OVER--------------------------------------------------------------------------------------------------
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: You clench your fist tighter around the orb, trying to resist. You refuse. You will not be a part of this 
eternal struggle.

The figure's gaze sharpens, their form shifting as the shadows around them twist and writhe. 'You resist,' they 
observe, their voice laced with amusement and disdain. 'Do you think you can defy the blood that calls you? Do you 
think you can stand against it?'

The air grows thick, suffocating. The orb in your hand flares with unbearable heat, burning into your skin like molten 
metal. Every nerve in your body screams for release, for escape from the overwhelming pressure. The whisper becomes a 
roar, deafening and relentless."""
            random_encounter()
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: 'Blood remembers. Blood calls. Blood obeys,' it repeats, now all-consuming.

You stumble backward, your vision blurring as the pressure on your chest tightens. The figure watches, their red eyes 
gleaming with cold amusement as you falter. The world around you distorts further, the trees now stretching and 
twisting, their bark cracking like bones. The shadowy figure steps closer, their presence suffocating.

'Fool,' they hiss, their voice now a snake’s hiss in your ear. 'You were never meant to defy it. The blood... will 
consume you.'

Before you can react, the orb pulses with blinding light. The warmth turns to fire, scorching your hand and spreading 
through your entire body. You try to scream, but your mouth is dry, your voice lost in the roar of the curse that now 
claims you. Your vision fades as the world crumbles, the last thing you hear being the echo of the figure's voice:

'Blood obeys.'

And then, there is nothing. The battlefield, the forest, the figure—all vanish as you are consumed, lost to the 
Crimson Veil."""
            print()
            print("""████████████████████████████████""")
            time.sleep(6)
            game_over()
#---wield--------------------------------------------------------------------------------------------------------------
def wield():
    narration = Narrator("Wield")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You feel the heat intensify as the crimson orb pulses in your hand, its power seeping deeper into your very 
soul. Without hesitation, you embrace the offer, binding yourself to the Crimson Veil. A rush of ancient memories 
floods your mind—visions of warriors long past, blood-drenched rituals, and a force older than the world itself. You 
are now one with the Veil, its power coursing through your veins.

The figure before you nods, a twisted smile curling beneath the shadowed hood.

'As the blood binds, so too does your fate. With this power, you are no longer a mere traveler. You are a harbinger of 
the Veil, a master of rebirth and ruin.'

The ground beneath your feet cracks open, and the battlefield vision begins to fold into itself, the warriors rising 
from their graves, now seeming to await your command. The air is thick with anticipation."""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[COMMAND] the dead
Type '2' ......[EXPLORE] the veil
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            random_encounter()
            clear_screen()
            print("""████████████████████████████████""")
        #---GAME OVER--------------------------------------------------------------------------------------------------
            narration.text = """
Narrator: You focus your newfound power, commanding the dead to rise. The crimson energy in your veins pulses 
violently, the ground beneath you cracking open as skeletal hands and broken bodies claw their way to the surface. 
Their hollow eyes flicker to life, glowing with the same fierce red hue.

'Arise,' you command, your voice resounding with the authority of the Crimson Veil.

The fallen warriors, bound to your will, rise from their graves, their once lifeless forms now moving with unnatural 
speed. You direct them towards the horizon, leading the army into the chaos of battle. But as the dead march, something 
begins to feel... wrong.

The air grows heavier, the shadows deeper. The warriors’ movements slow, their red-glowing eyes flickering with 
confusion. A sudden, unnatural chill sweeps over the battlefield, and the ground trembles."""
            random_encounter()
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: From behind the rising army, a voice—deep, ancient, and filled with wrath—echoes through your mind.

'Foolish mortal. You have awakened more than the Veil. You have disturbed the balance.'

Before you can react, the battlefield warps. The dead, now more like hungry predators, begin to turn on each other. 
Their corrupted souls tear at their bones, fighting for control. You try to control them, but the crimson energy is 
slipping away from you, twisting into something far darker.

In that moment, the full extent of the Veil’s power becomes clear: it is not just a tool of control—it is a parasite, 
feeding on its own master. You feel your heart race, your strength falter, as the very blood within you rebels against 
your will.

You scream, but no sound escapes your lips. The last thing you see is the army of the dead, now fully turned against 
you, descending with horrific hunger.

The world fades into darkness."""
            print()
            print("""████████████████████████████████""")
            time.sleep(6)
            game_over()
        case '2':
            random_encounter()
            explore()
#---Explore------------------------------------------------------------------------------------------------------------
def explore():
    narration = Narrator("Explore")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You hesitate for a moment, the weight of your decision pressing on you. The power surging through your veins 
is intoxicating, but there’s a part of you that craves understanding before you fully succumb to it. With a deep 
breath, you turn away from the battlefield and focus on the figure before you.

'I need to understand,' you say, your voice steadier than you feel. 'What is this Veil? What am I truly wielding?'

The figure’s eyes glint in the shadow, and a deep chuckle echoes from beneath the hood.

'Ah, curious... very well. You seek knowledge, and knowledge you shall have.'"""
    random_encounter()
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: The world around you begins to shift once more. The battlefield fades into darkness, replaced by a vast, 
swirling crimson void. In the center of this abyss, a massive, ancient tome appears before you, its pages flickering 
with symbols and blood-red writing. The tome opens on its own, its pages fluttering as if alive. The figure gestures toward it.

'The Crimson Veil is a force that exists beyond time and death. It binds the blood of mortals and immortals alike, 
drawing upon their essence, their memories, their very souls. To wield it is to control life itself, but also to be 
consumed by it. It is a gift, yes, but one that comes with a heavy price.'

As you gaze at the tome, the symbols on the pages begin to form images. You see glimpses of warriors, kings, and rulers 
who have come before you, all of them bound to the Veil in some form. Some use its power to conquer, others to 
resurrect loved ones. But there’s a dark pattern in the images. A cycle of destruction, rebirth, and loss. None who 
wield the Veil are ever free of its pull.

'But you, traveler,' the figure continues, 'you stand at a crossroads. You may choose to walk the path of knowledge, 
seeking to control the Veil for your own ends, or you may reject it altogether, finding another way to live. The 
choice, as always, is yours.'"""
    print()
    print("""████████████████████████████████""")
    narration.text = f"""Narrator: What will you do?"""
    selection = input("""Type '1' ......[EMBRACE] the knowledge
Type '2' ......[REJECT] the veil
Make your Selection: """)
    if selection != '1' and selection != '2':
        random_selection = random.randint(1, 2)
        selection = str(random_selection)
    match selection:
        case '1':
            embrace()
        case '2':
        #---Game Over--------------------------------------------------------------------------------------------------
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: You step back from the tome, feeling the weight of the decision settle in your chest. The truth, harsh and 
unrelenting, is clear now. The Crimson Veil is too dangerous, its power too corrupting. You cannot let yourself fall 
prey to it.

With a deep breath, you make your choice.

'I reject the Veil,' you say firmly, feeling the pull of the crimson energy begin to weaken as you turn away from the 
abyss.

The figure watches silently, its expression unreadable. As you sever your connection with the orb, the world around 
you begins to distort. The crimson void pulses and trembles, as though rejecting your decision. You feel the power in 
your veins begin to writhe, a tightening, a burning sensation spreading through your entire body. The orb in your hand 
flickers, its once soothing glow now sharp and painful.

'Foolish mortal,' the figure’s voice echoes, distorted by the growing tension. 'You cannot simply walk away from what 
you have bound yourself to. The Veil does not release its hold.'"""
            random_encounter()
            clear_screen()
            print("""████████████████████████████████""")
            narration.text = """
Narrator: Panic rises in your chest as the ground beneath you begins to crack. The very air seems to shift, turning 
heavy, suffocating. The blood in your veins burns like fire, as if it’s trying to tear you apart from the inside out. 
You stagger, your vision blurring as the power of the Veil violently rebels against you. Your limbs shake, your breath 
shallow and ragged, but it’s too late.

The crimson energy pulses one last time, and you feel your life force draining away. Your heart begins to slow, the 
pressure building in your chest until, with one final, agonizing breath, your body collapses. The last thing you see is 
the shadowy figure, its hood now fully raised, watching with an unreadable gaze."""
            print()
            print("""████████████████████████████████""")
            time.sleep(6)
            game_over()
#---Embrace------------------------------------------------------------------------------------------------------------
def embrace():
    narration = Narrator("Embrace")
    clear_screen()
    print("""████████████████████████████████""")
    narration.text = """
Narrator: You feel the weight of the knowledge settle within you as you make your choice. The crimson energy surges 
through your body with newfound clarity. This time, it doesn't consume you. Instead, you focus, controlling it, 
channeling it like a current flowing through your veins. The power of the Veil is yours to wield, but you will not be 
its slave.

The figure before you nods approvingly, and for the first time, a sense of peace emanates from the shadowy form.

'Well done,' it murmurs. 'The Veil is no longer a burden. You are its master, not the other way around.'

You feel the battlefield flicker before you once more, but this time it is different. The risen dead stand at 
attention, their glowing eyes waiting for your command, but you now know how to direct them with precision. The Veil 
hums with the energy of possibility, a conduit through which you can control life, death, and rebirth.

As the dead begin to move in response to your will, you see the true scope of what you can do. The power to heal, to 
protect, to destroy, and to reshape the world as you see fit. You understand now that the Veil is not just a tool of 
destruction—it is a tool of transformation. But the true challenge is not in wielding its power, but in mastering it 
without falling into madness.

The figure bows slightly, as if acknowledging your decision.

'Your journey has just begun, traveler. What will you do with the power of the Crimson Veil?'

The world around you shifts once more, and the vision begins to fade. You stand at the edge of a new chapter in your 
story, where the Veil is no longer a threat, but a tool in your hands."""
    print()
    print("""████████████████████████████████""")
    time.sleep(10)
    end_chapter()
    loading_bar()
    #---Chapter 3 - Embrace--------------------------------------------------------------------------------------------