import requests
import xmltodict
import greenworld.settings as setting

from django.views.generic import View
from django.shortcuts import render


# Create your views here.
class AptInfoView(View):
    """
    Cross-origin 문제로 인해서 프론트단에서 API를 호출하기 힘들다.
    서버단으로 옮겨서 처리
    """

    template_name = 'aptinfo/apt_info.html'

    def get(self, request, *args, **kwargs):

        if 'kapt_code' in request.GET:
            kapt_code = request.GET['kapt_code']
        else:
            return render(request, self.template_name, {'response': '아파트 코드를 찾지못했습니다.'})

        res = self.get_apt_info_by_kapt_code(kapt_code)
        apt_dict = xmltodict.parse(res.text)
        apt = apt_dict['response']['body']['item']

        apt_pack = {
            'name': apt['kaptName'],
            'addr': apt['kaptAddr'],
            'hall': apt['codeHallNm'],
            'heat': apt['codeHeatNm'],
            'ho_cnt': apt['hoCnt'],
            'company': apt['kaptBcompany'],
            'dong_cnt': apt['kaptDongCnt'],
            'fax': apt['kaptFax'],
            'tel': apt['kaptTel'],
            'area': apt['kaptTarea'],
            'date': apt['kaptUsedate'],
            'area_60': apt['kaptMparea_60'],
            'area_85': apt['kaptMparea_85'],
            'area_135': apt['kaptMparea_135'],
            'area_136': apt['kaptdaSize_136']

        }
        print(apt_pack)

        return render(request, self.template_name, {'apt_pack': apt_pack})

    def post(self, request, *args, **kwargs):

        if 'road_code' in request.POST:
            road_code = request.POST['road_code']
        else:
            return render(request, self.template_name, {'response': '도로명 코드를 찾지못했습니다.'})

        res = self.get_apt_list_by_road_code(road_code)

        apt_dict = self.parse_apt_list(xmltodict.parse(res.text))

        print(apt_dict)

        return render(request, self.template_name, {'apt_dict': apt_dict})

    def get_apt_list_by_road_code(self, road_code):

        # TODO : 추후 settings.py 로 옮기기

        SITE = 'http://apis.data.go.kr'
        PAGE = 'pageNo=1&startPage=1&numOfRows=10&pageSize=10'
        KEY = 'qmtrltW6G7zoOxVeLWJJ%2FE%2BYEnmZeicm4b8mQQmJPnS1ZKDpg1dg1xLMIiKfzleMVxHD%2F9%2FvECvVBINhw2QcEw%3D%3D'

        api_url = f'{SITE}/1611000/AptListService/getRoadnameAptList?serviceKey={KEY}&loadCode={road_code}&{PAGE}'

        res = requests.get(api_url)

        return res

    def get_apt_info_by_kapt_code(self, kapt_code):

        SITE = 'http://apis.data.go.kr'
        KEY = 'qmtrltW6G7zoOxVeLWJJ%2FE%2BYEnmZeicm4b8mQQmJPnS1ZKDpg1dg1xLMIiKfzleMVxHD%2F9%2FvECvVBINhw2QcEw%3D%3D'

        api_url = f'{SITE}/1611000/AptBasisInfoService/getAphusBassInfo?serviceKey={KEY}&kaptCode={kapt_code}'

        res = requests.get(api_url)

        return res

    def parse_apt_list(self, xml_dict):
        """
        도로명 주소를 활용해 아파트 정보들을 가져오는 공공 API를 활용한다.
        불완전한 딕셔너리 형태를 필요한 부분만 가공해 리턴한다.
        :param xml_dict: GET으로 받아온 xml파일에서 변환된 dict
        :return: 완전하게 가공된 아파트 정보
        """
        apt_dict = dict()
        apt_ = xml_dict['response']['body']['items']['item']

        print(apt_)

        if len(apt_) > 2:
            for apt in apt_:
                apt_dict.update({'kaptCode': apt['kaptCode']})
                apt_dict.update({'kaptName': apt['kaptName']})

        elif len(apt_) <= 2:
            apt_dict['kaptCode'] = apt_['kaptCode']
            apt_dict['kaptName'] = apt_['kaptName']

        print(apt_dict)

        return apt_dict
