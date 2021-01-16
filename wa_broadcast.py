
from tkinter import *
from tkinter import filedialog
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException,InvalidArgumentException
from time import sleep 
import os 
import pandas as pd
import numpy as np

from tkinter import filedialog

OUTLIER = {'99066':'099066','99109':'099109','99243':'099243','99239':'099239',
'7385':'007385','7371':'007371','7407':'007407'
,'18424':'018424'}
MONTH = {'Januari' : '01', 'Februari' : '02','Maret' : '03','April' : '04','Mei' : '05','Juni' : '06',
                'Juli' : '07','Agustus' : '08','September' : '09','Oktober' : '10','November' : '11','Desember':'12'}
WEBDRIVER = webdriver.Chrome('C:/Webdriver/bin/chromedriver.exe')
LARGEFONT =("Montserrat", 20) 
NORMALFONT = ("Montserrat", 10)



class wa_web() :
	def __init__(self,Chrome=WEBDRIVER) :
		self.Chrome = WEBDRIVER
	def get_url(self) :
		self.Chrome.get('https://web.whatsapp.com/')
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
		send_doc_box.click() 
	def msg_only(self,user,message) :
		search_box = self.Chrome.find_element_by_xpath('//div[@data-tab="3"]')
		search_box.send_keys(user)
		search_box.send_keys(Keys.ENTER)
		chat_box = self.Chrome.find_element_by_xpath('//div[@data-tab="6"]')
		chat_box.click() 
		chat_box.send_keys(message)
		chat_box.send_keys(Keys.ENTER) 
class functionality() :

	def fix_rekon(self) : 
		user_name = pd.read_excel(path[0])
		user_name = [str(x) for x in user_name['KDSATKER']]
		def generate_file_MONTH(bulan) : 
			return MONTH[bulan]

		def generate_path(user,bulan_rekon) : 
			return f'20{generate_file_MONTH(bulan_rekon)}00_{user}_excel.xlsx'
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				if user  in  OUTLIER.keys() : 
					satker = OUTLIER[user]
					lokasi = os.path.join(dir_path[0],generate_path(satker,bulan_rekon))
					wa_bot.msg_document(satker,message,lokasi)
				else : 
					lokasi = os.path.join(dir_path[0],generate_path(user,bulan_rekon))
					wa_bot.msg_document(user,message,lokasi)
			except InvalidArgumentException : 
				continue
				print(f'file {user} ga ada')  
	def belum_rekon(self) :
		user_name = pd.read_excel(path[0])
		user_name = [str(x) for x in user_name['KDSATKER']]


		
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				if user  in  OUTLIER.keys() : 
					satker = OUTLIER[user]
					wa_bot.msg_only(satker,message)
				else : 
					wa_bot.msg_only(user,message)
			except InvalidArgumentException : 
				continue

	def fix_LPJ(self) :
		user_name = pd.read_excel(path[0])
		user_name = [str(x) for x in user_name['KDSATKER']]
		def generate_file_MONTH(bulan) : 
			return MONTH[bulan]

		def generate_path(user,bulan_rekon) : 
			return f'{generate_file_MONTH(bulan_rekon)}_{user}.png'
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				if user  in  OUTLIER.keys() : 
					satker = OUTLIER[user]
					lokasi = os.path.join(dir_path[0],generate_path(satker,bulan_rekon))
					wa_bot.msg_document(satker,message,lokasi)
				else : 
					lokasi = os.path.join(dir_path[0],generate_path(user,bulan_rekon))
					wa_bot.msg_document(user,message,lokasi)
			except InvalidArgumentException : 
				continue
				print(f'file {user} ga ada')  
	def belum_LPJ(self):
		user_name = pd.read_excel(path[0])
		user_name = [str(x) for x in user_name['KDSATKER']]


		
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				if user  in  OUTLIER.keys() : 
					satker = OUTLIER[user]
					wa_bot.msg_only(satker,message)
				else : 
					wa_bot.msg_only(user,message)
			except InvalidArgumentException : 
				continue
	def broadcast_lain(self) :
		user_name = pd.read_excel(path)
		user_name = [str(x) for x in user_name['KDSATKER']]


		#PATH to attachment
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)

		for user in user_name :
			try : 
				if user  in  OUTLIER.keys() : 
					satker = OUTLIER[user]
					wa_bot.msg_document(satker,message,attachment_path)
				else : 
					wa_bot.msg_document(user,message,attachment_path)
			except InvalidArgumentException : 
				continue
				print(f'file {user} ga ada')  
	def aset_fix(self) :
		data_aset = pd.read_excel(path[0])
		username = [x for x in data_aset['Kode Satker']]
		def message_generate(data_aset,satker) :
			# data_aset['Kode Satker'] = data_aset['Kode Satker'].split('.')[2]
			sentence = 'Selamat Pagi/Siang/Sore Bapak /Ibu{} memiliki {} yang belum diinput sebesar Rp{:,}'.format(data_aset.loc[data_aset['Kode Satker'] == satker,'Kode Satker'],data_aset.loc[data_aset['Kode Satker'] == satker,'Nama Akun'],data_aset.loc[data_aset['Kode Satker'] == satker,'Rupiah'])
			print(sentence)
			return sentence
		wa_bot = wa_web()
		wa_bot.get_url()
		time.sleep(20)
		for user in username :
			if user  in  OUTLIER.keys() :
				satker = OUTLIER[user]
				wa_bot.msg_only(satker,message_generate(data_aset,satker))
			else : 
				wa_bot.msg_only(user,message_generate(data_aset,user))

