from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import json

#la classe est un script qui permet de faire tourner un serveur python et d gérer des requêtes venant de script javascript
#testé sur windows 10 en 2020 sur python 3.7.5 et python 3.6.8


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        to_send = "Ca marche" #il faut modifier cette var par le contenu des pages webs pour pouvoir les afficher
        if self.path =="/":
            self.path = "/test.html"#redirige vers la page principale
        try:
            with open(self.path[1:]) as f:
                to_send = f.read() #lit le chemin dans la barre d'url et cherche une page avec ce nom dans les pages html à disposition
        except Exception as e:
            to_send = "Error page not found"
        self.send_response(200)# renvoie "tout va bien"
        self.end_headers()
        self.wfile.write(bytes(to_send, "utf-8"))# renvoie la page html à afficher

    def do_POST(self):
        try:
            self.send_response(303)
            self.end_headers()

            #print(self.headers)
            content_type, paramsdict = cgi.parse_header(self.headers["content-type"]) #analyse les infos primordiales de la requête type de contenu + autres arguments (encodage par exemple)

            if content_type == "application/json": #va décoder le json de la requête pour en faire un dictionnaire d'informations utilisables
                length = int(self.headers['content-length'])
                data = self.rfile.read(length).decode('utf-8')
                data = json.loads(data)
            

        except Exception as e:
            print("error")
            raise


serv = HTTPServer(('localhost', 8000), Server)#on lance le serveur
serv.serve_forever()
