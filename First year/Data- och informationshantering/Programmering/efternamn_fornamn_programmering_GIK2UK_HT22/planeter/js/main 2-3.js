/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 2: Variabler och villkorssatser                     */
/*                                                              */
/*      2-3     Mer om variabler som del av sträng              */
/*                                                              */
/****************************************************************/


/*
    Visst blev det väldigt repetitivt med if-satserna i förra programmet?
    I det här programmet ska vi uppnå samma sak, men på ett snyggare sätt.
    Namnet på planeten är ju det som skiljer namnen på filerna åt... det
    kan vi utnyttja!
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
nameElement.innerText = "Europa";


// 3. Vi lägger in en bild, beroende av sidans titel, i två steg.
//   a) Vi lokaliserar platsen att lägga bilden på:
var headerElement = document.querySelector(".header");
//   b) Vi skjuter in HMTL-kod för att lägga in bilden, och utnyttjar
//      (innehållet i) variabeln "titleText" direkt:
headerElement.insertAdjacentHTML(
    "beforeend",
    `<img class="image" src="./img/${titleText}_2048.webp" alt="Usually an important piece of text">`
);

/*
    Stega igenom programmet i debuggern och titta på resultatet - och kom
    ihåg att du behöver ändra på något i HTML-filen för att det ska hända något intressant!
*/