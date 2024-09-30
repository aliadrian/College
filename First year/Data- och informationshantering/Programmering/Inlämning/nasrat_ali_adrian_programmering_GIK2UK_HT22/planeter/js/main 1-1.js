/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 1: Grunderna                                        */
/*                                                              */
/*      1-1     Att hämta och manipulera ett html-element,      */
/*              att använda debuggern                           */
/*                                                              */
/****************************************************************/


/*
    Öppna filen index.html i webläsare för att exekvera detta JS-program.

    För att öppna debuggern i webläsaren, välj den lilla "..."-menyn uppe till höger,
        därefter:     "More Tools"  -->  "Developer Tools" 
        eller använd tangentbordet:   Ctrl + Shift + i
    (Det ser likadant ut i åtminstone Edge och Chrome.)

    I högra halvan av webläsaren kan du nu välja olika flikar. Välj fliken "Elements". 
    Q:  Vad visas där? Vad händer när du rör musen, och väljer olika element? 
    
    Välj fliken "Source". Öppna denna JS-fil med Ctrl+P.
    Klicka någonstans i kolumnen med radnummer.
    Q:  Vad händer?
    
    Ladda om sidan, t.ex. med F5.
    Q:  Vad händer?
    
    Tryck F10 ett par gånger.  
    Q:  Vad händer?

    Du har lagt in en s.k. "breakpoint", och kan nu stega dig genom 
    JavaScript-programmet med F10.

    Q:  Håll muspekaren över t.ex. "nameElement" i JavaScript-koden. Vad
        får du reda på?

    Utforska vidare höger del av "Sources"-tabben.
*/


// Så här hämtar vi ut ett s.k. "element":
var nameElement = document.querySelector(".name");
// Q:   Vad gör vi här med elementet?
nameElement.innerText = "Hej hej";


// Bra att veta:  Två snedstreck (division, framåtslash) används för att
// skriva s.k. "kommentarer". Kommentarer används för att förklara programmet
// för en människa som läser JavaScript-koden.

/* 
    Vi kan också 
    använda 
    den här notationen
    med snedstreck och stjärna!
*/

/*
    Fortsätt vidare till filen "main 1-2.js".
*/