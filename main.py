import pyautogui as pag
import time


def move_mouse():
    while True:
        xpos, ypos = 1, 1
        time.sleep(30)  # Move mouse every 58 seconds to prevent timeouts
        pag.moveRel(xpos, ypos)
        xpos *= -1  # Multiply xpos by -1 to remain mouse in same position
        ypos *= -1  # Multiply ypos by -1 to remain mouse in same position


while __name__ == "__main__":
    move_mouse()
