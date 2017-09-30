

def parse_xml(xml_dict):
    """
    도로명 주소를 활용해 아파트 정보들을 가져오는 공공 API를 활용한다.
    불완전한 딕셔너리 형태를 필요한 부분만 가공해 리턴한다.
    :param xml_dict: GET으로 받아온 xml파일에서 변환된 dict
    :return: 완전하게 가공된 아파트 정보
    """
    apt_dict = dict()
    apt_ = xml_dict['response']['body']['items']['item']

    print (apt_)

    if len(apt_) > 2:
        for apt in apt_:
            apt_dict.update({'kaptCode': apt['kaptCode']})
            apt_dict.update({'kaptName': apt['kaptName']})

    elif len(apt_) <= 2:
        apt_dict['kaptCode'] = apt_['kaptCode']
        apt_dict['kaptName'] = apt_['kaptName']

    print (apt_dict)

    return apt_dict