const carousel = document.querySelector('.carousel');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
let slidePosition = 0;
const slides = carousel.querySelectorAll('.slide');
const totalSlides = slides.length;

prevBtn.addEventListener('click', function() {
  if (slidePosition === 0) {
    slidePosition = totalSlides - 1;
  } else {
    slidePosition--;
  }
  updateSlidePosition();
});

nextBtn.addEventListener('click', function() {
  if (slidePosition === totalSlides - 1) {
    slidePosition = 0;
  } else {
    slidePosition++;
  }
  updateSlidePosition();
});

function updateSlidePosition() {
  for (let slide of slides) {
    slide.classList.remove('active');
    slide.classList.add('inactive');
  }
  slides[slidePosition].classList.remove('inactive');
  slides[slidePosition].classList.add('active');
}

// watsapp starts
window.addEventListener("scroll", function () {
  var whatsappButton = document.getElementById("whatsapp-button");
  if (window.scrollY > 300) {
    whatsappButton.style.opacity = "1";
  } else {
    whatsappButton.style.opacity = "0";
  }
});
// watsapp ends


