from socket import *
import _thread,sqlite3,pickle,math,ssl
global con,clients_speed
clients_speed = []
# get free port
def port():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(("",0))
    s.listen()
    port = s.getsockname()[1]
    s.close()
    return int(port)

#update db when disconnecting or connecting to server
def update_database(addr,serverport,status):
    check = cursor.execute("SELECT IP FROM users WHERE IP = '"+addr[0]+"'").fetchall()
    
    if status == 'Connected':
        if check != []:
            sql = "UPDATE users Set STATUS = (?), PORT = (?), SERVER_PORT = (?) WHERE IP = (?)"
            args = (status,str(addr[1]),str(serverport),str(addr[0]))   
            cursor.execute(sql,args)
        else:
            sql ="INSERT INTO users (IP, PORT, SERVER_PORT, STATUS) VALUES (?, ?, ?, ?)"
            args = (str(addr[0]),str(addr[1]),str(serverport),status)   
            cursor.execute(sql,args)
    
    elif status == 'Disconnected':
        sql = "UPDATE users Set STATUS = ? WHERE IP = ? "
        args = (status,str(addr[0]))   
        cursor.execute(sql,args)
    con.commit()


# Error disconnction                     
def error_disconnect(client,serverport,addr):
    print("error,disconnected from: ",addr)
    update_database(addr,serverport,'Disconnected')
    client.close()

#temp
def save_info(HOST,PORT):
    text = open("client.txt", "w")
    text.write(str(HOST)+"\n"+str(PORT))


#when client ask to upload give him all connected clients and add the file to the shared_files db
def to_upload(client,ip,serverport):
    print("to_upload") #DEBUG
    details = client.recv(2048).decode().split("$$$")
    print(details) #DEBUG
    sql = "SELECT IP FROM files WHERE NAME = ? AND TYPE = ? AND SIZE_KB =?"
    args = (str(details[0]),str(details[1]),details[2])
    cursor.execute(sql,args)
    result = cursor.fetchall()
    print(result)
    if result == []:
        sql = "INSERT INTO files (IP, SERVER_PORT, NAME, TYPE, SIZE_KB) VALUES (?,?,?,?,?)"
        args = (str(ip),str(serverport),str(details[0]),str(details[1]),details[2])
        cursor.execute(sql,args)
        con.commit()
    print("DONE1") #DEBUG
    cursor.execute("SELECT IP,SERVER_PORT FROM users WHERE STATUS = 'Connected' ")
    result = cursor.fetchall()
    print("done") #DEBUG
    print(result)
    data = pickle.dumps(result)
    client.send(data)
    print("SEND") #DEBUG

# when client ask to upload give him all connected clients that has the file/part of it
def files_to_download(client,addr):
    print("download")
    cursor.execute("SELECT IP FROM users WHERE STATUS = 'Connected'")
    result = cursor.fetchall()
    print(result)
    files= []
    if len(result) > 1:
        cursor.execute("SELECT files.name , files.type FROM files JOIN users ON files.IP = users.IP WHERE users.STATUS = 'Connected' GROUP BY files.name ORDER BY files.name ")
        result = cursor.fetchall()
        print(result)
        for file in result:
            files.append(str(file[0]+"."+str(file[1]).lower()))
    print(files)        
    data = pickle.dumps(files)
    client.send(data)

def users_that_has_files(client,addr):
    client.send("OK".encode())    
    data = client.recv(2048).decode()
    print(data)
    name = data
    cursor.execute("SELECT files.IP, files.SERVER_PORT, files.NUMBER_OF_PARTS,files.SIZE_KB FROM files JOIN users ON files.IP = users.IP WHERE users.STATUS = 'Connected' AND files.name = '"+data+"' ")
    result = cursor.fetchall()
    print(result)
    data = pickle.dumps(result)
    client.send(data)
    cursor.execute("SELECT SIZE_KB FROM files WHERE NUMBER_OF_PARTS IS NULL AND name = ?",(name,))
    result = cursor.fetchone()
    print(result)
    client.send(str(result[0]).encode())
    print(client.recv(2048).decode())
    if result[0] < 2:
        chunks = 1
    else:    
        print(math.ceil(float(int(result[0]) / 2)))
        chunks = math.ceil(float(int(result[0]) / 2))
    print(chunks)
    client.send(str(chunks).encode())    