class tkinterApp(Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		super().__init__(*args, **kwargs)
		
		# creating a container 
		container = Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (MainMenu, Page1, Page2,Page3,Page4,Page5,Page6): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# MainMenu, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(MainMenu) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 
class Path() :

	def file_path(self) : 
		global path
		file_path = filedialog.askopenfilename(title='Silahkan pilih file monitoring satker yang rekoonya perlu diperbaiki')
		path = file_path
		return path
	def directory(self) : 
		global dir_path 
		directory_path = filedialog.askdirectory(title='Silahkan pilih folder tempat menyimpan dok perbaikan ')
		dir_path = [directory_path]
		return dir_path
	def attachment(self) :
		global attachment_path 
		att_path = filedialog.askopenfilename(title='Silahkan pilih file lampiran ')
		attachment_path = att_path
# first window frame MainMenu 

class MainMenu(Frame): 
	def __init__(self, parent, controller): 
		Frame.__init__(self, parent) 
		
		
		# label of frame Layout 2 
		label = Label(self, text ="MainMenu", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 0, column = 1, padx = 10, pady = 10) 

		button1 = Button(self, text ='Broadcast Kesalahan Rekon', width=30,command = lambda : controller.show_frame(Page1),font=NORMALFONT) 
		button2 = Button(self,text='Broadcast yang belum rekon', width=30,command= lambda : controller.show_frame(Page2),font=NORMALFONT)
		button3 = Button(self,text='Broadcast Kesalahan LPJ', width=30,command= lambda : controller.show_frame(Page3),font=NORMALFONT)
		button4 = Button(self,text='Broadcast yang belum LPJ', width=30,command= lambda : controller.show_frame(Page4),font=NORMALFONT)
		button5 = Button(self,text='Broadcast Aset Belum Register', width=30,command= lambda : controller.show_frame(Page5),font=NORMALFONT)
		button6 = Button(self,text='Broadcast Lain-Lain', width=30,command= lambda : controller.show_frame(Page6),font=NORMALFONT)
		# putting the button in its place by 
		# using grid 
		button1.grid(row=1,column=1, sticky=W+E) 
		button2.grid(row=2,column=1, sticky=W+E)
		button3.grid(row=3,column=1, sticky=W+E)
		button4.grid(row=4,column=1, sticky=W+E)
		button5.grid(row=5,column=1, sticky=W+E)
		button6.grid(row=6,column=1, sticky=W+E)

	
		# putting the button in its place by 
		# using grid 
class Page1(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
	

		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		directory_label = Button(self,text='Silahkan pilih folder tempat menyimpan file perbaikan',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		directory_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)


# third window frame page2 
class Page2(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
	
		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		directory_label = Button(self,text='Silahkan pilih folder tempat menyimpan file perbaikan',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		directory_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)

class Page3(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
	

		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		directory_label = Button(self,text='Silahkan pilih folder tempat menyimpan file perbaikan',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		directory_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)
class Page4(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		directory_label = Button(self,text='Silahkan pilih folder tempat menyimpan file perbaikan',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		directory_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)
class Page5(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		attachment_label = Button(self,text='Silahkan pilih   file lampiran',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.attachment,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		attachment_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)
class Page6(Frame): 
	# functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get() 
			message = message_entry.get()

		#functionality Label 
		bulan_label = Label(self,text='Silahkan Input Bulan Pelaporan seperti November',font=NORMALFONT)
		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		attach_path = Button(self,text='Silahkan pilih folder tempat menyimpan file lampiran',command=path_class.attachment,font=NORMALFONT)
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=functionality().broadcast_lain,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		attach_path.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)

if __name__ == '__main__':
	app = tkinterApp() 
	app.mainloop() 

