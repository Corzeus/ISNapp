function change_state(ele) {
    if (ele.className.baseVal == "vide") {
      ele.className.baseVal  = "occupe";
    }
    else if (ele.className.baseVal == "occupe") {
      ele.className.baseVal = "inaccessible";
    }
    else if (ele.className.baseVal == "inaccessible") {
      ele.className.baseVal = "vide";
    }
}

function load(){
  var fileName = location.href.split("/").slice(-1)[0];
  var src = fileName.split(".")[0];
  var body = document.getElementsByTagName("body")[0];
  id = body.getAttribute("id_data");

  cmd = "?id="+id;
  var data = {};
  //Envoie de la commande pour recevoir les infos de la base de données
  var rq = new XMLHttpRequest();
  rq.onreadystatechange = function(){
    if ( this.status == 200){
      data = rq.response;
      if (data!=null){var keys = Object.keys(data);
      if (keys.includes("nom")){
        if (data["nom"]=="EnvoieDesInfosFrontEnd") {
          console.log(data);
          chambres_plan = document.getElementsByTagName('rect');
          delete data["nom"];
          for (var i = 0; i < data.chambres.length; i++) {
            for (var j = 0; j < chambres_plan.length; j++){
              if (data["chambres"][i]["id"]==chambres_plan[j].getAttribute("id_data")){
                chambres_plan[j].className.baseVal = data["chambres"][i]["etat"];
              }
            }
          }}}
    }}

  };

  rq.open("GET", cmd);
  rq.responseType = 'json';
  rq.send();
}

function send(){
  //partie récupération des données de  la page
  var possibles_chambres = document.getElementsByTagName("rect");
  console.log(possibles_chambres);
  var tous_les_etats = ["vide", "occupe", "inaccessible"];
  var chambres=[];
  for (var i =0; i<possibles_chambres.length; i++){
    if (tous_les_etats.includes(possibles_chambres[i].className.baseVal)){
      chambres.push(possibles_chambres[i]);
    }
  };
  //partie création des données d'envoi
  var data = {};
  chambres.forEach(item => {
    data[item.getAttribute("id_data")] = item.className.baseVal;
  });
  data["nom"] = "RetourDesDonneesDeLaPage";
  //partie envoie des informations au serveur
  var rq = new XMLHttpRequest;
  rq.open("POST", true);
  rq.setRequestHeader("Content-Type", "application/json");
  rq.send(JSON.stringify(data));
}
