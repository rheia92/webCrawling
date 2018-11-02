# driver.get(url)
#
# element_id = driver.find_element_by_name("username")
# element_id.send_keys("ssomini92")
# element_password = driver.find_element_by_name("password")
# element_password.send_keys("f45rn9500$")
#
# password = 0  # RESET Password
#
# driver.find_element_by_tag_name('button').click()
# driver.implicitly_wait(5)

# url = "https://m.instagram.com/explore/tags/마켓컬리/"



def post_list(request):

    # 크롤링할 url 주소
    url = "https://www.instagram.com/explore/tags/20180813/"
    # 다운로드 받은 driver 주소
    DRIVER_DIR = '/Users/parksomin/Desktop/chromedriver'
    # 크롬 드라이버를 이용해 임의로 크롬 브라우저를 실행시켜 조작한다.
    driver = webdriver.Chrome(DRIVER_DIR)
    # 암묵적으로 웹 자원을 (최대) 5초 기다리기DRIVER_DIR)
    driver.implicitly_wait(5)
    # 크롬 브라우저가 실행되며 해당 url로 이동한다.
    driver.get(url)
    # 총 게시물 수를 클래스 이름으로 찾기
    totalCount = driver.find_element_by_class_name('g47SY').text
    totalCount = int(totalCount.replace(',', '').strip())
    print("총 게시물:", totalCount)
    # body 태그를 태그 이름으로 찾기
    elem = driver.find_element_by_tag_name("body")
    # alt 속성의 값을 담을 빈 리스트 선언
    alt_list = []



    # 페이지 스크롤을 위해 임시 변수 선언
    pagedowns = 1
    # 스크롤을 20번 진행한다.
    while pagedowns < totalCount/6:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다.
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)
        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)

        # 브라우저에 보이는 모든 img 태그를 css 선택자 문법으로 찾는다.
        img = driver.find_elements_by_css_selector('div.KL4Bh > img')
        # 위에서 선언한 alt_list 리스트에 alt 속성의 값을 중복을 방지하며 할당한다.
        for i in img:
            if not i.get_attribute('alt') in alt_list:
                alt_list.append(i.get_attribute('alt'))
        pagedowns += 1

    # 키:해시태그, 값:횟수 형식으로 저장하기 위한 빈 딕셔너리 선언
    dict_data = {}
    # alt 속성의 값인 제목과 해시태그 중 해시태그 만을 가져오기 위한 Tiwitter 객체 생성
    tw = Okt()
    tempList = []
    # alt_list에 담긴 값의 크기만큼 반복한다.
    for alt in alt_list:
        # pos 메서드를 통해 alt 속성의 모든 해시태그의 값을 (값, 품사) 형태의 튜플을 요소로 갖는 리스트로 반환한다.
        temp = tw.pos(alt, True)
        tempList.append(temp)
        # 리스트의 크기만큼 반복한다.
        for data in temp:
            # 품사가 만약 해시태그이면
            if data[1] == "Hashtag":
                # 결과 값을 저장할 딕셔너리에 값이 있는지 확인하고 없다면 새로이 키를 추가하고 0, 있다면 기존 키에 1을 더해준다.
                if not (data[0] in dict_data):
                    dict_data[data[0]] = 0
                dict_data[data[0]] += 1



    # 딕셔너리를 횟수를 가지고 내림차순으로 정렬한다.
    keys = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)

    # 1~15위 까지의 키:값을 출력한다.
    for k, v in keys[:15]:
        print("{}({})".format(k, v))

    tagInfo = []
    index = 0;
    for k, v in keys:
        temp = {}
        temp['tag'] = k
        temp['cnt'] = v
        tagInfo.append(temp)

    print(tagInfo)

    # 드라이버를 종료한다.
    driver.close()

    return render(request, 'templates/page/post_list.html', {'data':tagInfo})


def instagram_tag_list1(request):

    # 크롤링할 url 주소

    #url = "https://www.instagram.com/accounts/login/"
    url = "https://m.instagram.com/explore/tags/myyouthpsm/"
    # 다운로드 받은 driver 주소
    DRIVER_DIR = '/Users/parksomin/Desktop/chromedriver'
    # 크롬 드라이버를 이용해 임의로 크롬 브라우저를 실행시켜 조작한다.
    driver = webdriver.Chrome(DRIVER_DIR)
    # 암묵적으로 웹 자원을 (최대) 5초 기다리기DRIVER_DIR)
    driver.implicitly_wait(5)
    # 크롬 브라우저가 실행되며 해당 url로 이동한다.
    #driver.get(url)
    #
    # element_id = driver.find_element_by_name("username")
    # element_id.send_keys("ssomini92")
    # element_password = driver.find_element_by_name("password")
    # element_password.send_keys("f45rn9500$")
    #
    # password = 0  # RESET Password
    #
    # driver.find_element_by_tag_name('button').click()
    # driver.implicitly_wait(5)

    url = "https://m.instagram.com/explore/tags/에피톤프로젝트_선인장/"
    driver.get(url)
    driver.implicitly_wait(10)

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

    img = []
    # 스크롤을 20번 진행한다.
    while no_of_pagedowns < totalCount/6:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다.
        # 기본적으로 브라우저 조작을 통해 값을 얻어올 때는 실제 브라우저에 보이는 부분이어야 요소를 찾거나 특정 이벤트를 발생시킬 수 있다.
        elem.send_keys(Keys.PAGE_DOWN)

        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)

        # 브라우저에 보이는 모든 img 태그를 css 선택자 문법으로 찾는다.
        img = driver.find_elements_by_css_selector('div.KL4Bh > img')

        # 위에서 선언한 alt_list 리스트에 alt 속성의 값을 중복을 방지하며 할당한다.
        for i in img:
            if not i.get_attribute('alt') in alt_list:
                alt_list.append(i.get_attribute('alt'))

        no_of_pagedowns+=1

    # 키:해시태그, 값:횟수 형식으로 저장하기 위한 빈 딕셔너리 선언
    dict_data = {}
    # alt 속성의 값인 제목과 해시태그 중 해시태그 만을 가져오기 위한 Tiwitter 객체 생성
    okt = Okt()
    idx = 0
    tempList = []
    # alt_list에 담긴 값의 크기만큼 반복한다.
    for alt in alt_list:
        # pos 메서드를 통해 alt 속성의 모든 해시태그의 값을 (값, 품사) 형태의 튜플을 요소로 갖는 리스트로 반환한다.
        temp = okt.pos(alt, True)

        # 리스트의 크기만큼 반복한다.
        for data in temp:
            # 품사가 만약 해시태그이면
            if data[1] == "Hashtag":
                print(data[0])
                # 결과 값을 저장할 딕셔너리에 값이 있는지 확인하고 없다면 새로이 키를 추가하고 0, 있다면 기존 키에 1을 더해준다.
                if data[0] in dict_data:
                    dict_data[data[0]] = dict_data[data[0]] + 1
                else:
                    dict_data[data[0]] = 1


    # 딕셔너리를 횟수를 가지고 내림차순으로 정렬한다.
    keys = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)
    print(idx)
    # 1~15위 까지의 키:값을 출력한다.
    # for k, v in keys[:15]:
    #     print("{}({})".format(k, v))

    tagInfo = []

    for k, v in keys:
        temp = {}
        temp['tag'] = k
        temp['cnt'] = v
        tagInfo.append(temp)

    # 드라이버를 종료한다.
    #driver.close()
    return render(request, 'templates/page/post_list.html', {'data':tagInfo})

