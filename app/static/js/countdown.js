const zeroPad = (num, places) => String(num).padStart(places, "0");
const time_limit = 600;
const toast_target = document.getElementsByClassName("spectrum-Toast")[0];
const countdown_text = document.getElementById("countdown");
const countdown_progress = document.querySelector(".progress-bar #bar");

function countdown_wrapper(id) {
  setInterval(function () {
    const start_time = Number(id);
    const end_time = start_time + time_limit;
    const curr_time = Math.floor(Date.now() / 1000);
    const delta = end_time - curr_time;
    const elapsed = curr_time - start_time;

    if (delta <= 0) {
      window.location.href = "/merger/session-expired/";
    }

    if (delta < time_limit / 3) {
      toast_target.classList.add("spectrum-Toast--negative");
      toast_target.classList.remove("spectrum-Toast--positive");
      toast_target.classList.remove("spectrum-Toast--info");
    } else if (delta < (time_limit * 2) / 3) {
      toast_target.classList.add("spectrum-Toast--info");
      toast_target.classList.remove("spectrum-Toast--positive");
      toast_target.classList.remove("spectrum-Toast--nevative");
    } else {
      toast_target.classList.add("spectrum-Toast--positive");
      toast_target.classList.remove("spectrum-Toast--nevative");
      toast_target.classList.remove("spectrum-Toast--info");
    }

    const minutes = Math.floor((delta % (60 * 60)) / 60);
    const seconds = Math.floor(delta % 60);

    // console.log(minutes + ":" + seconds);
    countdown_text.innerHTML = zeroPad(minutes, 2) + ":" + zeroPad(seconds, 2);
    // console.log((elapsed / time_limit) * 100);
    countdown_progress.style.width = (elapsed / time_limit) * 100 + "%";
  }, 1000);
}
