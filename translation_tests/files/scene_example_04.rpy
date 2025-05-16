    hbox:
        xalign .5
        ypos .15
        if (showll):
            vbox:
                $ ll = GetLiberationLimit()
                text "{b}Liberation Limit" xminimum 300 xalign .5 size 40
                for category, specific, increase in ll[1]:
                    if (not isinstance(specific, str)):
                        $ specific = pokedexlookup(specific, DexMacros.Name)
                    if (specific not in category):
                        text category + " (" + specific +"): " + str(math.floor(increase)) xminimum 300 size 40
                    else:
                        text category + ": " +  str(math.floor(increase)) xminimum 300 size 40
                text "{b}Total:{/b} " + str(math.floor(ll[0])) + "/" + str(math.floor(maxliberationlimit))
            null width 50