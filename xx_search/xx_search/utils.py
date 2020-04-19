from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import requests
import random

cookiesList = [{'QiHooGUID': '4B8401DA0CF874A18E4BFF757EB90AE1.1559194913641','__guid': '15484592.1937232903330800000.1559194915338.2622','HSPK': 'e233796b2ddb62b46b356063af241c0.1559194953.1'},
               {'QiHooGUID': '0EFD4F5BD0052491974CAED4F706DF45.1559179861562','__guid': '15484592.814590072574967200.1559179861246.2769','HSPK': '160ff6e1afae22e60d0321036f692f9.1559179998.1'},
               {'QiHooGUID': '117C9371BC637FDC5C410F7B05C04CBD.1559179860932','__guid': '15484592.1180757161332586200.1559179861157.9478','HSPK': '96db7fb23d1c854555fba80e4c827bc.1559180056.1'},
			   {'QiHooGUID': '397CF97029E2031C7FE185F323BC4591.1559179862317','__guid': '15484592.4234635624280693000.1559179861608.329','HSPK': '788f84234c87aff1807a434c968aa67.1559180114.1'},
			   {'QiHooGUID': '7677BC494C9AEB59BF338C34BE065908.1559179860461','__guid': '15484592.772992706594705000.1559179860839.9106','HSPK': '054120f3987b7a26dff500e099e238a.1559180167.1'}
]
 
headersPool = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
	"Opera/9.27 (Windows NT 5.2; U; zh-cn)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
]

headers = {"User-Agent": random.choice(headersPool)}
cookies = random.choice(cookiesList)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()

def realurl(baidu_url):
    try:
        baidu_realurl = requests.get(baidu_url,headers=headers, cookies=cookies)
    except:
        return baidu_url
    return baidu_realurl.url

def baidu(word):
    baidudict = {}
    driver.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s' %word)
    soup = BeautifulSoup(driver.page_source ,'lxml')
    for result in soup.find_all(class_ = 'result c-container'):
        for description in result.find_all(class_ = 'c-abstract'):
            description = description.text
        for h3 in result.find_all(name='h3'):
            h3_next = h3.find_all(name='a')
            for link in h3_next:
                title = link.text
                url = link.get('href')
                # print('\n')
                # print(a,title)
                # print(url)
                # print(description)
                # url1 = realurl(url)
                baidudict[title] = [description, url]
    print('百度',baidudict)           
    return baidudict


def so(word):
    driver.get('https://www.so.com/s?ie=utf-8&fr=so.com&src=home_so.com&q=%s' %word)
    # print(driver.page_source)
    soup360 = BeautifulSoup(driver.page_source,'lxml')			
    dict_360 = {}
    #print('360soup',soup360.text)
    for i in soup360.find_all('h3'):
        for j in i.find_all('a'):
            if j.text != '反馈' and j.text != '换一换' and j.text != '想在360搜索推广您的产品服务吗？':
                title = j.text
                url2 = j.get('href')
                if url2 != 'javascript:;':
                    # url3 = sogou_real_url(url2)
                    dict_360[title] = url2 
            else:
                break
    print('360', dict_360)
    return dict_360


def search(word):
    word = word
    result_list = []
    result_dict = {}
    baidu1 = baidu(word)
    so1 = so(word)
    for d1 in baidu1.keys():
        baidu_key_format = re.sub("[^a-zA-Z0-9\u4e00-\u9fa5]", '', d1)
        print('百度=> ' + baidu_key_format)
        for d2 in so1.keys():
            so360_key_format = re.sub("[^a-zA-Z0-9\u4e00-\u9fa5]", '', d2)
            print('360=> ' + so360_key_format)
            if baidu_key_format == so360_key_format:
                # print('找到一个')
                result_list.append(d1)
                # d1 是标题
    for result in result_list:
            url = baidu1[result][1]
            description = baidu1[result][0]
            title = result

            # 这里处理真实链接
            url1 = realurl(url)

            result_dict['url'] = url1
            result_dict['description'] = description
            result_dict['title'] = title
    print('结果', result_dict)
    return result_dict

