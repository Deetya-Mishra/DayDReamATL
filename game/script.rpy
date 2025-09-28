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
define sec1 = Character("Security 1")
define sec2 = Character("Security 2")
define sec3 = Character("Security 3")
define g1 = Character("Group 1 Leader")
define g2 = Character("Group 2 Leader")
define ceo = Character("Alexander 'Bruce' Lighter")
define deathphrase = "a"
define weapons = []
define wepdescs = []
define weaponcounter = 0
define abilityusecounter = 0
define dead = 0
define alive = 0
define t = t1
define nt = t2
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
    play music "elevator.mp3"
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
    stop music
    "On the lower level, food courts buzz with chatter and sizzling grills. Agents on break rush to grab a quick bite before their next shift. Others drag themselves toward the exits, exhausted from the one they just finished."
    play music "lobby.mp3"
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
    jump weapontime
    # Part 4 begins
label weapontime:
    stop music
    play music "lab.mp3"
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
    "You study the gear in front of you. 986 is already strapping on a grappling hook like it's a fashion accessory. 675 is more focused, methodically examining each item."
    $ weapons.clear()
    $ wepdescs.clear()
    jump wepselect
label wepselect:
    if weaponcounter <=5:
        $ weaponcounter += 1
        # Updating weaponcounter allows the game to know when the user has acquired five weapons and stop them from collecting more.
        "You move to grab your next item."
        menu:
            mat "Here's what's available:"
            "":
                pass
            "":
                pass
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
            # "X-ray Vision goggles — See through walls and containers":
                # if "xray" in weapons:
                    # mat "Sorry, you already have that one!"
                    # $ weaponcounter -= 1
                # else:
                    # $ weapons.append("xray")
                    # $ wepdescs.append("X-ray Vision goggles — See through walls and containers")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                # jump wepselect
                # Jumping to wepselect allows for the user to continue their selection after selecting their nth weapon.
            #"Night Vision Goggles — Great for dark, unlit areas":
            #     if "night" in weapons:
            #       mat "Sorry, you already have that one!"
            #       $ weaponcounter -= 1
                # else:
                #  $ weapons.append("night")
                #  $ wepdescs.append("Night Vision Goggles — Great for dark, unlit areas")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                # jump wepselect
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
            #"Voice Changer — Mimic another person's voice for disguise":
            #     if "voichan" in weapons:
            #       mat "Sorry, you already have that one!"
            #       $ weaponcounter -= 1
                # else:
                #   $ weapons.append("voichan")
                #   $ wepdescs.append("Voice Changer — Mimic another person's voice for disguise")
                    # This adds the weapon into the list of weapons, which will be used later to add in options for the crises.
                # jump wepselect
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
    "You turn to your teammates. 986 has picked up a motorcycle, grappling hook, and iPad. 675 has picked up a hoverboard, grappling hook, and night vision goggles."
    hide a675 standby
    show matt standby at lefpos
    with move
    mat "Ah, I almost forgot."
    "Matt hands each of you a case."
    mat "You'll need these weapons for your mission. Good luck, you guys."
    hide a986 standby
    show expression "a874[gender] standby" as a874 at ripos
    with moveinbottom
    u "Thanks. I greatly appreciate it."
    hide matt standby
    show a986 standby at lefpos with moveinleft
    t2 "All right, Team Hyperdrive for the win!"
    hide a874
    show a675 standby at ripos
    with moveinright
    t1 "Team Hyperdrive?"
    t2 "Yeah, you like it? I came up with it myself!"
    "You look at your watch and see a new message from your field coordinator:"
    c "Groups 4 and 5, please report to training center four tomorrow at 11 am to get ready for your mission. You deploy at 7 pm. Get good rest."
    show expression "a874[gender] standby" as a874 at genpos
    u "Hey team, sleepover at my place?"
    jump sleepover
    # Part 5 begins.
