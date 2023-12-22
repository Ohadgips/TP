import socket,_thread,os,sqlite3,subprocess,sys
sys.path.append("Client\Gui_py")
from socket import *
#from QtGUI import add_to_download,add_to_upload
from socket import socket
from PyQt5.QtWidgets import QListWidget,QDialog,QProgressBar
from os import remove
import time
from os.path import exists
global uploadpath,downloadspath,chunks_recived,cursor,con
chunks_recived = {}
# path for all downloads and uploads files
uploadpath = str("\Client\shared_files")
downloadspath = str("\Client\Downloads")
# connecting to database    
path = os.getcwd()    
file_name = path+"/shared_files.db"
con = sqlite3.connect(file_name,check_same_thread=False)
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE files (name TEXT NOT NULL, type TEXT NOT NULL,path TEXT ,size_in_KB REAL NOT NULL)")
except:
    print("already exists") 
# get free  port
def port():
    s = socket.socket(AF_INET,SOCK_STREAM)
    s.bind(("",0))
    s.listen()
    port = s.getsockname()[1]
    s.close()
    return int(port)



# disconnect if there is an error
def Error(client,addr):
    print("error,disconnected from: ",addr)
    client.close()

#temp
def save_info(HOST,PORT): #temp
    text = open("info.txt", "w")
    text.write(str(HOST)+"\n"+str(PORT))

# connect all the data
def connect(name,chunks,size):
    print(chunks)
    path = os.getcwd()
    try:
        fileM = open(path+downloadspath+"/"+name, "wb")
        full_path = path+downloadspath+"/"

    except:
        fileM = open(path+"/Downloads"+"/"+name, "wb") 
        full_path = path+"/Downloads"+"/"
    chunks_number = chunks
    #len(chunks) 
    chunk = 0
    
    # build the file together using all chunks
    while chunk < chunks_number:
        print(" - Chunk #" + str(chunk) + " done.")
        fileName = downloadspath + name+"$chunk_" + str(chunk) + "$.txt"
        
        #check if chunk exists if not stop the connect process
        if exists(path+downloadspath+"/"+name+"$chunk_" + str(chunk) + "$.txt"):
            fileName = path+downloadspath+"/"+name+"$chunk_" + str(chunk) + "$.txt"
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            fileTemp = open(fileName, "rb")
            byte = fileTemp.read(2048)
            fileM.write(byte)
            fileTemp.close()
            remove(fileName)
            chunk += 1
        elif exists(path+"/Downloads"+"/"+ name+"$chunk_" + str(chunk) + "$.txt") :
            fileName =  path+"/Downloads"+"/"+ name+"$chunk_" + str(chunk) + "$.txt"
            os.makedirs(os.path.dirname(fileName), exist_ok=True)
            fileTemp = open(fileName, "rb")
            byte = fileTemp.read(2048)
            fileM.write(byte)
            fileTemp.close()
            remove(fileName)
            chunk += 1
        else:
            print("a chunk is missing")
            fileM.close() 
            remove(full_path+name)
            chunks_status = 0
            break
# delete all chunks because already have the file connected
    if chunk >= chunks_number:
        chunks_status = chunks_number    
        while chunk > 0:
            fileName = full_path + name+"$chunk_" + str(chunk) + "$.txt"
            if exists(fileName):
                remove(fileName)
            chunk = chunk -1        
        update_database(name,path,size)
    else:
        print("")            
    return str(full_path+name),chunks_status

# update personal db if files got downloaded of uploaded to the client device
def update_database(name,path,size = None):
    print(size)
    split = name.split(".")
    if len(split) > 2:
        name = split[0]+"."+split[1]
        type = split[2]
    else:
        name = split[0]
        type = split[1]
    #if size != None:        
        #size = float(int(size) / 1024)
    cursor.execute("INSERT INTO files (name , type ,Path,size_in_KB) VALUES ('"+name+"', '"+type+"','"+path+"' ,'"+str(size)+"')")
    con.commit()


#----------------------------------------------------------------- server ------------------------------------------------------------------------
import PyQt5,socket,os,_thread,pickle,sqlite3
from PyQt5 import QtWidgets

#get info from txt about the port
def info():
    text = open("Manager/client.txt", "r")
    text = str(text.read()).split('\n')
    return text

#split file to chunks
def split_file(name,size = None,path=None):
    file_name = name
    chunknames = []
    if path != None:
        fileR = open(path, "rb")
    else:
        path = os.getcwd()
        try:
            fileR = open(path+uploadpath+"/"+name, "rb")
            path = path+uploadpath+"/"+name
        except:
            try:
                fileR = open(path+"/shared_files"+"/"+name, "rb")
                path = path+"/shared_files"+"/"+name
            except:
                try:
                    fileR = open(path+downloadspath+"/"+name, "rb")
                    path = path+downloadspath+"/"+name
                except:
                    try: 
                        fileR = open(path+"/Downloads"+"/"+name, "rb") 
                        path = path+"/Downloads"+"/"+name
                    except:
                        file_name = name.split(".")[0]
                        print(file_name)
                        cursor.execute("SELECT path FROM files WHERE name = ?",(file_name,))
                        path = cursor.fetchone()
                        fileR = open(path[0],'rb')
    chunk = 0
    #update database
    cursor.execute("SELECT name FROM files WHERE name = ?",(file_name,))
    result = cursor.fetchone()
    if result == None:
        update_database(name,path,size)
    byte = fileR.read(2048)
    while byte:
 
        # Open a temporary file and write a chunk of bytes
        fileN = str(name) +"$chunk_" + str(chunk) + "$.txt".encode('utf-8').decode('utf-8')
        path = os.getcwd()
        if os.path.exists(path+uploadpath+"/"+fileN) == False and os.path.exists(path+"/shared_files"+"/"+fileN) == False:
            try:
                fileT = open(path+uploadpath+"/"+fileN, "wb") 
            except:
                fileT = open(path+"/shared_files"+"/"+fileN, "wb")    
            fileT.write(byte)
            fileT.close()
        chunknames.append(fileN)
        
        byte = fileR.read(2048)
        chunk += 1
    return chunknames

