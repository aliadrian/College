/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-6     Vi använder allt vi lärt oss hittills           */
/*                                                              */
/****************************************************************/


/*
    Du kanske redan när du öppnade denna fil i editorn noterade att fliken med 
    filnamnet lyser irriterat rött? Och har en siffra efter filnamnet?
    Håll musen över fliken, så får du reda på varför. 
    
    Som du märker innehåller filen texten "VAD SAKNAS HÄR?", och där
    ska naturligtvis du själv lägga in rätt sak.

    Nu sätter vi som vårt mål att manipulera vilket planetnamn som
    visas, och lägga till en bild. Vi utför flera steg där vi hämtar 
    element ur html-filen, och väljer den metod som passar bäst:
    att ändra property:n "innerText," eller att skjuta in html-kod.

    Nu börjar det bli dags att jobba mer systematiskt. Vi numrerar och 
    förklarar för oss själva vad som händer steg för steg. 

    Som alltid: stega igenom hela programmet i debuggern!
*/


// 1. Vi hämtar ut header-elementet, för att lägga bilden i slutet av det:
var headerElement = document.querySelector(".header");


// 2. Och så skjuter vi in kod för att lägga in bilden på, säg, Jupiter:
headerElement.insertAdjacentHTML(
    "beforeend",
    `<img class="image" src="./img/jupiter_2048.webp" alt="Usually an important piece of text">`
);
// Q: Hur lokaliseras egentligen bilden på Jupiter? Alltså, i vilken folder ligger den?


// 3. Vi uppdaterar även namnet till rätt planet - i detta fall "Jupiter".
//   a) Vi hämtar elementet som är av klassen "name":
var nameElement = document.querySelector(".name");

//   b) Vi gör något kul, inte för att vi måste utan för att roa oss. Vi använder en variabel:
var planetName = "Jupiter";
//   c) Nu skriver vi ut planeten Jupiters namn. 
nameElement.innerText = planetName;


/*
    Gå nu vidare med filen "main 2-1.js" och fortsätt framåt därifrån.
*/