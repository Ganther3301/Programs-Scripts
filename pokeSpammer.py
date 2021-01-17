import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os, shutil

driver = webdriver.Firefox()

driver.get("https://discord.com/login")
time.sleep(6)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 
username = 'Enter username here	'
password = 'Enter password here'

# Copy the URL of channel where you wanna send messages and paste below
channelURL = ""

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email
username_input = driver.find_element_by_name('email')
username_input.send_keys(username)

# Initialize and input password
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

# Initialize and login
login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login_button.click()
print(">>Login Complete!")
time.sleep(10)

driver.get(channelURL)
print(">Opening The Server Link...")
time.sleep(5)

# Msg Sending
i = 0
while(True):
	time.sleep(1)
	msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div') 
	msg_input.click()
	actions = ActionChains(driver)
	actions.send_keys("Enter the message")
	actions.send_keys(Keys.ENTER) 
	actions.perform()
	i += 1 
	print(">Number of Messages sent: "+str(i)) 

print("Its Done!")
