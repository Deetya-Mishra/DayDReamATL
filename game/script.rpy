# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a874 = Character("Agent 874")
define c = Character("Computer", color="#bc13fe")


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
    show a874f standby
    a874 "Seriously? Today was supposed to be quiet."
    "The words hang in the air as the screen's glow reflects off your tired eyes. You sit there for a moment — five minutes, maybe more — the calm before the storm. But in this business, calm never lasts."
    "Suddenly, your wristwatch buzzes sharply, snapping you to attention. A message blinks on its display:"
    menu: 
        c "Are you ready to deploy?"
        "Yes":
            jump briefingf
label briefingf:

    # This ends the game.

    return
