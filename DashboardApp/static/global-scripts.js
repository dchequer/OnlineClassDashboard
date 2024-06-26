// DashboardApp/core/static/global-scripts.js

function showErrors(duration) {
  const errorsDiv = document.getElementById("errors");
  const progressBar = document.getElementById("progress-bar");

  let width = 100;
  const intervalTime = 10; 
  const step = (intervalTime / duration) * 100;

  if (errorsDiv.childElementCount > 1){ // if there are any errors start showing the errors div 
    errorsDiv.style.display = "block";

    // start progress bar
    const interval = setInterval(() => {
      if (width <= 0) { // if progress bar is full, stop interval and hide errors div
        clearInterval(interval);
        errorsDiv.style.display = "none";
      } else {          // decrease progress bar width
        width -= step;
        progressBar.style.width = `${width}%`;
      }
    }, intervalTime);
  }
}

function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  var burgerIcon = document.getElementById("burger")
  var mainContent = document.getElementById("content")
  var errorsDiv = document.getElementById("errors");

  sidebar.classList.toggle("expanded");
  burgerIcon.classList.toggle("expanded")
  mainContent.classList.toggle("expanded");
  errorsDiv.classList.toggle("expanded")

  // Adjust main content so it doesnt go off screen (to the right)
  mainContent.style.width = sidebar.classList.contains("expanded") ? "calc(100% - 250px)" : "100%";

  // Change burger icon position to the rightmost side of the sidebar and change it to an arrow pointing back
  burgerIcon.innerHTML = sidebar.classList.contains("expanded") ?  "⬅" : "☰";
};

function openCard(cardDiv){
  var cardTitleElem = cardDiv.querySelector(".card-title");
  var cardTitle = cardTitleElem.innerHTML;
  console.log(cardTitleElem);
  console.log(cardTitle)
  var newUrl = `${window.location.href}/${encodeURIComponent(cardTitle)}`;
  console.log(newUrl);
  window.location.href = newUrl;
};

document.addEventListener("DOMContentLoaded", () => {
  // if error div has anything in it, display it
  showErrors(5000); // 5 seconds
});