function setStyles(element, styles) {
  const oldStyles = {};
  for (let property in styles) {
    oldStyles[property] = element.style[property];
    element.style[property] = styles[property];
  }
  return oldStyles;
}

class Coach {
  constructor(coachMetadata) {
    this.coachMetadata = coachMetadata;
    // this.coachTargetList = coachTargetList;
    // this.coachDataList = coachDataList;
    this.totalItems = coachMetadata.length;
    this.currCoachNum = -1;
    this.coachDiv = document.createElement("div");

    this.overlay = this.buildOverlay();
    document.getElementsByTagName("body")[0].appendChild(this.overlay);
    document.getElementsByTagName("body")[0].appendChild(this.coachDiv);

    this.initialZIndex = null;

    this.attachEventListeners();
  }

  attachEventListeners() {
    $(document).on("click", "#skip-coach", () => this.resetCoach());
    $(document).on("click", "#next-coach", () => this.nextCoach());
  }

  buildOverlay() {
    const overlay = document.createElement("div");
    const oldOverlayStyles = setStyles(overlay, {
      height: "100%",
      width: "100%",
      position: "fixed",
      backgroundColor: "rgba(0,0,0, 0.8)",
      top: 0,
      left: 0,
      zIndex: 1000,
      display: "none",
    });

    return overlay;
  }

  nextCoach() {
    if (this.currCoachNum + 1 >= this.totalItems) {
      this.resetCoach();
      return;
    }
    if (this.currCoachNum >= 0) {
      const oldcoachTarget = document.querySelector(this.coachMetadata[this.currCoachNum].target);
      setStyles(oldcoachTarget, this.initialZIndex);
    }
    this.currCoachNum++;
    const coachTarget = document.querySelector(this.coachMetadata[this.currCoachNum].target);
    var rect = coachTarget.getBoundingClientRect();
    this.buildCoachDiv(
      (rect.top + rect.bottom) / 2 + window.scrollY,
      (rect.left + rect.right) / 2 + window.scrollX
    );

    console.log((rect.top + rect.bottom) / 2 + window.scrollY, (rect.left + rect.right) / 2 + window.scrollX);

    this.initialZIndex = setStyles(coachTarget, { zIndex: 1001 });

    this.overlay.style.display = "block";
    this.coachDiv.style.display = "block";
    this.coachDiv.scrollIntoView();
  }

  pauseCoach() {
    if (this.currCoachNum >= 0) {
      const oldcoachTarget = document.querySelector(this.coachMetadata[this.currCoachNum].target);
      setStyles(oldcoachTarget, this.initialZIndex);
    }
    this.overlay.style.display = "none";
    this.coachDiv.style.display = "none";
  }

  resetCoach() {
    if (this.currCoachNum >= 0) {
      const oldcoachTarget = document.querySelector(this.coachMetadata[this.currCoachNum].target);
      setStyles(oldcoachTarget, this.initialZIndex);
    }
    this.overlay.style.display = "none";
    this.coachDiv.style.display = "none";
    this.currCoachNum = -1;
  }

  buildCoachDiv(top, left) {
    this.coachDiv.innerHTML = `
    <div class="spectrum-CoachMarkIndicator">
      <div class="spectrum-CoachMarkIndicator-ring"></div>
      <div class="spectrum-CoachMarkIndicator-ring"></div>
      <div class="spectrum-CoachMarkIndicator-ring"></div>
    </div>

    <div class="spectrum-CoachMarkPopover">
      <div class="spectrum-CoachMarkPopover-header">
        <div class="spectrum-CoachMarkPopover-title">${this.coachMetadata[this.currCoachNum].head}</div>
        <div class="spectrum-CoachMarkPopover-step"><bdo dir="ltr">${this.currCoachNum + 1} of ${
      this.totalItems
    }</bdo></div>
      </div>
      <div class="spectrum-CoachMarkPopover-content">
        ${this.coachMetadata[this.currCoachNum].body}
      </div>
      <div class="spectrum-CoachMarkPopover-footer">
        <button class="spectrum-Button spectrum-Button--secondary spectrum-Button--quiet" id="skip-coach">
          <span>Skip Tour</span>
        </button>
        <button class="spectrum-Button spectrum-Button--primary" id="next-coach">
          <span>${this.currCoachNum + 1 === this.totalItems ? "Finish" : "Next"}</span>
        </button>
      </div>
    </div>
    `;

    setStyles(this.coachDiv, {
      position: "absolute",
      top: top + "px",
      left: left + "px",
      zIndex: 1002,
      display: "none",
    });
  }
}
