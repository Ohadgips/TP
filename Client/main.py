import sys,os,sqlite3,pickle,ssl
import time
from socket import *
from PyQt5.QtCore import pyqtSignal,QTimer
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton, QWidget,QFrame\
    ,QScrollArea,QVBoxLayout,QLabel,QProgressBar,QDialog,QListWidget,QFileDialog,QSlider
from PyQt5.uic import loadUi
import _thread,threading
from os.path import exists
from pathlib import Path
from Client import * 
sys.path.append("..\Client\Gui_py")
#from downloading_widget import Ui_Form
from Client_GUI import Ui_MainWindow
from file_window import Files_Window 
from downloading_widget import Ui_Form

global download_layout,upload_layout,bars
bars = {}
class Download_Window(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        self.ui = Files_Window()
        self.ui.setupUi(self)
        self.selected_item = None
        self.listWidget_2 = self.ui.listWidget_2
        self.ui.ok_button.setEnabled(False)
        self.ui.ok_button.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self):
        # Perform the desired action when the button is clicked
        selected_items = self.listWidget_2.selectedItems()
        if selected_items:
                self.selected_item = selected_items[0].text()
        else:
            self.selected_item =  None
        self.accept    

class MainWindow(QMainWindow):
    global ui
    start_other_function = pyqtSignal()
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.full_menu.hide()          
        self.ui.pages.setCurrentIndex(0)

    def download_dialog(self):
        self.download_window = Download_Window()
        self.list = self.download_window.findChild(QListWidget,"listWidget_2")
        files = download_files(manager)
        print(files)
        self.list.addItems(files)
        self.download_window.show()
        if self.download_window.exec_() == QDialog.Accepted:
            selected_item = self.download_window.selected_item
            widget = add_to_download()
            _thread.start_new_thread(proccess_download,(manager,port_,selected_item,widget))
            #proccess_download(manager,port_,selected_item)    
    #For Search
    def on_search_button_clicked(self):
        self.ui.pages.setCurrentIndex(5)
        search_text = self.ui.search_tab.text().strip()
        if search_text:
            print(search_text)
    #open_file dialog to choose a file
    
    def open_file_dialog(self):
        print("open_file_dialog")
        path, ok = QFileDialog.getOpenFileName(self,"Select A File", r'C:/Users/USER/Downloads/')
        print(path)
        print(path.split("/")[len(path.split("/"))-1])
        dialog = QFileDialog()
        if path:
           size = os.path.getsize(path)
           size = float(size / 1024)
           upload(manager,path.split("/")[len(path.split("/"))-1],path,size)
    
    def on_stackedWidget_currentChanged(self, index):
            buttons = self.ui.icons_only.findChildren(QPushButton) \
            + self.ui.full_menu.findChildren(QPushButton)
            
            for button in buttons:
                if index in [5, 6]:
                    button.setAutoExclusive(False)
                    button.setChecked(False)
                else:
                    button.setAutoExclusive(True)
  # all buttons for changing to pages functions
    def on_upload_button_ico_toggled(self):
        self.ui.pages.setCurrentIndex(1)
    def on_upload_button_toggled(self):
        self.ui.pages.setCurrentIndex(1)
    def on_download_button_ico_toggled(self):
        self.ui.pages.setCurrentIndex(2)
    def on_download_button_toggled(self):
        self.ui.pages.setCurrentIndex(2)
    def on_history_button_ico_toggled(self):
        self.ui.pages.setCurrentIndex(3)
    def on_history_button_toggled(self):
        self.ui.pages.setCurrentIndex(3)
    def on_settings_button_ico_toggled(self):
        self.ui.pages.setCurrentIndex(4)
    def on_settings_button_toggled(self):
        self.ui.pages.setCurrentIndex(4)
    def on_download_page_button_toggled(self):
        self.download_dialog()
    def on_upload_page_button_toggled(self):
        self.open_file_dialog()
    
def add_to_layout(file_details):
    widget,size,bar = set_widget(upload_layout,file_details)
    widget.setGeometry(0, 0, scroll_area_widget.width(), widget.height())
    scroll_area_widget.setLayout(upload_layout)
    return bar

def add_to_download():#file_details
    widget,size,bar = set_widget(download_layout,("","","",0))
    widget.setGeometry(0, 0, scroll_area_widget2.width(), widget.height())
    scroll_area_widget2.setLayout(download_layout)
    return widget

