import socket,_thread,os,sqlite3
from socket import *
from os import remove
from os.path import exists
global uploadpath,maxsize,downloadspath,HOST

# path for all downloads and uploads files
uploadpath = str(r"shared_files/")
downloadspath = str(r"Downloads/")

# get free  port
def port():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(("",0))
    s.listen()
    port = s.getsockname()[1]
    s.close()
    return int(port)

maxsize = 1 * 1000000000

# disconnect if there is an error
def Error(client,addr):
    print("error,disconnected from: ",addr)
    client.close()

#temp
def save_info(HOST,PORT): #temp
    text = open("Client/"+"info.txt", "w")
    text.write(str(HOST)+"\n"+str(PORT))

# connect all the data
def connect(name,chunks,size):
    
    fileM = open(downloadspath+name, "wb")
    chunks_number = len(chunks) 
    chunk = 0
    
    # build the file together using all chunks
    while chunk <= chunks_number:
        print(" - Chunk #" + str(chunk) + " done.")
        fileName = downloadspath + name+"$chunk_" + str(chunk) + "$.txt"
        
        #check if chunk exists if not stop the connect process
        if exists(fileName):
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
            remove(name)
            break
    
    # delete all chunks because already have the file connected
    if chunk >= chunks_number:    
        while chunk > 0:
            fileName = downloadspath + name+"$chunk_" + str(chunk) + "$.txt"
            if exists(fileName):
                remove(fileName)
            chunk = chunk -1        
        update_database(name,size)
    else:
        print("")            

# update personal db if files got downloaded of uploaded to the client device
def update_database(name,size):
    split = name.split(".")
    if len(split) > 2:
        name = split[0]+"."+split[1]
        type = split[2]
    else:
        name = split[0]
        type = split[1]    
    size = float(int(size) / 1024)
    print(size)
    cursor.execute("INSERT INTO files (name , type , size_in_KB) VALUES ('"+name+"', '"+type+"', '"+str(size)+"')")
    con.commit()

# get all chunks from the other clients in the end connect all
def get_files(client,addr):
    # get file name and number of chunks
    data = client.recv(2048).decode().split(" ")
    print(data)
    name = data[0]
    chunks = data[1]
    chunks = eval(chunks)
    
    file_size_name = client.recv(1024).decode().split("$$$")
    file_size = 0
    file_name = file_size_name[0]
    while file_name != '' and file_name != 'END':
        file_size = int(file_size_name[1]) + file_size
        os.makedirs(os.path.dirname(downloadspath+file_name), exist_ok=True)
        file = open(downloadspath+file_name, "wb")
        file_bytes = b""
        data = client.recv(2048)
        file_bytes += data
        file.write(file_bytes)
        file.close()
        
        # get next chunk
        try:
            file_size_name = client.recv(2048).decode().split("$$$")
        except:
            Error(addr,client)

    client.close()
    connect(name,chunks,file_size) # need to only connect when have all chunks !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# get all upload file if not passing the size limit default is 1 gb can be changed in the settings(GUI)
def shared_files(client,addr):#manager
    
    # get file name and number of chunks
    data = client.recv(2048).decode().split(" ")
    print(data)
    name = data[0]
    chunks = data[1]
    chunks = eval(chunks)
    
    # get size of chunk if more than the max then stop receiving
    full_size = 0
    file_size_name = client.recv(1024).decode().split("$$$")
    file_name = file_size_name[0].strip("$")
    print(file_size_name)
    while file_name != '' and file_name != 'END':
        file_size = file_size_name[1].strip("$")
        print(file_size)
        
        #reject stop receiving
        if maxsize - int(file_size) <= 0:
            client.send("REJECT".encode())
            break
        
        # accept
        else:
            client.send("ACCEPT".encode())
            maxsize = maxsize - int(file_size)
            full_size = full_size + int(file_size)
            #save file
            os.makedirs(os.path.dirname(uploadpath+file_name), exist_ok=True)
            file = open(uploadpath+file_name, "wb")
            file_bytes = b""
            data = client.recv(2048)
            file_bytes += data
            file.write(file_bytes)
            file.close()
            
            #update database
            update_database(file_name,file_size)
            
            #get next chunk
            try:
                file_size_name = client.recv(2048).decode().split("$$$")
            except:
                break    
            file_name = file_size_name[0]
    
    client.close()
    #to update the
    return file_name,full_size
    #manager.send("UPDATE_FILES")
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
            get_files(client,addr)
            break 
        
        # get upload file
        elif message == 'UPLOAD':
            shared_files(client,addr)
            break
        else:
            break      
      print('Disconnected: ' + addr[0] + ' , ' + str(addr[1]))
      client.close()

# connect to db and create the table if needed
file_name = "shared_files.db"
con = sqlite3.connect(file_name,check_same_thread=False)
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE files (name TEXT NOT NULL, type TEXT NOT NULL, size_in_KB REAL NOT NULL)")
except:
    print("already exists no need to create again")

global host,port_
host = gethostbyname(gethostname())
port_ = port()
ADDR = (host,port_)
save_info(host,port_) #temp

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen()
data = b''
while True:
     accept_conns(server)
con.close()
server.close()