# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define U = Character("Agent 874")
define c = Character("Computer", color="#bc13fe")
define f = Character("Field Coordinator")
define g = character("Lilith")
define m = character("Levi")
define t2 = charcter("Agent 986")
define t1 = Character("Agent 675")


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
            jump female
        "Male":
            jump male
label female:
    

    # These display lines of dialogue.
    "The door creaks shut behind you as you step into your dimly lit office."
    "The scent of metal and ozone lingers in the air, remnants of the storm that passed through earlier."
    "You flick the light switch. A soft hum echoes as the fluorescents buzz to life, casting harsh shadows across the cluttered desk."
    "Dropping into your chair, you let out a tired sigh and power on your console. The screen glows to life with a flicker, a black background illuminated by sharp, violet text that pulses with urgency."
    c "Welcome, Special Agent 874"
    c "Codename: Quinn"
    c "{b}Mission #436: Project Starlight{/b}"
    c "Objective: Infiltrate Lighter's Headquarters and retrieve the encrypted flash drive."
    c "Instructions: Contact your field manager for briefing."
    c "Team assignments incoming, please stand by."
    "You lean back, letting the wheels of your chair squeak beneath you, and run a hand down your face."
    show U standby
    U "Seriously? Today was supposed to be quiet."
    "The words hang in the air as the screen's glow reflects off your tired eyes. You sit there for a moment — five minutes, maybe more — the calm before the storm. But in this business, calm never lasts."
    "Suddenly, your wristwatch buzzes sharply, snapping you to attention. A message blinks on its display:"
    menu: 
        c "Are you ready to deploy?"
        "Yes":
            jump briefingf
label briefingf:
   

    # These display lines of dialogue.
    "You step into the elevator, still adjusting your tie with one hand. The knot’s crooked, but it’ll have to do. Around here, one thread out of place gets you a week of mind-numbing overtime, and the field coordinators have eyes sharper than the most advanced lie detectors."
    "The elevator hums softly as it descends. The transparent glass walls reveal the city’s heartbeat inside HQ: a sprawling, high-tech lobby bursting with controlled chaos."
    "With a hiss, the elevator doors part. You step out onto the upper level of the lobby and scan the scene:"
    "On the lower level, food courts buzz with chatter and sizzling grills. Agents on break rush to grab a quick bite before their next shift. Others drag themselves toward the exits, exhausted from the one they just finished."
    "The mid-level is alive with motion, labs open to the air like vendor stalls, where agents queue up for any last-minute tech for their mission: neural headsets, cloaking pins, EMP gloves. A few younger agents zip by on hoverboards, clearly showing off."
    "Up here on the upper level, where you're standing, twenty agents gather in a tight formation. You recognize the unmistakable posture of professionals—alert, quiet, sharp. You blend into the group just as your field coordinator steps forward. They’re sharp-dressed, with a silver streak in their hair, and glued to an oversized iPad. They scan the group, give a single nod, and adjust their tie with military precision."
    f "Welcome, everyone. Today you’ve been selected for a special operation."
    "They tap the iPad. A sleek hologram shimmers to life above it—a glowing interface pulsing softly with light. An artificial voice hums to readiness."
    f "These are the two AI assistants. They’ll be your mission assistant. You can activate them by saying, ‘Hey Lilith or Levi,’ into your watch. They’ll provide intel, navigation, and emergency support."
    f "Now you may be wondering what the difference between the two is. Lilith is a cloaking machine that can create disguises and turn you invisible for a short period of time however it will impact your mental health and mess with your self identity."
    f " Levi can help you phase through walls and teleportation. However, each time you use it, it will leave a scar on your body. The farther you teleport or the thicker the wall you phase through will determine your injury. Sacrifices must be made for this mission so choose wisely."
    f"Now agents, please note that sacrifices must be made for this mission so choose wisely. A prompt will show up on your watch for you to choose your assistant."
    menu:
        f "Now you shall choose your auxillary"
        "Lilith": jump Lilith
        "Levi": jump Levi

