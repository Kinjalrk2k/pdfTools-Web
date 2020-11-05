document.getElementById("toggle-mode-btn").addEventListener("click", () => {
  const html = document.getElementsByTagName("html")[0];
  if (html.classList.contains("spectrum--light")) {
    localStorage.setItem("theme", "spectrum--dark");
    html.classList.remove("spectrum--light");
    html.classList.add("spectrum--dark");
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-sun";

    if (document.getElementsByClassName("tutorial-img-row").length > 0) {
      document.getElementById("tutorial-img-light").style.display = "none";
      document.getElementById("tutorial-img-dark").style.display = "block";
    }
  } else {
    localStorage.setItem("theme", "spectrum--light");

    html.classList.remove("spectrum--dark");
    html.classList.add("spectrum--light");
    document.querySelector("#toggle-mode-btn span i").className = "fas fa-moon";

    if (document.getElementsByClassName("tutorial-img-row").length > 0) {
      document.getElementById("tutorial-img-dark").style.display = "none";
      document.getElementById("tutorial-img-light").style.display = "block";
    }
  }
});

(function () {
  const onpageLoadTheme = localStorage.getItem("theme") || "spectrum--light";
  const html = document.getElementsByTagName("html")[0];

  if (onpageLoadTheme === "spectrum--light") {
    if (document.getElementsByClassName("tutorial-img-row").length > 0) {
      document.getElementById("tutorial-img-dark").style.display = "none";
      document.getElementById("tutorial-img-light").style.display = "block";
    }

    document.querySelector("#toggle-mode-btn span i").className = "fas fa-moon";
  } else {
    if (document.getElementsByClassName("tutorial-img-row").length > 0) {
      document.getElementById("tutorial-img-light").style.display = "none";
      document.getElementById("tutorial-img-dark").style.display = "block";
    }

    document.querySelector("#toggle-mode-btn span i").className = "fas fa-sun";
  }
  html.classList.remove("spectrum--light");
  html.classList.remove("spectrum--dark");
  html.classList.add(onpageLoadTheme);
})();
