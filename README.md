This project is a simple showcase of socket programming that shows the server and client model. The client.py has several requests that should be commented out depending on the type of request that want to be sent. The server will be able to handle multiple clients and will display the number of connected users as they connect. This is done by using a multi-threaded approach, where a server will assign each client with a thread.

How to Run:
1. Comment out the desired request in client.py
2. Run server.py
3. Run client.py

There is also a proxy server implementation that requires proxy.py to run. We treat the proxy as a dictionary with filename as the key and the HTML content as the value. It works although this might not be the best implementation. If the file is found in this proxy, then the client does not need to interact with the server and use the proxy file instantly. If not found, the client will just request from the server as usual.

 
