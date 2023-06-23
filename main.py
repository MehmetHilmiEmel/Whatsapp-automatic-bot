from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openai
import time
import random




def start():
    driver=webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get("https://web.whatsapp.com/")
    
    while True:
        try:
            qr_area=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div')
            time.sleep(2)
        except:
            message=driver.find_elements(By.XPATH," //span[@data-testid='icon-unread-count']")
            my=driver.find_elements(By.XPATH," //span[@data-testid='you-label']")
            for i in message:
                i.click()
                time.sleep(1)
                about=driver.find_elements(By.XPATH,"//*[@id='main']/header/div[2]/div[1]/div/span")
                about[0].click()
                time.sleep(2)
                wp_source=driver.page_source
                soup=bs(wp_source,"html.parser")
                grup=soup.find('span',{'class':['enbbiyaj','e1gr2w1z','hp667wtd']})
                print(grup.text)
                if "Grup" in grup.text:
                    time.sleep(2)
                    my[0].click()
                    time.sleep(2)
                else:
                    close=driver.find_element(By.XPATH,"//*[@id='app']/div/div/div[6]/span/div/span/div/header/div/div[1]/div/span")
                    close.click()
                    time.sleep(2)
                    

                    name=driver.find_element(By.XPATH," //span[@data-testid='conversation-info-header-chat-title']")
                    print(name.text)
                    
                    wp_source=driver.page_source
                    soup=bs(wp_source,"html.parser")
                    time.sleep(2)
                    okunmamis=soup.find_all('span',{'class':'_2jRew'})
                    print(okunmamis[-1].text)
                    
                    if "okunmamış" in okunmamis[-1].text:
                        time.sleep(2)
                        message_list = driver.find_elements(By.XPATH,'.//div[@class="copyable-text"]')[-5:]
                        
                        ####################
                        # my_messages = []
                        # friend_messages = []
                        total_messages=[]
                        #total_messages="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. AI's name is Hilmi."
                        for message in message_list:
                            message_classes = message.get_attribute("data-pre-plain-text")
                            print(message_classes)
                            system={"role": "system", "content": "I am Hilmi Emel's chatbot. He is not in here right now. I am the only one in here. Hilmi Emel is 22 years old. He studies computer science at Bahcesehir University."}
                            if "Mehmet Hilmi Emel" in message_classes:
                                # Message was sent by your friend
                                
                                try:
                                    text = message.find_element(By.XPATH,'.//span[contains(@class, "selectable-text")]')
                                    print(text.text)
                                    my_messages=text.text
                                    # friend_messages.append(""+text.text)
                                    me_dict={"role":"assistant","content":my_messages}
                                    total_messages.append(me_dict)
                                except:
                                    print("")
                            else:
                                # Message was sent by you
                                try:
                                    text = message.find_element(By.XPATH,'.//span[contains(@class, "selectable-text")]')
                                    print(text.text)
                                    friend_messages=text.text
                                    friend_dict={"role":"user","content":text.text}
                                    total_messages.append(friend_dict)
                                except:
                                    print("")
                                # my_messages.append(text.text)
                        # print(my_messages)
                        # print(friend_messages)
                        total_messages.insert(0, system)
                        print(total_messages)
                        # Determine the latest message
                        # if len(friend_messages) > 0:
                        #     latest_message = friend_messages[-1]
                        # elif len(my_messages) > 0:
                        #     latest_message = my_messages[-1]
                        # else:
                        #     latest_message = ""
                            
                        # if latest_message != "":
                        openai.api_key = "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"
                        while True:
                            try:
                            # messages = [
                            # {"role": "system", "content": text},
                            # ]

                                model = "gpt-3.5-turbo-0301"
                                response_open = openai.ChatCompletion.create(
                                model=model,
                                messages=total_messages,
                                temperature=0.9,
                                max_tokens=3000
                                )

                        # Start conversation with chatbot
                                text_gpt=response_open["choices"][0]["message"]["content"]
                                
                                print(text_gpt)
                                time.sleep(1)
                                message_area=driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
                                message_area.click()
                                message_area.send_keys(text_gpt)
                                message_area.send_keys(Keys.ENTER)
                                break
                            except:
                                time.sleep(1)
                        # else:
                        #     print("tatest message is naot emoty")

                        # for message in message_list:
                        #     text = message.find_element(By.XPATH,'.//span[contains(@class, "selectable-text")]')
                        #     print(text.text)


                    # wp_source=driver.page_source
                    # soup_end=bs(wp_source,"html.parser")
                    # search=soup_end.find_all('span',{'class':['_11JPr','selectable-text', 'copyable-text']})
                    # last_five_messages=search[-5:]
                    # prompt_string=""
                    # for i in last_five_messages:
                        
                    #     ##### buraya kod eklenecek
                    
                    # son_tweet=search[-1].find_all('span')[0].text
                    # text=son_tweet

                    # print(text)
                    # while True:
                    #     try:
                    #         messages = [
                    #         {"role": "system", "content": text},
                    #         ]

                    #         model = "gpt-3.5-turbo-0301"
                    #         response_open = openai.ChatCompletion.create(
                    #         model=model,
                    #         messages=messages,
                    #         temperature=0,
                    #         )

                    #         # Start conversation with chatbot
                    #         text_gpt=response_open["choices"][0]["message"]["content"]
                            
                    #         print(text_gpt)
                    #         time.sleep(1)
                    #         message_area=driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
                    #         message_area.click()
                    #         message_area.send_keys(text_gpt)
                    #         message_area.send_keys(Keys.ENTER)
                    #         break
                    #     except:
                    #         time.sleep(1)
                        time.sleep(2)
                        my[0].click()
                        message_area=driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
                        message_area.click()
                        message_area.send_keys(text_gpt)
                        message_area.send_keys(Keys.ENTER)
                    else:
                
                        wp_source=driver.page_source
                        soup=bs(wp_source,"html.parser")
                        search=soup.find_all('span',{'class':['_11JPr','selectable-text', 'copyable-text']})
                        print(search)
                        son_tweet=search[-1].find_all('span')[0].text
                        text=son_tweet

                        print(text)
            my
            print("you entered qr code")
            time.sleep(2)                         
                        

                


    
start()