import os

# -------------------- CONSTANT DEFINITION --------------------
IGNORE_SYMBOLS = ["$", "queue"]

SPECIAL_CHARACTER_TO_REPLACE = "#!#"
DEFAULT_LANGUAGE = "LANG_ENG"
SPECIAL_CHARACTER = "\\\""

# -------------------- GLOBAL DEFINITION --------------------

selected_language = DEFAULT_LANGUAGE
write_output = False
output_text = ""
global_path = ""
pos_var = 0


# -------------------- Private methods --------------------

#     >>>>>   Utils
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


#     >>>>>   Output

def _str_init_text_file(var_name):
    return f"init -1 python:\n    {var_name} = [\n        "


def _str_end_text_file():
    return "\n    ]\n"


def _write_output(text):
    global output_text, write_output
    if not write_output:
        return
    new_str = "EvolvedString({\n"
    new_str += f'            {selected_language}: "{text}",\n'
    new_str += "        }), "
    output_text += new_str


#     >>>>>   Logic
def _replace_line_and_write_output(line, var_name):
    split_line_comma = line.split('"')
    new_text = line
    if len(split_line_comma) > 2:
        new_text = split_line_comma[0]
        for i in range(1, len(split_line_comma)):
            if i % 2 == 1:
                new_text += _get_processed_line(var_name)
                _write_output(split_line_comma[i])
            else:
                new_text += split_line_comma[i]
    return new_text + '\n'


# -------------------- Public methods --------------------
#     >>>>>   Setters
def set_global_path(path):
    global global_path
    global_path = path


def set_global_pos_var(new_pos_var):
    global pos_var
    pos_var = new_pos_var


def set_language(language):
    global selected_language
    selected_language = language


def fuse_scene_text(file_path_original, file_path_translation, write_out=True):
    text_new = ""
    txt_spl1 = "EvolvedString({"
    txt_spl2 = "        }), "
    with open(file_path_original) as f:
        text_original = f.read()
    if file_path_translation is None or not os.path.isfile(file_path_translation):
        text_new = text_original
    else:
        with open(file_path_translation) as f:
            text_translated = f.read()
        to_slc = text_original.split(txt_spl1)
        tt_slc = text_translated.split(txt_spl1)
        if len(to_slc) != len(tt_slc):
            raise ValueError(
                "The length of the dictionaries of the original and translated versions are not the same." +
                " Impossible to fuse both files. Contact with the translation team to fixed the bug. \n\n" +
                "## --> File involved: " + file_path_original
            )
        if len(to_slc) == 1:
            text_new = text_original
        else:
            text_new = to_slc[0]
            for i in range(1, len(to_slc)):
                text_new = f"{text_new}{txt_spl1}{to_slc[i].split(txt_spl2)[0]}{tt_slc[i].split(txt_spl2)[0][1:]}{txt_spl2}"
                print("hey")
                print(tt_slc[i].split(txt_spl2)[0][1:].split(txt_spl2))

            text_new = f"{text_new}{to_slc[-1].split(txt_spl2)[-1]}"
    if write_out:
        with open(file_path_original, 'w') as f:
            f.write(text_new)
    else:
        return text_new


#     >>>>>   Conversor
def convert_scene(scene_name, path_to_scene, test_mode=False, write_out=False, output_file_name=None):
    global pos_var, output_text, write_output
    write_output = write_out
    pos_var = 0
    scene_path = _get_path_rpy(scene_name, path_to_scene)
    var_name = f"day_{scene_name}_scene_text"
    with open(scene_path) as file:
        all_scene_info = file.read().split("\n")
    new_scene_text = ""
    if write_output:
        output_text = _str_init_text_file(var_name)
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
    if write_output:
        output_text += _str_end_text_file()
    if test_mode:
        if write_output:
            return new_scene_text, output_text
        else:
            return new_scene_text
    else:
        with open(scene_path, 'w') as f:
            f.write(new_scene_text)
        if write_output:
            if output_file_name is not None:
                with open(output_file_name, 'w') as f:
                    f.write(output_text)
            else:
                with open(_get_path_rpy(f"{scene_name}_text", path_to_scene), 'w') as f:
                    f.write(output_text)
