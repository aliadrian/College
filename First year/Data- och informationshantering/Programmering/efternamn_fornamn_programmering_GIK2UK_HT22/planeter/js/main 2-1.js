/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 2: Variabler och villkorssatser                     */
/*                                                              */
/*      2-1     Variabel som del av sträng                      */
/*                                                              */
/****************************************************************/


/*
    Nu ska vi börja göra saker mer och mer dynamiskt.
    Det innebär att vi vill göra innehållet eller utseendet på vissa delar av sidan
    beroende av annat, som vi inte känner till fullt ut då filen skrivs.

    Vi gör en kort avstickare, för att lära oss hur man lägger en variabel 
    som del av en sträng.
*/

// Vi deklarerar två variabler, och tilldelar dem något intressant(?).
var planetName1 = "Jupiter";
var planetName2 = "Mercury";

var planetNameOrigin = new Map();
planetNameOrigin["Jupiter"] = "The main god of the romans.";
planetNameOrigin["Saturn"] = "Something about Saturn.";
planetNameOrigin["Moon"] = "Something about Moon.";
planetNameOrigin["Venus"] = "Something about Venus.";
planetNameOrigin["Pluto"] = "Something about Pluto.";

// Vi deklarerar en till variabel, och tilldelar den en hyperintressant(?!?) text.
// Q: Vad kommer variabeln interestingFact innehålla efter följande tilldelning?
var interestingFact = "";
// Hade du rätt? (Inspektera i debuggern!)

if (planetName1 == "Saturn") {
    interestingFact = `${planetName1} is the second largest planet.`
} else if (planetName1 == "Jupiter") {
    interestingFact = `${planetName1} is the largest planet.`
} else {
    interestingFact = `I have no, interesting fact`
}

for (var i = 0; i < planetNameOrigin.size; i++) {
    nameOriginElement.innerText = planetNameOrigin[planetName1];
}

var planetNames = new Array("Pluto", "Jupiter", "Saturn");

for (let planetName of planetNames) {
    nameOriginElement.innerText = planetName;
}

// Vi skriver ut den intressanta texten någonstans på sidan, inte för att det ska 
// vara snyggt utan bara för att se att det fungerar.
// Q: Var kommer texten att skrivas ut?
var anElement = document.querySelector("dt");
anElement.innerText = interestingFact;

var nameElement = document.querySelector(".name");
nameElement.innerText = planetName1;

nameElement.insertAdjacentHTML(
    "afterend",
    `<img class="image" `
)
// Hade du rätt?
var nameOriginElement = document.querySelector(".name_origin");
//nameOriginElement.innerText = planetNameOrigin[planetName1];




