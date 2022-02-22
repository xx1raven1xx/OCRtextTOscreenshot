import pytesseract
from PIL import ImageGrab
import keyboard
import pyautogui

'''Данный скрипт работает только на основном экране. На дополнительном мониторе не определяется картинка(походу не работает ImageGrab)'''

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
global X1, Y1, X2, Y2

def GetCoord1():
    '''Читаем координаты левого верхнего угла'''
    global X1, Y1
    X1, Y1 = pyautogui.position()

def GetCoord2():
    '''Читаем координаты правого нижнего угла'''
    global X2, Y2
    X2, Y2 = pyautogui.position()


def pic():
    '''Читаем координаты и сразу определяем что написанно'''
    GetCoord2()
    global X1, Y1, X2, Y2
    bbox = (X1, Y1, X2, Y2)
    im = ImageGrab.grab(bbox)
    # im.show()
    rus_string = pytesseract.image_to_string(im, lang='rus')
    print(rus_string)

'''По данным горячим клавишам мы производим действия'''
keyboard.add_hotkey('Ctrl + 1', GetCoord1)
keyboard.add_hotkey('Ctrl + 2', pic)

keyboard.wait('Ctrl + Q')