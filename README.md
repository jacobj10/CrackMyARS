# CrackMyARS
Robust RSA cracking tool, used for CTF mainly but can have other applications

## Setup

Clone this repository `git clone https://github.com/jacobj10/CrackMyARS`

Build the pacakge `python3 setup.py build`

Install the pacakge `sudo python3 setup.py install`

## Usage

```python3
from CrackMyARS.utils.key import Key

# Instantiate Key (put in keyword args as necessary i.e. n=..., e=...)
x = Key(**kwargs)

# Add necessary files
x.add_pem('PATH_TO_PEM')
x.c_from_file('PATH_TO_C')

# Multiple N and C supported (Only for CRT, of course)
x.add_multiple_c_from_file([FILE_LIST])
x.add_multiple_n_from_file([FILE_LIST])

# Finally, run the internal deciding mechanism to try and retrieve either D if no message or C
x.decide()
```
