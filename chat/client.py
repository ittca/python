import socket
import threading

nickname = input("Choose a nickname: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                print("helo")
            else:
                print(message)

        except:
            print("A tentar conectar ao servidor...")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.64', 55555))

client.send(nickname.encode('utf-8'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

