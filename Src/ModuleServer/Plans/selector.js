var allStates = $("svg.us > *");

allStates.on("click", function() {

  allStates.removeClass("on");
  $(this).addClass("on");

});
