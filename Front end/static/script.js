let startTime, timerInterval;
const slides = document.querySelectorAll(".slide");
var counter = 0;
const intervalTime = 60000;
let slideInterval;

slides.forEach((slide, index) => {
  slide.style.left = `${index * 100}%`;
});

const goprev = () => {
  clearInterval(slideInterval);
  if (counter == 0) {
    counter = slides.length - 1;
    slideimage();
  } else {
    counter--;
    slideimage();
  }
  startSlideShow();
};

const gonext = () => {
  clearInterval(slideInterval);
  if (counter == slides.length - 1) {
    counter = 0;
    slideimage();
  } else {
    counter++;
    slideimage();
  }
  startSlideShow();
};

const startSlideShow = () => {
  slideInterval = setInterval(gonext, intervalTime);
};

const slideimage = () => {
  slides.forEach((slide) => {
    slide.style.transform = `translateX(-${counter * 100}%)`;
  });
};
startSlideShow();

const passageDisplay = document.getElementById("passage");
const timerDisplay = document.getElementById("timer");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

startBtn.addEventListener("click", startTimer);
stopBtn.addEventListener("click", stopTimer);

function startTimer() {
  startTime = Date.now();
  timerInterval = setInterval(updateTimer, 1000);
  startBtn.disabled = true;
}

function stopTimer() {
  clearInterval(timerInterval);
  startBtn.disabled = false;
}

function updateTimer() {
  const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
  const minutes = Math.floor(elapsedTime / 60);
  const seconds = elapsedTime % 60;
  timerDisplay.textContent = `${minutes.toString().padStart(2, "0")}:${seconds
    .toString()
    .padStart(2, "0")}`;
}
