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
from django.conf.urls import url, include
from django.contrib import admin
from main.urls import urlpatterns as main_urls
from maps.urls import urlpatterns as maps_urls
from strategies.urls import urlpatterns as strat_urls
from tactics import settings
from django.conf.urls.static import static
from maps.views import list_maps


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(main_urls, namespace="main")),
    url(r'^maps/', include(maps_urls, namespace="maps")),
    url(r'^strat/', include(strat_urls, namespace="strats")),
    url(r'^$', list_maps, name="maps-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
