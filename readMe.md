# Ascii Clock

## Description

A simple command-line clock made using python. For visiblity reason, the digits are colorize using 'lolpython'.

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/FloppyCacti/ascii-clock.git
cd ascii-clock/src/
```

## Usage

Enter into src directory and run makeClock.sh file:

```bash
./makeClock.sh
``` 

## Configuration

To disable colorized digits, modify main.py:

```bash
lol_py(ascii_art)
```

To:

```bash
print(ascii_art)
```

To change ascii font, first install the font(*.flf) file. To install multiple font files at once run:

```bash
pyfiglet -L /path/to/the/font/file/*.flf/
```
Alternatively, put the font file(s) in fonts directory in src directory, then change the custom_font in main.py:
```bash
custom_font = set_Font('3D-ASCII')
```
To:
```bash
custom_font = set_Font('Font_name')
```

## Contributing

Feel free to submit pull reqests or open issues if you have suggestions or improvements.

## Acknowledgements

- [pyfiglet](https://github.com/pwaller/pyfiglet.git) for ASCII art generation
- [lolpython](https://github.com/KartikTalwar/LOLPython.git) for colorizing text
