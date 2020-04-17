import xml.dom.minidom as _m
import re
import lxml.html

class GenPlan():
    """docstring forGenPlan."""

    def __init__(self):
        pass

    def recup_bouttons(self, svg_path):
        future_boutons = {}
        image = _m.parse(svg_path)

        chambres = image.getElementsByTagName("rect")
        for chambre in chambres:
            if re.match(chambre.attributes["id"].value, "Chambre\w"):
                future_boutons[chambre.attributes["id"]] = chambre.toxml()

        for buttons in future_boutons.keys():
            i = f'<button id="{buttons}"> <svg>{future_boutons[buttons]}</svg> </button>'
        return future_boutons

    def new_plan(self, svg_path, nom_du_plan):
        #récupération des bouttons
        f_b = self.recup_bouttons(svg_path)

        content = ""
        with open("PlanSqueletteHTML.html", "r") as f:
            content = f.read()
        root_node = lxml.html.fromstring(content)

        div = root_node.find(".//div[@id='main_plan']") #. = seulement les enfants du node qui cherche, // = tous les éléments

        for i in f_b:
            el = lxml.html.fromstring(i) #on récupère les éléments créés
            div.append(el)

        with open(f'{nom_du_plan}.html', "w") as f:
            f.write(lxml.html.tostring(root_node))
t = GenPlan()

t.new_plan("Plantest.svg", "Superplan")
