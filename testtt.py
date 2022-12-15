import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

pyautogui.size()
pyautogui.position()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("https://twitter.com/login")

time.sleep(5)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("willbechong@yahoo.com")
time.sleep(1)
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Далее')]")
next_button.click()
time.sleep(1)

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("willbechong")
log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Далее')]")
log_in.click()
time.sleep(1)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('9nzgG9U8Ea2')
log = driver.find_element(By.XPATH, "//span[contains(text(),'Войти')]")
log.click()
time.sleep(3)
search_box = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
search_box.send_keys("ZakzyNFT")
time.sleep(4)
search_boxing = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[4]/div/div/span").click()
time.sleep(4)
send_message = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]").click()
time.sleep(4)
pyautogui.moveTo(800, 1000, duration=1)

