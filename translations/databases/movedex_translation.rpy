init python:
    for i in range(len(movedex)):
        move_name = movedex[i][1]
        move_names = {
            LANG_ENG: move_name,
        }
        move_type = {
            LANG_ENG: movedex[i][2],
        }
        move_category = {
            LANG_ENG: movedex[i][3],
        }
        move_descriptions = {
            LANG_ENG: movedex[i][9],
        }
        for language in languages:
            if language == LANG_ENG:
                continue
            else:
                if move_name in move_translations[language]:
                    info = move_translations[language][move_name]
                    move_names[language] = info[0]
                    move_descriptions[language] = info[1]
                if move_type[LANG_ENG] in type_translation[language]:
                    move_type[language] = type_translation[language][move_type[LANG_ENG]]
                if move_category[LANG_ENG] in category_translation[language]:
                    move_category[language] = category_translation[language][move_category[LANG_ENG]]
        # Change names
        movedex[i][1] = EvolvedString(move_names)
        # Change type
        movedex[i][2] = EvolvedString(move_type)
        # Change category
        movedex[i][3] = EvolvedString(move_category)
        # Change descriptions
        movedex[i][9] = EvolvedString(move_descriptions)