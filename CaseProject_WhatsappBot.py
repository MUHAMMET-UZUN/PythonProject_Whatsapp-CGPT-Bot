import requests
from bs4 import BeautifulSoup
#!/usr/bin/env python
# -*- coding: latin-1 -*-
from WhatsappBot import WhatsApp
from time import sleep


wp_bot = WhatsApp(speed=.1,click_speed=.4)
sleep(2)


print("\n\nProgramın dosya konumuna gidip gerekli olan butonların ss'ini alıp\nüzerlerine kaydederek kendi whatsapp'ınıza uyumlu hale getirebilirsiniz")
input("\n\tEğer ayarları değiştirmek istemiyorsanız"
      "\n\tDefault ayarlar"
      "\n\tWhatsapp'ı web sürümünde ve TAM EKRAN kullanmak."
      "\n\tKARANLIK TEMAYA geçirmek ZORUNDASINIZ"
      "\n\n\tWhatsApp kurulumundan sonra Enter\'a basınız ve programı aşağı alıp whatsapp'a geçiniz.")

"""url = "https://chat.openai.com/chat"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
h1 = soup.find('h1').text
print(h1)

"""

while True:
    wp_bot.nav_green_dot()
    wp_bot.nav_x()
    wp_bot.nav_message()
    wp_bot.get_message()
    #sekme değiştirmeliyiz
    #wp_bot.solve_message()
    wp_bot.nav_input_box()
    wp_bot.send_message()

    sleep(10)


