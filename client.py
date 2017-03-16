import socket
import _thread
import sys

BUFFER_SIZE = 1024

s = socket.socket()
s.connect(("localhost",9999))
f = open ("pol.jpg", "rb")
l = f.read(1024)

while (l):
    s.send(l)
    l = f.read(1024)

data = s.recv(BUFFER_SIZE)
# def recv(s):
#     while True:
#          data = s.recv(1024)
#         #  if not data: sys.exit(0)
#          print(data.decode('utf-8'))

# # Thread(target=recv).start()
# _thread.start_new_thread(recv, (s,))



# data = s.recv(BUFFER_SIZE)
# print(data.decode('utf-8'))
# s.close()



