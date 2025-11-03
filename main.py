from pynput.keyboard import Key, Listener
from playsound3 import playsound
import threading

alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def play_sound(path):
    playsound(path)


def on_press(key):
    try:
        # convert all keys pressed to lowercase
        i = alphabet.index(key.char.lower())

        # name = out0{INDEX} where index is 2 digits long
        name = f"out0{i:02d}"

        # ./sounds/NAME/.wav
        path = f"./sounds/{name}.wav"

        # new thread created to play multiple sounds at once
        threading.Thread(target=play_sound, args=(path,), daemon=True).start()

    except (AttributeError, ValueError):
        # ignore all non-alphabet keys
        pass


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
