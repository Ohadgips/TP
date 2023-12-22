import PyQt5,socket,os,_thread,pickle,sqlite3
from PyQt5 import QtWidgets
from pathlib import Path

#get info from txt about the port
def info():
    text = open("client.txt", "r")
    text = str(text.read()).split('\n')
    return text

#open_file dialog to choose a file
def open_file_dialog():
        filename, ok = QtWidgets.QFileDialog.getOpenFileName("Select a File", r'C:/Users/USER/Downloads/')
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(r'C:/Users/USER/Downloads/')
        if filename:
            return filename,Path(filename)

# upload a file when pressing the upload button        
def upload_button(client):
    file_name,file_path = open_file_dialog()
    chunks = split_file(file_path,file_name)
    
    file_name = file_name.split(".")
    type = file_name[1]
    file_name = file_name[0]
    
    client.send(b"UPLOAD")
    size = len(chunks)
    msg = file_name+"$$$"+type+"$$$"+str(size)
    client.send(msg.encode())
    
    users = pickle.loads(client.recv(2048))
    for user in users:
        _thread.start_new_thread(send_files_to_users,(file_name,user,chunks))

#split file to chunks
def split_file(path,name):
    chunknames = []
    fileR = open(path, "rb")
    chunk = 0
 
    byte = fileR.read(2048)
    while byte:
 
        # Open a temporary file and write a chunk of bytes
        fileN = name +"$_chunk_" + str(chunk) + "&.txt"
        chunknames.append(fileN)
        fileT = open(fileN, "wb")
        fileT.write(byte)
        fileT.close()
        byte = fileR.read(2048)
        chunk += 1
    return chunknames

def update_manager(manager):
    pass
        
# send chosen file to all connected users
def send_files_to_users(filename,addr,chunks):
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(addr)
    msg = filename +str(len(chunks)-1)
    client.send(msg.encode())
    
    for file_name in chunks:
        file = open(file_name,"rb")
        file_size = os.path.getsize(file_name)
        file_size = str(file_size)
        
        msg = file_name+"$$$"+file_size
        client.send(msg.encode().strip())
        data = client.recv(2048).decode()
        
        if data == 'REJECT':
            break
        else:
            data = file.read()
            client.sendall(data)
            file.close()      
    client.close()            


# connecting to database
file_name = "shared_files.db"
con = sqlite3.connect(file_name,check_same_thread=False)
cursor = con.cursor()

# connecting to manage server
manager = info()
HOST = manager[0]
PORT = int(manager[1])
ADDR = (HOST,PORT)

manager = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
manager.connect((HOST,PORT))
data = manager.recv(2048)
manager.send(str(Client_Server_Side._port).encode())
