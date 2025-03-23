

// Materialize
$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
  // $('.modal').modal();
  $('login_success').tooltip();
  $('.parallax').parallax({ responsiveThreshold: 0 });
});

//Modal//
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, {});
});

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.datepicker');
  var instances = M.Datepicker.init(elems, format = 'dd-mm-yyyy', autoclose = true, showClearBtn = true);
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

// Materialize select
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

  // // Autofill experience price based on selected experience
  // var experienceSelect = document.getElementById('id_experience_name');
  // var experiencePriceInput = document.getElementById('id_experience_price');

  // experienceSelect.addEventListener('change', function() {
  //   var selectedExperienceId = this.value;
  //   fetch(`/get_experience_price/${selectedExperienceId}/`)
  //     .then(response => response.json())
  //     .then(data => {
  //       experiencePriceInput.value = data.experience_price;
  //     });
  // });

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


// delete reservation
  // Handle delete reservation button click
  $(document).on('click', '.delete_reservation', function() {
    var reservationId = $(this).data('id');
    $('#delete-reservation-id').val(reservationId);
    console.log('Delete reservation button clicked with reservation ID:', reservationId);
  });

  // Log form submission
  $('#delete-reservation-form').on('submit', function(e) {
    e.preventDefault(); 
    var reservationId = $('#delete-reservation-id').val();
      this.submit();    
  });
