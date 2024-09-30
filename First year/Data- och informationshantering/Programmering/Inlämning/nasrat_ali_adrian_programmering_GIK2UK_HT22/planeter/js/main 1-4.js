/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-4     Strängar: enkelfnutt och dubbelfnutt            */
/*                                                              */
/****************************************************************/


/*
    Nu sätter vi som vårt mål att lägga till en bild. 
    Det kan vi göra genom att skjuta in html-kod för just detta.
*/

// Vi rasslar vidare...
var headerElement = document.querySelector(".header");

// Här skjuter vi in lite mer avancerad html:
headerElement.insertAdjacentHTML(
  "beforeend",
  `<img class="image" src="./img/jupiter_2048.webp" alt="Usually an important piece of text">`
);

/*
  Notera att strängen med HTML-kod här ovanför använder enkelfnuttar! 
  På mitt tangentbord skriver jag detta tecken med tangentkombinationen
  Shift + [tangent mellan "+"" och backspace]

  Q:  Varför?  (Editera filen, prova olika kombinationer av enkel- och 
      dubbelfnutt. Vad signalerar editorn VS Code? Vad händer när du 
      öppnar html-filen i en webläsare?)
*/

