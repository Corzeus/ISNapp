import xml.dom.minidom as _m
import re
import lxml.html
import lxml.etree
import os
import Data

class GenPlan():
    """docstring forGenPlan."""
    Data = Data.DataManager()

    def recup_plan(self, svg_path):
        list_chambres_id = []
        image = _m.parse(svg_path)

        chambres = image.getElementsByTagName("rect") #on récupère tout ce qui s'apparente à une chambre
        for chambre in chambres:
            if re.match(r"Chambre\w?" ,chambre.attributes["id"].value):#on vérifie que c'est bien une chambre
                #partie storage des informations
                caracs = {
                          "nom":chambre.attributes["id"].value,
                          "etat": "vide",
                          "lits": "" #vide pour l'instant car les lits n'ont pas encore été implémentés
                }
                id = self.Data.new_chambre(caracs)
                list_chambres_id.append(str(id))
                chambre.setAttribute("id_data", str(id))

                #Partie "front-end" et intéraction avec l'utilisateur
                chambre.setAttribute("onclick", "change_state(this);")
                chambre.setAttribute("class", "vide")
                style_sans_fill = re.sub(r"fill:#\w+;",'',chambre.getAttribute("style"))
                style_sans_fill_sans_stroke = re.sub(r"stroke:#\w+;",'',style_sans_fill)
                chambre.setAttribute("style", style_sans_fill_sans_stroke) #va permettre d'appeler la fonction javascript change_state lors du click
        #il est important de mettre l'argument "this" pour permettre au code javascript de reconnaître le bouton enquestion et le modifier
         #il y a un problème d'ordre: le style de l'objet passe après la classe, ce qui fait que le style de la classe n'est paspris en compte
        #il faut donc régler cela en mettant supprimant la valeure stroke et fill du style de chaques chambres



        return image.toxml(), list_chambres_id

    def new_plan(self, svg_path, nom_du_plan):
        #récupération des bouttons
        f_b, list_chambres_id = self.recup_plan(svg_path)
        root_node = lxml.html.parse("Data/PlanSqueletteHTML.html")

        div = root_node.find(".//div[@id='main_plan']") #. = le noeud courant , // = tous les éléments à partir de ce noeud
        #donne donc: je cherche tous les enfants de div où div a pour id 'main_plan'
        el = lxml.html.fromstring(f_b) #on récupère les éléments créés
        div.append(el)# on l'ajoute à notre principale partie


        caracs_plan = {
                       "nom":nom_du_plan,
                       "chambres": "|".join(list_chambres_id)
        }
        id = self.Data.new_plan(caracs_plan)
        body = root_node.find(".")[0]
        body.attrib["id_data"] = str(id)
        body.attrib["onload"] = "load();"
        nom = root_node.find(".//label[@class='name_plan']")
        nom.text = nom_du_plan

        # partie enregistrement de l'image +
        path = f'Plans/{nom_du_plan}.html'
        os.makedirs(os.path.dirname(path), exist_ok=True)#marche suelement avec python 3.2
        with open(path, "w") as f:
            f.write(lxml.html.tostring(root_node).decode("utf-8"))

        return path
g = GenPlan()
chemin = input("Rentrez le chemin vers votre plan (avec le nom et l'extension du plan) : ")
nom_de_sortie = input("Rentrez le nom de sortie que vous voulez lui attribuer : ")
g.new_plan(chemin, nom_de_sortie)
fin = input("Génération terminée...")
