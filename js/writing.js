let elements = document.querySelectorAll("h2");

elements.forEach(elem => {
    elem.innerText = "# " + elem.innerText;
});

hljs.highlightAll();