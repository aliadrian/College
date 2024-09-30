/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 4:  Att hämta och manipulera html-element           */
/*              Variabler                                       */
/*              Selektion (if-sats)                             */
/*              Iteration (for-loop)                            */
/*              Datastrukturer (array och Map)                  */
/*                                                              */
/****************************************************************/

/*
    I denna uppgift knyter vi ihop alltsammans. Det är denna uppgift
    du ska lämna in som redovisning av momentet "Programmering" i kursen. 
    
    Kraven på inlämningen finner du längst ner.
*/


/*
    Målen för detta program ("kraven"), är att göra den ytterligare
    mer dynamisk. 
    
    Lägg in hela det förra programmet, och fyll på med fler dynamiska 
    texter efter eget huvud.


    Not 1:
    ------
    Här ska det också sägas att JavaScript-programmet börjar bli 
    alltför svåröverskådligt. Även html-sidan blir svårare att 
    förstå, eftersom det man ser i filen inte nödvändigtvis är 
    det som visas i webläsaren.

    Q: Kan det vara bättre att ändra delar av html-filen för att 
    göra det tydligare vilka delar som ska ändras eller bytas ut?

    Snegla på "index 4.html" så fattar du nog grejen.


    Not 2:
    ------
    För att skapa den sida vi håller på med nu, skulle man i
    praktiken strukturera både den html-kod och den JavaScript-kod 
    vi skriver på andra sätt. Men just nu nöjer vi oss med att öva
    på grunderna i programmering, och hur JavaScript hänger ihop 
    med html och CSS. 

    Målet just nu är ju "bara" att vi ska lära oss centrala 
    programmeringskoncept som "variabel", och nå en viss praktisk
    färdighet i grunderna. Som när man övar på isolerade moment 
    för vilken färdighet som helst - man kan inte lära sig "allt"
    eller öva på "allt" på en gång när allt är nytt.
*/

// 1.   Array med planetnamn. Denna ska användas för att vi ska veta
//      vilka planeter/månar vi tänker oss att hantera. Om vi senare 
//      lägger till eller tar bort en planet, eller ändrar namn, börjar
//      vi här.
var planetNames = ["Pluto", "Jupiter", "Mars", "Venus"];

// 2a. Map för filnamn
var planetFilenames = new Map();
planetFilenames["Europa"] = "./img/europa_2048.webp";
planetFilenames["Jupiter"] = "./img/jupiter_2048.webp";
planetFilenames["Mars"] = "./img/mars_2048.webp";
planetFilenames["Pluto"] = "./img/pluto_2048.webp";
planetFilenames["Venus"] = "./img/venus_2048.webp";
planetFilenames["Müsli"] = "./img/musli.jpg";

// 2b.  Map för namnets ursprung
var nameOrigins = new Map();
nameOrigins["Europa"] = "The name of Europa comes from...";
nameOrigins["Jupiter"] = "Jupiter is the chief among the roman gods.";
nameOrigins["Mars"] = "Mars is the roman god of war.";
nameOrigins["Pluto"] = "Pluto is the roman god of the underworld.";
nameOrigins["Venus"] = "Venus is the roman goddess of love.";
nameOrigins["Müsli"] = "Probably german.";

// 2c.  Map för kort beskrivning
var planetTerms = new Map();
planetTerms["Europa"] = "Europa is a moon with an ocean beneath an ice layer.";
planetTerms["Jupiter"] = "Jupiter is the solar system's largest planet.";
planetTerms["Mars"] = "Mars is red.";
planetTerms["Pluto"] = "Pluto is no longer a planet, but defined as a dwarf planet.";
planetTerms["Venus"] = "Venus is hot hot hot.";
planetTerms["Müsli"] = "Müsli is no planet at all.";

// 2d.  Map för ... ja, här kan du fylla på med vad du vill!
var planetDiameter = new Map();
planetDiameter["Europa"] = "3,121.6 km";
planetDiameter["Jupiter"] = "139,820 km";
planetDiameter["Mars"] = "6,779 km";
planetDiameter["Pluto"] = "2,376.6 km";
planetDiameter["Venus"] = "12,104 km";

var navigationElement = document.querySelector(".navigation");
var selectedPlanetName = document.querySelector("title");
var aSelectedPlanet = document.querySelector("title").innerText;

