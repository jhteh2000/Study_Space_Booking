import pyautogui as gui
from datetime import datetime
from time import sleep

while True:
    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    print(current_time)
    sleep(1)

    if current_time == "15:28":
        break

print("operation ended")