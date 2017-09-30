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

        SITE = 'http://apis.data.go.kr'
        PAGE = 'pageNo=1&startPage=1&numOfRows=10&pageSize=10'
        KEY = 'qmtrltW6G7zoOxVeLWJJ%2FE%2BYEnmZeicm4b8mQQmJPnS1ZKDpg1dg1xLMIiKfzleMVxHD%2F9%2FvECvVBINhw2QcEw%3D%3D'

        if 'road_code' in request.POST:
            road_code = request.POST['road_code']
        else:
            return render(request, self.template_name, {'response': '도로명 코드를 찾지못했습니다.'})

        apt_url = f'{SITE}/1611000/AptListService/getRoadnameAptList?serviceKey={KEY}&loadCode={road_code}&{PAGE}'

        res = requests.get(apt_url)

        apt_dict = parse_xml(xmltodict.parse(res.text))

        print(apt_dict)

        return render(request, self.template_name, {'apt_dict': apt_dict})


# 추후에 옮겨야함
class MainView(TemplateView):
    template_name = 'simulator/simulator.html'