def add_to_download2(widget,file_details):
    name = widget.findChild(QLabel, "label_39")
    type = widget.findChild(QLabel, "label_41")
    size = widget.findChild(QLabel, "label_43")
    bar = widget.findChild(QProgressBar,"progressBar_6")
    bar.setRange(0,file_details[3])
    name.setText(file_details[0])
    type.setText(file_details[1])
    size.setText(str(file_details[2])+" KB")
    widget.setGeometry(0, 0, scroll_area_widget2.width(), widget.height())
    scroll_area_widget2.setLayout(download_layout)
    return bar

def set_widget(layout,file_details):
    path = os.getcwd()
    try:
        widget = loadUi(path+"/Gui/ui/downloading_widget.ui")
    except:
        widget = loadUi(path+"/Client/Gui/ui/downloading_widget.ui")
    name = widget.findChild(QLabel, "label_39")
    type = widget.findChild(QLabel, "label_41")
    size = widget.findChild(QLabel, "label_43")
    bar = widget.findChild(QProgressBar,"progressBar_6")
    bar.setRange(0,file_details[3])
    name.setText(file_details[0])
    type.setText(file_details[1])
    size.setText(str(file_details[2])+" KB")
    layout.insertWidget(0, widget)
    return widget,size,bar
    
    
    
################################################# server main functions ###########################################
global uploadpath,maxsize,downloadspath,HOST,manager,host,port_
# path for all downloads and uploads files
uploadpath = str("\Client\shared_files")
downloadspath = str("\Client\Downloads")

# Error disconnction                     
def error_disconnect(client,addr):
    print("error,disconnected from: ",addr)
    client.close()

# upload a file when pressing the upload button        
def upload(manager,file_name,file_path,size):
    print("upload")
    chunks = split_file(file_name,size,file_path)
    file_name = file_name.split(".")
    file_type = file_name[1]
    file_name = file_name[0]
    manager.send("UPLOAD".encode())
    bar_value =0
    msg = file_name+"$$$"+file_type+"$$$"+str(size)
    manager.send(str(msg).encode())
    data = manager.recv(2048)
    users = pickle.loads(data)
    bar = add_to_layout((file_name,file_type,size,len(users)))
    for user in users:
        print(user)
        if user[0] != gethostbyname(gethostname()):
            _thread.start_new_thread(send_files_to_users,(file_name,file_type,(user[0],eval(user[1])),chunks,size))
        bar_value = bar_value + 1
        bar.setValue(bar_value)


def proccess_download(manager,_port,file_name,widget):
    print("proccess_download")
    name = file_name.split(".")[0]
    manager.send("DOWNLOAD_2".encode())
    data = manager.recv(2048).decode()
    if data != "OK":
        print("there is an error")
    manager.send(name.encode())
    files = manager.recv(2048)
    files = pickle.loads(files)
    size = manager.recv(2048).decode()
    manager.send("OK".encode())
    data = manager.recv(2048).decode()
    all_chunks = eval(data)
    print((name,file_name.split(".")[1],size,all_chunks))
    bar = add_to_download2(widget,(name,file_name.split(".")[1],size,all_chunks))
    bars[file_name] = [bar,0]
    files.sort(key=lambda details: details[2] if details[2] is not None else float('-inf'))
    asked_chunks = 0
    #clientsbyspeed = []
    while asked_chunks < all_chunks:
        if all_chunks > 1:
            for client in files :
                print(client)
                if client[0] != gethostbyname(gethostname()):
                    if asked_chunks == all_chunks:
                        break
                    if asked_chunks < all_chunks:
                        if client[2] == None:
                            pass
                        else:
                            print((client[0],client[1]))
                            if client[2] < asked_chunks:
                                pass
                            elif client[2] == asked_chunks:
                                _thread.start_new_thread(connect_to_servers,(_port,file_name,(client[0],int(client[1])),(asked_chunks)))
                                asked_chunks += 1
                            else:
                                _thread.start_new_thread(connect_to_servers,(_port,file_name,(client[0],int(client[1])),(asked_chunks,asked_chunks+1)))
                                asked_chunks += 2    
        
            if asked_chunks != all_chunks:
                _thread.start_new_thread(connect_to_servers,(_port,file_name,(files[0][0],int(files[0][1])),(tuple(range(asked_chunks,all_chunks+1)))))
                asked_chunks = all_chunks
        else:
            _thread.start_new_thread(connect_to_servers,(_port,file_name,(files[0][0],int(files[0][1])),(tuple(range(asked_chunks,all_chunks)))))
            asked_chunks = all_chunks
    print("all chunks was requested")         






