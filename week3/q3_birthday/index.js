$(document).ready(function () {
  $("button").bind("click", function () {
    // set the greeting message
    var greeting = $("#greeting").val();
    $(".message-div").html(greeting);

    // set the border
    var borderProp = $('input[name="border"]:checked').val();
    $(".card-result").css({
      "border-color": "black",
      "border-weight": "1px",
      "border-style": borderProp,
    });

    // set the background color
    var colorProp = $("#color").val();
    $(".card-result").css({ "background-color": colorProp });

    // change font size
    var fontSize = $("#font-size").val();
    $(".message-div").css({ "font-size": fontSize + 'px' });

    // change font 
    var font = $("#font").val();
    $(".message-div").css({ "font-family": font });
    

    // remove image if unchecked
    var imgProp = $('input[name="image"]:checked').val();
    if (!imgProp) {
      $("img").css({ visibility: "hidden" });
    } else {
      $("img").css({ visibility: "visible" });
    }
  });
});
