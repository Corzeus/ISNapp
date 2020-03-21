from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        to_send = "Ca marche" #il faut modifier cette var par le contenu des pages webs pour pouvoir les afficher
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(to_send, "utf-8"))

    def do_POST(self):
        pass
        #recevoir les informations de modification des plans, agir en conséquence puis renvoyer la page d'acceuil

serv = HTTPServer(('localhost', 8000), Server)
serv.serve_forever()
