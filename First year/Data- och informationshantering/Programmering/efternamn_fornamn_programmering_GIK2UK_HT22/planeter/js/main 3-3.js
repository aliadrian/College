/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 3: Datastrukturer och iteration                     */
/*                                                              */
/*      3-3    Introduktion till for-loopar                     */
/*                                                              */
/****************************************************************/


/*
    Målen för detta program ("kraven"), är att göra sidan ännu mer 
    dynamisk. Vi vill nu även bygga upp navigationslänkarna programmatiskt,
    istället för att ha dem statiskt definierade som del av html-filen. 

    Vi bestämmer oss för att endast lägga in länkar till de _andra_ 
    planeterna än den vi just nu visar. (Dålig design? Förmodligen. Men
    just nu är syftet att öva på de olika byggstenarna i programmering.)
    
    Vi deklarerar en s.k. Array, en enklare struktur än en Map,
    enbart för att göra det tydligt vilka planeter vi hanterar
    i resten av programmet.

    Därefter använder vi en s.k. for-loop för att skriva ut alla
    länkar.
*/

// 1. Array med planetnamn. Denna ska användas för att vi ska veta
//    vilka planeter/månar vi tänker oss att hantera. Om vi senare 
//    lägger till eller tar bort en planet, eller ändrar namn, börjar
//    vi här.
var planetNames = new Array("Pluto", "Jupiter", "Mars");

// 2. Vi hämtar ut sidans titel som tidigare, 
var selectedPlanetName = document.querySelector("title");

var navigationElement = document.querySelector(".navigation");
// Q: Vad händer i steg 3 här nedanför? Inspektera i debuggern!

// 3a. Vi stegar oss igenom arrayen med en s.k. for-loop.
for (let planetName of planetNames) {

    //3b. Vi vill _inte_ skriva ut länk till den planet vi just nu visar:
    if (planetName == selectedPlanetName) {
        // Här gör vi ingenting.
    }
    else {
        //Här lägger vi in en länk:
        navigationElement.insertAdjacentHTML(
            "beforeend",
            `<a class="int_link" href="#">${planetName}</a>`
        );
    }
};