label sleepover:
    scene bg bed
    with dis
    show expression "a874[gender] standby" as a874 at genpos
    show a675 standby at lefpos
    show a986 standby at ripos
    "You sit in your room with the other team members. 675 is sitting in the corner looking at their screen. 986 is struggling with a large bag and drops it on the floor, causing a large assortment of snacks to fall out."
    hide a675 standby
    with dis
    show expression "a874[gender] standby" as a874 at lefpos
    with move
    t2 "Okay, I have popcorn, gummy bears, and soda. Oh, and apples, so we can tell the director we were being healthy."
    menu:
        t2 "Let's play a game."
        "Yes":
            u "Sure."
            "You grab a board game off the shelf and sit with your teammates. After a few rounds, you feel like you've gotten to know them a lot better. You look at the clock and notice that it's getting late."
            u "We should probably get some rest."
            hide a986 standby
            with dis
            show a675 standby at ripos
            with dis
            t1 "Yes. But before that, we need a plan."
            hide a874 
            with dis
            show a986 standby at lefpos 
            with moveinbottom
            t2 "I agree!"
            jump plan
        "No":
            u "We should probably come up with a plan for tomorrow."
            hide a986 standby
            with dis
            show a675 standby at ripos
            with dis
            t1 "I agree."
            jump plan
label plan:
    hide a874
    show a986 standby at lefpos
    t2 "Well, I'm good with tech. I can hack through the security and edit it to hide our tracks."
    t1 "I'm good with combat."
    hide a675 standby
    with dis
    show expression "a874[gender] standby" as a874 at ripos
    with dis
    u "Great. Then you can take care of any guards that come our way. I've already made a pathway for us to follow with the map of the building. I've also made multiple exit plans."
    t2 "You sound like a team leader already."
    u "Huh???"
    hide a986 standby
    with moveoutbottom
    show a675 standby at lefpos
    with dis
    t1 "She's right. You should lead our group through this mission, since you already came up with a plan."
    u "Are you sure?"
    hide a675 standby
    with dis
    show a986 standby at lefpos
    with moveinbottom
    t2 "I can't think of anyone more fit for the job."
    u "All right. Let's do this, team."
    jump locker
label locker:
    scene bg lockers
    with dis
    show expression "a874[gender] standby" as a874 at genpos
    with dis
    "You and the teams meet up in the locker room. Everyone has their game faces on."
    "This could be one of the most difficult missions in your entire career. Rumor has it that it will determine whether you get a promotion or be banished to the lower ranks."
    "{b}{u}Stakes are high...{/b}{/u}"
    show a675 standby at lefpos
    with dis
    show a986 standby at ripos
    with moveinbottom
    hide a874
    with dis
    "Aaaaaaaaand 986 is talking with 675 about what ice cream they should have."
    t2 "I am telling you, Cherry Blossom Blast is THE best ice cream flavor in existence."
    t1 "It's too sweet, though. Midnight Raspberry is better."
    t2 "Ugh, you're so emo. Is your middle name \"The Dark One\" or something?"
    t1 "No. It's Ronan."
    hide a986 standby
    show a986 hi at ripos
    "986 bursts out laughing."
    t2 "Oh my gosh, that's even worse!"
    "675 rolls his eyes."
    hide a986 hi with moveoutbottom
    show expression "a874[gender] standby" as a874 at ripos
    with dis
    t1 "Hey 874, you ready?"
    u "Yeah. Are we ready to go?"
    show expression "a874[gender] standby" as a874 at genpos
    with move
    show a986 standby at ripos
    with dis
    "They both nod."
    u "All right. Let's do this."
    jump mission
label mission:
    stop music
    play music "entry.mp3"
    scene bg rooftop with dis
    show expression "a874[gender] standby" as a874 at genpos
    with dis
    "You find your group on the roof of Lighter Industries."
    show a986 standby at lefpos
    with moveinbottom
    show a675 standby at ripos
    with dis
    "986 is checking their gear and 675 is sharpening their weapon. You review the plan again. Suddenly, you get a ping on your watch. A message from Group 2."
    c "We're inside and mingling with some guests. You can proceed with the mission."
    "You turn to your group members and give them the okay signal."
    u "Follow my lead."
    play sound "vent.mp3"
    scene bg galahallway
    with dis
    "You and your group members crawl through the vents trying to locate the flash drive. You took on the west side of the building, while Group 7 works on the east side."
    play sound "vent.mp3"
    "You eventually climb out of the vents and land in a dark hallway."
    show expression "a874[gender] standby" as a874 at genpos
    with dis
    show a675 standby at ripos
    with moveinbottom
    show a986 standby at lefpos
    with dis
    u "All right, team. Let's spread out between these two hallways. We have about an hour to find the flash drive."
    t2 "All right, time to destroy the industry!"
    hide a986 standby with moveoutright
    show expression "a874[gender] standby" as a874 at lefpos
    with move
    "986 runs off and 675 lets out a chuckle. He then turns to you."
    t1 "Are you sure you'll be okay by yourself?"
    u "I'll be fine."
    t1 "Okay. Call us if you need anything."
    stop music
    play music "split.mp3"
    hide a675 standby with moveoutleft
    show expression "a874[gender] standby" as a874 at genpos
    with move
    "He runs off in the other direction as you search the hallway. You eventually find a door at the end of the hallway and decide to open it. Inside you find a briefcase. You try to open it to see what's inside. Just then, you hear a noise outside the door."
    u "Shoot, security."
    play sound "footsteps.mp3"
    "You hear their steps getting closer. There's not much time left."
    u "[lil], I need to borrow your powers."
    show expression "[lil.lower()] standby" as aia at lefpos
    ai "Are you sure that you would like to use my abilities? Side effects may include: nausea, dizziness, headaches-"
    u "I don't care, just do it."
    show expression "a874[gender] standby" as a874 at ripos
    with move
    if lil == "Lilith":
        jump liluse1
    else:
        jump levuse1
