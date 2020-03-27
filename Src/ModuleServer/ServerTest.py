from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        to_send = "Ca marche" #il faut modifier cette var par le contenu des pages webs pour pouvoir les afficher
        if self.path =="/":
            self.path = "/test.html"
        try:
            with open(self.path[1:]) as f:
                to_send = f.read()
        except Exception as e:
            to_send = "Error page not found"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(to_send, "utf-8"))

    def do_POST(self):
        try:
            self.send_response(303)
            self.end_headers()

                print("ok")

        except Exception as e:
            pass
        #recevoir les informations de modification des plans, agir en conséquence puis renvoyer la page d'acceuil

serv = HTTPServer(('localhost', 8000), Server)
serv.serve_forever()
