document.getElementById("toggle-mode-btn").addEventListener("click", () => {
  const html = document.getElementsByTagName("html")[0];
  if (html.classList.contains("spectrum--light")) {
    html.classList.remove("spectrum--light");
    html.classList.add("spectrum--dark");
    localStorage.setItem("theme", "spectrum--dark");
  } else {
    html.classList.remove("spectrum--dark");
    html.classList.add("spectrum--light");
    localStorage.setItem("theme", "spectrum--light");
  }
});

(function () {
  const onpageLoadTheme = localStorage.getItem("theme") || "spectrum--light";
  const html = document.getElementsByTagName("html")[0];
  html.classList.remove("spectrum--light");
  html.classList.remove("spectrum--dark");
  html.classList.add(onpageLoadTheme);
})();
