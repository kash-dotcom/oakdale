/* global $, document */

// Materialize
$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.datepicker').datepicker();
  $('select').formSelect();
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true,
  });
  // $('.modal').modal();
  $('login_success').tooltip();
  $('.parallax').parallax({ responsiveThreshold: 0 });
  console.log('Materialize loaded');
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

// delete reservation
  // Handle delete reservation button click
  $(document).on('click', '.delete_reservation', function() {
    var reservationId = $(this).data('id');
    $('#delete-reservation-id').val(reservationId);
    console.log('Delete reservation button clicked with reservation ID:', reservationId);
  });
