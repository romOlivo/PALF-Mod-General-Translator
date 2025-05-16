import pytest

import translation_tests.temp
from translation_tests.temp import EvolvedString, LANG_ENG, LANG_ESP


class TestEvolvedString:
    @pytest.mark.parametrize("first,second,expected_result", [
        (EvolvedString({LANG_ENG: "hello"}), "hello", True),
        (EvolvedString({LANG_ENG: "hello"}), "bye", False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), "hello", True),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), "bye", False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), "hola", True),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}, prefix="hey-"), "hola", False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}, prefix="hey-"), "hey-hola", True),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}, prefix="hey-"), "hello", False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}, prefix="hey-"), "hey-hello", True),
        (EvolvedString({LANG_ENG: "hello"}), EvolvedString({LANG_ENG: "hello"}), True),
        (EvolvedString({LANG_ENG: "hello"}), EvolvedString({LANG_ENG: "bye"}), False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), EvolvedString({LANG_ENG: "hello"}), True),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), EvolvedString({LANG_ENG: "bye"}), False),
        (EvolvedString({LANG_ENG: "hello"}, prefix="hey-"), EvolvedString({LANG_ENG: "hello"}, prefix="hey-"), True),
        (EvolvedString({LANG_ENG: "hello"}, prefix="hey-"), EvolvedString({LANG_ENG: "hello"}), False),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}, prefix="hey-"), EvolvedString({LANG_ENG: "hello"}, prefix="hey-"), True),
        (EvolvedString({LANG_ENG: "hello", LANG_ESP: "hola"}), EvolvedString({LANG_ENG: "bye"}, prefix="hey-"), False),
    ])
    def test_eq(self, first, second, expected_result):
        translation_tests.temp.selected_language = LANG_ESP
        assert (first == second) == expected_result

    @pytest.mark.parametrize("first,second,expected_result", [
        (EvolvedString({LANG_ENG: "a"}), "a", False),
        (EvolvedString({LANG_ENG: "a"}), "b", False),
        (EvolvedString({LANG_ENG: "b"}), "a", True),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}), "a", False),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}), "b", False),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}), "a", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}), "a", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}), "b", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}), "a", True),
        (EvolvedString({LANG_ENG: "b"}, prefix="a"), "a", True),
        (EvolvedString({LANG_ENG: "b"}, prefix="a"), "b", False),
        (EvolvedString({LANG_ENG: "a"}, prefix="b"), "a", True),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}, prefix="a"), "a", True),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}, prefix="a"), "b", False),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}, prefix="b"), "a", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}, prefix="a"), "a", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}, prefix="a"), "b", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}, prefix="b"), "a", True),
    ])
    def test_gt(self, first, second, expected_result):
        translation_tests.temp.selected_language = LANG_ESP
        assert (first > second) == expected_result

    @pytest.mark.parametrize("first,second,expected_result", [
        (EvolvedString({LANG_ENG: "a"}), "a", False),
        (EvolvedString({LANG_ENG: "a"}), "b", True),
        (EvolvedString({LANG_ENG: "b"}), "a", False),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}), "a", False),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}), "b", True),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}), "a", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}), "a", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}), "b", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}), "a", False),
        (EvolvedString({LANG_ENG: "b"}, prefix="a"), "a", False),
        (EvolvedString({LANG_ENG: "b"}, prefix="a"), "b", True),
        (EvolvedString({LANG_ENG: "a"}, prefix="b"), "a", False),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}, prefix="a"), "a", False),
        (EvolvedString({LANG_ENG: "b", LANG_ESP: "c"}, prefix="a"), "b", True),
        (EvolvedString({LANG_ENG: "a", LANG_ESP: "c"}, prefix="b"), "a", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}, prefix="a"), "a", False),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "b"}, prefix="a"), "b", True),
        (EvolvedString({LANG_ENG: "c", LANG_ESP: "a"}, prefix="b"), "a", False),
    ])
    def test_lt(self, first, second, expected_result):
        translation_tests.temp.selected_language = LANG_ESP
        assert (first < second) == expected_result
