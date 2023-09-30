# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define tp = Character("Teepee")
define m = Character("[name]", what_slow_cps=50)


# The game starts here.

label start:

    $ name = renpy.input("What is your name?")

    $ name = name.strip()

    if name == "":
        $ name = "Leon"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "(After a long freshers week, I've finally finished my first lecture...)"
    m "(It was in a fairly modern building called the Bedford Labs.)"
    m "(As I approach the door to leave, I can't help but notice someone loitering in the corner of the lobby.)"

    with fade
    scene bg lobby

    m "(Who is that?)"

    with fade
    show teepee disgusted

    tp "Who the fuck are you?"


    return
