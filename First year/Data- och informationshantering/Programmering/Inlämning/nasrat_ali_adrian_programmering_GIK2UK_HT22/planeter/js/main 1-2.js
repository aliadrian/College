/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-2     Olika sätt att manipulera ett html-element      */
/*                                                              */
/****************************************************************/


/*
    Viktigt: ändra taggen <script> längst ner i index.html, så att 
    denna JavaSript-fil väljs istället för den förra. Det gäller
    naturligtvis för varje ny fil!

    Tips: Om du vill ha kvar uppgift 1-1, kopiera "index.html" och 
    ge den namnet "index 1-2.html" innan du ändrar i den.
*/


// Vi börjar på samma sätt som sist, med att hämta ett element av klassen "name":
var nameElement = document.querySelector(".name");

/* 
    Tips: Medan man provar sig fram är det mycket vanligt att kommentera
    och avkommentera rader, en i taget.
    Detta är ett vanligt, och praktiskt, sätt att hålla saker färska i minnet, 
    medan man programmerar. 

    Viktigt: så snart du har övertygat dig om att du använder rätt properties
    o.s.v., radera de överflödiga raderna! (Alternativt: kommentera tydligt
    varför du behåller dem.

    Använd dig av detta arbetssätt, ihop med debuggern, för att svara på frågan
    nedan.
*/

// Utöver "innerText" finns även en egenskap (property) "innerHTML".
// Q:   Vad är skillnaden på följande anrop?
nameElement.innerText = "Hej hej";
//nameElement.innerText = "<b>Hoj hoj</b>";
//nameElement.innerHTML = "Huj huj";
//nameElement.innerHTML = "<b>Höj höj</b>";


/*
    Och nu...? Jo, nu när du arbetat dig igenom denna fil, ska du fortsätta
    vidare till nästa fil i nummerordningen, alltså: "main 1-3.js". 
    
    Detta gäller naturligtvis också för alla följande filer.
*/