import requests
from bs4 import BeautifulSoup
#!/usr/bin/env python
# -*- coding: latin-1 -*-
from WhatsappBot import WhatsApp
from time import sleep


wp_bot = WhatsApp(speed=.1,click_speed=.4)
sleep(2)

print("""
-TR-
    Programın dosya konumuna gidip gerekli olan butonların ekran görüntüsünü alıp
    üzerlerine kaydederek kendi whatsapp'ınıza uyumlu hale getirebilirsiniz
    
        Eğer ayarları değiştirmek istemiyorsanız
        Varsayılan ayarlar:
        Whatsapp'ı web sürümünde ve PENCERELİ TAM EKRAN kullanmak.
        KARANLIK TEMAYA geçirmek ZORUNDASINIZ
        
    ChatGPT için sadece yazmaya hazır hale getirmeniz yeterli
        
-EN-
    Go to the file location of the program and take a screenshot of the necessary buttons.
    You can make them compatible with your own whatsapp by saving them on
    
        If you do not want to change the settings
        Default settings:
        Using Whatsapp in web version and FULL SCREEN WITH WINDOW.
        YOU MUST switch to DARK THEME
        
    For ChatGPT, you just have to get it ready to write
""")

input("\n\n\tWhatsApp ve ChatGPT kurulumundan sonra Enter\'a basınız ve programı aşağı alıp tarayıcıya geçiniz."
      "\n\t")

while True:
    wp_bot.nav_green_dot()
    wp_bot.nav_x()
    wp_bot.nav_message()
    wp_bot.get_message()
    #sekme değiştirmeliyiz/need to change tab to cgpt
    wp_bot.nav_cgpt_tab()
    wp_bot.solve_message()
    wp_bot.nav_input_box()
    wp_bot.send_message()

    sleep(10)


