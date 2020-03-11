from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()


	def closeBroswer(self):
		self.driver.close()

		
	def login(self):
		driver = self.driver
		driver.get("https//www.instagram.com")
		time.sleep(2)

		login_button = driver.find_get_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)

		username_input = driver.find_get_element_by_xpath("//input[@name='username']")
		username_input.clear()
		username_input.send_keys(self.username)

		password_input = driver.find_get_element_by_xpath("//input[@name='password']")
		password_input.clear()
		password_input.send_keys(self.password)
		password_input.send_keys(keys.RETURN)
		time.sleep(2)


	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
		time.sleep(2)
		for i in range(1, 3):
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			time.sleep(2)

		hrefs = driver.find_elements_by_tag_name("a")
		pic_hrefs = [elem.get_atribute("href") for elem in hrefs]
		pic_hrefs = [href for href in pic_hrefs if hashtag in href]

if __main__ == '__name__':
	user_insta = InstagramBot("username", "password")
	user_insta.login() 
	user_insta.like_photo("nudes")
