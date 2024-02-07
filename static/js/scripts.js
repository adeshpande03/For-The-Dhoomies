var addTeammateButton = document.getElementById("addTeammate");
var formfield = document.getElementById("formfield");

function add() {
  var newField = document.createElement("input");
  newField.setAttribute("type", "text");
  newField.setAttribute("name", "playerName[]");
  newField.setAttribute("class", "form-control formtext");
  formfield.appendChild(newField);
}

function remove() {
  var input_tags = formfield.getElementsByTagName("input");
  formfield.removeChild(input_tags[input_tags.length - 1]);
}

window.onload = function () {
  document.getElementById("randomImage").src =
    "/get-random-image?" + new Date().getTime();
};

function showRandomImage() {
  document.getElementById("randomImage").src =
    "/get-random-image?" + new Date().getTime();
}

function modifyScore(index, delta) {
  var scoreSpan = document.getElementById("score" + index);
  var score = parseInt(scoreSpan.innerText) + delta;
  scoreSpan.innerText = score.toString();
}
