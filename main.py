
from tkinter import *
from tkinter import filedialog
import os 
import pandas as pd
import numpy as np

from functionality import Path,broadcast_functionality
from scrapper import wa_web



LARGEFONT =("Montserrat", 20) 
NORMALFONT = ("Montserrat", 10)







class MultiPurposeBroadcaster(Tk): 
	
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
		for F in (MainMenu, Message_Only, Message_With_Attachment): 

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

# first window frame MainMenu 

class MainMenu(Frame): 
	def __init__(self, parent, controller): 
		Frame.__init__(self, parent) 
		
		
		# label of frame Layout 2 
		label = Label(self, text ="MainMenu", font = LARGEFONT) 
		
		# putting the grid in its place by using 
		# grid 
		label.grid(row = 0, column = 1, padx = 10, pady = 10) 

		button1 = Button(self, text ='Broadcast Message Only', width=30,command = lambda : controller.show_frame(Message_Only),font=NORMALFONT) 
		button2 = Button(self,text='Broadcast yang belum rekon', width=30,command= lambda : controller.show_frame(Message_With_Attachment),font=NORMALFONT)

		# putting the button in its place by 
		# using grid 
		button1.grid(row=1,column=1, sticky=W+E) 
		button2.grid(row=2,column=1, sticky=W+E)


	
		# putting the button in its place by 
		# using grid 
class Message_Only(Frame): 
	# broadcast_functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
	

		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#broadcast_functionality Label 

		message_label = Label(self,text='Silahkan Input pesan',font=NORMALFONT)
		bulan_entry = Entry(self,text='Input Bulan Rekonsiliasi') 
		message_entry = Entry(self,text='Silahkan input pesan broadcast')
		file_path = Button(self,text='Silahkan pilih file tujuan broadcast',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Simpan Semua Input',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Jalankan Broadcast',command=broadcast_functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		bulan_label.grid(row=0,column=0,sticky=W+E)
		message_label.grid(row=1,column=0,sticky=W+E)
		bulan_entry.grid(row=0,column=1,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)


# third window frame page2 
class Message_With_Attachment(Frame): 
	# broadcast_functionality.__init__(self)
	def __init__(self, parent, controller): 
		# Database.__init__(self,db)
		Frame.__init__(self, parent) 
	
		path_class = Path()
		

		def save_record() : 
			global bulan_rekon,message
			bulan_rekon = bulan_entry.get()
			message = message_entry.get()

		#broadcast_functionality Label 
		message_label = Label(self,text='Please Input Messages',font=NORMALFONT)
		message_entry = Entry(self,text='Please Input Messages')
		directory_label = Button(self,text='Please Choose Attachment File',command=path_class.directory,font=NORMALFONT)
		file_path = Button(self,text='Choose Recipient List File',command=path_class.file_path,font=NORMALFONT)
		save_record = Button(self,text='Save All Records',command=save_record,font=NORMALFONT)
		execute_button = Button(self,text='Run Broadcast',command=broadcast_functionality().fix_rekon,font=NORMALFONT)

		
		#grid a file 
		message_label.grid(row=1,column=0,sticky=W+E)
		message_entry.grid(row=1,column=1,sticky=W+E)
		directory_label.grid(row=2,column = 1,sticky=W+E)
		file_path.grid(row=3,column=1,sticky=W+E)
		save_record.grid(row=4,column=1,sticky=W+E)
		execute_button.grid(row=5,column=1,sticky=W+E)



		# button to show frame 2 with text 
		# layout2 
		back_button = Button(self, text ="MainMenu",command = lambda : controller.show_frame(MainMenu),font=NORMALFONT) 
		
		back_button.grid(row=10,column=1,sticky=W+E)



if __name__ == '__main__':
	app = MultiPurposeBroadcaster() 
	app.mainloop() 
