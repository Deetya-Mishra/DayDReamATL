# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("Agent 874")
define c = Character("Computer", color="#bc13fe")
define f = Character("Field Coordinator")
define g = Character("Lilith")
define m = Character("Levi")
define t1 = Character("Agent 675", color="#000000")
define t2 = Character("Agent 986", color="#e93356")
define un = Character("???")
define mat = Character("Matt")
define dis = Dissolve(.5)
define weapons = []
define wepdescs = []
define weaponcounter = 0
transform genpos:
    xalign 0.5
    yalign 0.125
transform lefpos:
    xalign 0
    yalign 0.125
transform ripos:
    xalign 1.0
    yalign 0.125
default gender = "f"
default lil = "Lilith"
default ai = g
default abil = "cloaking"
default codnam = "Quinn"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office874

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    menu: 
        "Please select your character gender."
        "Female":
            jump room
        "Male":
            $ gender = "m"
            $ codnam = "Kai"
            jump room
label room:
    

    # These display lines of dialogue.
    "The door creaks shut behind you as you step into your dimly lit office."
    "The scent of metal and ozone lingers in the air, remnants of the storm that passed through earlier."
    "You flick the light switch. A soft hum echoes as the fluorescents buzz to life, casting harsh shadows across the cluttered desk."
    "Dropping into your chair, you let out a tired sigh and power on your console. The screen glows to life with a flicker, a black background illuminated by sharp, violet text that pulses with urgency."
    c "Welcome, Special Agent 874"
    c "Codename: [codnam]"
    c "{b}Mission #436: Project Starlight{/b}"
    c "Objective: Infiltrate Lighter's Headquarters and retrieve the encrypted flash drive."
    c "Instructions: Contact your field manager for briefing."
    c "Team assignments incoming, please stand by."
    "You lean back, letting the wheels of your chair squeak beneath you, and run a hand down your face."
    show expression "a874[gender] standby" at genpos
        
    u "Seriously? Today was supposed to be quiet."
    "The words hang in the air as the screen's glow reflects off your tired eyes. You sit there for a moment — five minutes, maybe more — the calm before the storm. But in this business, calm never lasts."
    "Suddenly, your wristwatch buzzes sharply, snapping you to attention. A message blinks on its display:"
    menu: 
        c "Are you ready to deploy?"
        "Yes":
            jump briefing
label briefing:
    scene bg hq
    with dis
    show expression "a874[gender] standby" at genpos

    # These display lines of dialogue.
    "You step into the elevator, still adjusting your tie with one hand. The knot’s crooked, but it’ll have to do. Around here, one thread out of place gets you a week of mind-numbing overtime, and the field coordinators have eyes sharper than the most advanced lie detectors."
    "The elevator hums softly as it descends. The transparent glass walls reveal the city’s heartbeat inside HQ: a sprawling, high-tech lobby bursting with controlled chaos."
    scene bg hq 
    with vpunch
    hide expression "a874[gender] standby" at genpos
    with moveoutbottom
    pause .5
    show expression "a874[gender] standby"
    with moveintop
    pause .5
    scene bg hq
    with vpunch
    "With a hiss, the elevator doors part. You step out onto the upper level of the lobby and scan the scene:"
    show expression "a874[gender] standby" as a874 at genpos
    "On the lower level, food courts buzz with chatter and sizzling grills. Agents on break rush to grab a quick bite before their next shift. Others drag themselves toward the exits, exhausted from the one they just finished."
    "The mid-level is alive with motion, labs open to the air like vendor stalls, where agents queue up for any last-minute tech for their mission: neural headsets, cloaking pins, EMP gloves. A few younger agents zip by on hoverboards, clearly showing off."
    "Up here on the upper level, where you're standing, twenty agents gather in a tight formation. You recognize the unmistakable posture of professionals—alert, quiet, sharp. You blend into the group just as your field coordinator steps forward. "
    hide a874
    show expression "a874[gender] standby" as a874 at lefpos
    with move
    show fieldcoord standby at genpos
    "They’re sharp-dressed, with a silver streak in their hair, and glued to an oversized iPad. They scan the group, give a single nod, and adjust their tie with military precision."
    f "Welcome, everyone. Today, you have been selected for a special operation."
    "They tap the iPad. A sleek hologram shimmers to life above it—a glowing interface pulsing softly with light. An artificial voice hums to readiness."
    show fieldcoord standby at genpos
    with move
    hide a874
    show lilith standby at lefpos
    show levi standby at ripos
    f "These are the two AI assistants. They’ll be your mission assistant. You can activate them by saying, ‘Hey Lilith or Levi,’ into your watch. They’ll provide intel, navigation, and emergency support."
    f "Now you may be wondering what the difference between the two is. Lilith is a cloaking machine that can create disguises and turn you invisible for a short period of time. However, every time you use this power, the line between your own identity and that of the disguise will blur further."
    f "Levi can help you phase through walls and teleportation. However, each time you use this power, it will leave a scar on your body. The distance teleported and/or the thickness of the wall phased through will determine the severity of your injury."
    f "Now, agents, please note that sacrifices must be made for this mission and choose wisely. A prompt to choose your assistant will appear on your watch."
    menu:
        c "Now you shall choose your auxiliary."
        "Lilith": 
            jump assistant
        "Levi": 
            $ lil = "Levi"
            $ abil = "phasing"
            jump assistant

