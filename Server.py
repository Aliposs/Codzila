import threading
from socket import *
import _thread

# define port number and ip address
ip_address = "127.0.0.1"
port_number = 2004
# establish socket
sokt = socket(AF_INET, SOCK_STREAM)
# establish bind to socket
sokt.bind((ip_address, port_number))
# establish listen to server 
sokt.listen(5)
print("Server Established")
#_________________________________________________________________________________________________________
# create function to handle received messages
def receive_thread(sess):
    while True:
        message = sess.recv(2004)
        print("Client Message: ", message.decode('UTF-8'))
        

#create function to handle receiving and sending messages
def client_thread(c):
    receive = threading.Thread(target = receive_thread, args = (c,))
    receive.start()

    while True:
        c.send(input("Server: ".encode('UTF-8')))

#_________________________________________________________________________________________________________
#Confirm connection 
while True:
    session, address = sokt.accept()
    print("Currently, The Connection from:", address)
    #thread starts
    _thread.start_new_thread(client_thread, (session,))

