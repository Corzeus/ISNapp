import sqlite3

class DataManager():
    """ Il y aura qautres tables dans la base de données:
    - une pour les plans avec trois champs: nom->texte, id->entier, chambres->texte
    - une pour les chambres avec quatre champs: nom->texte, id->entier, état->texte, lits->texte
    - une pour les lits avec deux champs: id->entier, état->texte
    - une pour tenir à jour les id: plans, chambres, lits"""
    def __init__(self):
        self.conn = sqlite3.connect("Data/data.db")
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    def new_chambre(self, caracs):
        #caracs est un dictionnaire contenant: {nom":?, "etat":?, "lits":[?]}
        caracs["id"] = self.determiner_id("chambres")
        cmd = "INSERT INTO chambres VALUES (:nom,:id, :etat, :lits)"
        self.c.execute(cmd, caracs)
        self.conn.commit()
        return caracs["id"]

    def new_plan(self, caracs):
        #caracs est un dictionnaire contenant: {nom":?, "chambres":[?]}
        caracs["id"] = self.determiner_id("plans")
        cmd = "INSERT INTO plans VALUES (:nom,:id, :chambres)"
        self.c.execute(cmd, caracs)
        self.conn.commit()
        return caracs["id"]

    def get_chambre(self, id):
        list_args = ["nom", "id", "etat", "lits"]
        self.c.execute("SELECT * FROM chambres WHERE id=:id", {'id':id})
        row = self.c.fetchone()
        if row != None:
            Data = {}
            for i in range(len(list_args)):
                Data[list_args[i]] = row[i]
            return Data
        else:
            return "NoChambreData"

    def get_plan(self, id):
        list_args = ["nom", "id", "chambres"]
        print(id)
        self.c.execute("SELECT * FROM plans WHERE id=:id", {'id':id})
        row = self.c.fetchone()
        if row != None:
            Data = {}
            for i in range(len(list_args)):
                Data[list_args[i]] = row[i]
            return Data
        else:
            return "NoPlanData"

    def determiner_id(self, table):
        #fonction qui détermine une id UNIQUE pour chaques membres de la base de données
        data_to_send = {}
        cmd = "SELECT * FROM id"
        self.c.execute(cmd)
        ids = self.c.fetchone()
        id_disponible = ids[table]
        for key in ids.keys():
            data_to_send[key] = ids[key]
        data_to_send[table]+=1
        cmd = "UPDATE id SET plans=:plans, chambres=:chambres, lits=:lits"
        self.c.execute(cmd, data_to_send)
        self.conn.commit()
        return id_disponible
