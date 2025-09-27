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
    show a874f happy

    # These display lines of dialogue.
    "The door creaks shut behind you as you step into your dimly lit office."
    "The scent of metal and ozone lingers in the air, remnants of the storm that passed through earlier."
    "You flick the light switch. A soft hum echoes as the fluorescents buzz to life, casting harsh shadows across the cluttered desk."
    "Dropping into your chair, you let out a tired sigh and power on your console. "
    a874 "You've created a new Ren'Py game."

    a874 "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
