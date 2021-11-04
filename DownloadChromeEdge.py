from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import subprocess
import os
import time

if __name__ == '__main__':

    browser = webdriver.Edge(r"C:\Users\fxavier\selenium\msedgedriver.exe")

    browser.maximize_window()
    browser.get('https://www.google.com/intl/pt-BR/chrome/')
    browser.find_element_by_id("js-stats-cb-sdf-win64").click()
    browser.find_element_by_id("js-download-hero").click()
    time.sleep(5)

    username = os.getlogin()
    os.startfile("C:\\Users\\" + username + "\\Downloads\\ChromeSetup.exe")

    time.sleep(2)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

    browser.get('https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR')