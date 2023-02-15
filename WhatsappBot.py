import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response
from whatsapp_responses import nav_whatsapp_tab

mouse = Controller()

class WhatsApp:

    #Defines the starting values
    def __init__(self, speed = .5,click_speed = .3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png',confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100,0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ',e)


    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png',confidence = .7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100,10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ',e)

    def nav_message(self):
        try:
            position = pt.locateOnScreen('paperclip.png',confidence = .9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10,-60, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message): ',e)

    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10,-160,duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message = pc.paste()
        print('User says: ',self.message)

    def solve_message(self):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print("You say: ", bot_response)

                pt.typewrite(bot_response,interval=.1)
                #pt.typewrite("\n")

                #Son mesajın ayarlanması
                self.last_message = self.message
            else:
                nav_whatsapp_tab(self.speed,self.click_speed)
                print("No new messages...")
        except Exception as e:
            print("Exception (solve_message): ",e)

    def nav_cgpt_tab(self):
        try:
            position = pt.locateOnScreen('cgpt_tab_icon.png', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(30, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception (nav_cgpt_tab): ",e)

    def send_result(self):
        try:
            if self.message != self.last_message:

                #position = pt.locateOnScreen('paperclip.png', confidence=.9)
                #pt.moveTo(position[0:2], duration=self.speed)
                #pt.moveRel(10, -60, duration=self.speed)
                #pt.doubleClick(interval=self.click_speed)

                print("You say: ", self.message)

                pt.typewrite(self.message,interval=0)
                pt.typewrite("\n")

                #Son mesajın ayarlanması / Assign last message
                self.last_message = self.message
            else:
                print("No new messages...")
        except Exception as e:
            print("Exception (send_message): ",e)

    def take_result(self):
        self.message = pc.paste()

    def nav_x(self):
        try:
            position = pt.locateOnScreen('x.png',confidence = .9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10,10, duration=self.speed)
            mouse.click(Button.left,1)
        except Exception as e:
            print('Exception (nav_x): ',e)
