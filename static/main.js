document.addEventListener('DOMContentLoaded', (_event) => {
  document.querySelectorAll('.src').forEach((el) => {
    if (el.className.includes("src-lua")) {
      el.classList.add("language-lua");
    }

    hljs.highlightElement(el);
  });
});

document.getElementById("org-div-home-and-up").innerHTML = "<a accesskey=\"H\" href=\"/\"> HOME </a>"

//let elements = document.getElementsByClassName("src");
//for (let i = 0; i < elements.length; i++) {
//  let el = elements[i];
//
//  if (el.className.includes("src-lua")) {
//    el.classList.add("language-lua");
//  }
//}
