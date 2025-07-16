MODIFICATIONS = {
    "not isinstance(specific, str)": "not isinstance(specific, str) and not isinstance(specific, EvolvedString)",
    "move.Name": "str(move.Name)",
    "specific not in category": "str(specific) not in category",
}


"""
    Adapt the screen file with the modifications needed to be able to use the EvolvedString correctly.
    Input variables:
    path --------> Relative path where the file to modify is located.
    scene_name --> Name of the file to modify.
    Output:
    screen_str --> String containing the modified text of the file.
"""
def adapt_scene(path:str="", scene_name:str="screens") -> str:
    with open(f"./{path}{scene_name}.rpy", encoding="utf8") as f:
        screen_str = f.read()
        for modification in MODIFICATIONS:
            screen_str = screen_str.replace(modification, MODIFICATIONS[modification])
    return screen_str

