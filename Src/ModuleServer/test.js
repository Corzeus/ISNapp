const form = document.getElementById("f");
console.log(form);
form.addEventListener("submit", (e) => {
  e.preventDefault();

  var data = new FormData(form);

  var rq = new XMLHttpRequest();

  rq.onreadystatechange = function(){
    if (this.readystate == 4 && this.status == 200){
      console.log(this);
    }
  };

  rq.open("POST", true);
  rq.responseType = "json";
  rq.setRequestHeader("Content-Type", "application/json");
  rq.send(data);

  return false;
})
