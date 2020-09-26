import json
import requests
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Enter a keyword for the item (Nike is an example)
itm_name = 'Badge'

#Enter color for item
color = 'Blue'

#Enter size for item. Leave empty for an accessory with no sizes
size = ''

#Categories: Accessories, Hats, Pants, Sweatshirts, Shorts, Bags, Tops/Sweaters, Jackets, Shoes, Shirts
category = 'Accessories'

#Loads Supreme JSON website into an object
stock = requests.get("https://www.supremenewyork.com/mobile_stock.json").json() 
sesh = requests.Session()

#We only want to iterate through the necessary category to save time
items = stock["products_and_categories"][category]

#Finds the item_id to open the item's variants
item_id = 0

for index, item in enumerate(items, start=0):
        if(itm_name in items[index]["name"]):
                item_id = item['id']
                break

#Gets the item variants from the mobile website
item_variants = requests.get(f'https://www.supremenewyork.com/shop/{item_id}.json').json()

styles = item_variants['styles']
size_id = 0
style_id = 0

for sty in styles:
        if sty['name'] == color:
                sizes = sty['sizes']
                for siz in sizes:
                        if siz['name'] == size and size != '':
                                size_id = siz['id']
                                break
                        elif size == '':
                                size_id = siz['id']
                                break
                style_id = sty['id']
                break

atc_url = f"https://www.supremenewyork.com/shop/{item_id}/add.json"
headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.supremenewyork.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.supremenewyork.com/mobile/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
}

data = {
        "s": size_id,
        "st": style_id,
        "qty": "1" 
}

cookies = sesh.post(atc_url, headers=headers, data=data).cookies

option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.headless = True # Option to open up chrome in headless mode, better performance by an average of 3 sec.
driver = webdriver.Chrome(options=option)
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

driver.get('https://www.supremenewyork.com')
for x, y in zip(list(cookies.keys()), list(cookies.values())):
        driver.add_cookie({'name': x, 'value': y})

driver.get('https://www.supremenewyork.com/checkout')

#Fill info
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "order[billing_name]"))).send_keys('your_name')

#Enter email
driver.find_element_by_id('order_email').send_keys('your_email')

#Enter phone number
driver.execute_script("document.getElementById('order_tel').value = 'your_phone_number';")

#Enter street address
driver.find_element_by_id('bo').send_keys('your_street_address')

#Enter apartment number
driver.find_element_by_id('oba3').send_keys('your_apt_number')

#Enter zip code
driver.find_element_by_id('order_billing_zip').send_keys('your_zip')

#Enter city
driver.find_element_by_id('order_billing_city').send_keys('your_city')

#Choose State
driver.find_element_by_xpath("//select[@name='order[billing_state]']/option[text()='VA']").click()

#Enter credit card number
driver.execute_script("document.getElementById('rnsnckrn').value = 'your_card_number';")

#Select expiration month
driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='01']").click()

#Select expiration year
driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='2022']").click()

#Enter CVV
driver.find_element_by_id('orcer').send_keys('your_cvv')

#Find checkboxes
checks = driver.find_elements_by_class_name("icheckbox_minimal")
checks[1].click()

#Checkout
driver.find_element_by_xpath("//input[@value='process payment']").click()