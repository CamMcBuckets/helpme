from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html 
import requests 
from time import sleep 
import time 
import schedule 
import smtplib 

# Change This for your personal email.
amazon_email = "cameronmurillo@gmail.com"
amazon_password = "Alex2177"
browser  = webdriver.Chrome(ChromeDriverManager().install())
x = True
# Change this depending on which URL you want. 
browser.get('https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-tech-2-9-Slot/dp/B08J6F174Z?ref_=ast_sto_dp')
while(x==True):
    if(browser.find_element_by_id('outOfStock')):
        x = True
        browser.refresh()
        time.sleep(5)
    else:
        browser.find_element_by_id('buy-now-button').click()
        browser.find_element_by_id('ap_email').send_keys(amazon_email)
        browser.find_element_by_id('continue').click()
        browser.find_element_by_id('ap_password').send_keys(amazon_password)
        browser.find_element_by_id('signInSubmit').click()
        browser.find_element_by_name('placeYourOrder1').click()
