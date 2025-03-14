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
        empty_label=None,)

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

        widgets = {
            'number_of_guests': forms.Select(choices=[(
                    i, i) for i in range(1, 11)], attrs={
                    'placeholder': 'Number of Guests'}),
            'reservation_date': forms.DateInput(
                attrs={'class': 'datepicker',
                       'placeholder': 'Reservation Date'}),
        }

    # def save(self, commit=True):
    #     total_price = super().save(commit=False)
    #     total_price.reservation_price = (
    #         total_price.number_of_guests
    # * total_price.experience.experience_price
    #     )
    #     if commit:
    #         total_price.save()
    #     return total_price
