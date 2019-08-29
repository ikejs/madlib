$("#story").hide();
$("#redoButton").hide();

function bold(word) {
    word.css("font-weight","Bold");
    return word;
}

$("#userInput").submit(function(event) {
  event.preventDefault();
  var one = $("#one").val();
  var two = $("#two").val();
  var three = $("#three").val();
  var four = $("#four").val();
  var five = $("#five").val();
  var six = $("#six").val();
  var seven = $("#seven").val();
  var eight = $("#eight").val();
  var nine = $("#nine").val();
  var ten = $("#ten").val();
  var eleven = $("#eleven").val();
  $("form").hide();
  $("#story").show();
  $("#story").append("Two <b>"+one+"</b>, both alike in dignity,<br>");
  $("#story").append("In fair <b>"+two+"</b>, where we lay our scene,<br>");
  $("#story").append("From ancient <b>"+three+"</b> break to new mutiny,<br>");
  $("#story").append("Where civil blood makes civil hands unclean.<br>");
  $("#story").append("From forth the fatal loins of these two foes<br>");
  $("#story").append("A pair of star-cross`d <b>"+four+"</b> take their life;<br>");
  $("#story").append("Whole misadventured piteous overthrows<br>");
  $("#story").append("Do with their <b>"+five+"</b> bury their parents` strife.<br>");
  $("#story").append("The fearful passage of their <b>"+six+"</b> love,<br>");
  $("#story").append("And the continuance of their parents` rage,<br>");
  $("#story").append("Which, but their children`s end, nought could <b>"+seven+"</b>,<br>");
  $("#story").append("Is now the <b>"+eight+"</b> hours` traffic of our stage;<br>");
  $("#story").append("The which if you with <b>"+nine+" "+ten+"</b> attend,<br>");
  $("#story").append("What here shall <b>"+eleven+"</b>, our toil shall strive to mend.");
  $("#story").append("<hr><small>Prologue by <a target='_blank' href='https://www.madtakes.com/libs/186.html'>madtakes.com</a></small>");
  $("#redoButton").show();
});

$("#redoButton").click(function() {
    $("#story").hide();
    $("#redoButton").hide();
    $("#story").empty();
    $("#userInput").find("input[type=text], textarea").val(""); //https://stackoverflow.com/questions/6364289/clear-form-fields-with-jquery
    $("form").show();
    $("#one").focus();
})
