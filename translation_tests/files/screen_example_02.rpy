if not hasfvl:
    $ canteditreason = "You do not have this foreveral."
elif inbattle:
    $ canteditreason = "Can't edit Pokémon moves or foreveral during combat."
elif foreveral in WhoHasFVLs(True) and not WhoHasFVLs(True)[foreveral][1]:
    $ canteditreason = "This foreveral is held by {} in the PC.".format(WhoHasFVLs(True)[foreveral][0].GetNickname())

$ LLmsg = ""

if liberationlimit:
    $ LLmsg = "Liberation Limit breakdown:\n"
    for category, specific, increase in liberationlimit[1]:
        if (not isinstance(specific, str)):
            $ specific = pokedexlookup(specific, DexMacros.Name)
        $ LLmsg += specific + ": " + str(math.floor(increase)) + "\n"
    $ LLmsg += "Total: " + str(liberationlimit[0]) + "/" + str(maxliberationlimit)
elif not loadoutdic["moves"]: # No moves
    $ LLmsg = "Please choose at least one move."

$ whoholdsfvlinparty = None
if foreveral in WhoHasFVLs(True) and WhoHasFVLs(True)[foreveral][1]:
    $ whoholdsfvlinparty = WhoHasFVLs(True)[foreveral][0]