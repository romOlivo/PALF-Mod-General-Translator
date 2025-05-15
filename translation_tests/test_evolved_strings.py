import pytest

from translation_tests.temp import EvolvedString, LANG_ENG


class TestEvolvedString:
    def test_eq_evstr_str(self):
        assert EvolvedString({LANG_ENG: "hello"}) == "hello"

