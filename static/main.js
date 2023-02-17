document.addEventListener('DOMContentLoaded', (_event) => {
  document.querySelectorAll('.src').forEach((el) => {
    // sometimes hljs detected lua as visual basic
    // so to prevent that:
    if (el.className.includes("src-lua")) {
      el.classList.add("language-lua");
    }

    hljs.highlightElement(el);
  });
});

const letters = "QWERTYUIOPASDFGHJKLZXCVBNM";
const originaltext = document.querySelector("h1").innerText; 

let interval = null;

document.querySelector("h1").onmouseover = event => {
  let iteration = 0;

  clearInterval(interval);

  interval = setInterval(() => {
    event.target.innertText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if (index < iteration) {
          return originaltext[index];
        }

        return letters[Math.floor(Math.random() * 26)]
      })
      .join("");

    if (iteration >= originaltext.length) {
      clearInterval(interval);
    }

    iteration += 1 / 3;
  }, 30);
}
