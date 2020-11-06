const zeroPad = (num, places) => String(num).padStart(places, "0");

function countdown_wrapper(id) {
  setInterval(function () {
    const start_time = Number(id);
    const end_time = start_time + 600;
    const curr_time = Math.floor(Date.now() / 1000);
    const delta = end_time - curr_time;

    if (delta <= 0) {
      window.location.href = "/merger/session-expired/";
    }

    const minutes = Math.floor((delta % (60 * 60)) / 60);
    const seconds = Math.floor(delta % 60);

    console.log(minutes + ":" + seconds);
    document.getElementById("countdown").innerHTML = zeroPad(minutes, 2) + ":" + zeroPad(seconds, 2);
  }, 1000);
}
