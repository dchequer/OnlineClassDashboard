// DashboardApp/core/static/js/subject-scripts.js

/* - - - SUBJECTS PAGE - - - */
// Get modal element
var modal = document.getElementById("add-subject-modal");
// Get button that opens the modal
var btn = document.getElementById("add-subject-button");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