# update the manager about received files
def update_manager(manager,name,file_type,size,chunks = None):
    manager.send("UPDATE_FILES".encode())
    data = manager.recv(2048).decode()
    
    msg = name+"$$$"+file_type+"$$$"+str(size)+"$$$"+str(chunks)
    manager.send(msg.encode())  
    data = manager.recv(2048).decode()
    if data == 'OK':
        print("manager updated")
    else: 
        update_manager(name,file_type,size)  





# send chosen file to all connected users
def send_files_to_users(filename,type,addr,chunks,full_size):
    print("send_files_to_users")
    client = socket.socket(AF_INET,SOCK_STREAM)
    #print(addr)
    client.connect(addr)
    client.send("UPLOAD".encode())
    print(client.recv(2048).decode())
    msg = filename +"$$$"+str(full_size)
    client.send(msg.encode())
    for file_name in chunks:
        path = os.getcwd()
        try:
            file = open(path+uploadpath+"/"+file_name, "rb")
            file_size = os.path.getsize(path+uploadpath+"/"+file_name)

        except:
            file = open(path+"/shared_files"+"/"+file_name, "rb")
            file_size = os.path.getsize(path+"/shared_files"+"/"+file_name)   
        
        file_size = str(file_size)
        
        msg = file_name+"$$$"+type+"$$$"+file_size
        client.send(msg.encode().strip())
        data = client.recv(2048).decode()
        print(data)
        if data == 'REJECT':
            break
        else:
            data = file.read()
            client.sendall(data)
            file.close() 
    client.close()

# send chosen file to the user (download)
def send_file(addr,file_name,chunks_lst):
    print("send_file")
    chunks = split_file(file_name)
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(addr)
    client.send("DOWNLOAD".encode())
    print(client.recv(2048).decode())
    msg = file_name +"$$$"+str(len(chunks))
    client.send(msg.encode('utf-8'))
    num = 0

    path = os.getcwd()

    name = file_name.split(".")[0]
    file_type = file_name.split(".")[1]
    for file_name in chunks:
        if str(num) in chunks_lst:
            try:
                file = open(path+uploadpath+"/"+file_name, "rb")
                file_size = os.path.getsize(path+uploadpath+"/"+file_name)

            except:
                file = open(path+"/shared_files"+"/"+file_name, "rb")
                file_size = os.path.getsize(path+"/shared_files"+"/"+file_name)   
            msg = file_name+"$$$"+"txt"+"$$$"+str(file_size)
            print(msg)
            #try:
            client.send(msg.encode('utf-8'))
            data = client.recv(2048).decode()
            data = file.read()
            client.sendall(data)
            print("NEXT\n")
            file.close()
            chunks_lst.remove(str(num))
            '''
            except ConnectionAbortedError or ConnectionRefusedError:
                print("try again",chunks)
                send_file(addr,name+"."+file_type,chunks_lst)
                #else: break '''
        num += 1         
    client.close()                       

def connect_to_servers(_port,name,server_address,chunks_numbers):
    print("connect_to_servers")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(server_address)
    server.send("GET".encode())
    server.recv(2048)
    msg = str(_port)+"$$$"+name + "$$$" #CHECK
    for num in chunks_numbers:
        msg = msg + str(num)+","
    print(msg,sys.getsizeof(msg))
    server.send(str(sys.getsizeof(msg)).encode())
    server.recv(2048)
    server.send(msg.encode())
    server.close()

def download_files(manager):
        manager.send("DOWNLOAD".encode())
        try:
            files = pickle.loads(manager.recv(2048))
        except:
            files  = []
        return files






"""def upload_speed():
    import speedtest
    speed_test = speedtest.Speedtest(secure=True)
    upload_speed = speed_test.upload()"""

"""def best_download(users):
    return users"""



# active server
#_thread.start_new_thread(server())



"""def start_client():
    # connecting to database    
    file_name = "shared_files.db"
    con = sqlite3.connect(file_name,check_same_thread=False)
    cursor = con.cursor()
    try:
        cursor.execute("CREATE TABLE files (name TEXT NOT NULL, type TEXT NOT NULL, size_in_KB REAL NOT NULL)")
    except:
        print("already exists")    
    #uploadspeed = upload_speed()
    global host,port_,manager
    host = gethostbyname(gethostname())
    port_ = port()  
    # connecting to manage server
    HOST = '10.100.102.13'
    PORT = 54200
    ADDR = (HOST,PORT)
    manager = socket.socket(AF_INET,SOCK_STREAM)
    print(ADDR)
    manager.connect(ADDR)
    data = manager.recv(2048)
    manager.send(str(port_).encode())
    manager.send("SPEED".encode())
    data = manager.recv(2048).decode()
    if data != "OK":
        print("error")
    else:    
        manager.send(str(uploadspeed).encode())

    ADDR = (host,port_)
    save_info(host,port_) #temp
    server = socket.socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    data = b''
    manager.send(str(port_).encode())
    while True:
        accept_conns(server)
    con.close()
    server.close()
"""