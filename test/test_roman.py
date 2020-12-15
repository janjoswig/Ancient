from typing import MutableMapping
import pytest

from ancient import roman

INT_TO_ROMAN_ASCII_ADDITIVE_CASES = [
    (0, "N"),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IIII"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "VIIII"),
    (10, "X")
]

INT_TO_ROMAN_ASCII_STD_CASES = [
    (4, "IV"),
    (9, "IX"),
    (40, "XL"),
    (90, "XC"),
    (400, "CD"),
    (900, "CM"),
]

INT_TO_ROMAN_ASCII_VARIANT_CASES = [
    (18, "IIXX"),
    (17, "IIIXX"),
]

INT_TO_ROMAN_CUSTOM = [
    (6, "ZZZ"),
    (13, "XYZ")
    ]

ROMAN_TO_INT_CUSTOM = [
    ("ZZZ", 6),
    ("XYZ", 13)
    ]

custom_symbols = roman.Symbols()
custom_symbols["Z"] = 2
custom_symbols["XYZ"] = 13

ROMAN_TO_INT_ASCII_CASES = [
    ("N", 0),
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IIII", 4),
    ("IV", 4),
    ("V", 5),
    ("VI", 6),
    ("VII", 7),
    ("VIII", 8),
    ("VIIII", 9),
    ("IX", 9),
    ("X", 10)
]


class TestRomanNumbers:

    @pytest.mark.parametrize(
        "number,expected",
        INT_TO_ROMAN_ASCII_ADDITIVE_CASES
    )
    def test_integer_to_roman_ascii_additive(self, number, expected):
        assert roman.roman(number, mapping="ascii-additive") == expected

    @pytest.mark.parametrize(
        "number,expected",
        INT_TO_ROMAN_ASCII_STD_CASES
    )
    def test_integer_to_roman_ascii_std(self, number, expected):
        assert roman.roman(number) == expected

    @pytest.mark.parametrize(
        "number,expected",
        INT_TO_ROMAN_ASCII_VARIANT_CASES
    )
    def test_integer_to_roman_ascii_variant(self, number, expected):
        assert roman.roman(number, mapping="ascii-variant") == expected

    @pytest.mark.parametrize(
        "number,expected",
        INT_TO_ROMAN_CUSTOM
    )
    def test_integer_to_roman_custom(self, number, expected):
        assert roman.roman(number, mapping=custom_symbols) == expected

    def test_fail_to_roman_if_not_integer(self):
        with pytest.raises(AssertionError):
            roman.roman("0b0101")

    @pytest.mark.parametrize(
        "string,expected",
        ROMAN_TO_INT_ASCII_CASES
    )
    def test_roman_to_integer_ascii(self, string, expected):
        assert roman.interpret_roman(string) == expected

    @pytest.mark.parametrize(
        "string,expected",
        ROMAN_TO_INT_CUSTOM
    )
    def test_roman_to_integer(self, string, expected):
        assert roman.interpret_roman(string, mapping=custom_symbols) == expected

    def test_create_with_no_argument_and_check_value(self):
        number = roman.Roman()
        assert number == 0

    @pytest.mark.parametrize(
        "number,expected",
        INT_TO_ROMAN_ASCII_STD_CASES
    )
    def test_create_and_check_representations(self, number, expected):
        roman_number = roman.Roman(number)
        assert f"{roman_number!r}" == expected

    def test_add(self):
        a = roman.Roman(1)
        b = roman.Roman(2)
        c = a + b
        assert c == 3
        assert isinstance(c, roman.Roman)
        assert a + 2 == 3

    def assert_symbols(self, symbols):
        assert isinstance(symbols, MutableMapping)
        symbol_values = list(symbols.values())
        check_order = (
            symbol_values[i] < symbol_values[i - 1]
            for i in range(1, len(symbol_values))
            )
        assert all(check_order)

    def test_access_symbols(self):
        for symbols in roman.symbols.values():
            self.assert_symbols(symbols)

    def test_symbols_representation(self):
        symbols = roman.Symbols()
        assert f"{symbols!r}" == "{}"
        assert f"{symbols!s}" == "{}"

    def test_manipulate_symbols(self):
        symbols = roman.Symbols()
        symbols["Z"] = 99
        assert symbols["Z"] == 99

        self.assert_symbols(symbols)

        symbols["Y"] = 98
        del symbols["Y"]

        with pytest.raises(LookupError):
            _ = symbols["Y"]

        symbols.update({"A": 1, "B": 8, "C": 4})

        self.assert_symbols(symbols)

        symbols.reset()
        with pytest.raises(LookupError):
            _ = symbols["Z"]

        self.assert_symbols(symbols)

        symbols.nullum = "nn"
        assert symbols.nullum == "nn"

        with pytest.raises(AssertionError):
            symbols.nullum = 0