label liluse1:
    ai "If you say so."
    "Your watch starts to glow and you feel a tingling sensation throughout your body. You notice that your hands start to take a different form. The doorknob clicks open as security enters."
    show expression "[lil.lower()] standby" as aia at lefpos
    hide aia
    sec1 "What are you doing here? Are you not supposed to be outside?"
    u "I was, sir. However, I heard crashing sounds coming from the room. I just wanted to make sure everything was all right here."
    sec1 "Yes, there were crashing sounds. However, that was in another room and we have security taking care of it right now. Be vigilant. This is one of the biggest events the boss has ever hosted and the threat of a break-in has been ever-growing."
    u "Yes, sir."
    sec1 "Good. I leave you to it."
    "The security guard closes the door and you let out a sigh of relief."
    jump closet
label levuse1:
    ai "As you wish."
    "Your watch starts to glow and you feel a tingling sensation throughout your body. You look at your hand and see that it is almost see through. The knob on the door handle clicks."
    "You grab hold of the briefcase and phase through the wall. You find yourself in an empty room with the lights off. The wall wasn’t thick, but you still received a scar on your right arm. A small price to pay for the success of the mission."
    jump closet
label closet:
    u "[lil], power off."
    scene bg closet
    hide aia with dis
    "You watch as your hand slowly turns back to its normal self. Overall, you seem fine, minus the slight headache, You send a message to your teammates and agree to meet in the storage closet. You open the door and run to the location."
    # Start of Part 8
    "You enter the storage closet where your two teammates are already sitting down."
    show expression "a874[gender] standby" as a874 at genpos
    with move
    show a675 standby at lefpos
    with dissolve
    show a986 standby at ripos
    with moveinbottom
    u "I have a briefcase. I think there might be some information inside and-"
    hide a986 standby with dissolve
    show expression "a874[gender] standby" as a874 at ripos
    with move
    t1 "That doesn't matter."
    u "What?"
    hide a675 standby with dissolve
    show a986 standby at lefpos
    with moveinbottom
    t1 "Yeah. Well, the mission does matter..."
    t1 "But you're ten times more important than that stupid briefcase. You could've been caught!"
    hide a986 standby with moveoutbottom
    show a675 standby at lefpos
    with dissolve
    t2 "You also used the AI to escape."
    with vpunch
    with hpunch
    t2 "DO YOU HAVE ANY IDEA HOW DANGEROUS THAT WAS?!?!"
    u "Look, I did what I had to. Sacrifices must be made for this mission. I'm fine. Let's just open the briefcase."
    "You open up the briefcase and find multiple CDs and hard drives, along with the flash drive."
    hide a675 standby with dissolve
    show a986 standby at lefpos
    t2 "You did it!"
    u "Great. Let's get this back to HQ and-"
    stop music
    play music "battle.mp3"
    sec2 "Over here! They're in the supply closet."
    hide a986 standby with moveoutbottom
    show a675 standby at lefpos
    with dis
    t1 "Shoot, they found us."
    hide a874
    with dis
    show expression "a874[gender] standby" as a874 at genpos
    with move
    show a986 standby at ripos
    with moveinbottom
    hide a874
    t2 "What do we do?!"
    menu:
        t1 "We can either fight or make a run for it. What do you think?"
        "Fight":
            
            jump fight
        "Run":
            
            jump run
