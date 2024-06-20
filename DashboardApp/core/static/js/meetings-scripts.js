// DashboardApp/core/static/js/meetings-scripts.js
var USER_ID;

/* - - - MEETINGS PAGE - - - */
// Get modal element
var modal = document.getElementById("add-meeting-modal");
// Get button that opens the modal
var openModalButton = document.getElementById("add-meeting-button");
// Get the <span> element that closes the modal
var closeSpan = document.getElementsByClassName("close")[0];
// Get the button that filters cards
var filterButton = document.getElementById("filter-meetings-button")
// Get the dropdown where the user selects the subject
var subjectSelect = document.getElementById("subject-select");

function fetchUserId() {
  return new Promise((resolve, reject) => {
    fetch("/api/user/id")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.text();
      })
      .then((userId) => {
        resolve(userId);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

async function setUserId() {
  USER_ID = await fetchUserId();
}

/* - - - Modal - - - */
// When the user clicks the button, open the modal
openModalButton.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
closeSpan.onclick = function () {
  modal.style.display = "none";
};

// fetch user's subjects and populate the dropdown
async function populateSubjectDropdown(USER_ID) {
  await fetch(`/api/subjects/user_id=${USER_ID}`)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((subject) => {
        var option = document.createElement("option");
        option.text = subject.name;
        option.value = subject.id;
        subjectSelect.add(option);
      });
    });
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

/* - - - Cards - - - */
// on click open specific assignment
function openSubject(meetingCard) {
  console.log(meetingCard);
  console.log(meetingCard.id);
}

/* - - - MISC - - - */
// when page loads populate the dropdown
async function populate() {
  await setUserId();

  populateSubjectDropdown(USER_ID);
}
populate();
