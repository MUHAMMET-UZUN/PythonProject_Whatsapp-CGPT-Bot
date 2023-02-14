from ChatGPT_Bot import ChatGPT
import pyautogui as pt
from time import sleep

cgptBot = ChatGPT(speed=.1,click_speed=.4)
sleep(2)

def response(input_message):
    message = input_message.lower()

    cgptBot.create_new_chat()
    cgptBot.nav_message_box()
    cgptBot.solve_message(message)
    while True:
        if cgptBot.check_message_is_answered():
            break
    cgptBot.nav_message()
    cgptBot.save_result()
    cgptBot.nav_whatsapp_tab()

def nav_whatsapp_tab(speed,click_speed):
    try:
        position = pt.locateOnScreen('cgpt_https_icon.png', confidence=.9)
        pt.moveTo(position[0:2], duration=speed)
        pt.moveRel(-10, -25, duration=speed)
        pt.doubleClick(interval=click_speed)
    except Exception as e:
        print("Exception (nav_whatsapp_tab): ", e)