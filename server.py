from http.server import SimpleHTTPRequestHandler, HTTPServer

class IPLoggingHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        client_ip = self.client_address[0]
        print(f"Request from IP: {client_ip} - {self.requestline}")

PORT = 8000
httpd = HTTPServer(('0.0.0.0', PORT), IPLoggingHandler)
print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()