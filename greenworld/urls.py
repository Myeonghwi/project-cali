"""greenworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from greenworld.views import HomeView, UserCreateView, UserCreateDoneTV
from accounts.views import AccountView
from aptinfo.views import AptInfoView
from calibration.views import CalibrationView, CalibrationResultView
from simulator.views import SimulatorView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='index'),

    # account
    url(r'^account/profile$', AccountView.as_view(), name='account'),

    # registration
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^register/$', UserCreateView.as_view(), name='register'),
    url(r'^register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    # main simulation
    url(r'^simulation/apt_info/$', AptInfoView.as_view(), name='apt_info'),
    url(r'^simulation/calibration/$', CalibrationView.as_view(), name='calibration'),
    url(r'^simulation/calibration/result/$', CalibrationResultView.as_view(), name='calibration_result'),
    url(r'^simulation/main/$', SimulatorView.as_view(), name='main'),
]
