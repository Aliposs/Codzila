from socket import *
from threading import *


# create function to handle received messages
def receive_thread(Mass):
    while True:
        message = Mass.recv(2004)
        print("Server Message: ", message.decode('UTF-8'))
#________________________________________________
# establish socket
sokt = socket(AF_INET, SOCK_STREAM)
# define port number and ip address
ip_address = "192.168.56.1"
port_number = 2004
sokt.connect((ip_address, port_number))
print("Connection Successed!")
if __name__ == "__main__":
   # thread starts
   receive = Thread(target=receive_thread, args=(sokt,))
   receive.start()

   while True:
        sokt.send(input("Client: ").encode('UTF-8'))


