/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-3     Att skjuta in ny html-kod                       */
/*                                                              */
/****************************************************************/


/*
    Kom ihåg att ändra taggen <script> i index.html. ;-)
*/

// Den här gången kan vi väl välja ut ett element som är en header:
var headerElement = document.querySelector(".header");


// Q: Vilka strängar är giltiga som parameter 1? (Alltså: "afterbegin", "beforeend", osv.)
//    (Börja editera, och lägg märke till att du får hjälp av Visual Studio Code!) 
headerElement.insertAdjacentHTML(
    "afterbegin",
    "<p>Hej</p>"
);

headerElement.insertAdjacentHTML(
    "beforeend",
    "<p><b>Hoj hoj</b></p>"
);
