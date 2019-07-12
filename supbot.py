import selenium
import json
import urllib2
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#Loads Supreme JSON website into an object
url = urllib2.urlopen('https://www.supremenewyork.com/mobile_stock.json')
obj = json.load(url)

#Categories: Accessories, Hats, Pants, Sweatshirts, Shorts, Bags, Tops/Sweaters, Jackets, Shoes, Shirts
items = obj["products_and_categories"]["Bags"]

itm_name = "Nike"

index = 0;
for i in items:
        if(itm_name in items[index]["name"]):
                found_url = i["image_url"]
                break
        index += 1

link = found_url.replace("ca","vi")

#Using Google Chrome to access web
driver = webdriver.Safari()

#Open the website
driver.get('https://www.supremenewyork.com/shop/all')

#Find item
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='inner-article']/a/img[@src='{}']".format(link)))).click()

#Select color - NOT ALWAYS NEEDED
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-style-name='Silver']"))).click()

#Select size - NOT ALWAYS NEEDED
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='s']/option[text()='Large']"))).click()

#Add to cart
time.sleep(.5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "commit"))).click()

#Checkout
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "checkout now"))).click()

#Fill info
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "order[billing_name]"))).send_keys('Nicolas Pavlakovic')

#Enter email
driver.find_element_by_id('order_email').send_keys('nicolaspav@comcast.net')

#Enter phone number
driver.find_element_by_id('order_tel').send_keys('7085228849')

#Enter street address
driver.find_element_by_id('bo').send_keys('220 Northwood Rd')

#Enter apartment number
#driver.find_element_by_id('oba3').send_keys('Apt 304')

#Enter zip code
driver.find_element_by_id('order_billing_zip').send_keys('60546')

#Enter city
driver.find_element_by_id('order_billing_city').send_keys('Riverside')

#Choose State
driver.find_element_by_xpath("//select[@name='order[billing_state]']/option[text()='IL']").click()

#Enter credit card number
driver.find_element_by_id('nnaerb').send_keys('4599540662281454')

#Select expiration month
driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='03']").click()

#Select expiration year
driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='2024']").click()

#Enter CVV
driver.find_element_by_id('orcer').send_keys('550')

#Find checkboxes
checks = driver.find_elements_by_class_name("icheckbox_minimal")
checks[1].click()

#Checkout
#driver.find_element_by_xpath("//input[@value='process payment']").click()
