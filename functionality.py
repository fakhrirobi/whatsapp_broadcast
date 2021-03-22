from tkinter import filedialog
import pandas as pd
from scrapper import wa_web
import time
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException,InvalidArgumentException
from time import sleep 
import os 





class Path() :

	def file_path(self) : 
		global path
		file_path = filedialog.askopenfilename(title='Please Select File That Contains RECIPIENT LIST')
		path = file_path
		return path
	def directory(self) : 
		global dir_path 
		directory_path = filedialog.askdirectory(title='Please Select Location Where Contain List of Files')
		dir_path = [directory_path]
		return dir_path
	def attachment(self) :
		global attachment_path 
		att_path = filedialog.askopenfilename(title='Please Select Attachment File')
		attachment_path = att_path

class broadcast_functionality() :

	def sent_messages_without_attachment(self,message,path) : 
		user_name = pd.read_excel(path,engine='openpyxl')
		user_name = [str(x) for x in user_name['RECIPIENT']]

		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				wa_bot.msg_only(user,message)
			except InvalidArgumentException : 
				continue
				print(f'{user} does not exists')  

	def sent_messages_with_attachment(self,message,path,attachment) : 
		user_name = pd.read_excel(path,engine='openpyxl')
		user_name = [str(x) for x in user_name['RECIPIENT']]

		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 

				file_location = attachment
				wa_bot.msg_document(user,message,file_location) 
			except InvalidArgumentException : 
				continue
				print(f'{user} does not exists')  



