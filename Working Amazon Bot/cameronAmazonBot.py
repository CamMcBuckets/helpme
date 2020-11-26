from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Change This for your personal email.
amazon_email = "cameronmurillo@gmail.com"
amazon_password = "Alex2177"

browser  = webdriver.Chrome(ChromeDriverManager().install())

# Change this depending on which URL you want. 
browser.get('https://www.amazon.com/Ruputas-Precision-Screwdriver-Rechargeable-Electronics/dp/B07DB7ZT5P/ref=sr_1_3?dchild=1&keywords=wowstick+screw&psr=EY17&qid=1606393075&s=black-friday&sr=1-3')
browser.find_element_by_id('buy-now-button').click()


browser.find_element_by_id('ap_email').send_keys(amazon_email)
browser.find_element_by_id('continue').click()

browser.find_element_by_id('ap_password').send_keys(amazon_password)
browser.find_element_by_id('signInSubmit').click()

#browser.find_element_by_name('placeYourOrder1').click()
