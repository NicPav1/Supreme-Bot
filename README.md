# BOT INFO
Every Thursday, Supreme releases new items on their website at 11 am EST.
The purpose of this script is to checkout items quickly and automatically from www.supremenewyork.com after they release.

This bot was coded in python using Selenium Webdriver and requests.

How it works:
  1) The script gets Supreme's stock from https://www.supremenewyork.com/mobile_stock.json
  2) The script finds the desired item in the json stock list.
  3) The script makes a request to Supreme's mobile website to add the desired item to the cart.
  4) The script opens a Google Chrome instance with the desired item already in cart, and it navigates through the checkout process.
  5) Sometimes captcha doesn't appear because I disabled the Automation Controlled flag. If it does appear, the user has to manually solve the captcha.

## Future Improvements
1) I would like the bot to be able to bypass captcha 100% of the time.
2) I would like the bot to support threads so that multiple items can be purchased at once.
3) I would like the user to be able to start the bot in advance; currently you have to start the bot once the website goes live.
4) I would like the bot to re-run itself if there are errors in finding the item or checking out.


## HOW TO RUN
1) Create a new local directory and clone this repo into it
2) cd into that directory and run:
```
python3 -m pip install -r requirements.txt
```
3) Change your info inside of the supbot2.py for checkout and item finding
4) On the command line run
```
python3 supbot2.py
```
5) After the bot clicks process payment, solve the captcha manually
6) Enjoy :)

**CURRENTLY CANNOT PASS CAPTCHA. SOLVE MANUALLY**
