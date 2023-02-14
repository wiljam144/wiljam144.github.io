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
