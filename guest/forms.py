# from django import forms
# from guest.models import Guest
# from experience.models import Experience
# from .models import Reservation


# class GuestForm(forms.ModelForm):
#     class Meta:
#         model = Guest
#         fields = ['first_name',
#                   'last_name', 'address', 'city',
#                   'postcode', 'email', 'phone_number',]
#         widgets = {
#             'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
#             'address': forms.TextInput(attrs={'placeholder': 'Address'}),
#             'city': forms.TextInput(attrs={'placeholder': 'City'}),
#             'postcode': forms.TextInput(attrs={
#                         'placeholder': 'Postcode'}),
#             'phone_number': forms.TextInput(attrs={
#                             'placeholder': 'Phone Number'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#         }


# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = ['experience_name', 'experience_price',]

#         widgets = {
#             'experience_name': forms.TextInput(attrs={'placeholder': 'Experience Name'}),
#             'experience_price': forms.TextInput(attrs={'placeholder': 'Experience Price'}),
#         }


# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['number_of_guests', 'reservation_date', 'reservation_price']

#         widgets = {
#             'number_of_guests': forms.Select(choices=[(i, i) for i in range(1, 10)], attrs={'placeholder': 'Number of Guests'}),
#             'reservation_date': forms.DateInput(attrs={'placeholder': 'Reservation Date'}),
#             'reservation_price': forms.TextInput(attrs={'placeholder': 'Reservation Price'}),
#         }

#     def save(self, commit=True):
#         total_price = super().save(commit=False)
#         total_price.reservation_price = total_price.number_of_guests * total_price.experience.experience_price
#         if commit:
#             total_price.save()
#         return total_price
    