# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Strategy, Steps
from .forms import StratForm, StepForm
from maps.models import Map
from django.db.models import Q


# Create your views here.


@login_required
def strat_detail(request, id):
    strat = Strategy.objects.get(id=id)
    steps = Steps.objects.filter(user=request.user).filter(strategy=id).order_by("priority")
    c = Steps.objects.filter(user=request.user).filter(strategy=id).count()
    return render(request, "strat_detail.html", {"strat": strat, "steps": steps, "count": c})


@login_required
def strat_add(request, map_id):
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


@login_required
def step_add(request, strat_id):
    strat = Strategy.objects.get(id=strat_id)
    if request.method == "GET":
        CHOICES = [('0', 0), ('1', 1)]
        form = StepForm(initial={'priority': CHOICES})
        return render(request, "step_add.html", {"form": form, "strat": strat})
    else:
        form = StepForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            data = form.cleaned_data
            pr = int(data['priority'])
            x = Steps.objects.filter(user=data['user']).filter(strategy=strat).order_by("priority")
            for i in range(pr - 1, len(x)):
                print x[i], pr, x[i].priority, i
                x[i].priority = i + 2
                x[i].save()
            s = Steps(command=data['command'], image=data['image'], strategy=strat, user=data['user'],
                      priority=data['priority'])
            s.save()
            return redirect("strats:strat-detail", id=strat_id)
        else:
            return HttpResponse(form.errors)


@login_required
def step_edit(request, id):
    if request.method == "POST":
        step = get_object_or_404(Steps, id=id)
        form = StepForm(request.POST or None, instance=step)
        if form.is_valid():
            form.save()
            return redirect("strats:strat-detail", id=str(step.strategy.id))
        return render(request, "step_detail.html", {"form": form, "step": step})
    else:
        step = get_object_or_404(Steps, id=id)
        form = StepForm(instance=step)
        return render(request, "step_detail.html", {"form": form, "step": step})


@login_required
def step_delete(request, id):
    step = get_object_or_404(Steps, id=id)
    if step:
        pr = step.priority
        x = Steps.objects.filter(user=step.user.id).filter(strategy=step.strategy.id).order_by("priority")
        for i in range(pr, len(x)):
            print x[i], pr, x[i].priority, i
            x[i].priority = i
            x[i].save()
        step.delete()
    return redirect("strats:strat-detail", id=str(step.strategy.id))


@login_required
def move_down(request, id):
    step = get_object_or_404(Steps, id=id)
    count = Steps.objects.filter(user=request.user).filter(strategy=step.strategy.id).count()
    if step:
        if step.priority < count:
            new_priority = step.priority + 1
            other_step = Steps.objects.filter(strategy=step.strategy.id).filter(priority=new_priority).first()
            other_step.priority = new_priority - 1
            other_step.save()
            step.priority = new_priority
            step.save()
    return redirect("strats:strat-detail", id=str(step.strategy.id))


@login_required
def move_up(request, id):
    step = get_object_or_404(Steps, id=id)
    if step:
        if step.priority > 0:
            new_priority = step.priority - 1
            other_step = Steps.objects.filter(strategy=step.strategy.id).filter(priority=new_priority).first()
            other_step.priority = new_priority + 1
            other_step.save()
            step.priority = new_priority
            step.save()
    return redirect("strats:strat-detail", id=str(step.strategy.id))