for (let planetName of planetNames) {

    //3b. Vi vill _inte_ skriva ut länk till den planet vi just nu visar:
    if (planetName == aSelectedPlanet) {
        planetNames.splice();
    }
    else {
        //Här lägger vi in en länk:
        navigationElement.insertAdjacentHTML(
            "beforeend",
            `<a class="int_link" href="#">${planetName}</a>`
        );
    }
};

// 4.   Vi hämtar ut sidans titel som tidigare, och använder för
//      att fylla på olika delar av sidan med hjälp av våra Map::
// VAD SAKNAS HÄR ?;
var titleElement = document.querySelector("title").text;


// 4a.  Vi skriver ut titeln som planetens namn:
// VAD SAKNAS HÄR ?;
var nameElement = document.querySelector(".name");
nameElement.innerHTML = titleElement;


// 4b.  Vi lägger in en bild, beroende av sidans titel:
// VAD SAKNAS HÄR ?
var planetname = titleElement;
var planetFilename = planetFilenames[planetname];

var headerElement = document.querySelector(".header");
headerElement.insertAdjacentHTML(
    "beforeend",
    `<img class="image" src="${planetFilename}" alt="Usually an important piece of text">`
);


// 4c.  Vi lägger in origin:
var nameOriginElement = document.querySelector(".name_origin");
nameOriginElement.innerHTML = nameOrigins[titleElement];
// nameOriginElement.innerHTML = nameOrigins[VAD SAKNAS HÄR ?];

// 4d.  Vi lägger in en term:
var termElement = document.querySelector(".term");
termElement.innerHTML = planetTerms[titleElement];
// VAD SAKNAS HÄR ?;

// 4e.  Vi lägger in... ja, mer och mer text dynamiskt!
// OCH SÅ VIDARE...;

var marsDetails = new Array("Info about Mars", "Info about Mars", "Info about Mars");
var plutoDetails = new Array("info about Pluto", "Info about Pluto", "Info about Pluto");
var detailsFromHTML = document.querySelector(".details");

if (titleElement == "Mars") {
    [...document.getElementsByClassName('details')].forEach(el => {
        for (let marsDetail of marsDetails) {
            el.innerHTML = `${marsDetail}`;
        }
    })
} else if (titleElement == "Pluto") {
    [...document.getElementsByClassName('details')].forEach(el => {
        for (let plutoDetail of plutoDetails) {
            el.innerHTML = `${plutoDetail}`;
        }
    })
}


function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

var wikiLink = document.querySelector(".ext_link");
wikiLink.innerHTML = `Wikipedia ${capitalizeFirstLetter(planetname)}`;

/*
    Hint:   Vill du ha ett godtyckligt antal smårubriker och 
            faktatexter ("term" och "details")? Vilken typ av 
            datastruktur vill man använda då...?? Och vilken 
            programmatisk konstruktion behöver man använda?
            
            Kan du skapa en Map, där nyckeln är planetens namn, 
            och värdet är en array - eller Map - av texter?

            Kan du sedan iterera igenom alla element i den 
            datastrukturen?
*/



/*            
    Krav vid inlämning av webprojektet:
            
            Programmet ska innehålla de numrerade
            stegen här ovan, utökade till ett fungerande program. Du
            får gärna lägga till annat på sidan, som använder de
            programmeringskonstruktioner vi tränat på. 
            
            Html-filen ska då innehålla markörer som visar var
            programmet skulle ändra på ytterligare innehåll. (Alltså,
            något i stil med "länk_till_wikipedia" istället för 
            "https://en.wikipedia.org/wiki/Pluto".)

            Du ska lämna in en zip-fil som innehåller:
            *   Alla html-, CSS-, och bildfiler som behövs för att visa websidan
                korrekt. 
            *   Inga andra filer!
            Innan du lämnar in uppgiften, kontrollera zip-filen själv, utifrån
            dessa enkla två punkter.

    Du måste _inte_ fylla exakt hela sidan med innehåll,
    eftersom du då inte tränar särskilt mycket på just
    programmering. Men jobba med det som känns intressantast 
    och mest lärorikt. 

    Du _får_ gärna utforska JavaScript vidare och använda t.ex.
    andra properties, datastrukturer, metoder för strängmanipulation, 
    och andra typer av satser för selektion och iteration.
*/