label fight:
    u "We stand out ground. Ready your weapons. The mission depends on it."
    "The others nod and ready themselves for battle."
    show expression "a874[gender] standby" as a874 at genpos
    u "On my count, we attack. Three..."
    u "Two..."
    stop music
    play music "battle.mp3"
    u "One..."
    play sound "door.mp3"
    hide a874
    jump battle
label run:
    u "We make a run for it. There's no use in fighting unnecessary battles."
    "The others nod."
    show expression "a874[gender] standby" as a874 at genpos
    u "On my count, we run. Three..."
    u "Two..."
    stop music
    play music "battle.mp3"
    u "One..."
    play sound "door.mp3"
    hide a874
    jump flight
label battle:
    "The door swings open revealing three security guards. You and your team immediately attack them with full power." 
    "Your weapon meets the head of a security guard with a loud crack. They stumble back and groan in pain."
    show expression "a874[gender] standby" as a874 at genpos
    sec2 "Ack! My head."
    sec3 "We need backup over here! Keep fighting, we can't let them aahhh-"
    "Agent 986 raises their weapon to the back of the security guard's head, knocking them out. She then turns to the other guard."
    t2 "You wanna fight too?"
    sec1 "No, please spare me!!"
    t2 "Too late!"
    with hpunch
    "She and 675 knock him out."
    stop music
    play music "run.mp3"
    t1 "Come on, let's find an exit."
    "You run out the door with your teammates to find an exit."
    t2 "Over there! I see a door!"
    hide a874
    jump sacrifice
label flight:
    "The door swings open, revealing three security guards. You and your team immediately run out the door with full power."
    sec2 "They're getting away!"
    show expression "a874[gender] standby" as a874 at genpos
    sec1 "Well, don't just stand there!"
    with hpunch
    sec1 "AFTER THEM!!!"
    t2 "We are so dead."
    stop music
    play music "run.mp3"
    t1 "Only if you don't run faster. Come on!"
    u "Over there, I see an exit!"
    hide a874
    jump sacrifice
label sacrifice:
    show expression "a874[gender] standby" as a874 at genpos
    "You run over to the door and push it open."
    play sound "door.mp3"
    "Ten more security guards are waiting behind it."
    t1 "We're surrounded."
    u "Push through!"
    stop music
    play music "secentry.mp3"
    "You and your teammates attack the security guard with full power. Weapons clash. Fists collide with faces."
    t2 "We can't hold them off much longer!"

    hide a874 with dis
    hide a986 standby with dis
    pause 0.5
    show a675 standby at genpos
    with dis
    t1 "I can hold them off while you guys escape with the briefcase."
    hide a675 standby with dis
    pause 0.5
    show a986 standby at genpos
    with dis
    t2 "No, I'll do it. You shouldn't risk your life for this."
    hide a986 standby with dis
    pause 0.5
    show expression "a874[gender] standby" as a874 at genpos
    with dis
    u "Neither should you. All of you are too valuable to risk your lives."
    hide a874
    t1 "The same with you. You said sacrifices must be made. All for the greater good."
    t1 "You have to make a sacrifice."
    menu:
        t1 "So, who will stay behind?"
        "675":
            jump d675
        "986":
            jump d986
        "874(you)":
            jump d874
label d675:
    u "All right. 675, you will stay behind. 986 and I will return to HQ."
    show a675 standby at genpos
    with dis
    "675 nods."
    t1 "Affirmative."
    u "Will you be all right?"
    "675 smiles."
    t1 "Of course. Now, go!"
    "You and 986 run, leaving him behind."
    $ dead = 675
    $ alive = 986
    $ t = t2
    $ nt = t1
    jump conc
label d986: 
    u "All right. 986, you will stay behind. 675 and I will return to HQ."
    show a986 standby at genpos
    with dis
    "986 nods."
    t2 "You got it, boss!"
    u "Will you be all right?"
    "986 smiles."
    t2 "Of course! Now, scram, ya lazy bums!"
    "You and 675 run, leaving her behind."
    $ dead = 986
    $ alive = 675
    jump conc
