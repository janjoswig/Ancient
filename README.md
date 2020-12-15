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

```python
from ancient import roman
```

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