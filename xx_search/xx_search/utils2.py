import requests
import time
import random
from bs4 import BeautifulSoup




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


baidu_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'Host': 'www.baidu.com',
        'Referer': 'https://www.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
baiducookies = {'BAIDUID': '8CDC812BAB231B0FFE749C948AA7B973:FG=1', 'PSTM': '1584262478', 'H_PS_PSSID':'30962_1431_21095_30995_30823_26350_30717',  'BIDUPSID': 'A28B3168D0FD604B003BF7B4AB8C236E', 'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598', 'BD_UPN':'12314753', 'delPer':'0', 'BD_CK_SAM':'1','COOKIE_SESSION':'59232_0_6_4_3_17_0_2_4_4_3_6_0_0_4_0_1584285670_0_1584344898%7C8%230_0_1584344898%7C1', 'H_PS_645EC':'cca4Bomr3KW3KrTSqaLruVvZ%2FHGZ7KgbafvUFmBYFNVn6dn2wOBEQoWjSj8'}

sogou_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
   
    'Host': 'www.sogou.com',
    'Referer': 'https://www.sogou.com/web?ie=UTF-8&query=so',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

bing_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

headers = {"User-Agent": random.choice(headersPool)}
cookies = random.choice(cookiesList)


def realurl(baidu_url):
    baidu_realurl = requests.get(baidu_url,headers=headers, cookies=baiducookies)
    # soup = BeautifulSoup(realurl.content,'lxml')
    # print(soup.text)
    return baidu_realurl.url

def sogou_real_url(url):
    try:
        get_real_url = requests.get(url, headers=headers, cookies=cookies)
        real_url_soup = BeautifulSoup(get_real_url.content ,'lxml')
        get_real_url.close()
        real_url_str = str(real_url_soup.text).split('"')
    except:
        pass
    return real_url_str[1]

def baidu(word):
    baidudict = {}
    
    r = requests.get('https://www.baidu.com/s?ie=UTF-8&wd=%s' %word, headers=headers, cookies=baiducookies)
    soup = BeautifulSoup(r.content ,'lxml')
    r.close()
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
                time.sleep(0.5)
    print('百度',baidudict)           
    return baidudict


def so(word):
    requests360 = requests.get('https://www.so.com/s?ie=utf-8&fr=so.com&src=home_so.com&q=%s' %word, cookies=cookies, headers=headers)
    soup360 = BeautifulSoup(requests360.content,'lxml')			
    requests360.close()
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




# word = 'python'
# # def bing(word):
# bingdict = {}
# r = requests.get('https://cn.bing.com/search?q=python',headers=bing_headers)
# soup = BeautifulSoup(r.content ,'lxml')
# print(soup)
# i = soup.find_all('a')
# print(i)
# for results in i.find_all('h2'):
#     print(results.text)
#     for result in results.find_all('a'):
#         print('ceshi')

# for title_url in result.find_all('li',class_ = 'b_algo'):
#     title = title_url.h2.text
    
#     description = title_url.p.text
#     url = title_url.a.get('href')
#     bingdict[url] = [description, title] 




#def sogou(word):
# word = 'python字典'
# sogoubidct = {}
# r = requests.get('https://www.sogou.com/web?query=%s' %word,headers = baidu_headers )
# soup = BeautifulSoup(r.content ,'lxml')
# # results = soup.find(class_ = 'results')
# # for result in soup.find_all(class_ = 'rb'):
# title_url = soup.find_all(class_ = 'results')
# print('\n')
# print(title_url)
# for i in title_url:
#     print(i)
#     url = i.a.get('href')
#     url = 'https://www.sogou.com' + url
#     url = sogou_real_url(url)
#     print(url)
# for description in soup.find_all(class_ = 'ft'):
#     print(description.text)

#     sogoubidct[url] = [description.text, title_url.a.text]

    #return sogoubidct

def search(word):
    word = word
    result_list = []
    result_dict = {}
    baidu1 = baidu(word)
    so1 = so(word)
    for d1 in baidu1.keys():
        for d2 in so1.keys():
            if d1 == d2:
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

#sogou('python字典')



# r = s.get('https://www.so.com/link?m=ahxmnnmZdqsXmKUs6%2BBa08V8F%2BuLy1C3Z%2BNWcRdo%2F3xu8KwR0Se7MJN5Ah30nev4dvQe3JBxg7NMdXHFFLvzdv%2FrHlVvQ1782W%2B%2FYHDygCPBzMxYca%2FK9XOIcWvY%2Bi3ZXx1uHME5vMghuVOnh5Pj4ax2HQM0UAxMfJkw5Aw%3D%3D')
# soup = BeautifulSoup(r.content ,'lxml')
# print(soup.text)

