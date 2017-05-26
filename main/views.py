# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("maps:maps-list")
            else:
                return HttpResponse("Invalid login credentials")

    else:
        if request.user.is_authenticated:
            return HttpResponse("You are already logged in")
        else:
            form = LoginForm()
            return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("main:login"))
