def draw_tilted_smiley():
    # Eyes stay as bold blocks
    # Mouth is now a horizontal curve like a real smile
    smiley = [
        "   XXXX      XXXX   ",
        "   XXXX      XXXX   ",
        "   XXXX      XXXX   ",
        "   XXXX      XXXX   ",
        "                    ",
        "                    ",
        "  XX            XX  ",
        "   XX          XX   ",
        "    XX        XX    ",
        "     XXXXXXXXXX     "
    ]

    for line in smiley:
        print(line)

draw_tilted_smiley()
