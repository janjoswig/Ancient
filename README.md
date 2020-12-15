[![PyPi Version](https://img.shields.io/pypi/v/ancient.svg)](https://pypi.org/project/ancient/)
[![PyPi License](https://img.shields.io/pypi/l/ancient.svg)](https://pypi.org/project/ancient/)
[![Python Versions](https://img.shields.io/pypi/pyversions/ancient.svg)](https://pypi.org/project/ancient/)
[![Build Status](https://travis-ci.com/janjoswig/Ancient.svg?branch=main)](https://travis-ci.com/janjoswig/Ancient)
[![Code Coverage](https://raw.githubusercontent.com/janjoswig/Ancient/master/badges/coverage.svg)](https://github.com/janjoswig/Ancient)

# Ancient
Convert between integers and roman numerals in Python

## Install

Install from PyPi

```bash
$ pip install cnnclustering
```

or clone the developement version from GitHub

```bash
$ git clone https://github.com/janjoswig/Ancient.git
$ cd Ancient
$ pip install .
```
## Usage

### Import
```python
from ancient import roman
```

### Basic conversions

Convert integer values to Roman numerals

```python
for i in range(10):
    print(roman.roman(i))
```

```bash
N
I
II
III
IV
V
VI
VII
VIII
IX
```

By default, the conversion follows the standard scheme using a subtractive representation for the values 4, 9, 14, etc. (e.g. IV instead of IIII). An additive representation can be selected via the `mapping` keyword (see also [Custom Mappings](#Mappings)).

```python
for i in range(10):
    print(roman.roman(i, mapping="ascii-additive"))
```

```bash
N
I
II
III
IIII
V
VI
VII
VIII
VIIII
```

Composition of large numbers (>4999) can be improved using an extended mapping.

```python
for i in [5000, 10000, 50000, 100000]:
    print(roman.roman(i, mapping="unicode-extended"))
```

```bash
ↁ
ↂ
ↇ
ↈ
```

Interpretation of Roman numerals

```python
for i in ["I", "IV", "IIII", "XX", "XL", "C"]:
    print(roman.interpret_roman(i))
```

```bash
1
4
4
20
40
100
```

### The Roman data type

The packag provides the `Roman` data type to handle Roman numerals

```python
number = roman.Roman(5)

print(f"{number!r}")
print(f"{number!s}")
```

```bash
Roman(5, format='ascii-std')
V
```

The type behaves like an integer in arithmetic operations

```python
print(number + 2)
print(number - roman.Roman(1))
print(number * 2)
print(number / 2)  # Integer division!
```

```bash
VII
IV
X
II
```

### <a name="Mappings"></a> Custom Mappings

A mapping of Roman symbols to integer values used for interconversions has the form

```python
mapping = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    }
```

For the conversion of integers to Roman numerals, such a mapping should have a decreasing order in the integer values. To ensure this, mappings can inherit from `roman.Symbols`. Note, that only one symbol is effectively used if the same value is mapped to more than one symbols.

```python
custom_mapping = roman.Symbols()
custom_mapping.update({"ↆ": 50, "Ж": 100, "I": 1, "Ʌ": 5})
print(custom_mapping)
```

```bash
{'Ж': 100, 'ↆ': 50, 'Ʌ': 5, 'I': 1}
```

A cutsom mapping can be used in conversions instead of the default mappings

```python
roman.roman(156, mapping=custom_mapping)
```

```bash
'ЖↆɅI'
```

A set of mappings is provided as instances of f `roman.Symbols` in `roman.symbols`

```python
print(roman.symbols.keys())
```

```bash
dict_keys(['ascii-additive', 'ascii-std', 'ascii-variant', 'unicode-additive', 'unicode-std', 'unicode-extended', 'unicode-extended-claudian'])
```

Mappings stored in this place can be used by their key in conversions. Instances of type `Roman` have an attribute `format` that controls the conversion and should be a valid mapping key.

```python
number = roman.Roman(100)
print(number)

roman.symbols["custom"] = custom_mapping
number.format = "custom"
print(number)
```

```bash
C
Ж
```

### Zero and negative numbers

The package can handle negative numbers

```python
number = roman.Roman(-10)
print(number)
```

```bash
-X
```

The symbol used to represent 0 is stored on the used mappings and can be changed.

```python
print(roman.symbols["unicode-std"].nullum)
```

```bash
N
```
