import socket
HOST = '192.168.1.11'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        s.sendall(f'Hello This is msg{i}'.encode('utf-8'))
        data =s.recv(1024).decode('utf-8')
        print(f'Recieved {data}')

        