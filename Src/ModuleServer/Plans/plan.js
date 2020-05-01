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
  //Envoie de la command pour recevoir les infos de la base de données
  var rq = new XMLHttpRequest();
  rq.onreadystatechange = function(){
    console.log("ok");
    if ( this.status == 200){
      data = rq.response;
      chambres_plan = document.getElementsByTagName('rect');
      for (var i = 0; i < data.chambres.length; i++) {
        for (var j = 0; j < chambres_plan.length; j++){
          if (data["chambres"][i]["id"]==chambres_plan[j].getAttribute("id_data")){
            chambres_plan[j].className.baseVal = data["chambres"][i]["etat"];
          }
        }

      }
    }
  };

  rq.open("GET", cmd);//"/Plans/HtmlFinalVersion/"+src+
  rq.responseType = 'json';
  rq.send();
  console.log(data);

}
