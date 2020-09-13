# BOT INFO
Every Thursday, Supreme releases new items on their website at 11 am EST.
The purpose of this script is to checkout items quickly and automatically from www.supremenewyork.com after they release.

This bot was coded in python using Selenium Webdriver and requests.

How it works:
  The code is pretty self explanitory if you look at it. Even though none of these methods are a secret, I don't want them to change the way they add items to cart.

In the future I want to figure out a way to bypass captcha.


## HOW TO RUN
1) Create a new local directory and clone this repo into it
2) cd into that directory and run:
'''
python3 -m pip install -r requirements.txt
'''
3) Change your info inside of the supbot2.py for checkout and item finding
4) On the command line run
'''
python3 supbot2.py
'''
5) After the bot clicks process payment, solve the captcha manually
6) Enjoy :)

**CURRENTLY CANNOT PASS CAPTCHA. SOLVE MANUALLY**
