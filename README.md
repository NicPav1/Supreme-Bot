# bot
Every Thursday, Supreme releases new items on their website at 11 am EST.
The purpose of this script is to checkout items quickly and automatically from www.supremenewyork.com after they release.

This bot was coded in python using Selenium Webdriver.

How it works:
1) The bot connects to https://www.supremenewyork.com/mobile_stock.json where Supreme keeps a list of its in-stock items in      JSON format.
2) The bot parses through the JSON and finds the desired item based on user keyword input.
3) The bot navigates through the steps of finding the item on the website, adding to cart, clicking checkout, inputting all user information into the text fields, agreeing to the terms of agreement, and finally purchasing.

In the future I want to make the bot faster by using requests instead of web automation.
