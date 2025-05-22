elif (invoverwrite[:10] == "Which move"):
    vbox:
        xfill True
        spacing 30
        null
        text invoverwrite color "#000000" size 40 xalign 0.5
        null
        grid 2 2:
            spacing 20
            xalign 0.5
            for move in passedpokemon.Moves:
                if ValidateItemUsage(selecteditem, move):
                    textbutton move.Name action (Function(InvokeUseItem, selecteditem, move, passedpokemon)) xsize 200 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", move = move, vertoffset = .40) unhovered Hide("movedata")
                else:
                    null
            for x in range(4 - len(playerparty)):
                null
        textbutton "Nevermind." action [SetVariable("selecteditem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
