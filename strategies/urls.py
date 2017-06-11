"""tactics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import strat_detail, strat_add, step_add, step_delete, step_edit, move_up, move_down

urlpatterns = [
    url(r'^(?P<id>\d+)/$', strat_detail, name="strat-detail"),
    url(r'^maps/(?P<map_id>\d+)/add/$', strat_add, name="strat-add"),
    url(r'^(?P<strat_id>\d+)/add/$', step_add, name="strats-step-add"),
    url(r'^delete/(?P<id>\d+)/$', step_delete, name="step-delete"),
    url(r'^edit/(?P<id>\d+)/$', step_edit, name="step-edit"),
    url(r'^move_up/(?P<id>\d+)/$', move_up, name="step-move-up"),
    url(r'^move_down/(?P<id>\d+)/$', move_down, name="step-move-down"),

]
