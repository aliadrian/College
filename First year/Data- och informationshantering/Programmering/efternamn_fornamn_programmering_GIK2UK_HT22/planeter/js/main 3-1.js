/****************************************************************/
/*                                                              */
/*      PROGRAMMERING: INTRODUKTION TILL JAVASCRIPT             */
/*                                                              */
/*      Del 3: Datastrukturer och iteration                     */
/*                                                              */
/*      3-1    Introduktion till Map                            */
/*                                                              */
/****************************************************************/


/*
    Vi ska förbereda oss för att kunna göra ännu mer saker dynamiskt.
    
    I just denna uppgift ska vi bara känna på en s.k. "Map", som vi sedan ska 
    använda i följande uppgift. 


    En "Map" är en datastruktur, bestående av ett antal positioner som kan 
    ha ett innehåll - vi kan tänka oss dem dem "fack", eller "lådor".
    För varje position finns en unik "nyckel" som hänger ihop med positionens
    "värde". Man använder "nyckeln" för att hämta det innehåll man är intresserad 
    av.

    Några liknelser:
    *  Ett väldigt strukturerat förrådsutrymme, där varje flyttlåda har en
       etikett: "Gosedjur", "Böcker", "Lego", "Dockor", "Pussel", "dagböcker". 
       "Nyckeln" motsvaras av etiketten, och "värdet" motsvaras av lådans 
       innehåll.
    *  En medicindosett. Nyckeln motsvaras av veckodagen som står tryckt
       på varje lucka, och värdet av pillren som ligger i den luckan.
    *  Eller varför inte en adventskalender. Nyckel = siffra 1-24, och 
       värdet = jättespännande bild på t.ex. en pepparkaksgubbe.
    *  Din CSS-fil. "Nyckel" = class, och "värde" = själva innehållet. 
       Browsern ser att en tag ska formatteras enligt en viss "class". Den
       scannar igenom CSS-filen för att hitta "innehållet" i denna CSS-class,
       och applicera det.
       
    Det faller sig naturligt att nycklarna måste vara unika - däremot kan 
    innehållet vara detsamma. (I varje dosett-fack ligger likadana piller.
    Bakom varje lucka 1-24 döljer sig samma bild på en spännande pepparkaksgubbe.
    Flera CSS-class:er kan beskriva exakt samma utseende.)


    Vi ger oss själva ett problem, där det passar bra med en lösning i form av en
    Map. Vi tänker oss att bilderna som vi visar på vår sida inte är namngivna så 
    där enhetligt och snyggt som de bildfiler vi hanterat hittills, men vi vill ändå 
    skriva lättbegriplig kod.

    Gör först följande:
    A.  Leta rätt på en lämplig bild du vill kunna visa. (Det spelar ingen roll 
        vad den föreställer - det kan vara ditt älsklingsdjur, en kaktus,
        en superhjälte, en cirkusdirektör, eller världens längsta man. Varför 
        inte ha müsli i filen?) Du kan naturligtvis kopiera en av de existerande
        bilderna och ge den ett annat namn.
    
    B.  Lägg bilden i samma folder som de övriga bilderna, alltså foldern "img". 
        Låt filen behålla ett namn.

*/

// Notering: En "Map" är mer komplex än en grundläggande datatyp (som tal och 
// strängar), så den måste vi först skapa med hjälp av "new".
var planetFilenames = new Map();
// Nu kan vi definiera nyckel (planetnamn) och värde 
planetFilenames["europa"] = "./img/europa_2048.webp";
planetFilenames["jupiter"] = "./img/jupiter_2048.webp";
planetFilenames["mars"] = "./img/mars_2048.webp";
planetFilenames["pluto"] = "./img/pluto_2048.webp";
planetFilenames["venus"] = "./img/venus_2048.webp";

// I detta JavaScript-program antar vi att våran nya bild visar müsli, och heter
// "musli.jpg" - men du ska naturligtvis byta ut det mot namnet på din fil:
planetFilenames["mountain"] = "./img/mountain-horizontal.jpg";

// Q: Vad gör följande rad? (Inspektera i debuggern!)
var planetFilename = planetFilenames["mars"];


// Q: Kan vi lägga till samma innehåll till en ny nyckel?
planetFilenames["europa_igen"] = "./img/europa_2048.webp";

// Q: Vad gör följande rad? Läggs det till ett nyckel/värde-par?
planetFilenames["europa"] = "ett helt annat filnamn";


/*
    Om du vill kan du stanna upp här och göra något intressant med innehållet i 
    denna Map, t.ex. skriva ut det någonstans på sidan.

    Annars gör vi inget mer i denna fil. Se till att du förstått Map innan 
    du går vidare!
*/