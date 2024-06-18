// DashboardApp/core/static/global-scripts.js


function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var burgerIcon = document.getElementById("burger")
    var mainContent = document.getElementById("content")
  
    sidebar.classList.toggle("expanded");
    burgerIcon.classList.toggle("expanded")
    mainContent.classList.toggle("expanded");

    // Adjust main content so it doesnt go off screen (to the right)
    mainContent.style.width = sidebar.classList.contains("expanded") ? "calc(100% - 250px)" : "100%";
  
    // Change burger icon position to the rightmost side of the sidebar and change it to an arrow pointing back
    burgerIcon.innerHTML = sidebar.classList.contains("expanded") ?  "⬅" : "☰";
  };
  