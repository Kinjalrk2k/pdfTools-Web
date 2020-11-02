document.getElementById("toggle-mode-btn").addEventListener("click", () => {
  const html = document.getElementsByTagName("html")[0];
  if (html.classList.contains("spectrum--light")) {
    html.classList.remove("spectrum--light");
    html.classList.add("spectrum--dark");
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-sun";
    localStorage.setItem("theme", "spectrum--dark");
  } else {
    html.classList.remove("spectrum--dark");
    html.classList.add("spectrum--light");
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-moon";
    localStorage.setItem("theme", "spectrum--light");
  }
});

(function () {
  const onpageLoadTheme = localStorage.getItem("theme") || "spectrum--light";
  const html = document.getElementsByTagName("html")[0];

  if (onpageLoadTheme === "spectrum--light") {
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-moon";
  } else {
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-sun";
  }
  html.classList.remove("spectrum--light");
  html.classList.remove("spectrum--dark");
  html.classList.add(onpageLoadTheme);
})();
