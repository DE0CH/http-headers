from http.server import BaseHTTPRequestHandler, HTTPServer

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Write the headers sent by the client to the response
        for header, value in self.headers.items():
            response = f"{header}: {value}\n"
            self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=EchoHandler, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
