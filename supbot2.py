import selenium
import json
from urllib.request import urlopen
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from termcolor import colored
import sys

#Enter a keyword for the item (Nike is an example)
itm_name = 'Camo'

#Enter color for item
color = 'Royal'

#Enter size for item
size = 'Medium'

#Loads Supreme JSON website into an object
url = "https://www.supremenewyork.com/mobile_stock.json"
headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
}
obj = requests.get(url, headers=headers).json() 
sesh = requests.Session()

#Categories: Accessories, Hats, Pants, Sweatshirts, Shorts, Bags, Tops/Sweaters, Jackets, Shoes, Shirts
items = obj["products_and_categories"]["Shirts"]

index = 0
item_id = 0
for i in items:
        if(itm_name in items[index]["name"]):
                found_url = i["image_url"]
                item_id = i['id']
                break
        index += 1

#link = found_url.replace("ca","vi")
item_variants = requests.get(f'https://www.supremenewyork.com/shop/{item_id}.json').json()

#obj2 = json.load(url2)
styles = item_variants['styles']
size_id = 0
style_id = 0

for s in styles:
        if s['name'] == color:
                sizes = s['sizes']
                style_id = s['id']

for s in sizes:
        if s['name'] == size:
                size_id = s['id']


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

atc_post = sesh.post(atc_url, headers=headers, data=data)
cookies = atc_post.cookies
if atc_post.json():
        if atc_post.json()['cart'][0]["in_stock"]:
                print(colored("Added to Cart", "blue"))

driver = webdriver.Chrome()
driver.get('https://www.supremenewyork.com')
for x, y in zip(list(cookies.keys()), list(cookies.values())):
        driver.add_cookie({'name': x, 'value': y})

driver.get('https://www.supremenewyork.com/checkout')

#Fill info
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "order[billing_name]"))).send_keys('your_name')

#Enter email
driver.find_element_by_id('order_email').send_keys('your_email')

#Enter phone number
driver.find_element_by_id('order_tel').send_keys('your_phone_number')

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
driver.find_element_by_id('rnsnckrn').send_keys('your_card_number')

#Select expiration month
driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='01']").click()

#Select expiration year
driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='2022']").click()

#Enter CVV
driver.find_element_by_id('orcer').send_keys('your_cvv')

#Find checkboxes
#checks = driver.find_elements_by_class_name("icheckbox_minimal")
#checks[1].click()

#Checkout
#driver.find_element_by_xpath("//input[@value='process payment']").click()