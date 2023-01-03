import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

pyautogui.size()
pyautogui.position()

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
driver.set_window_size(1920, 1080)
time.sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("willbechong@yahoo.com")
time.sleep(1)
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()
time.sleep(1)
proverka = driver.find_element(By.XPATH, "//input[@name='text']")
proverka.send_keys('willbechong')
time.sleep(1)
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()
time.sleep(1)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('9nzgG9U8Ea2')
time.sleep(1)
log = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log.click()
time.sleep(3)
search_box = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")


class TwitterSpamer:
    def spamer(self):
        file = open("fsf.txt", "r", encoding='utf-8')
        peoples = file.readlines()
        for people in peoples:
            user = people.split('/')[-1]
            search_box = driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
            search_box.send_keys(f'{user.strip()}')
            time.sleep(4)
            search_boxing = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div/div/div/div[2]').click()
            time.sleep(4)

            send_message = driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]").click()

            time.sleep(4)
            pyautogui.moveTo(1220, 1050, duration=1)
            pyautogui.click()
            pyautogui.write('Hey')
            pyautogui.press('enter')
            nazad = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div/div[2]/span').click()
            continue


