import socket
import threading
import time

server_port = 8000
server_host = socket.gethostbyname(socket.gethostname())
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_host)

server_socket.bind((server_host, server_port))
server_socket.listen(1)
prev = ''

def handle_client(client, address):
    print(f"{address} [CONNECTED]")
    global prev
    connected = True
    while connected:
        message = client.recv(1024).decode()
        
        headers = message.split()
        print(headers)
        filename = headers[1]
        
        if headers[0] != 'GET' or headers[2] != 'HTTP/1.1':
            response = 'HTTP/1.1 400 BAD REQUEST\n\nBad Request'

        elif filename != '/test.html':
            response = 'HTTP/1.1 404 NOT FOUND\n\n%s Not Found' % filename

        elif filename == '/test.html':
            webpage = open('.' + filename)
            content = webpage.read()
            if content != prev:
                prev = content
                webpage.close()
                response = 'HTTP/1.1 200 OK\n\n' + content 
            else:
                webpage.close()
                response = 'HTTP/1.1 304 NOT MODIFIED\n\nNot Modified'
            
        # Send HTTP response
        client.sendall(response.encode())
        client.close()
        connected = False


def init_server():
    server_socket.listen()
    while True:
        client, address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("starting server... ")
init_server()