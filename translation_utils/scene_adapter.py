global_path = ""
pos_var = 0


# ---------- CONSTANT DEFINITION ----------
IGNORE_SYMBOLS = ["$", "queue"]

SPECIAL_CHARACTER = "\\\""
SPECIAL_CHARACTER_TO_REPLACE = "#!#"
DEFAULT_LANGUAGE = "LANG_ENG"

selected_language = DEFAULT_LANGUAGE


# ---------- Private methods ----------
def _get_path_rpy(scene_name, path_to_scene):
    path_to_scene = path_to_scene[1:] if path_to_scene[0] == '/' and global_path[-1] == '/' else path_to_scene
    path_to_scene = path_to_scene[:-1] if path_to_scene[-1] == '/' and scene_name[0] == '/' else path_to_scene
    init_slice = '/' if global_path[0] != '/' else ''
    first_slice = '/' if global_path[-1] != '/' and path_to_scene[0] != '/' else ''
    second_slice = '/' if path_to_scene[-1] != '/' and scene_name[0] != '/' else ''
    return f".{init_slice}{global_path}{first_slice}{path_to_scene}{second_slice}{scene_name}.rpy"


def _get_processed_line(var_name):
    global pos_var
    processed_line = f'"[{var_name}[{pos_var}].to_scene_text(vars())]"'
    pos_var += 1
    return processed_line


def _replace_line_and_write_output(line, var_name):
    split_line_comma = line.split('"')
    new_text = line
    if len(split_line_comma) > 2:
        new_text = split_line_comma[0]
        for i in range(1, len(split_line_comma)):
            if i % 2 == 1:
                new_text += _get_processed_line(var_name)
            else:
                new_text += split_line_comma[i]
    return new_text + '\n'


# ---------- Public methods ----------
def set_global_path(path):
    global global_path
    global_path = path


def set_global_pos_var(new_pos_var):
    global pos_var
    pos_var = new_pos_var


def convert_scene(scene_name, path_to_scene, test_mode=False):
    global pos_var
    pos_var = 0
    scene_path = _get_path_rpy(scene_name, path_to_scene)
    var_name = f"day_{scene_name}_scene_text"
    with open(scene_path) as file:
        all_scene_info = file.read().split("\n")
    new_scene_text = ""
    for line in all_scene_info:
        split_line_space = line.strip().split(" ")
        if len(split_line_space) == 1 and split_line_space[0] == "":
            # It is a blank line
            new_scene_text += line + "\n"
        else:
            line = line.replace(SPECIAL_CHARACTER, SPECIAL_CHARACTER_TO_REPLACE)
            is_ignorable = False
            for symbol in IGNORE_SYMBOLS:
                is_ignorable = is_ignorable or symbol in split_line_space[0]
            if split_line_space[-1][-1] == '"' and not is_ignorable:
                # It is a character line
                new_scene_text += _replace_line_and_write_output(line, var_name)
            elif '"' in split_line_space[0]:
                # Command start with string, so probably are menu options
                new_scene_text += _replace_line_and_write_output(line, var_name)
            elif 'renpy.input(' in line:
                new_scene_text += _replace_line_and_write_output(line, var_name)
            else:
                new_scene_text += line + "\n"
    if test_mode:
        return new_scene_text
    else:
        with open(scene_path, 'w') as f:
            f.write(new_scene_text)