label assistant:
    #hide expression "a874[gender] standby"
    hide lilith standby
    with zoomout
    hide levi standby
    with zoomout
    show fieldcoord standby at lefpos
    with move
    if lil.lower() == "levi":
        $ ai = m
    show expression "[lil.lower()] standby" as aias at ripos
    with moveinbottom
    ai "Hello! I’m [lil], a [abil] AI assistant! I'd tell you about what I do, but you already heard all that."
    f "You’ve all been handpicked for this assignment, meaning that you are here because you’re capable."
    "The coordinator swipes the hologram again. The screen shifts to an image: a luxury tower glowing gold against the city night. The words “Project Starlight” hover above it in crimson font."
    scene bg tower
    with dis
    show expression "[lil.lower()] standby" as aias at ripos
    with moveinbottom
    show fieldcoord standby at lefpos
    with move
    f "Mission #436: Project Starlight. As some of you know, Alexander Lighter, known to most as Bruce, is hosting an extravagant gala tonight, unveiling a so-called ‘life-changing’ technology."
    f "Don’t be fooled. Our intel says this device is some sort of trojan horse designed to steal user data on a massive scale."
    f "We suspect that’s only the beginning of his treacherous plots. However, we do not know the full extent of said plots yet, as the device is too well-protected."
    f "That’s where you come in. Your task is to infiltrate the event, locate the flash drive tied to this new app, and extract any files you can. If you succeed, we might finally learn what’s really going on and be able to stop it before it launches."
    "They pause to let that sink in. Then, with a swipe of their hand, the display fragments and re-forms into a list of names and assignments."
    show bg hq with pixellate
    f "Now, for team assignments. You’ll be working in trios. You’ll have thirty minutes to debrief and get to know each other before deployment. This is a high-stakes mission, so teamwork is key to your success."
    "One by one, they call out teams, sending agents off to form clusters. After several minutes, they get to you."
    f "Agent 874... You’ll be working with Agent 675 and Agent 986."
    "You glance over as the two other agents nod at you, one tall and unreadable behind tinted lenses, the other scanning a sleek datapad already. You smile back at your field coordinator."
    f "All teams are now assigned. Final briefings are being uploaded to your watches. Mission clocks start in thirty minutes. You are dismissed — and good luck out there."
    # Part 3 begins here
    hide aias
    with moveoutbottom
    hide fieldcoord standby
    "Agents quickly file out of the area, leaving you and your teammates standing in awkward silence. Agent 986 steps forward with a friendly smile and extends their hand."
    show a986 hi at lefpos
    with moveinbottom
    t2 "Hi! My name is Agent 986. I’m looking forward to working with you. What’s your name?"
    show expression "a874[gender] standby" at ripos
    u "I’m Agent 874. Nice to meet you."
    "You turn to Agent 675, who hasn't spoken yet."
    hide a986 hi 
    with moveoutbottom
    pause .5
    show a675 standby at lefpos
    u "What’s your name?"
    t1 "Agent 675"
    "They glance down at the floor and shuffle their feet. {i}Are they shy?{/i} you wonder."
    u "Well, we should probably start planning."
    u "Let’s sit over there and talk about what we’ll do next."
    scene bg bench
    with dis
    show a986 standby at lefpos
    with moveinbottom
    show expression "a874[gender] standby" as a874 at ripos
    "You and your teammates take a seat."
    t2 "Okay, so... Groups 1 through 3 will stay at the party and mingle to keep everyone distracted. Groups 6 and 7 will search the building for intel, and Group 5—along with us—will split up to look for the flash drive. Sounds easy enough."
    hide a874
    show a675 standby at ripos
    t1 "We should probably grab some gear from the science lab."
    hide a986 standby
    show expression "a874[gender] standby" as a874 at lefpos
    u "Good call. Let’s hurry before all the good stuff is gone."
    hide a675 standby
    show a986 standby at ripos
    t2 "Ooo, I heard they have flying motorcycles. Can we get one?"
    hide a874
    show a675 standby at lefpos
    t1 "Pretty sure hoverboards will do just fine. But hey, go for it if you want."
    t2 "Yessss"
    "They spring up from the bench, practically buzzing with excitement."
    hide a986 standby
    show a986 hi at ripos
    with moveinbottom
    t2 "Come on, let’s go!"
    # Part 4 begins
    scene bg sciwing
    with dis
    show a986 standby at ripos
    with moveinleft
    show expression "a874[gender] standby" as a874 at genpos
    with moveinleft
    show a675 standby at lefpos
    with moveinleft
    "The double doors to the science wing slide open with a quiet hiss. Bright white lights flood your vision as you and your teammates step into the lab. The room is alive with energy—agents and engineers are scattered around, examining prototypes, testing gear, and trying not to blow anything up."
    "One agent zooms by on a hoverboard, barely dodging a stack of crates. In the far corner, someone fiddles with a grappling hook, sending the claw whizzing up to the ceiling. Sparks fly from a test bench where a pair of goggles is being calibrated, and several screens display wireframe blueprints of weapons and tools."
    "You all pause, taking it in."
    hide a874
    with dis
    t2 "This place is awesome"
    t1 "I know, right? I used to work here when I first joined."
    t2 "You’re so cool!"
    t1 "{i}Chuckles awkwardly and rubs the back of their head.{/i}"
    "A young intern with a white lab coat and glasses approaches. He has tied back ginger hair that goes up to his shoulders. He pushes his glasses up his nose and smiles warmly."
    show matt standby at genpos
    with moveintop
    un "Ah, you must be in Group 4. Right on time. I'm Matt Gunderson, an intern here at Department Four."
    mat "Your field coordinator said that you guys would be stopping by. I'll walk you through what we've got ready."
    "He leads you down an aisle lined with display tables. Each one holds a gleaming piece of tech, neatly labeled and ready for field use."
    mat "Everything you see here is fully functional. Choose wisely — each of you can carry up to five items."
    jump wepselect
