import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try to import the packages, if not installed, install them
try:
    import pyfiglet
    from pyfiglet import Figlet
except ImportError:
    install('pyfiglet')
    import pyfiglet
    from pyfiglet import Figlet

try:
    from lolpython import lol_py
except ImportError:
    install('lolpython')
    from lolpython import lol_py

import datetime
import os
import time

# Function to clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to install a custom font in figlet
def install_font(font, font_file):
    try:
        subprocess.check_call([sys.executable, '-m', "pyfiglet", "-L", font_file])
        return font
    except:
        print(f"Error using custom font test")
        return 'standard'

# Function to set the font for figlet
def set_Font(font):
    # Font exist in pyfiglet
    if(font in pyfiglet.FigletFont.getFonts()):
        return font

    # Contruct the path to the custom font file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    FONT_PATH = os.path.join(script_dir, '.', 'fonts', f"{font}.flf")
    FONT_PATH = os.path.abspath(FONT_PATH)
    
    # Font file exist -> install it
    if os.path.isfile(FONT_PATH):
        return install_font(font, FONT_PATH)
    else:
        print(f"ERROR Font Not Found")
        return 'standard'

def main():
    custom_font = set_Font('3D-ASCII')

    while True:

        # Formate time to get "HH:MM:SS"
        formatted_time = datetime.datetime.now().strftime('%I:%M:%S')

        # Clear the screen for a fresh update
        clear_screen()

        try:
            # Formate formatted_time to get acsii
            f = Figlet(font=custom_font)
            ascii_art = f.renderText(formatted_time)
        except Exception as e:
            print(f"Error using custom font this: {e}")
            f = Figlet()
            ascii_art = f.renderText(formatted_time)


        # Colorrize text
        lol_py(ascii_art)

        # Pause for one second between updates
        time.sleep(1)

# Run the clock
if __name__ == "__main__":
    main()