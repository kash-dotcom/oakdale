# from django.shortcuts import render, redirect
# from django.views import generic, View
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# # from django import forms
# from .models import Guest
# from .forms import GuestForm, ExperienceForm, ReservationForm


# # Create your views here.


# class GuestList(generic.ListView):
#     model = Guest
#     queryset = Guest.objects.all()
#     template_name = "guest/guest.html"
#     context_object_name = 'guest_list'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             context['guest_form'] = GuestForm(instance=self.request.user)
#             context['experience_form'] = ExperienceForm()
#             context['reservation_form'] = ReservationForm()
#         else:
#             messages.info(self.request, 'Please log in to view your profile')
#             return redirect('signup')
#         return context

# # class SignUpView(View):
# #     def get(self, request):
# #         form = UserCreationForm()
# #         return render(request, 'account/signup.html', {'form': form})

# #     def post(self, request):
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)
# #             return redirect('guest_list')
# #         return render(request, 'account/signup.html', {'form': form})




# # def guest_profile(request):
# #     context = {}

# #     profile = GuestForm(request.POST or None, instance=request.user)

# #     if profile.is_valid():
# #         profile.save()

# #     context['profile'] = profile

# #     return render(request, 'guest/guest_form.html', context)

#     # if request.method == "POST":
#     #     profile = GuestForm(data=request.POST, instance=request.user)
#     #         return redirect('home')

#     #     messages.success(request, 'Welcome, {{ user.username }}')
#     # else:
#     #     form = GuestForm()
#     # return render(request, 'guest/guest_form.html', {'form': form})

# # class GuestCreate(generic.CreateView):
# #     model = Guest
# #     form_class = GuestForm
# #     template_name = "guest/guest_form.html"
# #     success_url = 'home'

# #     def form_valid(self, form):
# #         form.instance.user = self.request.user
# #         return super().form_valid(form)

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['guest_list'] = Guest.objects.all()
# #         return context
