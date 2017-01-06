from django.views.generic.base import TemplateView

from django.shortcuts import render


# Create your views here.
class AptInfoView(TemplateView):
    template_name = 'aptinfo/apt_info.html'
