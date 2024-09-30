/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-5     Olika sätt att lokalisera html-element          */
/*                                                              */
/****************************************************************/


/*
    Nu sätter vi som vårt mål att hämta ut sidans titel, och skriva
    ut den istället för "Pluto". 
    
    Stega dig igenom hela programmet i debuggern!
*/

// Q: Vad är skillnaden på följande rader? (Titta i debuggern!)
var titleElement = document.querySelector("title");
var titleText = document.querySelector("title").innerText;


/*
    Om du sätter en punkt först, så letar querySelector reda på ett element av angiven class.
        Exempel: ".term", ".details"
    Om du hoppar över punkten, får du tillbaka ett element av angiven tag.
        Exempel: "p", "dt"
*/


// Q: Vad hämtar vi här, och lägger i variabeln nameElement? 
//    Ett element av en viss klass, eller av en viss tag?
var nameElement = document.querySelector(".name");
// Inspektera variabeln i debuggern. Hade du rätt?


// Ska vi avrunda med det vi bestämde oss för i början av filen. 

// Q: Blir det här bra?
nameElement.replaceWith(titleText);

// Q: Blir det här bättre? (Kommentera raden ovan, och avkommentera följande.)
//nameElement.innerText = titleText;

// Q: Eller det här?
//nameElement.innerHTML = titleText;

/*
    Hint: Inspektera rad för rad vad som händer i debuggern. Förstår du vad som händer?
    Exekvera programmet flera gånger, genom att ladda om sidan.
*/