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

    @pytest.mark.parametrize("line,expected_result", [
        ('some visual command', 'some visual command\n'),
        ('"hello"', '"[my_var[0]]"\n'),
        ('"hello [something]"', '"[my_var[0]][something][my_var[1]]"\n'),
        ('"[something] bye"', '"[my_var[0]][something][my_var[1]]"\n'),
        ('"hello [something] bye"', '"[my_var[0]][something][my_var[1]]"\n'),
        ('command "hello"', 'command "[my_var[0]]"\n'),
        ('"[ellipse]"', '"[ellipse]"\n'),
        ('"hello [ellipse]"', '"[my_var[0]][ellipse][my_var[1]]"\n'),
        ('"[ellipse] bye"', '"[my_var[0]][ellipse][my_var[1]]"\n'),
        ('"hello [ellipse] bye"', '"[my_var[0]][ellipse][my_var[1]]"\n'),
        ('command1 command2 command3 "some text"', 'command1 command2 command3 "[my_var[0]]"\n'),
        ('"one [first] two [second] three [third] end"', '"[my_var[0]][first][my_var[1]][second][my_var[2]][third][my_var[3]]"\n'),
    ])
    def test_replace_line_and_write_output(self, line, expected_result):
        var_name = 'my_var'
        scenes_adapters.pos_var = 0
        assert scenes_adapters._replace_line_and_write_output(line, var_name) == expected_result




