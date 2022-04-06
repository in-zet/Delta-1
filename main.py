# 0401
# hanumoka.net/2020/07/05/python-20200705-python-selenium-install-start/
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/#%EC%9A%94%EC%86%8C-%EC%B0%BE%EA%B8%B0locating-elements
# https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/
# selenium, webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(3)
driver.get('https://namu.wiki/w/%ED%81%AC%EB%A6%BC%EB%B9%B5')
searching = driver.find_elements_by_class_name('wiki-paragraph')
for i in range(len(searching)):
    print(searching[i].text)
