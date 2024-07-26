let isEditing = false;
const dataType = document.getElementById("data-type").innerText;
const itemName = document.getElementById("item-name").innerText;
const parentURL = document.getElementById("parent-url").innerText;

// event listener for 'esc' to trigger the close circle
document.addEventListener("keyup", (event) => {
  if (event.key === "Escape") {
    if (!isEditing) {
      document.getElementById("close-circle").click();
      console.log("escape - close circle");
    } else {
      cancelChanges();
      console.log("escape - cancel changes only");
    }
  }
});


function restrictInput(event) {
  const allowedSymbols = "!@#$%^&*()., ";
  if (!event.key.match(new RegExp(`^[a-zA-Z0-9${allowedSymbols}]+$`)) || event.key === "Enter") {
    event.preventDefault();
    console.log("Invalid input");
  } else {
    console.log("Valid input");
  }
}


function enterEditMode() {
  console.log("enter edit mode");
  isEditing = true;
  // change buttons class to edit mode
  var parentDiv = document.getElementById("function-buttons");
  for (var i = 0; i < parentDiv.children.length; i++) {
    parentDiv.children[i].classList.add("edit-mode");
  }

  // make span elements with class "dynamic-content" editable
  var dynamicContents = document.getElementsByClassName("dynamic-content");
  for (var i = 0; i < dynamicContents.length; i++) {
    dynamicContents[i].classList.add("edit-mode");
    dynamicContents[i].setAttribute("contenteditable", "true");
    dynamicContents[i].addEventListener("keypress", restrictInput);
  }
}
function exitEditMode() {
  console.log("exit edit mode");
  isEditing = false;
  // remove buttons class edit mode
  var parentDiv = document.getElementById("function-buttons");
  for (var i = 0; i < parentDiv.children.length; i++) {
    parentDiv.children[i].classList.remove("edit-mode");
  }

  // make span elements with class "dynamic-content" not editable
  var dynamicContents = document.getElementsByClassName("dynamic-content");
  for (var i = 0; i < dynamicContents.length; i++) {
    dynamicContents[i].classList.remove("edit-mode");
    dynamicContents[i].setAttribute("contenteditable", "false");
    dynamicContents[i].removeEventListener("keypress", restrictInput);
  }
}


function cancelChanges() {
  // exit edit mode
  exitEditMode();

  // reset the values of the span elements with class "dynamic-content"
  var dynamicContents = document.getElementsByClassName("dynamic-content");
  for (var i = 0; i < dynamicContents.length; i++) {
    dynamicContents[i].innerText = dynamicContents[i].getAttribute("data-original");
  }
}
function saveChanges() {
  // exit edit mode
  exitEditMode();

  // get the new values and send them to the server
  var newValues = {};
  var dynamicContents = document.getElementsByClassName("dynamic-content");
  for (var i = 0; i < dynamicContents.length; i++) {
    var tag = dynamicContents[i];
    var key = tag.id;
    var value = tag.innerText;
    newValues[key] = value;
  }
  console.log(newValues);

  // Determine the dynamic URL based on the user's context
  const url = `/api/${dataType}/update/${itemName}`;
  console.log(url);
  // send the new values to the server
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newValues),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  // reload the page
  location.reload();
}