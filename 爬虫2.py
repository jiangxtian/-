import requests
import re

requests.packages.urllib3.disable_warnings()

headers = {
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
proxies = {"HTTPS": "HTTP://182.101.207.11:443"}


def fun1():
    picture = requests.get(url='https://950i.dpjhnp.com/task/uploadfile/202209/28/94161326159.jpg', headers=headers,
                           timeout=5)
    print(picture.status_code)

    if picture.status_code == 200:

        #print(picture.content)
        with open('6.jpg', "wb") as f:
            f.write(picture.content)
    else:
        print(picture.content.decode())
        print(type(picture.content))
        with open('5.jpg', "wb") as p:
            p.write(picture.content)


if __name__ == '__main__':
    fun1()
