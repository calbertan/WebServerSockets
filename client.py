import socket

server_port = 8000
server_host = socket.gethostbyname(socket.gethostname())

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Send the client request
request = "GET /test.html HTTP/1.1 \r\n"
client_socket.send(request.encode())

# Get HTTP response
response = client_socket.recv(1024)
print("From Server:", response.decode())

# Close socket
client_socket.close()