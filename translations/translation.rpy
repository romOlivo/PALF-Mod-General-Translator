init -3 python:
    LANG_ENG = "english"
    LANG_ESP = "spanish"
    selected_language = LANG_ESP

    languages = [LANG_ENG, LANG_ESP]

    class EvolvedString:
        def __init__(self, values, prefix=""):
            self.values = values
            self.prefix = prefix

        def _get_unique(self):
            return self.prefix + self.values[LANG_ENG]

        def __str__(self):
            global selected_language
            value = self.values[selected_language] if selected_language in self.values else self.values[LANG_ENG]
            return self.prefix + value

        def __eq__(self, other):
            return other == self._get_unique() or other == self.__str__()

        def __hash__(self):
            return hash(self._get_unique())

        def __iter__(self):
            return self.__str__().__iter__()

        def __next__(self):
            return self.__str__().__next__()

        def __getattr__(self, name):
            return self.__str__()

        def __add__(self, other):
            return self.__str__() + other

        def __radd__(self, other):
            return other + self.__str__()

        def __getitem__(self, item):
            return self._get_unique()[item]

        def __contains__(self, item):
            return item in self.__str__()

        def __lt__(self, other):
            return self._get_unique() < other

        def __le__(self, other):
            return self._get_unique() <= other

        def __gt__(self, other):
            return self._get_unique() > other

        def __ge__(self, other):
            return self._get_unique() >= other

        def __getstate__(self):
            return self._get_unique()

        def __setstate__(self, state):
            if isinstance(state, str):
                self.values = {LANG_ENG: state}
                self.prefix = ""
            else:
                self.__dict__.update(state)

        def split(self, value):
            return self._get_unique().split(value)

        def replace(self, value_original, value_replace):
            new_prefix = self.prefix.replace(value_original, value_replace)
            return EvolvedString(self.values, prefix=new_prefix)

        def index(self, value):
            return self._get_unique().index(value)
