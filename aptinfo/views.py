import requests
import xmltodict
import greenworld.settings as setting
from aptinfo.controller import parse_xml

from django.views.generic.base import TemplateView
from django.views.generic import View
from django.shortcuts import render


# Create your views here.
class AptInfoView(View):

    template_name = 'aptinfo/apt_info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        apt_url = "http://apis.data.go.kr/1611000/AptListService/getRoadnameAptList?serviceKey=qmtrltW6G7zoOxVeLWJJ%2FE%2BYEnmZeicm4b8mQQmJPnS1ZKDpg1dg1xLMIiKfzleMVxHD%2F9%2FvECvVBINhw2QcEw%3D%3D&loadCode=431113236035&pageNo=1&startPage=1&numOfRows=10&pageSize=10"
        res = requests.get(apt_url)

        apt_dict = parse_xml(xmltodict.parse(res.text))

        return render(request, self.template_name)


# 추후에 옮겨야함
class MainView(TemplateView):
    template_name = 'simulator/simulator.html'
