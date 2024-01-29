import http.server
import socketserver
import random
import time
import Reader

PORT = 8000

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            #Generate random num
            rand = random.randint(0, 100)
            rand = Reader.everything()

            #Display num on html webpage
            html_content = f"<html><head><title>Random Number Generator</title></head><body><h1>Random Number: {rand}</h1></body></html>"
            self.wfile.write(html_content.encode())

with socketserver.TCPServer(("", PORT), HTTPRequestHandler) as sserver:
    print(f"Server started on port: {PORT}")
    sserver.serve_forever()