/* global $, document, M, console */

/*This code was refactored by copilot*/
// Materialize
$(document).ready(function () {
  $(".sidenav").sidenav();
  $(".carousel.carousel-slider").carousel({
    fullWidth: true,
    indicators: true
  });
  $(".modal").modal();
  $("login_success").tooltip();
  $(".parallax").parallax({ responsiveThreshold: 0 });
});

document.addEventListener("DOMContentLoaded", function() {
  var elems = document.querySelectorAll(".datepicker");
  var instances = M.Datepicker.init(elems, {
    format: "dd-mm-yyyy",
    autoclose: true,
    showClearBtn: true
  });
});

// https://www.youtube.com/watch?v=4NqAiqdjMI8&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50&index=13&ab_channel=Codemy.com

$(document).on("click", "#add-reservation", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "{% url 'add_reservation' %}",
    data: {
      csrfmiddlewaretoken: "{{ csrf_token }}",
      experience_id: $("#add-reservation").val(),
      action: "post"
    },
    success: function (json) {
      console.log(json);
    },
    error: function (xhr, errmsg, err) {
      // Handle error
    }
  });
});
// Materialize select
document.addEventListener("DOMContentLoaded", function() {
  var elems = document.querySelectorAll("select");
  var instances = M.FormSelect.init(elems);
});

// delete reservation
// Handle delete reservation button click
$(document).on("click", ".delete_reservation", function() {
  var reservationId = $(this).data("id");
  $("#delete-reservation-id").val(reservationId);
  console.log("Delete reservation button clicked with reservation ID:", reservationId);
});

// Log form submission
$("#delete-reservation-form").on("submit", function(e) {
  e.preventDefault(); 
  var reservationId = $("#delete-reservation-id").val();
  this.submit();    
});
