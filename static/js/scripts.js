$(document).ready(function () {
    $('#menu-toggle').on('click', function() {
        $('#side-menu').css('left', '0'); // Slide in
    });

    $('#close-menu').on('click', function() {
        $('#side-menu').css('left', '-250px'); // Slide out
    });
  // Smooth scroll to sections
  $('a[href^="#"]').on('click', function (e) {
      e.preventDefault();
      var target = this.hash;
      $('html, body').animate({
          scrollTop: $(target).offset().top
      }, 600);
  });

  // Modal photo viewer
  $('.photo-gallery img').on('click', function () {
      var imgSrc = $(this).attr('src');
      $('body').append('<div class="modal"><img src="' + imgSrc + '"><span class="close-modal">&times;</span></div>');
      $('.modal').fadeIn(300);

      // Close modal
      $('.close-modal, .modal').on('click', function () {
          $('.modal').fadeOut(300, function () {
              $(this).remove();
          });
      });
  });

  // Image preview for guest photo upload
  $('input[type="file"]').change(function (e) {
      let reader = new FileReader();
      reader.onload = function (e) {
          $('#preview').attr('src', e.target.result);
      };
      reader.readAsDataURL(this.files[0]);
  });

  // Parallax effect for hero section
  const hero = document.querySelector('.hero');
  if (hero) {
      window.addEventListener('scroll', () => {
          const scrollPosition = window.scrollY;
          hero.style.transform = `translateY(-${scrollPosition * 0.5}px)`;
      });
  }

  // Initialize and show the slideshow
  let slideIndex = 0;
  let slideInterval;

  function showSlides() {
      let i;
      let slides = document.getElementsByClassName("mySlides");
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";  
      }
      slideIndex++;
      if (slideIndex > slides.length) { slideIndex = 1; }
      slides[slideIndex - 1].style.display = "block";  
      
      // Automatically change slide every 3 seconds
      slideInterval = setTimeout(showSlides, 3000);
  }

  function plusSlides(n) {
      clearTimeout(slideInterval); // Stop the current interval
      slideIndex += n;
      if (slideIndex > document.getElementsByClassName("mySlides").length) {
          slideIndex = 1;
      }
      if (slideIndex < 1) {
          slideIndex = document.getElementsByClassName("mySlides").length;
      }
      showSlides(); // Manually show slides
  }

  // Attach event listeners to prev/next buttons
  $('.prev').on('click', function() {
      plusSlides(-1);
  });

  $('.next').on('click', function() {
      plusSlides(1);
  });

  // Start the slideshow
  showSlides();
});