label d874:
    u "I'll stay behind. You and 986 have a better chance of getting the briefcase back to HQ."
    show expression "a874[gender] standby" as a874 at genpos
    with dis
    t2 "Are you sure you can do it alone?"
    u "Of course. Besides, sacrifices must be made."
    "986 and 675 nod."
    u "Good. Now, go!"
    "They both leave with the briefcase, leaving you behind."
    $ dead = 874
    jump conc
label conc:
    stop music
    play music "end.mp3"
    if not dead == 874:
        scene bg gala
        show expression "a[alive] standby" as living at ripos
        with dis
        show expression "a874[gender] standby" as a874 at lefpos
        with dis
        "You run down the stircase with [alive] and the briefcase in hand."
        t "Let's take this door. It will lead out into the back of the building. That way, we can escape without being spotted."
        u "Okay."
        "You bring out your watch to notify the other teams."
        u "We have the flash drive and a bunch of other hard drives and information. We're exiting the building now."
        g1 "Affirmative! Groups 7 and 8 have been spotted, so be on the lookout for security."
        u "We've already run into them. Agent [dead] decided to stay behind and fight off the guards."
        if dead == 986:
            g2 "She did what?"
        else:
            g2 "He did what?"
        "Your watch buzzes: A call from [dead]"
        u "[dead], what's your status?"
        nt "Listen to me carefully. I'm going to use the AI to fight them off, but it'll use a lot of power."
        t "What are you saying? You can't just sacrifice yourself. If you use it too much, you'll die! You got upset at 874 for doing that!!"
        if dead == 986:
            $ deathphrase = "go to waste. That would be a major aura loss for me."
        else: 
            $ deathphrase = "be in vain."
        nt "I know what I said. Just please, finish the mission. Don't let my sacrifice [deathphrase]"
        u "For the greater good."
        "You and [alive] rush out of the building."
        return
    else:
        "675 and 986 run down the stairs with the briefcase, leaving you with the security guards."
        with hpunch
        pause 0.25
        "One by one, you take them out. However, as you defeat one, it seems as if two more come in their place."
        with hpunch
        pause 0.5
        with hpunch
        u "How many security guards does this guy have?"
        with hpunch
        pause 0.75
        with hpunch
        pause 1.0
        with hpunch
        "You swing your weapon, knocking out another guard as exhaustion creeps up on you."
        play sound "footsteps.mp3"
        "Suddenly, you hear footsteps coming from behind you." 
        pause 5
        stop sound
        play sound "clap.opus"
        "You turn around to see the CEO clapping."
        ceo "Well, well, well. you've done a lot better than I expected. It seems I've underestimated you."
        with hpunch
        with vpunch
        u "YOU WON'T GET AWAY WITH THIS."
        with hpunch 
        with vpunch
        ceo "Oh? But it seems I already have."
        "The situation is grave. There is only one choice left. You turn on your watch and call your teammates."
        t1 "874, what's your status?"
        u "Listen to me carefully."
        u "I'm going to use the AI to fight them off, but it will use a lot of power."
        t2 "What are you saying? You can't just sacrifice yourself. If you use it too much, you'll die! We just told you not to do that like ten minutes ago!"
        u "I know, I know. Just please, finish the mission. Don't let my sacrifice go to waste. We need this mission to be a success. Besides, it's for the greater good."
        t1 "For the greater good."
        t2 "For the greater good."
        "You turn to face the CEO."
        u "[lil], power on."
        scene bg dark with dis
        if lil == "Lilith":
            jump lily
        else:
            jump levis
label lily:
    "You use your AI's shapeshifting powers to change yourself and your weapons into various forms. You end up taking out all enemies until only the CEO is left. Your headache intensifies and you feel a growing despair at the disparities in your identity."
    jump grandfinale
label levis:
    "You use your AI's teleportation and phasing powers to change yourself and your weapons into various forms. You end up taking out all of the enemies until the CEO is left, your injuries growing more severe."
    jump grandfinale
label grandfinale:
    ceo "You've reached your limit. How could you possibly expect to beat me?"
    scene bg galahallway
    show expression "a874[gender] standby" as a874 at genpos
    u "Sacrifices must be made."
    "You use the last of your power to change your weapon's form one last time."
    u "For the greater good."
    scene bg dark with dis
    stop music
    pause 5.0
    if lil == "Lilith":
        "After you slew the CEO, your mental state collapsed, and the sense of despair grew all-encompassing. You ended yourself."
        return
    else: 
        "After you slew the CEO, your injuries became fatal, and you died from an internal hemorrhage."
        return