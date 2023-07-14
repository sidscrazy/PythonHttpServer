from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8585)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port 8585')
    httpd.serve_forever()

if __name__ == '__main__':
    run()