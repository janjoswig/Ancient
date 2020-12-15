from collections.abc import Mapping, MutableMapping
from operator import itemgetter


class Symbols(MutableMapping):
    """Base class for symbol mappings"""

    defaults = {}

    def __init__(self):
        self.reset()
        self._nullum = "N"

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()

    @property
    def nullum(self):
        return self._nullum

    @nullum.setter
    def nullum(self, value):
        assert isinstance(value, str)
        self._nullum = value

    def __setitem__(self, key, value) -> None:
        self._data.__setitem__(key, value)
        self.sort()

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __delitem__(self, key) -> None:
        self._data.__delitem__(key)

    def update(self, *args, **kwargs):
        self._data.update(*args, **kwargs)
        self.sort()

    def __iter__(self):
        return self._data.__iter__()

    def __len__(self):
        return self._data.__len__()

    def sort(self):
        self._data = dict(
            sorted(self._data.items(), key=itemgetter(1), reverse=True)
            )

    def reset(self):
        self._data = dict(self.__class__.defaults)
        self.sort()


class SymbolsASCIIAdditive(Symbols):
    defaults = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }


class SymbolsUnicodeAdditive(Symbols):
    defaults = {
        "Ⅿ": 1000,
        "Ⅾ": 500,
        "Ⅽ": 100,
        "Ⅼ": 50,
        "Ⅹ": 10,
        "Ⅷ": 8,
        "Ⅶ": 7,
        "Ⅵ": 6,
        "Ⅴ": 5,
        'Ⅲ': 3,
        "Ⅱ": 2,
        "Ⅰ": 1,
    }


class SymbolsUnicodeStandard(Symbols):
    defaults = {
        "Ⅿ": 1000,
        "ⅭⅯ": 900,
        "Ⅾ": 500,
        "ⅭⅮ": 400,
        "Ⅽ": 100,
        "ⅩⅭ": 90,
        "Ⅼ": 50,
        "ⅩⅬ": 40,
        # "Ⅻ": 12,
        # "Ⅺ": 11,
        "Ⅹ": 10,
        "Ⅸ": 9,
        "Ⅷ": 8,
        "Ⅶ": 7,
        "Ⅵ": 6,
        "Ⅴ": 5,
        "Ⅳ": 4,
        'Ⅲ': 3,
        "Ⅱ": 2,
        "Ⅰ": 1,
    }


class SymbolsUnicodeExtended(Symbols):
    defaults = {
        "ↈ": 100000,
        "ↇ": 50000,
        "ↂ": 10000,
        "ↁ": 5000,
        "ↀ": 1000,
        "ⅭⅯ": 900,
        "Ⅾ": 500,
        "ⅭⅮ": 400,
        "Ⅽ": 100,
        "ⅩⅭ": 90,
        "Ⅼ": 50,
        "ⅩⅬ": 40,
        # "Ⅻ": 12,
        # "Ⅺ": 11,
        "Ⅹ": 10,
        "Ⅸ": 9,
        "Ⅷ": 8,
        "Ⅶ": 7,
        "Ⅵ": 6,
        "Ⅴ": 5,
        "Ⅳ": 4,
        'Ⅲ': 3,
        "Ⅱ": 2,
        "Ⅰ": 1,
    }


class SymbolsUnicodeExtendedClaudian(Symbols):
    defaults = {
        "ⅭⅭↀↃↃ": 100000,
        "ⅮↃↃ": 50000,
        "ⅭↀↃ": 10000,
        "ⅮↃ": 5000,
        "ↀ": 1000,
        "ⅭⅯ": 900,
        "Ⅾ": 500,
        "ⅭⅮ": 400,
        "Ⅽ": 100,
        "ⅩⅭ": 90,
        "Ⅼ": 50,
        "ⅩⅬ": 40,
        # "Ⅻ": 12,
        # "Ⅺ": 11,
        "Ⅹ": 10,
        "Ⅸ": 9,
        "Ⅷ": 8,
        "Ⅶ": 7,
        "Ⅵ": 6,
        "Ⅴ": 5,
        "Ⅳ": 4,
        'Ⅲ': 3,
        "Ⅱ": 2,
        "Ⅰ": 1,
    }

