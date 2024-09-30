/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 2: Variabler och villkorssatser                     */
/*                                                              */
/*      2-2     Introduktion till villkorssatser                */
/*                                                              */
/****************************************************************/


/*
    Tanken med programmet i den här filen är att den som skriver html-filen
    enbart ska behöva ändra "title"-taggen till ett planetnamn. (Eller måne då.)
    Programmet ska då:
    A. Skriva ut planetens namn istället för "Pluto", samt 
    B. Lägga in en bild på rätt planet i slutet av headern.
    
    Vi behöver då göra följande, i tur och ordning:
      1. Hämta ut sidans titel
      2. Skriva ut titeln på rätt plats.
      3. Lägga in en bild, beroende av sidans titel, på rätt plats.
*/


// 1. Vi hämtar ut sidans titel, i två steg. 
//   a) Vi hämtar först ut title-elementet:
var titleElement = document.querySelector("title");
//   b) Vi hämtar sedan ut texten i title-elementet:
var titleText = titleElement.innerText;


// 2. Vi skriver ut titeln som planetens namn (istället för "Pluto").
//   a) Vi hämtar rätt element genom att fråga efter ett element av klassen "name":
var nameElement = document.querySelector(".name");
//   b) Vi skriver ut det nya namne:
nameElement.innerText = "Jupiter";


// 3. Vi lägger in en bild, beroende av sidans titel, i två steg.
//   a) Vi lokaliserar platsen att lägga bilden på:
var headerElement = document.querySelector(".header");
//   b) Vi skjuter in HMTL-kod för att lägga in bilden:

if (titleText == "Jupiter") {
    headerElement.insertAdjacentHTML(
        "beforeend",
        `<img class="image" src="./img/jupiter_2048.webp" alt="Usually an important piece of text">`
    );
}
if (titleText == "Europa") {
    headerElement.insertAdjacentHTML(
        "beforeend",
        `<img class="image" src="./img/europa_2048.webp" alt="Usually an important piece of text">`
    );
}
if (titleText == "Mars") {
    "beforeend",
    `<img class="image" src="./img/mars_2048.webp" alt="Usually an important piece of text">`
}

// 4. OCH SÅ VIDARE, FÖR VARJE PLANET / MÅNE
if (titleText == "Moon") {
    "beforeend",
    `<img class="image" src="./img/moon_2048.webp" alt="Usually an important piece of text">`
}


/*
    Titta nu på resultatet. Till en början är det kanske ingen skillnad 
    - du ser fortfarande namnet Pluto och en bild på Pluto.
    
    Q: Vad behöver du göra för att det ska hända något intressant? 

    Hint: titta på målet vi satte upp för oss själva högst upp i denna .js-fil. 
    Du behöver ändra på något i HTML-filen kommer något annat att hända i steg 1b!)
*/