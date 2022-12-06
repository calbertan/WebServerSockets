import socket
import time

server_port = 8000
server_host = socket.gethostbyname(socket.gethostname())
timeout = time.time() + 10 # timeout in 10 seconds
# Create client socket

while True:
  try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    break # this line will be ran if client_socket successfully connects (server exists)
  except ConnectionRefusedError:
    if time.time() > timeout:
      print("HTTP/1.1 408 REQUEST TIMEOUT\n\n%s REQUEST TIMEOUT")
      break

# Send the client request
# request = "GET /test.html HTTP/1.1 \r\n"
# client_socket.send(request.encode())


# FOR 400 BAD REQUEST
# bad_request = "GET /test.html HTTP/1.0 \r\n"
# client_socket.send(bad_request.encode())

# FOR 404 NOT FOUND
# unfound_request = "GET /te.html HTTP/1.1 \r\n"
# client_socket.send(unfound_request.encode())

# Get HTTP response
response = client_socket.recv(1024)
print("From Server:", response.decode())

# Close socket
client_socket.close()