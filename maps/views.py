# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Map
from .forms import MapForm


# Create your views here.


def authentication_filter(request):
    if not request.user.is_authenticated:
        return redirect("main:login")


def list_maps(request):
    authentication_filter(request)
    maps = Map.objects.all()
    return render(request, "maps_index.html", {"maps": maps})


def add_map(request):
    authentication_filter(request)
    if request.method == "GET":
        form = MapForm()
        return render(request, "maps_add.html", {"form": form})
    else:
        form = MapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maps:maps-list")
        else:
            return HttpResponse("Give valid paramaters")


def delete_map(request, id):
    authentication_filter(request)
    map = Map.objects.get(id=id)
    if map:
        map.delete()
    return redirect("maps:maps-list")


def map_detail(request, id):
    authentication_filter(request)
    map = Map.objects.get(id=id)
    strategies = map.strategy_set.all()
    return render(request, "map_detail.html", {"strategies": strategies, "map": map})
