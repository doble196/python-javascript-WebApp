if (!localStorage.getItem("counter")) {
  // if counter doesn't exist in local storage
  localStorage.setItem("counter", 0); // set counter to 0
} // end if statement

function count() {
  // function to count
  let counter = localStorage.getItem("counter"); // get counter from local storage
  counter++; // increment counter
  document.querySelector("h1").innerHTML = counter; // set h1 to counter
  localStorage.setItem("counter", counter); // set counter to local storage
} // end count function

document.addEventListener("DOMContentLoaded", function () {
  // when DOM is loaded
  document.querySelector("h1").innerHTML = localStorage.getItem("counter"); // set h1 to counter
  document.querySelector("button").onclick = count; // when button is clicked, call count function
}); // end DOMContentLoaded event listener
