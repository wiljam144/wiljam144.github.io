const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const origText = document.querySelector(".title").innerText;

let interval = null;

document.querySelector("h1").onmouseover = event => {  
  let iteration = 0;
  
  clearInterval(interval);
  
  interval = setInterval(() => {
    event.target.innerText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if(index < iteration) {
          return event.target.dataset.value[index];
        }
      
        return letters[Math.floor(Math.random() * 52)]
      })
      .join("");
    
    if(iteration >= event.target.dataset.value.length){ 
      clearInterval(interval);
    }
    
    iteration += 1 / 3;
  }, 30);
}

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
