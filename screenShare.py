import cv2
import numpy as np
import pyautogui
from time import time


# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
FPS = 20.0
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output" + str(int(time())) + ".avi", fourcc, FPS, SCREEN_SIZE)
end = time() + 10
while time()<end:
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
