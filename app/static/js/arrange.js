dragula([document.getElementById("arrange-container")]);

// document.getElementById("stepUp").addEventListener("click", (e) => {
//   const ele = document.getElementById("stepUp");
//   console.log(e.target);
//   console.log(e.parentElement.parentElement.firstChild.nextSibling.firstChild.nextSibling.value);
//   let targert = ele.parentElement.parentElement.firstChild.nextSibling.firstChild.nextSibling;

//   targert.value = parseInt(targert.value) + 1;
//   e.preventDefault();
// });

// document.getElementById("stepDown").addEventListener("click", (e) => {
//   const ele = document.getElementById("stepDown");
//   console.log(ele.parentElement.parentElement.firstChild.nextSibling.firstChild.nextSibling.value);
//   let targert = ele.parentElement.parentElement.firstChild.nextSibling.firstChild.nextSibling;

//   targert.value = parseInt(targert.value) - 1;
//   e.preventDefault();
// });

$(".spectrum-Stepper-stepUp").on("click", function () {
  var $button = $(this);
  var oldValue = $button.parent().parent().find("input").val();
  console.log($button.parent().parent().find("input").val());

  var newVal = parseInt(oldValue) + 1;

  $button.parent().parent().find("input").val(newVal);
});

$(".spectrum-Stepper-stepDown").on("click", function () {
  var $button = $(this);
  var oldValue = $button.parent().parent().find("input").val();
  console.log($button.parent().parent().find("input").val());

  var newVal = parseInt(oldValue) - 1;

  $button.parent().parent().find("input").val(newVal);
});
