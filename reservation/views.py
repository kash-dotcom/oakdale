from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from experience.models import Experience
from django.http import JsonResponse
from .models import Reservation
from guest.models import Guest
# from experience.models import Experience
from .forms import GuestForm, ExperienceForm, ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# def reservation(request, experience_id=None):
#     experience = None
#     if experience_id:
#         experience = get_object_or_404(Experience, pk=experience_id)
#     return render(request, 'reservation.html', {
#         'experience': experience,
#         'experience_list': Experience.objects.filter(publish=True)
#     })


class ReservationListView(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = "reservation/reservation.html"
    context_object_name = 'reservations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['guest_form'] = GuestForm(instance=self.request.user)
            context['experience_form'] = ExperienceForm()
            context['reservation_form'] = ReservationForm()
        return context


def get_experience_price(request, experience_id):
    experience = get_object_or_404(Experience, experience_id=experience_id)
    return JsonResponse({'experience_price': experience.experience_price})


def add_reservation(request):
    if request.method == 'POST':
        guest_form = GuestForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if (guest_form.is_valid() and
            experience_form.is_valid() and
                reservation_form.is_valid()):
            guest, created = Guest.objects.get_or_create(user=request.user)
            if not created:
                guest_form = GuestForm(request.POST, instance=guest)
                guest = guest_form.save()

            experience = experience_form.cleaned_data['experience_name']

            reservation = reservation_form.save(commit=False)
            reservation.guest = guest
            reservation.experience = experience
            reservation.reservation_price = (
                experience.experience_price * reservation.number_of_guests
            )
            reservation.save()

            guest.last_visit = reservation.reservation_date
            guest.save()

            messages.success(request, 'Reservation created successfully!')
            return redirect('confirmation',
                            reservation_id=reservation.reservation_id)
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        guest_form = GuestForm()
        experience_form = ExperienceForm()
        reservation_form = ReservationForm()

    return render(request, 'reservation/reservation.html', {
        'guest_form': guest_form,
        'experience_form': experience_form,
        'reservation_form': reservation_form,
    })


def confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    guest = reservation.guest
    experience = reservation.experience

    context = {
        'reservation': reservation,
        'guest': guest,
        'experience': experience,
        'reservation_price': reservation.reservation_price,
    }
    return render(request, 'reservation/confirmation.html', context)


@login_required
def past_reservations(request):
    guest = Guest.objects.get(user=request.user)
    reservations = Reservation.objects.filter(guest=guest)
    return render(request, 'reservation/past_reservations.html',
                  {'reservations': reservations})


@login_required
def change_reservation(request, reservation_id):
    # Fetch the guest and reservation
    guest = Guest.objects.get(user=request.user)
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    # Check if the reservation belongs to the guest
    if request.method == 'POST':
        guest_form = GuestForm(request.POST, instance=reservation.guest)
        experience_form = ExperienceForm(request.POST,
                                         instance=reservation.experience)
        reservation_form = ReservationForm(request.POST, instance=reservation)

        if (reservation_form.is_valid() and
            guest_form.is_valid() and
                experience_form.is_valid()):
            guest = guest_form.save()

            experience = experience_form.save()
            reservation = reservation_form.save(commit=False)
            reservation.reservation_price = (
                experience.experience_price * reservation.number_of_guests
            )
            reservation.save()

            messages.success(request, 'Reservation updated successfully!')
            return redirect('past_reservations')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        guest_form = GuestForm(instance=guest)
        experience_form = ExperienceForm(
            instance=reservation.experience,
            initial={'experience_name': reservation.experience}
        )
        reservation_form = ReservationForm(instance=reservation)

    context = {
        'guest_form': guest_form,
        'experience_form': experience_form,
        'reservation_form': reservation_form,
        'reservation': reservation,
        'reservation_id': reservation_id,
    }
    return render(request, 'reservation/change_reservation.html', context)


@login_required
def delete_reservation(request):
    reservation_id = request.POST.get('reservation_id')
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    reservation.delete()

    messages.success(request, 'Reservation deleted successfully!')
    return redirect('past_reservations')

    # if request.method == 'POST':
    #     reservation_id = request.POST.get('reservation_id')
    #     reservation = get_object_or_404(Reservation,
    #       reservation_id=reservation_id)
    #     guest_form = GuestForm(request.POST, instance=reservation.guest)
    #     experience_form = ExperienceForm(request.POST,
    #       instance=reservation.experience)
    #     reservation_form = ReservationForm(request.POST,
    #       instance=reservation)

    #     if reservation_form.is_valid() and guest_form.is_valid() and
    #       experience_form.is_valid():
    #         guest = guest_form.save()
    #         experience = experience_form.save()
    #         reservation = reservation_form.save(commit=False)
    #         reservation.reservation_price = (
    #             experience.experience_price * reservation.number_of_guests
    #         )
    #         reservation_form.save(commit=True)

    #         messages.success(request, 'Reservation updated successfully!')
    #         return redirect('reservation_confirmation',
    #                         reservation_id=reservation.reservation)
    #     else:
    #         messages.error(request,
    #           'There was an error with your submission.')
    # else:
    #     reservation_id = request.GET.get('reservation_id')
    #     reservation = get_object_or_404(Reservation,
    #       reservation_id=reservation_id)
    #     guest_form = GuestForm(instance=reservation.guest)
    #     experience_form = ExperienceForm(instance=reservation.experience)
    #     reservation_form = ReservationForm(instance=reservation)

    #     return render(request, 'past_reservation.html',
    #                   {'guest_form': guest_form,
    #                    'experience_form': experience_form,
    #                    'reservation_form': reservation_form,
    #                    'reservation_id': reservation_id, })


# def change_reservation(request, reservation_id):
#     # Fetch the guest and reservation
#     guest = Guest.objects.get(user=request.user)
#     reservation = get_object_or_404(Reservation,
#       reservation_id=reservation_id)
#     # Check if the reservation belongs to the guest
#     if request.method == 'POST':
#         guest_form = GuestForm(request.POST, instance=reservation.guest)
#         experience_form = ExperienceForm(request.POST,
#           instance=reservation.experience)
#         reservation_form = ReservationForm(request.POST,
#             instance=reservation)

#         if reservation_form.is_valid() and guest_form.is_valid() and
#               experience_form.is_valid():
#             guest = guest_form.save()

#             experience = experience_form.save()
#             reservation = reservation_form.save(commit=False)
#             reservation.reservation_price = (
#                 experience.experience_price * reservation.number_of_guests
#             )
#             reservation.save()

#             messages.success(request, 'Reservation updated successfully!')
#             return redirect('past_reservations')
#         else:
#             messages.error(request,
#                  'There was an error with your submission.')
#     else:
#         guest_form = GuestForm(instance=guest)
#         experience_form = ExperienceForm(
#             instance=reservation.experience,
#             initial={'experience_name': reservation.experience}
#         )
#         reservation_form = ReservationForm(instance=reservation)

#     context = {
#         'guest_form': guest_form,
#         'experience_form': experience_form,
#         'reservation_form': reservation_form,
#         'reservation': reservation,
#         'reservation_id': reservation_id,
#     }
#     return render(request, 'delete_reservation.html', {})
