// Materialize
$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
  $('.modal').modal();
  $('login_success').tooltip();
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

// modal 
// document.querySelectorAll('.modal-trigger').forEach(function(trigger) {
//   trigger.addEventListener('click', function() {
//     var reservationId = this.getAttribute('data-id');
//     var reservationDate = this.getAttribute('data-date');
//     var numberOfGuests = this.getAttribute('data-guests');
//     var experienceId = this.getAttribute('data-experience');

//     if (this.href.includes('#modal2')) {
//       document.getElementById('reservation-id').value = reservationId;
//       document.getElementById('id_reservation_date').value = reservationDate;
//       document.getElementById('id_number_of_guests').value = numberOfGuests;
//       document.getElementById('id_experience_name').value = experienceId;
//     } else if (this.href.includes('#modal3')) {
//       document.getElementById('delete-reservation-id').value = reservationId;
//     }
//   });
// });


// // delete reservation
// $(document).on('click', 'delete-reservation', function(e) {
//   e.preventDefault();

//   var reservationId = $(this).data('id');

//   $.ajax({
//     type: 'POST',
//     url: '{% url "delete_reservation" %}',
//     data: {
//       reservation_id: (this).data('id'),
//       csrfmiddlewaretoken: '{{ csrf_token }}',
//       action: 'post'
//     },
//     success: function(json) {
//       console.log(json);
//       document.getElementById('reservation-' + reservationId).remove();
//       M.toast({html: 'Reservation deleted successfully!'});
//     },
//     error: function(xhr, errmsg, err) {

//     }
//   });