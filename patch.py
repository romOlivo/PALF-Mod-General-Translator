from translation_utils import convert_scene, set_global_path, adapt_scene
import shutil
import os

if __name__ == "__main__":
    # Adapt all scene texts, using the translated versions
    set_global_path("/scenes/")
    with open("translations/config.csv") as f:
        config = f.read().split("\n")[1:]
        for scene_config in config:
            scene_config_split = scene_config.split("#")
            convert_scene(scene_config_split[0], scene_config_split[1], write_out=True)
    # Adapt the file 'screens'
    adapt_scene()
    # Remove test if exists
    if os.path.exists("./translation_tests"):
        shutil.rmtree("./translation_tests")

