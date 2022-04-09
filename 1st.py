# 0401
# http://114.205.105.8/prime/list.php
# hanumoka.net/2020/07/05/python-20200705-python-selenium-install-start/
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/#%EC%9A%94%EC%86%8C-%EC%B0%BE%EA%B8%B0locating-elements
# https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/
# https://liveyourit.tistory.com/38
# https://jgpark.kr/766
# 추가:
# 중복시 페이지 잔류 // 비중복시 전페이지
# ==> 페이지 주소 대조하여 중복/비중복 경우 나누기
# 10000까지 실행
# selenium, webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'http://114.205.105.8/prime/add_form.php'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(3)
driver.get(url)
dict1 = {}
lim = 0

# 계산부
texta = ""
dict_e = {}
a = []
num = 2
i = 2
while num <= 50:
    number = num
    while i <= num:
        if num % i == 0:
            a.append(i)
            num = num / i
        else:
            i += 1
    dict_e[int(number)] = list(a)
    num = number + 1
    a = []
    i = 2

# 구동부
for i in range(len(dict_e)):
    prime = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input').send_keys(int(i + 2))
    for j in range(len(dict_e[i + 2])):
        texta += str(dict_e[i + 2][j])
        texta += " "
    texta = texta[0:-1]
    friction = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/textarea').send_keys(texta)
    clicking = driver.find_element_by_xpath('/html/body/form/input').click()
    alert_ok = driver.switch_to.alert
    alert_ok.accept()
    clicking = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/input').click()
    texta = ""

