from translation_utils import convert_scene, set_global_path, adapt_scene, fuse_scene_text
import shutil
import os


want_to_fuse_translations = True

if __name__ == "__main__":
    # Adapt all scene texts, using the translated versions
    set_global_path("/scenes/")
    with open("translations/config.csv") as f:
        config = f.read().split("\n")[1:]
        for scene_config in config:
            # Get info of the scene to convert
            scene_config_split = scene_config.split("#")
            # Convert the original scene into the new format
            convert_scene(scene_config_split[0], scene_config_split[1], write_out=True)
            # Add the new translations to the original text, if wanted
            if want_to_fuse_translations:
                path_original = f"./scenes/{scene_config_split[1]}/{scene_config_split[0]}_text.rpy"
                path_translated = f"./translations/scenes/{scene_config_split[0]}_text.rpy"
                fuse_scene_text(path_original, path_translated)
    # Adapt the file 'screens'
    adapt_scene()
    # Remove test if exists
    if os.path.exists("./translation_tests"):
        shutil.rmtree("./translation_tests")

