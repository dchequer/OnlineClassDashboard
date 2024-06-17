//DashboardApp/core/static/js/home-scripts.js

/* - - - HOME PAGE - - - */

function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("expanded");
  // Adjust main content margin if necessary
  document.getElementById("main-content").style.marginLeft =
    sidebar.classList.contains("expanded") ? "250px" : "50px";
};
