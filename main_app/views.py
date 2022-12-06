from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from .models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, "main_app/index.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name", None)
        if name:
            try:
                user_obj = User.objects.create(full_name = name, email = email)
                user_obj.set_password(password)
                user_obj.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Registered Successfully",
                    extra_tags="success",
                )

            except IntegrityError:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "You're already registered",
                    extra_tags="danger",
                )
                
        else:
            try:
                user_obj = User.objects.get(email = email)
                auth_user = authenticate(email = email, password = password)
                if auth_user is not None:
                    login(request, auth_user)
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Login successfully",
                        extra_tags="success",
                    )
                    return redirect('profile')
            
            except User.DoesNotExist:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "You're not registered user",
                    extra_tags="danger",
                )


        print("name == ", name)
        print("email == ", email)
        print("password == ", password)
        return redirect('home')

class Profile(View):
    def get(self, request):
        return HttpResponse("Profile")
