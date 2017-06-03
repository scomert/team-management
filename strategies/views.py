# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Strategy, Steps
from .forms import StratForm, StepForm
from maps.models import Map
from django.db.models import Q


# Create your views here.

def authentication_filter(request):
    if not request.user.is_authenticated:
        return redirect("main:login")


def strat_detail(request, id):
    authentication_filter(request)
    strat = Strategy.objects.get(id=id)
    steps = Steps.objects.filter(user=request.user).filter(strategy=id).order_by("priority")
    return render(request, "strat_detail.html", {"strat": strat, "steps": steps})


def strat_add(request, map_id):
    authentication_filter(request)
    if request.method == "GET":
        map = get_object_or_404(Map, id=map_id)
        form = StratForm(initial={'map': map})
        return render(request, "strat_add.html", {"form": form, "map": map})
    else:
        form = StratForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            s = Strategy(name=form.cleaned_data['name'], map=Map.objects.get(id=map_id))
            s.save()
            return redirect("maps:map-detail", id=map_id)
        else:
            return HttpResponse("Give valid paramaters")


def step_add(request, strat_id):
    authentication_filter(request)
    strat = Strategy.objects.get(id=strat_id)
    if request.method == "GET":
        CHOICES = [('0', 0), ('1', 1)]
        form = StepForm(initial={'priority': CHOICES})
        return render(request, "step_add.html", {"form": form, "strat": strat})
    else:
        form = StepForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data = form.cleaned_data
            st = Strategy.objects.get(id=int(strat_id))
            print st
            s = Steps(command=data['command'], image=data['image'], strategy=strat, user=data['user'])
            s.save()
            return redirect("strats:strat-detail", id=strat_id)
        else:
            return HttpResponse(form.errors)
            # s = Steps(command=form.cleaned_data['command'], image=form.cleaned_data['image'], strategy=int(strat_id), user=int(request.user.id))
            # s.save()
            # return redirect("strats:strat-detail", id=strat_id)


def step_delete(request, id):
    authentication_filter(request)
    step = get_object_or_404(Steps, id=id)
    if step:
        step.delete()
    return redirect("strats:strat-detail", id=str(step.strategy.id))
