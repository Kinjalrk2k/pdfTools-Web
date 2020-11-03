Dropzone.autoDiscover = false;
var myDropzone = new Dropzone("div#upload-box", {
  url: "upload",
  autoProcessQueue: false,
  parallelUploads: 10,
  uploadMultiple: true,
});
// var myDropzone = new Dropzone("div#upload-box");

document.getElementById("submit-btn").addEventListener("click", () => {
  console.log("here");
  myDropzone.processQueue();
});
