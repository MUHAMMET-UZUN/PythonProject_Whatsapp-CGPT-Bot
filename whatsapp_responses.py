from ChatGPT_Bot import ChatGPT
from time import sleep

cgptBot = ChatGPT(speed=.1,click_speed=.4)
sleep(2)

def response(input_message):
    message = input_message.lower()

    cgptBot.nav_message_box()
    cgptBot.solve_message(message)
    cgptBot.check_message_is_answered()

    """
    if message == 'merhaba':
        return 'Merhaba.'
    elif message == 'say my name':
        return 'Heisenberg.'
    elif message == 'mal':
        return 'Ayib.'
    elif message == 'naber':
        return 'Eh iste 0101 yasiyoruz.'
    elif message == 'selam':
        return 'selam naber?'
    elif message == 'iyi' or message == 'ıyi' or message == 'ıyı' or message == 'İyi':
        return 'Guzel.'
"""