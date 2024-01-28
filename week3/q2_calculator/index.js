$(document).ready(function () {
  $(".test-div").css("background-color", "yellow");

  var num1 = Number($("#num1").val());
  var num2 = Number($("#num2").val());

  $("#add").bind("click", function () {
    $("#result").html(num1 + num2);
  });
  $("#sub").bind("click", function () {
    $("#result").html(num1 - num2);
  });
  $("#mul").bind("click", function () {
    $("#result").html(num1 * num2);
  });
  $("#div").bind("click", function () {
    $("#result").html(num1 / num2);
  });
});