Label Lilith:


    # These display lines of dialogue.
    g "Hello! I’m a cloaking machine that can create disguises and turn you invisible for a short period of time. However it will impact your mental health and mess with your self identity if used for a numerous amount of time."
    f "You’ve all been handpicked for this assignment. Meaning you are here because you’re capable."
    "They swipe the hologram again. The screen shifts to an image: a luxury tower glowing gold against the city night. The words “Project Starlight” hover above it in crimson font."
    f "Mission #436: Project Starlight. As some of you know, Alexander Lighter or as most people know, 'Bruce' is hosting an extravagant gala tonight, unveiling a so-called ‘life-changing’ technology."
    f "Don’t be fooled. Our intel says this device is some sort of trojan horse designed to steal user data on a massive scale. And we suspect that’s only the beginning. We don’t know the full extent yet as it’s too well-protected."
    f "That’s where you come in. Your task is to infiltrate the event, locate the flash drive tied to this new app, and extract any files you can. If you succeed, we might finally learn what’s really going on and stop it before it launches."
    "They pause to let that sink in. Then, with a swipe of their hand, the display fragments and re-forms into a list of names and assignments."
    f "Now for team assignments. You’ll be working in trios. You’ll have thirty minutes to debrief and get to know each other before deployment. This is a high-stakes mission so teamwork is key to your success."
    "One by one, they call out teams, sending agents off to form clusters. After several minutes, they get to you."
    f "Agent 874... You’ll be working with Agent 675 and Agent 986."
    "You glance over as the two other agents nod at you, one tall and unreadable behind tinted lenses, the other scanning a sleek datapad already. You smile back at your field coordinator"
    f "All teams are now assigned. Final briefings are being uploaded to your watches. Mission clocks start in thirty minutes. You are dismissed—and good luck out there."
    return
    "Agents quickly file out of the area, leaving you and your teammates standing in awkward silence. Agent 986 steps forward with a friendly smile and extends their hand."
    t2 "Hi! My name is Agent 986. I’m looking forward to working with you. What’s your name?"
    U "I’m Agent 874. Nice to meet you."
    "You turn to Agent 675, who hasn't spoken yet."
    U "What’s your name?"
    t1 "Agent 675"
    "They glance down at the floor and shuffle their feet.Are they shy? You wonder."
    U "Well, we should probably start planning."
    U "Let’s sit over there and talk about what we’ll do next."
    "You and your teammates take a seat."
    t2 "Okay, so... Groups 1 through 3 will stay at the party and mingle to keep everyone distracted. Groups 6 and 7 will search the building for intel, and Group 5—along with us—will split up to look for the flash drive. Sounds easy enough."
    t1 "We should probably grab some gear from the science lab."
    U "Good call. Let’s hurry before all the good stuff is gone."
    t2 "Okay, so... Groups 1 through 3 will stay at the party and mingle to keep everyone distracted. Groups 6 and 7 will search the building for intel, and Group 5—along with us—will split up to look for the flash drive. Sounds easy enough."
    t1 "We should probably grab some gear from the science lab."
    U "Good call. Let’s hurry before all the good stuff is gone."
    t2 "Ooo, I heard they have flying motorcycles. Can we get one?"
    t1 "Pretty sure hoverboards will do just fine. But hey, go for it if you want."
    t2 "Yessss"
    "They spring up from the bench, practically buzzing with excitement."
    t2 "Come on, let’s go!"
    "The double doors to the science wing slide open with a quiet hiss. Bright white lights flood your vision as you and your teammates step into the lab. The room is alive with energy—agents and engineers are scattered around, examining prototypes, testing gear, and trying not to blow anything up."
    "One agent zooms by on a hoverboard, barely dodging a stack of crates. In the far corner, someone fiddles with a grappling hook, sending the claw whizzing up to the ceiling. Sparks fly from a test bench where a pair of goggles is being calibrated, and several screens display wireframe blueprints of weapons and tools."
    "You all pause, taking it in."
    t2 "This place is awesome"
    t1 "I know right. I used to work here when I was first starting here."
    t2 "You’re so cool!"
    t1 "Chuckles awkwardly and rubs the back of their head."