# get all chunks from the other clients in the end connect all
def get_files(client,addr):
    print("get_files")
    # get file name and number of chunks
    data = client.recv(2048).decode().split("$$$")
    name = data[0]
    print(name)
    bar = bars[name][0]
    chunks = data[1]
    print(chunks)
    chunks = eval(chunks)
    try:
        try:
            data = client.recv(2048).decode('utf-8')
        except:
            data = client.recv(2048).decode('latin-1')   
    except: 
            try:        
                data = client.recv(2048).decode('utf-16')
            except:
                data = client.recv(2048).decode('big5')
    file_size_name = data.split("$$$")
    file_size = 0
    bar_value = 0
    file_name = file_size_name[0]
    file_type = file_size_name[1]
    path = os.getcwd()
    while data != '' and data != 'END':
        client.send("OK".encode())
        try:
            file_size = int(file_size_name[2]) + file_size
        except:
            print("Try Again")
        try:
            file = open(path+"/Downloads"+"/"+file_name, "wb")
            print("created",file_name," : ",exists(path+"/Downloads"+"/"+file_name))
        except:
            file = open(path+downloadspath+"/"+file_name, "wb")
            print("created",file_name," : ",exists(path+downloadspath+"/"+file_name)) 
        file_bytes = b""
        data = client.recv(2048)
        file_bytes += data
        file.write(file_bytes)
        file.close()
        bar_value = bar_value + 1
        print(bars[name][1])
        bars[name][1] = bars[name][1]+ bar_value
        bar.setValue(bars[name][1])
        # get next chunk
        #try:
        data = client.recv(2048)
        try:
            try:
                data = data.decode('utf-8')
            except:
                data = data.decode('latin-1')    
        except:        
            try:        
                data = client.recv(2048).decode('utf-16')
            except:
                data = client.recv(2048).decode('big5')
        try:
            file_size_name = data.split("$$$")
            file_name = file_size_name[0]
            file_type = file_size_name[1]
        except:
            print("end")   
        '''  
        except:
            #error_disconnect(client,addr)
            #break
            print("eorr")
            break
            '''
    try:    
        client.close()
    except:
        print("already close")
    # when all chunks recived
    print("Connect")
    fullpath,status = connect(name,chunks,file_size)
    print(status)
    bar.setValue(bars[name][1])
    if exists(fullpath):
        status =int(bar.maximum())
        bar.setValue(status)
        file_name = name.split(".")[0]
        file_type = name.split(".")[1]
        update_manager(manager,file_name,file_type,file_size)
        bars.pop(name)


# get all upload file if not passing the size limit default is 1 gb can be changed in the settings(GUI)
def shared_files(client,addr):#manager
    global maxsize,size_saved
    client.send("OK".encode())
    # get file name and number of chunks
    data = client.recv(2048).decode()
    data = data.split("$$$")
    #print(data)
    name = data[0]
    chunks = data[1]
    chunks = eval(chunks)
    bar_value = 0
    received_chunks = 0
    # get size of chunk if more than the max then stop receiving
    full_size = 0
    file_name_type_size = client.recv(2048).decode().split("$$$")
    file_name = file_name_type_size[0]
    file_type = file_name_type_size[1]
    while file_name != '' and file_name != 'END':
        file_size = file_name_type_size[2]
        
        saved = open(size_saved,'r')
        kb_saved =saved.read().strip()
        saved.close() 
        if kb_saved == '':
            kb_saved = 0
        # reject stop receiving
        print(kb_saved)
        print(maxsize)
        if int(kb_saved) + int(int(file_size)/1024) > maxsize:
            client.send("REJECT".encode())
            break
        
        # accept
        else:
            client.send("ACCEPT".encode())
            saved = open(size_saved,'w')
            save = int(kb_saved) + int(int(file_size)/1024)
            saved.write(str(save))
            saved.close
            full_size = full_size + int(file_size)
            received_chunks += 1
            #save file
            path = os.getcwd()
            if os.path.exists(path+uploadpath+"/"+file_name) == True and os.path.exists(path+"/shared_files"+"/"+file_name) == True:
                pass
            else:
                try:
                    file = open(path+uploadpath+"/"+file_name, "wb")
                except:
                    file  =  open(path+"/shared_files"+"/"+file_name, 'wb')
                file_bytes = b""
                data = client.recv(2048)
                file_bytes += data
                file.write(file_bytes)
                file.close()
                
            #get next chunk
            try:
                file_name_type_size = client.recv(2048).decode().split("$$$")
            except:
                break    
            file_name = file_name_type_size[0]
    
    client.close()
    #to update the
    if chunks == received_chunks:
        update_manager(manager,name,file_type,full_size)    #manager.send("UPDATE_FILES")
    else:
        update_manager(manager,name,file_type,full_size,received_chunks)    
    #manager 



