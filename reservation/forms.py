from django import forms
from guest.models import Guest
from experience.models import Experience
from .models import Reservation


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name',
                  'last_name', 'address', 'city',
                  'postcode', 'email', 'phone_number',]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'postcode': forms.TextInput(attrs={
                        'placeholder': 'Postcode'}),
            'phone_number': forms.TextInput(attrs={
                            'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


class ExperienceForm(forms.ModelForm):
    experience_name = forms.ModelChoiceField(
        queryset=Experience.objects.filter(publish=True),
        empty_label="--------------",)

    class Meta:
        model = Experience
        fields = ['experience_name']
        widgets = {
            'experience_name': forms.Select(attrs={
                'placeholder': 'Name of Experience'}),
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'reservation_date']
        labels = {
            'number_of_guests': "Number of guests, don't forget yourself!",
            'reservation_date': 'Reservation Date', }

        widgets = {
            'number_of_guests': forms.Select(
                choices=[('', "Select the number of guests, don't forget yourself!")] + [(i, i) for i in range(1, 11)],
                attrs={'class': 'form-control'}
            ),
            'reservation_date': forms.DateInput(
                attrs={'class': 'datepicker',
                       'placeholder': 'Reservation Date',
                       'type': 'text', }),
        }
