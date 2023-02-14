from ChatGPT_Bot import ChatGPT
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
    #cgptBot.save_result()
    cgptBot.nav_whatsapp_tab()
