document.addEventListener("DOMContentLoaded", function() {
  const menuButton = document.querySelector(".head .menu .link");
  const navList = document.querySelector(".nav .list");

  const toggleNavList = () => {
    const currentDisplay = navList.style.display;
    navList.style.display = currentDisplay === "flex" ? "none" : "flex";
  };
  
  const updateNavList = () => {
    if (window.innerWidth < 996) {
      navList.style.display = "none";
    } else {
      navList.style.display = "flex";
    }
  };
  
  updateNavList();

  menuButton.addEventListener("click", function(event) {
    event.preventDefault();
    toggleNavList();
  });

  window.addEventListener("resize", updateNavList);
});
