import xml.dom.minidom as _m
import re
import lxml.html
import lxml.etree
import os

class GenPlan():
    """docstring forGenPlan."""

    def recup_plan(self, svg_path):
        future_boutons = {}
        image = _m.parse(svg_path)

        chambres = image.getElementsByTagName("rect") #on récupère tout ce qui s'apparente à une chambre
        for chambre in chambres:
            if re.match(r"Chambre\w?" ,chambre.attributes["id"].value) or re.match(r"Chambre\w?" ,chambre.attributes["inkscape:label"].value):#on vérifie que c'est bien une chambre
                chambre.setAttribute("onclick", "change_state(this);")
                chambre.setAttribute("class", "empty")
                style_sans_fill = re.sub(r"fill:#\w+;",'',chambre.getAttribute("style"))
                style_sans_fill_sans_stroke = re.sub(r"stroke:#\w+;",'',style_sans_fill)
                chambre.setAttribute("style", style_sans_fill_sans_stroke) #va permettre d'appeler la fonction javascript change_state lors du click
        #il est important de mettre l'argument "this" pour permettre au code javascript de reconnaître le bouton enquestion et le modifier
         #il y a un problème d'ordre: ls tyle de l'objet passe après la classe, ce qui fait que le style de la classe n'est paspris en compte
        #il faut donc régler cela en mettant supprimant la valeure stroke et fill du style de chaques chmabres

        return image.toxml()

    def new_plan(self, svg_path, nom_du_plan):
        #récupération des bouttons
        f_b = self.recup_plan(svg_path)
        root_node = lxml.html.parse("Plans/PlanSqueletteHTML.html")

        div = root_node.find(".//div[@id='main_plan']") #. = le noeud courant , // = tous les éléments à partir de ce noeud
        #donne donc: je cherche tous les enfants de div où div a pour id 'main_plan'
        el = lxml.html.fromstring(f_b) #on récupère les éléments créés
        div.append(el)# on l'ajoute à notre principale partie

        # partie enregistrement de l'image +
        path = f'Plans/HtmlFinalVersion/{nom_du_plan}.html'
        os.makedirs(os.path.dirname(path), exist_ok=True)#marche suelement avec python 3.2
        with open(path, "w") as f:
            f.write(lxml.html.tostring(root_node).decode("utf-8"))

        return path
g = GenPlan()
g.new_plan("Plans/Svg/Plantest.svg", "Superplan")
