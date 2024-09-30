var gulbunke = "Två ägg";
var vitbunke = "ett halvt kilo mjöl";

var planetNames = new Array("Pluto", "Jupiter", "Venus");



var item = document.querySelector("dd");

// Övning, kolla mer på foreach
// planetNames.forEach(item => {
//   nameElement.innerText = något med arrayen här
// });

var planetNameOirgins = new Map();
planetNameOirgins["Pluto"] = "Undejordens gud.";
planetNameOirgins["Mars"] = "Info om Mars.";
planetNameOirgins["Jupiter"] = "Info om Jupiter.";
planetNameOirgins["Europa"] = "Info om Europa.";
planetNameOirgins["Venus"] = "Infor om Venus.";

for (let planetName of planetNames) {
  var nameElement = document.querySelector(".name");
  nameElement.innerText = planetName;

  var originElement = document.querySelector(".name_origin");
  originElement.innerText = planetNameOirgins[planetName];
}