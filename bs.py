# 用於實現GET, POST 功能
import requests
# 用於解析HTML
from bs4 import BeautifulSoup 
# 模擬瀏覽器運行
from selenium import webdriver

# 使用PhantomJS瀏覽器做模擬, PS:路徑可能需要修改到本地目錄
driver = webdriver.PhantomJS(executable_path='/Users/wayneliu/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('https://ecshweb.pchome.com.tw/search/v3.3/?q=ps4')
soup = BeautifulSoup(driver.page_source, 'html.parser')

for item in soup.select('.col3f'):
    print(item.select('.nick')[0].text)
    print(item.select('.value')[0].text)
    print('----------------------------')