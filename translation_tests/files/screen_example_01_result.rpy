init python:
    config.character_id_prefixes.append('namebox')

    style window is default
    style say_label is default
    style say_dialogue is default
    style say_thought is say_dialogue

    style namebox is default
    style namebox_label is say_label


    style window:
        xalign 0.5
        xfill True
        yalign gui.textbox_yalign
        ysize gui.textbox_height

        background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ypos gui.name_ypos
        ysize gui.namebox_height

        background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        padding gui.namebox_borders.padding