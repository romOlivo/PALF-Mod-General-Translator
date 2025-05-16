import pytest

from translation_utils import adapt_scene


class TestScreenAdapter:
    @pytest.mark.parametrize("scene_name", [
        "scene_example_01",                    # Without any modification
        "scene_example_02",                    # With isinstance(evstr, str) modification
        "scene_example_03",                    # With move.Name modification
        "scene_example_04",                    # With isinstance(evstr, str) and specific modifications
    ])
    def test_screen_adapter(self, scene_name):
        result = adapt_scene(path="translation_tests/files/", scene_name=scene_name)
        with open(f"./translation_tests/files/{scene_name}_result.rpy") as f:
            expected_result = f.read()
        assert result == expected_result