Label Levi:


    # These display lines of dialogue.
     g "I’m Levi. I can help you phase through walls and teleportation. However, each time you use my powers, it will leave a scar on your body. The farther you teleport or the thicker the wall you phase through will determine your injury."
    f "You’ve all been handpicked for this assignment. Meaning you are here because you’re capable."
    "They swipe the hologram again. The screen shifts to an image: a luxury tower glowing gold against the city night. The words “Project Starlight” hover above it in crimson font."
    f "Mission #436: Project Starlight. As some of you know, Alexander Lighter or as most people know, 'Bruce' is hosting an extravagant gala tonight, unveiling a so-called ‘life-changing’ technology."
    f "Don’t be fooled. Our intel says this device is some sort of trojan horse designed to steal user data on a massive scale. And we suspect that’s only the beginning. We don’t know the full extent yet as it’s too well-protected."
    f "That’s where you come in. Your task is to infiltrate the event, locate the flash drive tied to this new app, and extract any files you can. If you succeed, we might finally learn what’s really going on and stop it before it launches."
    "They pause to let that sink in. Then, with a swipe of their hand, the display fragments and re-forms into a list of names and assignments."
    f "Now for team assignments. You’ll be working in trios. You’ll have thirty minutes to debrief and get to know each other before deployment. This is a high-stakes mission so teamwork is key to your success."
    "One by one, they call out teams, sending agents off to form clusters. After several minutes, they get to you."
    f "Agent 874... You’ll be working with Agent 675 and Agent 986."
    "You glance over as the two other agents nod at you, one tall and unreadable behind tinted lenses, the other scanning a sleek datapad already. You smile back at your field coordinator"
    f "All teams are now assigned. Final briefings are being uploaded to your watches. Mission clocks start in thirty minutes. You are dismissed—and good luck out there."
    return
    "Agents quickly file out of the area, leaving you and your teammates standing in awkward silence. Agent 986 steps forward with a friendly smile and extends their hand."
    t2 "Hi! My name is Agent 986. I’m looking forward to working with you. What’s your name?"
    U "I’m Agent 874. Nice to meet you."
    "You turn to Agent 675, who hasn't spoken yet."
    U "What’s your name?"
    t1 "Agent 675"
    "They glance down at the floor and shuffle their feet.Are they shy? You wonder."
    U "Well, we should probably start planning."
    U "Let’s sit over there and talk about what we’ll do next."
    "You and your teammates take a seat."
    t2 "Okay, so... Groups 1 through 3 will stay at the party and mingle to keep everyone distracted. Groups 6 and 7 will search the building for intel, and Group 5—along with us—will split up to look for the flash drive. Sounds easy enough."
    t1 "We should probably grab some gear from the science lab."
    U "Good call. Let’s hurry before all the good stuff is gone."
    t2 "Ooo, I heard they have flying motorcycles. Can we get one?"
    t1 "Pretty sure hoverboards will do just fine. But hey, go for it if you want."
    t2 "Yessss"
    "They spring up from the bench, practically buzzing with excitement."
    t2 "Come on, let’s go!"
    "The double doors to the science wing slide open with a quiet hiss. Bright white lights flood your vision as you and your teammates step into the lab. The room is alive with energy—agents and engineers are scattered around, examining prototypes, testing gear, and trying not to blow anything up."
    "One agent zooms by on a hoverboard, barely dodging a stack of crates. In the far corner, someone fiddles with a grappling hook, sending the claw whizzing up to the ceiling. Sparks fly from a test bench where a pair of goggles is being calibrated, and several screens display wireframe blueprints of weapons and tools."
    "You all pause, taking it in."
    t2 "This place is awesome"
    t1 "I know right. I used to work here when I was first starting here."
    t2 "You’re so cool!"
    t1 "Chuckles awkwardly and rubs the back of their head."
