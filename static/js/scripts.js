// sidenav

$(document).ready(function () {
  $('.sidenav').sidenav();
});

// carousel

$('.carousel.carousel-slider').carousel({
  fullWidth: true,
  indicators: true
});

// modal
$(document).ready(function () {
  $('.modal').modal();
});

// toast
$(document).ready(function () {
  $('login_success').tooltip();
});

// datepicker
$(document).ready(function () {
  $('.datepicker').datepicker();
});

// https://www.youtube.com/watch?v=4NqAiqdjMI8&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50&index=13&ab_channel=Codemy.com

$(document).on('click', '#add-reservation', function (e) {
  e.preventDefault();
  $.ajax({
    type: 'POST',
    url: '{% url "add_reservation" %}',
    data: {
      experience_id: $('#add-reservation').val(),
      csrfmiddlewaretoken: '{{ csrf_token }}',
      action: 'post'
    },
    success: function (json) {
      console.log(json);
    },
    error: function (xhr, errmsg, err) {

    }

  });

});

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

  // Autofill experience price based on selected experience
  var experienceSelect = document.getElementById('id_experience_name');
  var experiencePriceInput = document.getElementById('id_experience_price');

  experienceSelect.addEventListener('change', function() {
    var selectedExperienceId = this.value;
    fetch(`/get_experience_price/${selectedExperienceId}/`)
      .then(response => response.json())
      .then(data => {
        experiencePriceInput.value = data.experience_price;
      });
  });
