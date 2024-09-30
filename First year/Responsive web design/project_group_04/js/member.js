function memberThumbnail(member) {
  const thumbnail = `
  <div class="col-12 parent-div col-xs-6 col-md-4 col-lg-3 offst-xexl-0 col-xxl-2 br-3"> 
  <picture>
 <source type="image/webp"
       srcset="./img/informative/member/${member.id}/webp/${member.id}_256.webp 256w,
              ./img/informative/member/${member.id}/webp/${member.id}_512.webp 512w,
              ./img/informative/member/${member.id}/webp/${member.id}_860.webp 860w,
              ./img/informative/member/${member.id}/webp/${member.id}_1024.webp 1024w,
              ./img/informative/member/${member.id}/webp/${member.id}_2048.webp 2048w"
       sizes="(min-width: 2040px) 10vw,
             (min-width: 1024px) 15vw,
             (min-width: 860px) 18vw,
             (min-width: 768px) 22vw,
             100vw">
 <source type="image/jpeg"
       srcset="./img/informative/member/${member.id}/jpg/${member.id}_256.jpg 256w,
              ./img/informative/member/${member.id}/jpg/${member.id}_512.jpg 512w,
              ./img/informative/member/${member.id}/jpg/${member.id}_860.jpg 860w,
              ./img/informative/member/${member.id}/jpg/${member.id}_1024.jpg 1024w
              ./img/informative/member/${member.id}/jpg/${member.id}_2048.jpg 2048w"
         sizes="(min-width: 2040px) 10vw,
             (min-width: 1024px) 15vw,
             (min-width: 860px) 18vw,
             (min-width: 768px) 22vw,
             100vw">
 <img src="./img/informative/member/${member.id}/jpg/${member.id}_750.jpg"
       width="750" height="750"
       alt="Image of ${member.first_name} ${member.last_name}">
</picture>
    <div class="info">
    <div class="name"> ${member.first_name} ${member.last_name}
    <p> ${member.mail}@du.se </p>
    </div>
      </div>
 </div>
  `;
  return thumbnail;
}

function addMemberThumbnails(members) {
  let output = "";
  members.forEach(function (member) {
    output += memberThumbnail(member);
  });
  return output;
}

const gallery = document.querySelector(".gallery");

const members = [
  {
    id: "000000",
    eid: "zero",
    first_name: "Alexander",
    last_name: "Karlsson",
    gender: "Male",
    mail: "alk",
  },
  {
    id: "000001",
    eid: "one",
    first_name: "Robin",
    last_name: "Vredeskog",
    gender: "Male",
    mail: "rov",
  },
  {
    id: "000002",
    eid: "two",
    first_name: "Jane",
    last_name: "Sarani",
    gender: "Other",
    mail: "jas",
  },
  {
    id: "000003",
    eid: "three",
    first_name: "Nynaeve",
    last_name: "Al'Meara",
    gender: "Female",
    mail: "nya",
  },
  {
    id: "000004",
    eid: "four",
    first_name: "Ida",
    last_name: "Olsen",
    gender: "Female",
    mail: "ido",
  },
  {
    id: "000005",
    eid: "five",
    first_name: "Jonathan",
    last_name: "Eriksson",
    gender: "Male",
    mail: "joe",
  },
  {
    id: "000006",
    eid: "six",
    first_name: "Isak",
    last_name: "Rapp",
    gender: "Other",
    mail: "isr",
  },
  {
    id: "000007",
    eid: "seven",
    first_name: "Min",
    last_name: "Farshaw",
    gender: "Female",
    mail: "mif",
  },
  {
    id: "000008",
    eid: "eight",
    first_name: "Filippa",
    last_name: "Masonei",
    gender: "Female",
    mail: "fim",
  },
  {
    id: "000009",
    eid: "nine",
    first_name: "Elayne",
    last_name: "Trakand",
    gender: "Female",
    mail: "elt",
  },
  {
    id: "000010",
    eid: "ten",
    first_name: "Perrin",
    last_name: "Aybara",
    gender: "Male",
    mail: "pea",
  },
  {
    id: "000011",
    eid: "eleven",
    first_name: "Tuon",
    last_name: "Athaem",
    gender: "Other",
    mail: "tua",
  },
  {
    id: "000012",
    eid: "twelve",
    first_name: "Kamarile",
    last_name: "Maradim",
    gender: "Female",
    mail: "kam",
  },
  {
    id: "000013",
    eid: "thirteen",
    first_name: "Fail",
    last_name: "Bashere",
    gender: "Female",
    mail: "fab",
  },
  {
    id: "000014",
    eid: "fourteen",
    first_name: "Tom",
    last_name: "Bombadill",
    gender: "Other",
    mail: "tob",
  },
  {
    id: "000015",
    eid: "fifteen",
    first_name: "Elan",
    last_name: "Morin Tedronai",
    gender: "Other",
    mail: "elm",
  },
  {
    id: "000016",
    eid: "sixteen",
    first_name: "Mierin",
    last_name: "Eronaile",
    gender: "Female",
    mail: "mie",
  },
  {
    id: "000017",
    eid: "seventeen",
    first_name: "Barid Bel",
    last_name: "Medar",
    gender: "Male",
    mail: "bam",
  },
];


gallery.insertAdjacentHTML("beforeend", addMemberThumbnails(members));
