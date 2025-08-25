document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const loader = document.getElementById("loader");
  const loaderText = document.getElementById("loader-text");
  const resultBox = document.querySelector(".result");

  // Array of loading messages
  const messages = [
    "Fetching data...",
    "Polishing the results...",
    "Summoning the spiders 🕷️...",
    "Almost there...",
    "Final touch...",
  ];

  let msgIndex = 0;
  let intervalId;

  form.addEventListener("submit", () => {
    loader.style.display = "block";
    resultBox.style.display = "none";

    // Start rotating messages
    function showNextMessage() {
      loaderText.style.opacity = 0; // fade out
      setTimeout(() => {
        loaderText.textContent = messages[msgIndex];
        loaderText.style.opacity = 1; // fade in
        msgIndex = (msgIndex + 1) % messages.length;
      }, 130); // match transition duration
    }

    showNextMessage(); // show first immediately
    intervalId = setInterval(showNextMessage, 2000); // every 2s
  });
});
