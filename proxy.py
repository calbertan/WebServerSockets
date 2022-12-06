import socketserver
import http.server
import urllib
import requests

PORT = 7070

class MyProxy(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    #print("request received from some browser')
    url = self.path[1:]
    self.send_response(200)
    self.end_headers()
    self.copyfile(urllib.urlopen(url),self.wfile)

# requests.get("https://", proxies=)
httpd = socketserver.ForkingTCPServer(('',PORT), MyProxy)
print("Listening...")
httpd.serve_forever()