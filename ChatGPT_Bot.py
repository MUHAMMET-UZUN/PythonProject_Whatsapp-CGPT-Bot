import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from selenium.webdriver.common.by import By

mouse = Controller()

class ChatGPT:

    #Defines the starting values
    def __init__(self, speed = .5,click_speed = .3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def nav_message_box(self):
        try:
            position = pt.locateOnScreen('cgpt_send_button.png',confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100,20, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ',e)

    def create_new_chat(self):
        #position = pt.locateOnScreen('cgpt_stop_generating_button.png', confidence=.9)
        #pt.moveTo(position[0:2], duration=self.speed)
        pt.moveRel(-100, 120, duration=self.speed)
        pt.doubleClick(interval=self.click_speed)

    def solve_message(self,input_message):
        try:
            print("You say: ", input_message)
            pt.typewrite(input_message+" sadece bir paragrafta yaz",interval=0)
            pt.typewrite("\n")
            sleep(1)
            #Son mesajın ayarlanması / Assign last message
            self.last_message = self.message
        except Exception as e:
            print("Exception (solve_message): ",e)

    def nav_message(self):
        position = pt.locateOnScreen('cgpt_like_button.png', confidence=.9)
        pt.moveTo(position[0:2], duration=self.speed)
        pt.moveRel(-100,20, duration=self.speed)

    def save_result(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 10, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message = pc.paste()
        print('ChatGPT says: ', self.message)

    def check_message_is_answered(self):
        while True:
            try:
                position = pt.locateOnScreen('cgpt_send_button.png',confidence=.9)
                print("position::",position)
                if position:
                    break

            except Exception as e:
                print('Exception (check_message_is_answered): ', e)
                print("In progress...")
                continue
        return True

    def nav_whatsapp_tab(self):
        try:
            position = pt.locateOnScreen('cgpt_https_icon.png', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-10, -25, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception (nav_whatsapp_tab): ",e)