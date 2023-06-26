import os

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pymsgbox as pg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

username = "amirsdream@hotmail.com"
passwd = "Amiramir1366"
#driverpth = "/usr/lib64/chromium"
# exit()
option = webdriver.ChromeOptions()
#option.binary_location = driverpth
option.add_argument("--incognito")
option.add_argument("--disable-notifications")
option.add_argument("disable-infobars")
option.add_experimental_option('excludeSwitches', ['enable-logging'])  #
#option.add_argument("--headless")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                           options=option)
browser.maximize_window()
browser.get("https://instagram.com")
time.sleep(5)
browser.find_element(
    By.XPATH, "//button[normalize-space()='Allow all cookies']").click()
time.sleep(10)
browser.find_element(By.NAME, "username").send_keys(username)
browser.find_element(By.NAME, 'password').send_keys(passwd)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(100)
browser.get(f'https://instagram.com/{username}')
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, '[aria-label="New post"]').click()

# To Stop until Loaded

# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, “input[name=’username’]”)))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
# document.getElementsByTagName("input")[3].value
browser.find_element(
    By.XPATH,
    '//*[@id="mount_0_0_AM"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/form/input'
).send_keys("test.jpeg")

time.sleep(200)

browser.find_element(
    By.XPATH,
    "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
).click()

time.sleep(2)

browser.find_element(
    By.XPATH,
    "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
).click()

time.sleep(2)

browser.find_element(
    By.XPATH,
    "/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea"
).send_keys("test desc")

time.sleep(2)

browser.find_element(
    By.XPATH,
    "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button"
).click()

time.sleep(2)
ImageUploaded = False
while ImageUploaded == False:
    try:
        myElem = browser.find_element(
            By.XPATH,
            "/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/img"
        ).click()
        ImageUploaded = True
    except:
        time.sleep(5)
        ImageUploaded = False
time.sleep(5)