def update_about_files(client,ip,serverport):
    client.send("UPDATE_FILES".encode())
    details = client.recv(2048).decode()
    if details != '':
        details = details.split("$$$")
        client.send("OK".encode())
        print(details)
        print(" "+ip+"  "+serverport)
        details[2] = float(details[2]) / 1024
        if str(details[3]) != 'None':
            cursor.execute("INSERT INTO files (IP, SERVER_PORT, NAME, TYPE, SIZE_KB, NUMBER_OF_PARTS) VALUES ('"+str(ip)+"','"+str(serverport)+"','"+str(details[0])+"', '"+str(details[1])+"', '"+str(details[2])+"', '"+str(details[3])+"')")
        else:
            cursor.execute("INSERT INTO files (IP, SERVER_PORT, NAME, TYPE, SIZE_KB) VALUES ('"+str(ip)+"','"+str(serverport)+"','"+str(details[0])+"', '"+str(details[1])+"', '"+str(details[2])+"')")
        con.commit()

#handle clients at once 
def clients_handler(client,addr):
    client.send("Hi".encode())
    serverport= client.recv(2048).decode() #save server port and not client port
    print(addr[0])
    cursor.execute("SELECT IP FROM files WHERE IP = ?",(addr[0],))
    if cursor.fetchone() != None:
        cursor.execute("UPDATE files SET SERVER_PORT = ? WHERE IP = ? ",(serverport,addr[0]))
        con.commit()
    update_database(addr,serverport,'Connected')
    while True:
        #try:
            data = client.recv(2048)
            message = data.decode('utf-8')
            print(message)
            if message == 'BYE':
                client.send("Disconnected".encode())
                break
            if message == 'DOWNLOAD':
                files_to_download(client,addr)
            if message == 'SPEED':
                clients_speed.append((addr[0],serverport,client.recv(2048).decode()))
                print(clients_speed)    
            elif message == "DOWNLOAD_2":
                users_that_has_files(client,addr)    
            elif message == 'UPLOAD':
                to_upload(client,addr[0],serverport) 
            elif message == 'UPDATE_FILES':
                update_about_files(client,addr[0],serverport)
            else:
                print(message)    
        #except:
            #error_disconnect(client,serverport,addr)
            #break
             
    #update_database(addr[0],serverport,'Disconnected')
    client.close()
def accept_conns(serversock):
    Client, addr = serversock.accept()
    print('New Connection: ' + addr[0] + ' , ' + str(addr[1]))
    _thread.start_new_thread(clients_handler, (Client,addr))

file_name = "users.db"
con = sqlite3.connect(file_name,check_same_thread=False)
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE users (IP TEXT, PORT TEXT ,SERVER_PORT TEXT,STATUS TEXT)")
except:
    print("already exists no need to create again")    
try:
    cursor.execute("CREATE TABLE files (IP TEXT ,SERVER_PORT TEXT, NAME TEXT,TYPE TEXT,SIZE_KB INTEGER, NUMBER_OF_PARTS INTEGER NULL)")
except:
    print("already exists no need to create again")  

global active_clients

HOST = gethostbyname(gethostname())
print(HOST)
PORT = 54200
(HOST,PORT)#temp
BUFSIZ = 2048
ADDR = (HOST,PORT)
print(ADDR)
serversock = socket(AF_INET,SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(3)
active_clients = []
while True:
     accept_conns(serversock)                                                    
con.close()               
serversock.close()                