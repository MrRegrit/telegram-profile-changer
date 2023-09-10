import json
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from local_storage import LocalStorage

time_zone = 7

datafile_name = input('Inter file name: ')

url = "https://web.telegram.org/a/"

ua = UserAgent()
user_agent = ua.random

service = Service('/tg_bot/chromedriver')

opts = webdriver.ChromeOptions()
opts.add_argument(f"user-agent={user_agent}")
opts.add_argument('--no-sandbox')
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)

ls = LocalStorage(driver)

print('Program start...')

driver.get(url)

print('Opened url...')

time.sleep(3)

with open(f'{datafile_name}', 'r') as file:
    for key, value in json.load(file).items():
        ls.set(key, value)

driver.refresh()

print('Data loaded...')

time.sleep(5)

driver.find_element(By.CLASS_NAME, 'ripple-container').click()

time.sleep(5)

driver.find_elements(By.CSS_SELECTOR, '.MenuItem.compact')[3].click()

time.sleep(5)

driver.find_elements(By.CSS_SELECTOR, '.Button.smaller.translucent.round')[2].click()

time.sleep(5)

time_to_print = ''

print('Setting opened...')

while True:
    hours = str(time.gmtime().tm_hour + time_zone - (24 if time.gmtime().tm_hour + time_zone >= 24 else 0))
    if len(hours) == 1:
        hours = '0' + hours
    minutes = str(time.gmtime().tm_min)
    if len(minutes) == 1:
        minutes = '0' + minutes
    new_time = hours + ':' + minutes
    if new_time != time_to_print:
        time_to_print = new_time
        textarea = driver.find_elements(By.CSS_SELECTOR, '.form-control')[3]

        textarea.clear()
        textarea.send_keys(time_to_print)

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'Button.FloatingActionButton.revealed.default.primary.round').click()

        time.sleep(1)

        print('Time changed...')

    time.sleep(1)