#accept all new connection
def accept_conns(server):
    Client, addr = server.accept()
    print('New Connection: ' + addr[0] + ' , ' + str(addr[1]))
    _thread.start_new_thread(clients_handler, (Client,addr))




#handle all clients in once (threads)
def clients_handler(client,addr):
    while True:
        try:
            data = client.recv(2048)
        except:
            error(client,addr)# if there is and error close the client    
        message = data.decode('utf-8')
        
        if message == 'DOWNLOAD':
            client.send("OK".encode())
            get_files(client,addr)
            break 
        if message == 'GET':
            client.send("OK".encode())
            data = client.recv(2048).decode('utf-8')
            client.send("READY".encode())
            print(data)
            message = client.recv(int(data)).decode('utf-8')
            message = message.split("$$$")
            chunks = list(message[2].split(","))
            print(message[2])
            send_file((addr[0],int(message[0])),message[1],chunks)
        # get upload file
        elif message == 'UPLOAD':
            shared_files(client,addr)
            break
        else:
            break      
    print('Disconnected: ' + addr[0] + ' , ' + str(addr[1]))
    client.close()



def start_client():
    global host,port_,manager,size_saved
    path = os.getcwd()
    size_saved = path+"/size_saved"      
    #uploadspeed = upload_speed()
    host = gethostbyname(gethostname())
    port_ = port()  
    # connecting to manage server
    HOST = '10.100.102.13'
    PORT = 54200
    ADDR = (HOST,PORT)
    manager = socket.socket(AF_INET,SOCK_STREAM)
    print(ADDR)
    manager.connect(ADDR)
    data = manager.recv(2048).decode()
    print(data)
    """manager.send("SPEED".encode())
    data = manager.recv(2048).decode()
    if data != "OK":
        print("error")
    else:    
        manager.send(str(uploadspeed).encode())"""

    ADDR = (host,port_)
    server = socket.socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    data = b''
    manager.send(str(port_).encode())
    while True:
        accept_conns(server)
    con.close()
    server.close()

def update_value(value):
    global maxsize
    maxsize = value
    print("Changed max to: ",maxsize)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    _thread.start_new_thread(start_client,())

    window.show()

    # layout for upload page
    central_widget = window.centralWidget()
    pages_stacked_widget = central_widget.findChild(QWidget, "main_window")
    upload_page_widget = pages_stacked_widget.findChild(QWidget, "Upload_page")
    scroll_and_button = upload_page_widget.findChild(QFrame, "scroll_and_button") 
    scrollArea = scroll_and_button.findChild(QScrollArea, "scrollArea_3")
    scroll_area_widget = scrollArea.findChild(QWidget, "scrollAreaWidgetContents_4")
    upload_layout = QVBoxLayout(scroll_area_widget)

    # layout for download page
    central_widget = window.centralWidget()
    pages_stacked_widget = central_widget.findChild(QWidget, "main_window")
    upload_page_widget = pages_stacked_widget.findChild(QWidget, "download_page")
    scroll_and_button2 = upload_page_widget.findChild(QFrame, "scroll_and_button_2") 
    scrollArea2 = scroll_and_button2.findChild(QScrollArea, "scrollArea_4")
    scroll_area_widget2 = scrollArea2.findChild(QWidget, "scrollAreaWidgetContents_5")
    download_layout = QVBoxLayout(scroll_area_widget2)

    # layout for upload page
    central_widget = window.centralWidget()
    pages_stacked_widget = central_widget.findChild(QWidget, "main_window")
    settings_page_widget = pages_stacked_widget.findChild(QWidget, "settings_page")
    widget = settings_page_widget.findChild(QWidget, "widget_5")
    slider = widget.findChild(QSlider, "kb_slider_2")
    slider.valueChanged.connect(update_value)
    maxsize = slider.minimum()

    sys.exit(app.exec_())
