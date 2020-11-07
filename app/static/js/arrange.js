dragula([document.getElementById("arrange-container")]);

$(".spectrum-Stepper-stepUp").on("click", function () {
  var $button = $(this);
  var oldValue = $button.parent().parent().find("input").val();
  // console.log($button.parent().parent().find("input").val());

  if ($button.parent().parent().find("input").prop("disabled")) {
    return;
  }

  var newVal = parseInt(oldValue) + 1;

  $button.parent().parent().find("input").val(newVal);
});

$(".spectrum-Stepper-stepDown").on("click", function () {
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
  } else {
    targ.parentElement.parentElement.parentElement.classList.add("disabled");
    targ.parentElement.parentElement.parentElement
      .querySelectorAll(".spectrum-Stepper-input")
      .forEach((stepper) => {
        stepper.disabled = true;
      });
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
