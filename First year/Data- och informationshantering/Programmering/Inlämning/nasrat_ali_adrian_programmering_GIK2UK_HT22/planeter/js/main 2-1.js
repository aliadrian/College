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
var planetName1 = "Saturn";
var planetName2 = "Mercury";

// Vi deklarerar en till variabel, och tilldelar den en hyperintressant(?!?) text.
// Q: Vad kommer variabeln interestingFact innehålla efter följande tilldelning?
var interestingFact = `The planet ${planetName1} is much farther away from the Sun than ${planetName2}.`;
// Hade du rätt? (Inspektera i debuggern!)


// Vi skriver ut den intressanta texten någonstans på sidan, inte för att det ska 
// vara snyggt utan bara för att se att det fungerar.
// Q: Var kommer texten att skrivas ut?
var anElement = document.querySelector("dt");
anElement.innerText = interestingFact;
// Hade du rätt?