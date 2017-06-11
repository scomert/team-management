# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Map
from .forms import MapForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def list_maps(request):
    maps = Map.objects.all()
    return render(request, "maps_index.html", {"maps": maps})


@login_required
def add_map(request):
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


@login_required
def delete_map(request, id):
    map = Map.objects.get(id=id)
    if map:
        map.delete()
    return redirect("maps:maps-list")


@login_required
def map_detail(request, id):
    map = Map.objects.get(id=id)
    strategies = map.strategy_set.all()
    return render(request, "map_detail.html", {"strategies": strategies, "map": map})
