import pyautogui as pg
import keyboard as kb
import time
import cv2

previous = 1
current = 1
wasPressed = False
disabled = False

oneButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_1_on.png")
twoButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_2_on.png")
threeButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_3_on.png")
fourButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_4_on.png")
fiveButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_5_on.png")
sixButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_6_on.png")
sevenButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_7_on.png")
eightButton = cv2.imread(r"D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/button_8_on.png")


f = open("D:/Git-Stuff/Solo Work/Bias-FX-Quick-Snap-Hotkeys/Hotkeys/Documentation.txt", 'r')
file_contents = f.read()
print(file_contents)
f.close()

def findOne():
    global previous
    global current
    global oneButton
    previous, current = current, previous
    current = 1
    coords = pg.locateCenterOnScreen(oneButton)
    pg.click(coords)
def findTwo():
    global previous
    global current
    global twoButton
    previous, current = current, previous
    current = 2
    coords = pg.locateCenterOnScreen(twoButton)
    pg.click(coords)
def findThree():
    global previous
    global current
    global threeButton
    previous, current = current, previous
    current = 3
    coords = pg.locateCenterOnScreen(threeButton)
    pg.click(coords)
def findFour():
    global previous
    global current
    global fourButton
    previous, current = current, previous
    current = 4
    coords = pg.locateCenterOnScreen(fourButton)
    pg.click(coords)
def findFive():
    global previous
    global current
    global fiveButton
    previous, current = current, previous
    current = 5
    coords = pg.locateCenterOnScreen(fiveButton)
    pg.click(coords)
def findSix():
    global previous
    global current
    global sixButton
    previous, current = current, previous
    current = 6
    coords = pg.locateCenterOnScreen(sixButton)
    pg.click(coords)
def findSeven():
    global previous
    global current
    global sevenButton
    previous, current = current, previous
    current = 7
    coords = pg.locateCenterOnScreen(sevenButton)
    pg.click(coords)
def findEight():
    global previous
    global current
    global eightButton
    previous, current = current, previous
    current = 8
    coords = pg.locateCenterOnScreen(eightButton)
    pg.click(coords)

def findCurrent():
    global oneButton
    global twoButton
    global threeButton
    global fourButton
    global fiveButton
    global sixButton
    global sevenButton
    global eightButton 

    if current == 1:
        coords = pg.locateCenterOnScreen(oneButton)
        pg.click(coords)
    elif current == 2:
        coords = pg.locateCenterOnScreen(twoButton)
        pg.click(coords)
    elif current == 3:
        coords = pg.locateCenterOnScreen(threeButton)
        pg.click(coords)
    elif current == 4:
        coords = pg.locateCenterOnScreen(fourButton)
        pg.click(coords)
    elif current == 5:
        coords = pg.locateCenterOnScreen(fiveButton)
        pg.click(coords)
    elif current == 6:
        coords = pg.locateCenterOnScreen(sixButton)
        pg.click(coords)
    elif current == 7:
        coords = pg.locateCenterOnScreen(sevenButton)
        pg.click(coords)
    elif current == 8:
        coords = pg.locateCenterOnScreen(eightButton)
        pg.click(coords)

def goLeft():
    global previous
    global current
    current = current - 1
    previous = current + 1
    if current < 1:
        current = 8
    findCurrent()

def goRight():
    global previous
    global current
    current = current + 1
    previous = current - 1
    if current > 8:
        current = 1
    findCurrent()

def reverse():
    global previous
    global current
    current, previous = previous, current
    findCurrent()

def on_press_reaction(event):
    global disabled
    if event.name == "esc":
        disabled = not disabled
        if disabled: 
            print("Hotkeys have been disabled (press esc to re-enable)")
        if not disabled:
            print("Hotkeys have been enabled (press esc to disable)")

    if not disabled:
        if event.name == "1":
            findOne()
        if event.name == "2":
            findTwo()
        if event.name == "3":
            findThree()
        if event.name == "4":
            findFour()
        if event.name == "5":
            findFive()
        if event.name == "6":
            findSix()
        if event.name == "7":
            findSeven()
        if event.name == "8":
            findEight()
        if event.name == "shift":
            goLeft()
        if event.name == "right shift":
            goRight()
        if event.name == "space":
            reverse()

kb.on_press(on_press_reaction)

while True:
    pass

# while True:
#     try:
#         if kb.is_pressed("1"):
#             print("PRESS 1")
#             findOne()
#         if kb.is_pressed("2"):
#             print("PRESS 2")
#             findTwo()
#         if kb.is_pressed("3"):
#             print("PRESS 3")
#             findThree()
#         if kb.is_pressed("4"):
#             print("PRESS 4")
#             findFour()
#         if kb.is_pressed("5"):
#             print("PRESS 5")
#             findFive()
#         if kb.is_pressed("6"):
#             print("PRESS 6")
#             findSix()
#         if kb.is_pressed("7"):
#             print("PRESS 7")
#             findSeven()
#         if kb.is_pressed("8"):
#             print("PRESS 8")
#             findEight()
#         if kb.is_pressed("left shift"):
#             print("PRESS left")
#             goLeft()
#         if kb.is_pressed("right shift"):
#             print("PRESS right")
#             goRight()
#         if kb.is_pressed("space"):
#             print("PRESS space")
#             reverse()
        
#     except:
#         print("something broke")
        