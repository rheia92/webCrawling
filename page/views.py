from django.shortcuts import render
import time
from konlpy.tag import Okt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your views here.

# urls.py 파일에 선언한
# url(r'search/tag/', views.search_view)
# 이 설정으로 인해 아래 함수가 호출된다.
# 이 함수는 맨 처음에 보여질 검색 화면을 띄우는 역할을 한다.
def search_view(request):
    return render(request, 'templates/page/search_tag.html', {})


# search_tag.html에서 검색한 태그를 받아와서 크롤링을 하는 함수.
# 크롤링이 끝나고 해시태그 데이터만을 추출하여 횟수를 저장하고, 그 데이터를 instagram_tag_list.html에 뿌려준다.
# 단, 총 게시물의 수와 태그의 수는 다를 수 있음.
# 1. 동영상 게시물의 경우 사진 게시물처럼 태그에 text가 함께 딸려오는 구조로 되어있지 않기 떄문에 동영상 태그는 수집할 수 없음
# 2. 속도 문제 때문에 받아오는 태그 수를 제한 할 수 밖에 없었음.
def instagram_tag_list(request):
    # 크롤링할 url 주소
    # url = "https://www.instagram.com/accounts/login/"
    url = "https://m.instagram.com/explore/tags/" + request.POST.get("searchTag") + "/"

    # 다운로드 받은 driver 주소
    driver_dir = '/Users/My/Desktop/chromedriver'
    # 크롬 드라이버를 이용해 임의로 크롬 브라우저를 실행시켜 조작한다.
    driver = webdriver.Chrome(driver_dir)
    # 암묵적으로 웹 자원을 (최대) 3초 기다리기
    driver.implicitly_wait(2)

    # 크롬 브라우저가 실행되며 해당 url로 이동한다.
    driver.get(url)

    # 총 게시물 수를 클래스 이름으로 찾기
    totalCount = driver.find_element_by_class_name('g47SY ').text
    totalCount = int(totalCount.replace(',', '').strip())

    print("총 게시물:", totalCount)
    # body 태그를 태그 이름으로 찾기
    elem = driver.find_element_by_tag_name("body")
    # alt 속성의 값을 담을 빈 리스트 선언
    alt_list = []

    # 페이지 스크롤을 위해 임시 변수 선언
    no_of_pagedowns = 1

    while no_of_pagedowns < 30:
        # 스크롤에 따라서 결과 값이 달라짐.
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)

        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1.5)

        # 브라우저에 보이는 모든 img 태그를 css 선택자 문법으로 찾는다.
        post_img = driver.find_elements_by_css_selector('div.eLAPa > div.KL4Bh > img')

        # 위에서 선언한 alt_list 리스트에 alt 속성의 값을 중복을 방지하며 할당한다.
        for i in post_img:
            if not i.get_attribute('alt') in alt_list:
                alt_list.append(i.get_attribute('alt'))

        no_of_pagedowns = no_of_pagedowns + 1

    # 키:해시태그, 값:횟수 형식으로 저장하기 위한 빈 딕셔너리 자료형 선언
    instagram_data = {}

    # alt 속성의 값인 제목과 해시태그 중 해시태그 만을 가져오기 위한 Okt 객체 생성
    okt = Okt()

    # alt_list에 담긴 값의 크기만큼 반복한다.
    for alt in alt_list:
        # pos 메서드를 통해 alt 속성의 모든 해시태그의 값을 (값, 품사) 형태의 튜플을 요소로 갖는 리스트로 반환한다.
        tag_info = okt.pos(alt, True)

        # 리스트의 크기만큼 반복한다.
        for data in tag_info:
            # 품사가 만약 해시태그이면
            if data[1] == "Hashtag":

                # 결과 값을 저장할 딕셔너리에 값이 있는지 체크
                # 없다면 새로운 키와 값 0을 추가,
                # 있다면 기존 키에 +1
                if data[0] in instagram_data:
                    instagram_data[data[0]] = instagram_data[data[0]] + 1
                else:
                    instagram_data[data[0]] = 1

    # 조회된 태그 카운트를 가지고 내림차순으로 정렬.
    keys = sorted(instagram_data.items(), key=lambda x: x[1], reverse=True)

    searched_tags = []

    for k, v in keys:
        tag_info = {}
        tag_info['tag'] = k
        tag_info['cnt'] = v

        searched_tags.append(tag_info)

    # 드라이버를 종료한다.
    driver.close()

    return render(request, 'templates/page/instagram_tag_list.html',
                  {'data': searched_tags, 'searchTag': request.POST.get("searchTag")})
