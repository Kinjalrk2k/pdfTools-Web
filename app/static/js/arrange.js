dragula([document.getElementById("arrange-container")]);
(function () {
  document.querySelectorAll(".spectrum-Checkbox-input").forEach((chkb) => {
    if (chkb.checked) {
      chkb.parentElement.parentElement.parentElement.classList.remove("disabled");
      chkb.parentElement.parentElement.parentElement
        .querySelectorAll(".spectrum-Stepper-input")
        .forEach((stepper) => {
          stepper.disabled = false;
        });
    } else {
      chkb.parentElement.parentElement.parentElement.classList.add("disabled");
      chkb.parentElement.parentElement.parentElement
        .querySelectorAll(".spectrum-Stepper-input")
        .forEach((stepper) => {
          stepper.disabled = true;
        });
    }
  });
})();

$(document).on("click", ".spectrum-Stepper-stepUp", function () {
  var $button = $(this);
  var oldValue = $button.parent().parent().find("input").val();
  // console.log($button.parent().parent().find("input").val());

  if ($button.parent().parent().find("input").prop("disabled")) {
    return;
  }

  var newVal = parseInt(oldValue) + 1;

  $button.parent().parent().find("input").val(newVal);
});

$(document).on("click", ".spectrum-Stepper-stepDown", function () {
  var $button = $(this);
  var oldValue = $button.parent().parent().find("input").val();
  // console.log($button.parent().parent().find("input").val());

  // console.log($button.parent().parent().find("input").prop("disabled"));
  if ($button.parent().parent().find("input").prop("disabled")) {
    return;
  }

  var newVal = parseInt(oldValue) - 1;

  $button.parent().parent().find("input").val(newVal);
});

function checkbox(e) {
  e = e || window.event;
  var targ = e.target || e.srcElement || e;
  if (targ.checked) {
    targ.parentElement.parentElement.parentElement.classList.remove("disabled");
    targ.parentElement.parentElement.parentElement
      .querySelectorAll(".spectrum-Stepper-input")
      .forEach((stepper) => {
        stepper.disabled = false;
      });
    targ.parentElement.parentElement.parentElement.querySelector("#clone-btn").disabled = false;
  } else {
    targ.parentElement.parentElement.parentElement.classList.add("disabled");
    targ.parentElement.parentElement.parentElement
      .querySelectorAll(".spectrum-Stepper-input")
      .forEach((stepper) => {
        stepper.disabled = true;
      });
    targ.parentElement.parentElement.parentElement.querySelector("#clone-btn").disabled = true;
  }

  const cb_list = document.querySelectorAll(".spectrum-Checkbox-input");
  let count_cb_checked = 0;
  cb_list.forEach((checkb) => {
    if (checkb.checked) {
      count_cb_checked++;
    }
  });

  // console.log(count_cb_checked);
  if (count_cb_checked == 0) {
    cb_list.forEach((checkb) => {
      // console.log(checkb.parentElement.parentElement.parentElement);
      checkb.parentElement.parentElement.parentElement.classList.add("error");
      document.getElementById("submit-btn").disabled = true;
    });
    document.querySelector(".error-row div").style.display = "flex";
  } else {
    cb_list.forEach((checkb) => {
      // console.log(checkb.parentElement.parentElement.parentElement);
      checkb.parentElement.parentElement.parentElement.classList.remove("error");
      document.getElementById("submit-btn").disabled = false;
    });
    document.querySelector(".error-row div").style.display = "none";
  }
}

let clonedElementsNum = 0;

function clone(e) {
  const clonedElement = e.parentElement.parentElement.parentElement.cloneNode(true);
  const parent = document.getElementById("arrange-container");

  clonedElement.querySelector(".spectrum-Checkbox-input").name += "_cloned_" + clonedElementsNum;
  clonedElement.querySelector(".file-input").name += "_cloned_" + clonedElementsNum;
  clonedElement.querySelector("#p_start").name += "_cloned_" + clonedElementsNum;
  clonedElement.querySelector("#p_end").name += "_cloned_" + clonedElementsNum;

  clonedElementsNum++;
  // console.log(clonedElement.querySelector(".spectrum-Checkbox-input").name);
  // console.log(clonedElement.querySelector(".file-input").name);
  // console.log(clonedElement.querySelector("#p_start").name);
  // console.log(clonedElement.querySelector("#p_end").name);

  parent.appendChild(clonedElement);
}
