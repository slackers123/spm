import rsa
import socket

HOST = '127.0.0.1'
PORT = 1410

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn = None
addr = None
publicKey = None
privateKey = None
# message = "hello geeks"
#
# encMessage = rsa.encrypt(message.encode(),
#                          publicKey)
#
# decMessage = rsa.decrypt(encMessage, privateKey).decode()

def setup():
    publicKey, privateKey = rsa.newkeys(512)
    print(publicKey)
    s.bind((HOST, PORT))
    print("bound to " + str(HOST) + " at port " + str(PORT))

def listenForConnection():
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(publicKey)

if __name__ == '__main__':
    setup()
    print("Listening for connection")
    listenForConnection()
