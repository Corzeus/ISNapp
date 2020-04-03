const form = document.getElementById("f");
form.addEventListener("submit", (e) => {
  e.preventDefault();

  var data = {'username':'jean-paul'};

  var rq = new XMLHttpRequest();

  rq.onreadystatechange = function(){
    if (this.readystate == 4 && this.status == 200){
      console.log(form);
    }
  };

  rq.open("POST", true);
  //rq.responseType = "json";
  rq.setRequestHeader("Content-Type", "application/json");

  rq.send(JSON.stringify(data));

  return false;
})
