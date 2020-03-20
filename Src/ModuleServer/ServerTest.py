from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        to_send = "Ca marche"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(to_send, "utf-8"))
serv = HTTPServer(('localhost', 8000), Server)
serv.serve_forever()
