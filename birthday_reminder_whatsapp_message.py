import pyautogui
import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/chriskreienkamp/Python/automation/chromedriver')
driver.get('https://web.whatsapp.com/')
chat_search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
chat_search.send_keys('Chris Kreienkamp')




# os.system('open /Applications/WhatsApp.app')

# location = None
# imageFile = 'image.png'
# print('1')

# while (location == None):
#     try:
#         print('2')
#         location = pyautogui.locateCenterOnScreen(imageFile)
#     except Exception as e:
#         print('3')
#         print(e)

# print('4')

# pyautogui.hotkey('command','n')
# time.sleep(0.5)
# pyautogui.write('Chris Kreienkamp\n')
# pyautogui.write('first message\n')