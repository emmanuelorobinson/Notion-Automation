from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect

chromedriver = #Chrome web driver loacation
browser = webdriver.Chrome()
browser.get('http:\\notion.so\login')

def create():
    username = WebDriverWait(browser, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter your email address...']")))

    username.send_keys('enter your email')

    username = browser.find_element(By.XPATH,"//div[@style='user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; white-space: nowrap; height: 36px; border-radius: 3px; color: rgb(235, 87, 87); font-size: 14px; line-height: 1; padding-left: 12px; padding-right: 12px; font-weight: 500; background: rgb(253, 245, 242); box-shadow: rgba(15, 15, 15, 0.1) 0px 1px 2px, rgba(235, 87, 87, 0.3) 0px 0px 0px 1px inset; margin-top: 6px; margin-bottom: 12px; width: 100%;']" )
    username.click()

    username = WebDriverWait(browser, 120, 1).until(
        expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter your password...']")))

    username.send_keys('enter your password')
    username = browser.find_element(By.XPATH,
                                    "//div[@style='user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; white-space: nowrap; height: 36px; border-radius: 3px; color: rgb(235, 87, 87); font-size: 14px; line-height: 1; padding-left: 12px; padding-right: 12px; font-weight: 500; background: rgb(253, 245, 242); box-shadow: rgba(15, 15, 15, 0.1) 0px 1px 2px, rgba(235, 87, 87, 0.3) 0px 0px 0px 1px inset; margin-top: 6px; margin-bottom: 12px; width: 100%;']")
    username.click()

    username = browser.find_element(By.XPATH,
                                    "//div[@style='position: absolute; pointer-events: none; top: 0px; left: 0px; right: 0px; bottom: 0px; background: rgba(46, 170, 220, 0.2); z-index: 81; opacity: 1;']")
    username.click()


create()