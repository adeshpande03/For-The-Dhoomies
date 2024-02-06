var addTeammateButton = document.getElementById("addTeammate");
var formfield = document.getElementById("formfield");

function add() {
  var newField = document.createElement("input");
  newField.setAttribute("type", "text");
  newField.setAttribute("name", "text[]");
  newField.setAttribute("class", "text");
  formfield.appendChild(newField);
}

function showRandomImage() {
  document.getElementById("randomImage").src =
    "/get-random-image?" + new Date().getTime();
}
