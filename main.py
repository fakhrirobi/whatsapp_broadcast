import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout, QWidget
from datetime import datetime
from PyQt5 import *
from functionality import *



class MainScreen(QDialog):
    '''
    class for Defining Main Screen 
    '''
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("ui_file/main_menu.ui",self)
        self.Usage.clicked.connect(self.usage_instruction)
        self.BroadcastWithoutAtt.clicked.connect(self.broadcastWithoutAttachment)
        self.BroadcastWithAtt.clicked.connect(self.broadcastWithAttachment)
        self.FullProjectLink.clicked.connect(self.projectLink)
        
    def usage_instruction(self):
        usage = Usage_Screen()
        widget.addWidget(usage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def broadcastWithoutAttachment(self):
        broadcast_without_att= Broadcast_Without_Att_Screen()
        widget.addWidget(broadcast_without_att)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def broadcastWithAttachment(self):
        broadcast_with_att = Broadcast_With_Att_Screen()
        widget.addWidget(broadcast_with_att)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def projectLink(self):
        project_link = Full_Project_Link_Screen()
        widget.addWidget(project_link)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Usage_Screen(QDialog) : 
    def __init__(self):
        super(Usage_Screen, self).__init__()
        loadUi("ui_file/BroadcastWithoutDocs.ui",self)
        
        
class Broadcast_Without_Att_Screen(QDialog) : 
    '''
    class for Defining Broadcast Without Attachment Menu 
    '''
    def __init__(self):
        super(Broadcast_Without_Att_Screen, self).__init__()
        loadUi("ui_file/BroadcastWithoutDocs.ui",self)
        self.RunBroadcast.clicked.connect(self.run_broadcast)
        self.backButton.clicked.connect(self.backtomenu)
    def clicked_choose_recipient(self) : 
        file_path = QFileDialog.getOpenFileName(self, 'Silahkan Pilih File Tujuan Broadcast')
        print(file_path)
        return file_path
    def save_records(self): 
        message_content = self.MessageBox.toPlainText()
        return message_content
    def run_broadcast(self):
        recipient_path = self.clicked_choose_recipient()
        message_content = self.save_records()
        broadcast_functionality().sent_messages_without_attachment(message_content,recipient_path)
    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Broadcast_With_Att_Screen(QDialog) : 
    '''
    class for Defining Broadcast With Attachment Menu 
    '''
    def __init__(self):
        #//TODO : CREATE CLASS EXPLANATION AS DOCSTRING
        '''
        
        '''
        super(Broadcast_With_Att_Screen, self).__init__()
        loadUi("BroadcastWithDocs.ui",self)
        self.ChooseRecipient.clicked.connect(self.clicked_choose_recipient)
        self.ChooseAttachments.clicked.connect(self.choose_attachments)
        self.SaveRecords.clicked.connect(self.save_records)
        self.RunBroadcast.clicked.connect(self.run_broadcast)
        self.backButton.clicked.connect(self.backtomenu)
    def choose_attachments(self): 
        #//TODO : CREATE choose_attachments EXPLANATION AS DOCSTRING
        attachment_path = QFileDialog.getOpenFileName(self, 'Please Choose Attachment File ')
        return attachment_path
    def clicked_choose_recipient(self) : 
        #//TODO : CREATE clicked_choose_recipient EXPLANATION AS DOCSTRING
        file_path = QFileDialog.getOpenFileName(self, 'Please Choose Recipient File (.xlsx file)')
        return file_path
    def save_records(self): 
        #//TODO : CREATE save_records EXPLANATION AS DOCSTRING
        message_content = self.MessageBox.toPlainText()
        return message_content
        
    def run_broadcast(self):
        #//TODO : CREATE run_broadcast EXPLANATION AS DOCSTRING
        recipient_path = self.clicked_choose_recipient()
        message_content = self.save_records()
        att_path =self.choose_attachments()
        broadcast_functionality().sent_messages_with_attachment(message_content,recipient_path,att_path)
        
    def backtomenu(self) : 
        #//TODO : CREATE backtomenu EXPLANATION AS DOCSTRING
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Full_Project_Link_Screen(QDialog) : 
    '''
    class for Showing Full Project in Github
    '''
    def __init__(self):
        super(Full_Project_Link_Screen, self).__init__()
        loadUi("main_menu.ui",self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    welcome = MainScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(1000)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")