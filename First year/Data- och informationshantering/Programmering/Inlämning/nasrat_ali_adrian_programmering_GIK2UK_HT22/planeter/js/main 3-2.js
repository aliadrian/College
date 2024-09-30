/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 3: Datastrukturer och iteration                     */
/*                                                              */
/*      3-2    Användning av Map                                */
/*                                                              */
/****************************************************************/


/*
    Målen för detta program ("kraven") är desamma som i ett tidigare
    exempel - men vi ska vara lite smartare och använda en Map istället
    för if-satser. 
*/

// 1. Förbered genom att skapa en "Map":
var planetFilenames = new Map();
// Nu kan vi definiera nyckel (planetnamn) och värde (sökväg och namn på bildfil):
planetFilenames["pluto"] = "./img/pluto_2048.webp";
planetFilenames["europa"] = "./img/europa_2048.webp";
planetFilenames["venus"] = "./img/venus_2048.webp";
planetFilenames["jupiter"] = "./img/jupiter_2048.webp";
planetFilenames["mars"] = "./img/mars_2048.webp";
planetFilenames["mountain"] = "./img/mountain-horizontal.jpg";

// VAD SAKNAS HÄR ?;
// O.S.V.


// 1. Vi hämtar ut sidans titel som tidigare:
// VAD SAKNAS HÄR ?;
var titleElement = document.querySelector("title");

// 2. Vi skriver ut titeln som planetens namn:
// VAD SAKNAS HÄR ?;
var planetname = titleElement.innerText = "venus";

// 3. Vi lägger in en bild, beroende av sidans titel:
var planetFilename = planetFilenames[planetname];
var headerElement = document.querySelector(".header");
headerElement.insertAdjacentHTML(
    "beforeend",
    `<img class="image" src="${planetFilename}" alt="Usually an important piece of text">`
);


/*
    Titta nu på resultatet, som tidigare genom att ändra... Q: ja, vad behöver du ändra
    i HTML-filen?

    Men - är det inte något som är lite skumt?! Exekvera programmet (d.v.s. ladda sidan 
    så att JS-tolken i webläsarem kickar igång), och följ vad som händer i debuggern.
    
    Q: Kan du lokalisera problemet? Förstår du vad felet är?
*/