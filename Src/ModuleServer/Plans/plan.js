function change_state(ele) {
  console.log("ok");
    if (ele.className.baseVal == "empty") {
      ele.className.baseVal  = "occuped";
      console.log("removed");
    }
}
