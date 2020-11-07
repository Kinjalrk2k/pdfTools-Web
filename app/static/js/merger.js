document.getElementById("continue-btn").addEventListener("click", () => {
  const curr_time = Math.floor(Date.now() / 1000);
  const url = String(curr_time) + "/upload/";
  // console.log(url);
  window.location.replace(url);
});
