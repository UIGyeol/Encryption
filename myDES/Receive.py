import socket
from DES import myDES

HOST = 'localhost'
PORT = 8081


def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT)) 
        sock.sendall(filename.encode()) 
        key = sock.recv(8) 
        iv = sock.recv(8) 
        data = sock.recv(1024) 

        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 오류 발생'%filename)
            return

        with open(filename+'.des-CBC','wb') as f:
            try:
                
                des = myDES(key.decode(),iv.decode()) 

                
                while data:
                    des = des.decrypt_CBC(data)
                    f.write(des)
                    data_transferred +=len(data)
                    data = sock.recv(1024)


            except Exception as e:
                print(e)

            print('파일 [%s]전송 종료. 전송량: [%d]' %(filename, data_transferred))

getFileFromServer('example.txt')