import pytest

from translation_utils import scenes_adapters


class TestScenesAdapter:
    @pytest.mark.parametrize("scene_name,path_to_scene,expected_path", [
        ("hello", "be_afraid", "./hey/be_afraid/hello.rpy"),
        ("/hello", "be_afraid", "./hey/be_afraid/hello.rpy"),
        ("hello", "/be_afraid", "./hey/be_afraid/hello.rpy"),
        ("/hello", "/be_afraid", "./hey/be_afraid/hello.rpy"),
        ("a", "a", "./hey/a/a.rpy"),
        ("/a", "a", "./hey/a/a.rpy"),
        ("a", "/a", "./hey/a/a.rpy"),
        ("/a", "/a", "./hey/a/a.rpy"),
    ])
    def test_get_path_rpy(self, scene_name, path_to_scene, expected_path):
        scenes_adapters.set_global_path("hey/")
        assert scenes_adapters._get_path_rpy(scene_name, path_to_scene) == expected_path



