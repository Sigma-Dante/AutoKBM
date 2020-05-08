import pyautogui as pag
import time


def move_mouse():
    xpos, ypos = 1, 1
    while True:
        pag.moveRel(xpos, ypos)
        xpos *= -1  # Multiply pos values by -1 to remain mouse in same position
        ypos *= -1  # Multiply pos values by -1 to remain mouse in same position
        time.sleep(30)  # Move mouse every 30 seconds to prevent timeouts


while __name__ == "__main__":
    move_mouse()
