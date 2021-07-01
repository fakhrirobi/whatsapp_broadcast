import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException,InvalidArgumentException
from time import sleep 
import os 



current_path = os.getcwd()
webdriver_path = os.path.join(current_path,'chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')

WEBDRIVER = webdriver.Chrome(webdriver_path,chrome_options=options)

class wa_web() :
	def __init__(self,Chrome=WEBDRIVER) :
		self.Chrome = WEBDRIVER

	def get_url(self) :
		return self.Chrome.get('https://web.whatsapp.com/')

	def msg_document(self,user,message,filepath) :
		search_box = self.Chrome.find_element_by_xpath('//div[@data-tab="3"]')
		search_box.send_keys(user)
		search_box.send_keys(Keys.ENTER)
		chat_box = self.Chrome.find_element_by_xpath('//div[@data-tab="6"]')
		chat_box.click() 
		chat_box.send_keys(message)
		chat_box.send_keys(Keys.ENTER)
		#finding the attachment button 
		search_box = self.Chrome.find_element_by_xpath('//div[@data-tab="3"]')
		search_box.send_keys(user)
		search_box.send_keys(Keys.ENTER)
		attach_buton = self.Chrome.find_element_by_xpath('//div[@title="Attach"]')
		attach_buton.click()
		#sending doc
		doc_button = self.Chrome.find_element_by_xpath('//input[@accept="*"]')
		doc_button.send_keys(filepath)
		time.sleep(3)
		send_doc_box = self.Chrome.find_element_by_xpath('//span[@data-icon="send"]') 
		return send_doc_box.click() 

	def msg_only(self,user,message) :
		search_box = self.Chrome.find_element_by_xpath('//div[@data-tab="3"]')
		search_box.send_keys(user)
		search_box.send_keys(Keys.ENTER)
		chat_box = self.Chrome.find_element_by_xpath('//div[@data-tab="6"]')
		chat_box.click() 
		chat_box.send_keys(message)
		return chat_box.send_keys(Keys.ENTER) 