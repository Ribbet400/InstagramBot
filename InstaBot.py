rom selenium import webdriver
from time import sleep

username = 'username'
password = 'password'

usenameBox = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
passwordBox = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
button1 = '/html/body/div[2]/div/div/div/div[2]/button[1]'
button2 = '/html/body/div[1]/section/main/div/div/div/div/button'
button3 = '/html/body/div[5]/div/div/div/div[3]/button[2]'

def Login(username, password):

	browser.find_element_by_xpath(button1).click()

	sleep(3)

	browser.find_element_by_xpath(usenameBox).send_keys(username)
	browser.find_element_by_xpath(passwordBox).send_keys(password)
	browser.find_element_by_xpath('//button[@type = "submit"]').click()

	sleep(5)

	browser.find_element_by_xpath(button2).click()

	sleep(5)

	browser.find_element_by_xpath(button3).click()
	


browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
sleep(3)
Login(username, password)
sleep(3)
browser.close()
