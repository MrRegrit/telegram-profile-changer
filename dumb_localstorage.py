import json
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from local_storage import LocalStorage

url = "https://web.telegram.org/a/"

account_name = input('Inter name:')

ua = UserAgent()
user_agent = ua.random

opts = webdriver.ChromeOptions()
opts.add_argument(f"user-agent={user_agent}")
opts.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=opts)

ls = LocalStorage(driver)

print('Program start...')

driver.get(url)

print('Opened url...')

time.sleep(30)

with open(f'data_{account_name}.json', 'w') as file:
    json.dump(ls.items(), file)

print('File saved...')
