import time

import requests
import re
import os

requests.packages.urllib3.disable_warnings()

List = []
pic_url = []
string = ''
title = []
proxies = {"HTTPS": "HTTP://47.112.117.132:80"}
num = 1
tuji = 83819
z = 'https://www.xiurentu.net/'
# z = 'https://www.xiurentu.net/85595.html'
headers1 = {
    'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, '
              'image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh - CN, zh;q = 0.9, en - GB;q = 0.8, en;q = 0.7',
    'cache-control': 'no - cache',
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                  '105.0.0.0Safari / 537.36 ',
    'dnt': '1',
    'pragma': 'no - cache',
    'sec-ch-ua': '"Google Chrome";v = "105", "Not)A;Brand";v = "8", "Chromium";v = "105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'cookie': '__0d96285f334ce7a2b287aff21c13ebe8=1664608642; '
              '__51vcke__JNRQ5s5aa3aYLP3n=3181ebff-498e-5387-b8c4-08ef1aa95049; '
              '__51vuft__JNRQ5s5aa3aYLP3n=1664526151082; __51uvsct__JNRQ5s5aa3aYLP3n=5; cao_notice_cookie=1; '
              '__vtins__JNRQ5s5aa3aYLP3n={"sid": "525aaf19-b2af-5df0-a188-8f54498bc93c", "vd": 2, "stt": 10952, '
              '"dr": 10952, "expires": 1664615116022, "ct": 1664613316022} '

}
headers2 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh - CN, zh;q = 0.9, en - GB;q = 0.8, en;q = 0.7',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; HarmonyOS; EBG-AN00; HMSCore 6.7.0.322) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.303 Mobile Safari/537.36',

    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "HuaweiBrowser";v="92"',
    'sec-ch-ua-mobile': '?1',
    'sec-fetch-user': '?1',
    'pragma': 'no - cache',
    'dnt': '1',
    'referer':'https://www.xiurentu.net/',
    'sec-ch-ua-platform': '"Windows"',

}


def funGetUrl(url_zl):
    global List
    global title
    global pic_url
    global headers1
    global proxies

    url1 = url_zl
    print(url1)
    try:
        result = requests.get(url=url1, headers=headers1, timeout=7)


    except BaseException:
        print("error")
    else:
        # print(result.content.decode())
        Result = result.content.decode()
        # print(Result)
        pic_url = re.findall('src="(.*?)" alt', Result)
        title = re.findall('<title>(.*?)</title>', Result)

        if len(pic_url) == 0:
            print("没读到")
        else:

            List = list(filter(lambda x: len(x) < 100, pic_url))


def downloadpic():
    global num
    global title
    global string
    global headers1
    global proxies
    t = title[0]

    for each in List:

        print('正在下载第' + str(num) + '张图片，图片地址：' + str(each))
        try:
            if each is not None:

                picture = requests.get(url=each, headers=headers2, timeout=5)
                time.sleep(2)
                picture.close()
            else:
                continue
        except BaseException:
            print("当前图片无法下载")
            continue
        else:
            string = str(num) + '.jpg'
            path = 'D:\\TEST\\爬虫图片\\' + t
            y = os.path.exists(path)
            if y == 1:
                print("目录已存在")
            else:
                if picture.status_code == 200:
                    os.makedirs(path)
            if picture.status_code == 200:
                with open(path + '\\' + string, "wb") as f:
                    f.write(picture.content)
                num += 1
                print("下载成功！！")
            else:
                print(picture.status_code)


if __name__ == '__main__':
    # proxies = {"http": "http://116.117.134.135:80"}
    for i in range(1, 20):
        url_z = z + str(tuji) + '.html/' + str(i)
        # url_z = z + str(i) + '.html'
        funGetUrl(url_z)
        print('经过检测图片共有%d张' % len(List))
        downloadpic()
        time.sleep(3)
        num = 1
