import pandas as pd 
from scrapper import *








class broadcast_functionality() :
    #//TODO : CREATES CLASS DOCSTRING

	def sent_messages_without_attachment(self,message,path) : 
    #//TODO : 
		user_name = pd.read_excel(path,engine='openpyxl')
		user_name = [str(x) for x in user_name['RECIPIENT']]

		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				wa_bot.msg_only(user,message)
			except InvalidArgumentException : 
				print(f'{user} does not exists')  
				continue
				

	def sent_messages_with_attachment(self,message,path,att_path) : 
		user_name = pd.read_excel(path,engine='openpyxl')
		user_name = [str(x) for x in user_name['RECIPIENT']]

		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 

				file_location = att_path
				wa_bot.msg_document(user,message,file_location) 
			except InvalidArgumentException : 
				continue
				print(f'{user} does not exists')  

