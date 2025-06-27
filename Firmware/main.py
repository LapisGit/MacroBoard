import json
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D8, board.D9, board.D10, board.D11]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

def load_keymap(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    keymap = []
    for row in config.get("keymap", []):
        row_keys = []
        for key in row:
            try:
                # Check if the key is valid KC key from kmk.keys
                row_keys.append(getattr(KC, key))
            except AttributeError:
                print(f"Invalid key: {key}. Please ensure it's a valid KC key.")
                row_keys.append(None)
        keymap.append(row_keys)
    
    return keymap

keymap = load_keymap('keymap_config.json')
keyboard.keymap = keymap

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
