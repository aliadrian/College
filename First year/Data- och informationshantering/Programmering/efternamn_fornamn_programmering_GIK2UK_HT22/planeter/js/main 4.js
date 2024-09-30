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
var planetNames = ["Pluto", "Jupiter", "Mars"];

// 2a. Map för filnamn
var planetFilenames = new Map();
planetFilenames["europa"] = "./img/europa_2048.webp";
planetFilenames["jupiter"] = "./img/jupiter_2048.webp";
planetFilenames["mars"] = "./img/mars_2048.webp";
planetFilenames["pluto"] = "./img/pluto_2048.webp";
planetFilenames["venus"] = "./img/venus_2048.webp";
planetFilenames["müsli"] = "./img/musli.jpg";

// 2b.  Map för namnets ursprung
var nameOrigins = new Map();
nameOrigins["europa"] = "The name of Europa comes from...";
nameOrigins["jupiter"] = "Jupiter is the chief among the roman gods.";
nameOrigins["mars"] = "Mars is the roman god of war.";
nameOrigins["pluto"] = "Pluto is the roman god of the underworld.";
nameOrigins["venus"] = "Venus is the roman goddess of love.";
nameOrigins["müsli"] = "Probably german.";

// 2c.  Map för kort beskrivning
var planetTerms = new Map();
planetTerms["europa"] = "Europa is a moon with an ocean beneath an ice layer.";
planetTerms["jupiter"] = "Jupiter is the solar system's largest planet.";
planetTerms["mars"] = "Mars is red.";
planetTerms["pluto"] = "Pluto is no longer a planet, but defined as a dwarf planet.";
planetTerms["venus"] = "Venus is hot hot hot.";
planetTerms["müsli"] = "Müsli is no planet at all.";

// 2d.  Map för ... ja, här kan du fylla på med vad du vill!
let planetDetails = new Map();
planetDetails["europa"] = "Detail about Europa.";
planetDetails["jupiter"] = "Detail about Jupiter.";
planetDetails["mars"] = "Detail about Mars.";
planetDetails["pluto"] = "Detail about Pluto.";
planetDetails["venus"] = "Detail about Venus.";
planetDetails["müsli"] = "Detail about Müsli.";

// 3.   Vi lägger in navigationslänkar på rätt plats:
//      Q: Vad saknas? Fyll på kod-"skelettet" nedan:
// VAD SAKNAS HÄR ?
// for (VAD SAKNAS HÄR ?) {
//     if (VAD SAKNAS HÄR ?) {
//         VAD SAKNAS HÄR ?;
//     }
// };

var navigationElement = document.querySelector(".navigation");
var selectedPlanetName = document.querySelector("title");

for (let planetName of planetNames) {

    //3b. Vi vill _inte_ skriva ut länk till den planet vi just nu visar:
    if (planetName == selectedPlanetName) {
        navigationElement.insertAdjacentHTML(
            "beforeend",
            `<a class="int_link" href="#">/a>`
        );

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
// var detailClass = document.querySelector(".details");
// let details = ["Detail 1", "Detail 2", "Detail 3"];
// planetname["pluto"] = details[0];
// details.forEach(element => {
//     detailClass.insertAdjacentHTML(
//         "beforeend",
//         `${details}`
//     )
// });

// let map = new Map([
//     ["Pluto", "Detail abt pluto"],
//     ["Jupiter", "Detail abt jupiter"],
//     ["Mars", "Details abt mars"]
// ]);

// map.forEach(function (value, element) {
//     const span = document.querySelector('.details')
//     span.innerText = `${planetDetails[titleElement]}`
// });
var planetDetails = new Array("Pluto", "Jupiter", "Mars");
var detailsFromHTML = document.querySelector(".details");

for (let planetDetail of planetDetails) {

    //3b. Vi vill _inte_ skriva ut länk till den planet vi just nu visar:
    if (planetName == selectedPlanetName) {
        // Här gör vi ingenting.
    }
    else {
        //Här lägger vi in en länk:
        detailsFromHTML.insertAdjacentHTML(
            "beforeend",
            ` <dd class="details">
            ${planetDetail}
          </dd>`
        );
    }
};





function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

var wikiLink = document.querySelector(".ext_link");
wikiLink.innerHTML = `Wikipedia ${capitalizeFirstLetter(planetname)}`;

// const details = document.querySelectorAll('.list')

// details.forEach(element => {
//     const span = element.querySelector('.details')
//     span.innerText = `Details about ${planetname}` // Actually writes the word null, for no text use empty quotes
// })

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

