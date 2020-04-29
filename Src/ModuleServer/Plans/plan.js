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
