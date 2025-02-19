# Ascii Clock

## Description

A simple command-line clock made using python. For visiblity reason, the digits are colorize using 'lolpython'.

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/FloppyCacti/ascii-clock.git
cd ascii-clock/
```

Create and activate a virtual environment

```bash
python -m venv .
source bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
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

## Example

Default:

![Defulat Clock](https://github.com/user-attachments/assets/c03c75ef-ab04-4027-aca2-796fe1b47f68)

Disabled colorized digits:

![Simple Clock](https://github.com/user-attachments/assets/13e7db63-8b9d-464d-8d72-66f4ab3eaa05)

4max font:

![4max Font Clock](https://github.com/user-attachments/assets/024cc914-fb1e-4c47-8912-b322a1135857)

Computer font:

![Computer Font Clock](https://github.com/user-attachments/assets/38fbe05f-d2a8-4dc4-94a2-8576a7ca42ae)

## Contributing

Feel free to submit pull reqests or open issues if you have suggestions or improvements.

## Acknowledgements

- [pyfiglet](https://github.com/pwaller/pyfiglet.git) for ASCII art generation
- [lolpython](https://github.com/KartikTalwar/LOLPython.git) for colorizing text
