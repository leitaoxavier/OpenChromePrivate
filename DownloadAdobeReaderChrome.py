from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://get.adobe.com/br/reader/')

time.sleep(3)

#  pesquisar = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#  pesquisar.send_keys('download adobe reader dc')
#  pesquisar.submit()

#  driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a/h3')

driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[3]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/div[2]/div[1]/div[1]/div[3]/label/strong').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/section/div/div[3]/div[2]/div[1]/div[2]/div[2]/p[1]/a').click()

driver.execute_script('window.open("https://www.google.com", "_blank")')