# Script.rpy
# This is the main script that DDLC/Ren'Py calls upon to start
# your mod's story! 

label start:

    # Configures your mod to use a ID to prevent users from cheating.
    # Leave this as default and only change the value 'persistent.anticheat' has
    # in definitions.rpy if you want to change it
    $ anticheat = persistent.anticheat

    # Controls what chapter the game starts for the poem game.
    $ chapter = 0

    # Allows the player to dismiss or not based off config.developer 
    # (located in definitions.rpy)
    $ _dismiss_pause = config.developer

    # Names of the Characters
    # To add a character -> $ mi_name = "Mike". Don't forget to
    # add them also in definitions.rpy!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # Controls whether we have a menu in the textbox or not.
    $ quick_menu = True

    # Controls whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited' than 'style.normal'
    $ style.say_dialogue = style.normal

    # Controls whether Sayori is dead. Leave this alone unless needed.
    $ in_sayori_kill = None
    
    # Controls whether we allow skipping dialogue.
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Start of the script
    # 'persistent.playthrough' controls the playthrough number the player is on
    if persistent.playthrough == 0:
        # '$ chapter = 0' controls the chapter number the game is on for the poem game.
        # 'call tutorial_selection' controls what label to call from in your script files
        # Make sure to change this when coding your mod, else your player will face a script error

        scene bg club_day
        with wipeleft_scene
        call test_menu

# the end label of the game. Not the credits.    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

label test_menu:
    stop music fadeout 2.0

    menu:
        "Which feature do you want to test?"
        "Uncensored Mode":
            call uncensored
        "Let's Play Mode":
            call dokituber
        "Different Menu Colors.":
            call color_menu
        "Exit":
            pass
    return

label uncensored:
    if persistent.uncensored_mode:
        "Currently, Uncensored Mode is enabled."
    else:
        "Currently, Uncensored Mode is disabled."

    "..."
    mc "Hey Sayori. What happened this week?"
    if persistent.uncensored_mode:
        s "Nothing. My boobs got bigger again."
    else:
        s "Nothing. I... had some things going on."
    mc "Oh. I see."
    mc "What about you Monika?"
    if persistent.uncensored_mode:
        m "Huh? We literally went out on our 2nd honeymoon."
    else:
        m "Huh? We went out to the city."
    mc "Ah. Sorry. Have a dumb mind."
    "End of test."
    jump test_menu    

label dokituber:
    if persistent.lets_play:
        "Currently, Let's Play Mode is enabled."
    else:
        "Currently, Let's Play Mode is disabled."

    "..."
    mc "Hi everyone!"
    if persistent.lets_play:
        play music t3
        s "Hi redacted name I can't say else people will know your name!"
    else:
        play music t5
        s "Hi [currentuser]!"
    mc "Hey Sayori. Where's Monika?"
    if persistent.lets_play:
        m "I'm here redacted name mhm~"
    else:
        m "I'm here [currentuser] mhm~"
    mc "Ah. H-Hey..."
    "End of test."
    jump test_menu  

label color_menu:
    menu:
        "This is a preview of the buttons. No function is given to them except to return to the main screen."
        "Standard Menu Button":
            pass
        "Sayori-ish Color Menu Button (kwarg=#42b2f3, #72bce7)":
            pass
        "Monika-ish Color Menu Button (kwarg=#51f342, #80ee76)":
            pass
        "One Color  Menu Button (kwarg=#ce65e6)":
            pass
    jump test_menu