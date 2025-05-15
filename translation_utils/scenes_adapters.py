global global_path
global pos_var


# ---------- CONSTANT DEFINITION ----------
CHARACTER_NAMES = [
    # Special
    "narrator", "extend", "face", "mace", "security",
    # Red and Mom
    "red", "redmind", "mom",
    # Protagonists
    "blue", "leaf",
    # Professors
    "oak",
    # Last Year Students
    "roxanne", "brawly", "falkner",
    # Male roommates
    "ethan", "calem", "hilbert", "brendan",
    # Female roommates
    "may", "serena",
    # Future council
    "grusha", "cheren",
    # Other male students
    "silver", "wally",
    # Other female students
    "flannery", "whitney", "sabrina", "misty",
]
INMUTABLE_TEXTS = ["[ellipse]", "[ellipses]"]
SPECIAL_COMMAND_CHARACTER = "Character"

SPECIAL_CHARACTER = "\\\""
SPECIAL_CHARACTER_TO_REPLACE = "#!#"
DEFAULT_LANGUAGE = "LANG_ENG"

selected_language = DEFAULT_LANGUAGE


# ---------- Private methods ----------
def _get_path_rpy(scene_name, path_to_scene):
    return f".{global_path}{path_to_scene}/{scene_name}.rpy"


def _str_init_text_file(var_name):
    return f"init -1 python:\n    {var_name} = [\n        "


def _str_add_text_file(value):
    new_str = "EvolvedString({\n"
    new_str += f'            {selected_language}: "{value}",\n'
    new_str += "        }), "
    return new_str


def _str_end_text_file():
    return "\n    ]"


def process_single_text(line_to_process, var_name):
    global pos_var
    processed_line = ""
    if "[" in line_to_process:
        spl = line_to_process.split("[")
        processed_line = f'"[{var_name}[{pos_var}]]'
        pos_var += 1
        for i in range(1, len(spl)):
            spl_element = spl[i].split("]")
            processed_line = f'{processed_line}[{spl_element[0]}]'
            if len(spl_element) == 2:
                processed_line = f'{processed_line}[{var_name}[{pos_var}]]'
                pos_var += 1
        processed_line += '"'
    else:
        processed_line = f'"[{var_name}[{pos_var}]]"'
        pos_var += 1
    return processed_line


def _replace_line_and_write_output(line, var_name):
    global pos_var
    split_line_comma = line.split('"')
    new_text = line + "\n"
    if split_line_comma[1] not in INMUTABLE_TEXTS:
        new_text = split_line_comma[0] + process_single_text(split_line_comma[1], var_name) + split_line_comma[2]
        for i in range(3, len(split_line_comma)):
            new_text += '"' + split_line_comma[i]
    return new_text + '\n'


# ---------- Public methods ----------
def set_global_path(path):
    global global_path
    global_path = path


def convert_scene(scene_name, path_to_scene):
    global pos_var
    pos_var = 0
    scene_path = _get_path_rpy(scene_name, path_to_scene)
    var_name = f"day_{scene_name}_scene_text"
    with open(scene_path) as file:
        all_scene_info = file.read().split("\n")
    new_scene_text = ""
    for line in all_scene_info:
        split_line_space = line.split(" ")
        pos_first_word = 0
        while pos_first_word < len(split_line_space) and split_line_space[pos_first_word] == '':
            pos_first_word += 1
        if pos_first_word >= len(split_line_space):
            # It is a blank line
            new_scene_text += line + "\n"
        else:
            line = line.replace(SPECIAL_CHARACTER, SPECIAL_CHARACTER_TO_REPLACE)
            is_in_characters = False
            for character in CHARACTER_NAMES:
                is_in_characters = is_in_characters or character in split_line_space[pos_first_word]
            if 'TempCharacter' in line or SPECIAL_COMMAND_CHARACTER in line:
                split_line_comma = line.split('"')
                new_text = line + "\n"
                if split_line_comma[0] not in INMUTABLE_TEXTS:
                    new_text = (split_line_comma[0] + f'"[{var_name}[{pos_var}]]"' +
                                split_line_comma[2] + f'"[{var_name}[{pos_var+1}]]"' + split_line_comma[4])
                new_scene_text += new_text + '\n'
                pos_var += 2
            elif is_in_characters:
                # It is a character line
                new_scene_text += _replace_line_and_write_output(line, var_name)
            elif '"' in split_line_space[pos_first_word]:
                # Command start with string, so probably are menu options
                new_scene_text += _replace_line_and_write_output(line, var_name)
            elif 'renpy.input(' in line:
                new_scene_text += _replace_line_and_write_output(line, var_name)
            else:
                new_scene_text += line + "\n"

    with open(scene_path, 'w') as f:
        f.write(new_scene_text)
