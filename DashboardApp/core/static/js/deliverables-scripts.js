// DashboardApp/core/static/js/subject-scripts.js

/* - - - SUBJECTS PAGE - - - */
// Get modal element
var modal = document.getElementById("add-deliverable-modal");
// Get button that opens the modal
var openModalButton = document.getElementById("add-deliverable-button");
// Get the <span> element that closes the modal
var closeSpan = document.getElementsByClassName("close")[0];
// Get the button that filters cards
var filterButton = document.getElementById("filter-deliverable-button")


/* Modal */
// When the user clicks the button, open the modal
openModalButton.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
closeSpan.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

/* Cards */
// on click open specific assignment
function openDeliverable(deliverableCard) {
  console.log(deliverableCard.id);
}
