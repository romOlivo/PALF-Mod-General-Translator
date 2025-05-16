MODIFICATIONS = {
    "not isinstance(specific, str)": "not isinstance(specific, str) and not isinstance(specific, EvolvedString)",
    "move.Name": "str(move.Name)",
    "specific not in category": "str(specific) not in category",
}


def adapt_scene(path="", scene_name="screens"):
    with open(f"./{path}{scene_name}.rpy") as f:
        screen_str = f.read()
        for modification in MODIFICATIONS:
            screen_str = screen_str.replace(modification, MODIFICATIONS[modification])
    return screen_str

