// event listener for 'esc' to trigger the close circle
document.addEventListener("keyup", (event) => {
  if (event.key === "Escape") {
    document.getElementById("close-circle").click();
    console.log("escape");
  }
});