label wepselect:
    if weaponcounter <=5:
        $ weaponcounter += 1
        # Updating weaponcounter allows the game to know when the user has acquired five weapons and stop them from collecting more.
        "You move to grab your next item."
        menu:
            mat "Here's what's available:"
            "Hoverboard — Fast personal transport with silent operation":
                if "hoverboard" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("hoverboard")
                    $ wepdescs.append("Hoverboard — Fast personal transport with silent operation")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Grappling Hook — For scaling buildings or escaping quickly":
                if "grapple" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("grapple")
                    $ wepdescs.append("Grappling Hook — For scaling buildings or escaping quickly")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "GPS — Maps the layout of your environment in real time":
                if "gps" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("gps")
                    $ wepdescs.append("GPS — Maps the layout of your environment in real time")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "X-ray Vision goggles — See through walls and containers":
                if "xray" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("xray")
                    $ wepdescs.append("X-ray Vision goggles — See through walls and containers")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Night Vision Goggles — Great for dark, unlit areas":
                if "night" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("night")
                    $ wepdescs.append("Night Vision Goggles — Great for dark, unlit areas")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Heat Vision Goggles — Detect body heat and temperature changes":
                if "heat" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("heat")
                    $ wepdescs.append("Heat Vision Goggles — Detect body heat and temperature changes")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "EMP Grenade — Temporarily disables electronic devices":
                if "emp" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("emp")
                    $ wepdescs.append("EMP Grenade — Temporarily disables electronic devices")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Voice Changer — Mimic another person's voice for disguise":
                if "voichan" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("voichan")
                    $ wepdescs.append("Voice Changer — Mimic another person's voice for disguise")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Hologram Projector — Create a decoy image of yourself":
                if "holo" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("holo")
                    $ wepdescs.append("Hologram Projector — Create a decoy image of yourself")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Mini Drone — Remote surveillance with a live camera feed":
                if "mini" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("mini")
                    $ wepdescs.append("Mini Drone — Remote surveillance with a live camera feed")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            "Call Button — will bring extra units if help is needed":
                if "call" in weapons:
                    mat "Sorry, you already have that one!"
                    $ weaponcounter -= 1
                else:
                    $ weapons.append("call")
                    $ wepdescs.append("Call Button — will bring extra units if help is needed")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
    else: 
        "You move to grab an item, but your pockets are already stuffed full of gear."
        t1 "Wait. {i}glances at your gear{/i} Are you sure you want to go with those? Once we leave the lab, there's no swapping."
        mat "In case you need a review, this is the gear that you have currently chosen."
        mat "[wepdescs[0]]"
        mat "[wepdescs[1]]"
        mat "[wepdescs[2]]"
        mat "[wepdescs[3]]"
        mat "[wepdescs[4]]"
        menu:
            "Would you like to continue with these weapons?"
            "Yes":
                jump chosen
            "No":
                $ weapons.clear()
                $ wepdescs.clear()
                $ weaponcounter = 0
                "You empty your pockets."
                jump wepselect
label chosen:
    u "I'm done."
# Known issue: Not all of the buttons are visible on the screen. May need to remove some options.