# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define tp = Character("Teepee")
define m = Character("Me", what_slow_cps=50)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "(After a long freshers week, I've finally finished my first lecture...)"
    m "(It was in a fairly modern building called the Bedford Labs.)"
    m "(As I approach the door to leave, I can't help but notice someone loitering in the corner of the lobby.)"

    return