class SymbolsASCIIStandard(Symbols):
    defaults = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }


class SymbolsASCIIVariant(Symbols):
    defaults = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "IC": 99,
        "IIC": 98,
        "IIIC": 97,
        "XC": 90,
        "L": 50,
        "IL": 49,
        "IIL": 48,
        "XL": 40,
        "IIXX": 18,
        "IIIXX": 17,
        "X": 10,
        "IX": 9,
        "IIX": 8,
        "V": 5,
        "IV": 4,
        "I": 1,
    }


class Roman:
    def __init__(self, number=None, /):
        if number is None:
            self._int = 0

        elif isinstance(number, int):
            self._int = number

        elif isinstance(number, str):
            self._int = interpret_roman(number)

        else:
            try:
                self._int = int(number)
            except TypeError:
                raise TypeError(
                    "Positional argument `number` should be str or "
                    "(convertible to) int"
                    )

        assert isinstance(self._int, int)

        self.format = "ascii-std"

    def __str__(self):
        return roman(self._int, mapping=self.format)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._int}, format={self.format!r})"

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        assert value in symbols
        self._format = value

    def __eq__(self, other):
        return self._int == other

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self._int + other._int)
        return Roman(self._int + other)

    def __iadd__(self, other):
        if isinstance(other, Roman):
            self._int += other._int
        else:
            self._int += other
        return self

    def __radd__(self, other):
        return Roman(other + self._int)

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self._int - other._int)
        return Roman(self._int - other)

    def __isub__(self, other):
        if isinstance(other, Roman):
            self._int -= other._int
        else:
            self._int -= other
        return self

    def __rsub__(self, other):
        return Roman(other - self._int)

    def __int__(self):
        return self._int

    def __index__(self):
        return self._int


def roman(number, /, mapping="ascii-std"):
    """Return the roman representation of an integer"""

    assert isinstance(number, int)

    if isinstance(mapping, str):
        _symbols = symbols[mapping]
    else:
        _symbols = mapping

    assert isinstance(_symbols, Mapping)

    if number == 0:
        return _symbols.nullum

    string_repr = ""
    for symbol, value in _symbols.items():
        while number >= value:
            string_repr += symbol
            number -= value

    return string_repr


def interpret_roman(string, /, mapping="ascii-additive"):
    """Return integer value of roman numeral

    Args:
        string (str): Input string to intepret as integer.
        mapping (str, Mapping): Mapping of symbols to values used
            for the interpretation.  Could be either a valid string
            identifier for a mapping in `:obj:symbols` or an instance of
            a mapping.
    """

    assert isinstance(string, str)

    if isinstance(mapping, str):
        _symbols = symbols[mapping]
    else:
        _symbols = mapping

    if string == _symbols.nullum:
        return 0

    assert isinstance(_symbols, Mapping)

    # Create list of interpreted integer values
    intermediate = []
    j = len(string)
    while string:
        matched_value = _symbols.get(string[:j], None)
        if matched_value is not None:
            intermediate.append(matched_value)
            string = string[j:]
            j = len(string)
        else:
            j -= 1
            assert j > 0, "Cannot interpret symbols"

    # Apply subtraction rule
    for i in range(1, len(intermediate)):
        if intermediate[-(i + 1)] >= intermediate[-i]:
            continue
        intermediate[-(i + 1)] = intermediate[-i] - intermediate[-(i + 1)]
        intermediate[-i] = 0

    return sum(intermediate)


symbols = {
    "ascii-additive": SymbolsASCIIAdditive(),
    "ascii-std": SymbolsASCIIStandard(),
    "ascii-variant": SymbolsASCIIVariant(),
    "unicode-additive": SymbolsUnicodeAdditive(),
    "unicode-std": SymbolsUnicodeStandard(),
    "unicode-extended": SymbolsUnicodeExtended(),
    "unicode-extended-claudian": SymbolsUnicodeExtendedClaudian(),
}
