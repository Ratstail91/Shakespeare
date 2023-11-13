define r = Character(_("Romeo"), color="#e07746")
define j = Character(_("Juliet"), color="#73ffc2")

label start:
    #setup
    scene bg city morning with fade

    show romeo normal at Position(xpos=0.25) with dissolve

    show juliet frown at Position(xpos=0.75) with dissolve

    #go

    show romeo surprised

    r "But soft, what light through yonder window breaks?"

    show romeo smile

    r "It is the East, and Juliet is the sun."

    show juliet frown blush

    j "Uhh... are you talking to me?"

    show juliet frown

    r "Arise, fair sun, and kill the envious moon,"
    r "Who is already sick and pale with grief"
    r "That thou, her maid, art far more fair than she."

    j "Yeah, no. I'm not doing this."

    show romeo smile2

    r "Be not her maid since she is envious."
    r "Her vestal livery is but sick and green,"
    r "And none but fools do wear it. Cast it off."

    menu:
        "Be More Forceful":
            show juliet open

            show romeo oops

            j "I SAID I'M NOT DOING THIS."

            "..."

            jump failed
        
        "Leave":
            hide juliet frown with moveoutright

            jump failed
    
    return

label failed:
    show romeo oops

    r "...I blew it."

    return
