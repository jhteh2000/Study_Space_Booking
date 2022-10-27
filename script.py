from tkinter import Y
import pyautogui as pg
from datetime import datetime
from time import sleep

def check_current_time(target_time):
    while True:
        now = datetime.now()
        current_time = str(now.strftime("%H:%M"))
        print(current_time)
        sleep(0.1)

        if current_time == target_time:
            break

def auto_booking():
    global posX, posY

    posX, posY = pg.locateCenterOnScreen("page_arrow.png", confidence=.8)
    pg.moveTo(posX, posY, duration=0.1)
    pg.moveRel(20, 0, duration=0.1)
    pg.click()
    pg.moveTo(1305, 1025, duration=0.1)
    pg.click()

    for count in range(8):
        check_slot_status()
        pg.moveRel(90, 0, duration=0.1)
        pg.click()

def check_slot_status():
    global posX, posY

    # Booked(rgba(245,159,22,255))
    # Unavailable(rgba(204,204,204,255))
    posX, posY = pg.position()
    while True:
        if pg.pixelMatchesColor(posX, posY, (245,159,22), tolerance=10) or \
            pg.pixelMatchesColor(posX, posY, (204,204,204), tolerance=10):
            break

check_current_time("18:44")
auto_booking()
print("Operation Ended")