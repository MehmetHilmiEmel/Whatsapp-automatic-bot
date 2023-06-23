from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Set up Selenium web driver
driver = webdriver.Chrome() # Change this to the location of your web driver executable

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')
print('Please scan the QR code and wait for WhatsApp to load...')

# Wait for user to scan QR code and load WhatsApp Web
while True:
    try:
        chat_list = driver.find_element(By.XPATH,'//div[@class="_1eFbz"]')
        break
    except:
        time.sleep(1)

# Click on the latest chat
latest_chat = chat_list.find_elements(By.XPATH,'.//div[contains(@class, "DP7CM")]')[0]
latest_chat.click()

# Wait for chat window to load
while True:
    try:
        chat_window = driver.find_element(By.XPATH,'//div[contains(@class, "_2kHpK")]')
        break
    except:
        time.sleep(1)

# Scroll to the top of the chat window
chat_window.click()
chat_window.send_keys(u'\ue011')
time.sleep(1)

# Read the last 5 messages
message_list = chat_window.find_elements(By.XPATH,'.//div[@class="copyable-text"]')[-5:]
for message in message_list:
    text = message.find_element(By.XPATH,'.//span[contains(@class, "selectable-text")]')
    print(text.text)

# Close the driver
driver.quit()
