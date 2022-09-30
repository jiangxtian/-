import requests
import re
import os

List = []


def funGetUrl():
    global List

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
        'cookie': '__51vcke__JNRQ5s5aa3aYLP3n=3181ebff-498e-5387-b8c4-08ef1aa95049; '
                  '__51vuft__JNRQ5s5aa3aYLP3n=1664526151082; cao_notice_cookie=1; __51uvsct__JNRQ5s5aa3aYLP3n=3; '
                  '__0d96285f334ce7a2b287aff21c13ebe8=1664540980; __vtins__JNRQ5s5aa3aYLP3n={"sid": '
                  '"8891412d-679c-5c58-8426-a0ff64744d30", "vd": 6, "stt": 1922324, "dr": 762395, "expires": '
                  '1664543303990, "ct": 1664541503990} '

    }
    url1 = 'https://www.xiurentu.net/85595.html'
    try:
        result = requests.get(url=url1, headers=headers1, timeout=7)

    except BaseException:
        print("error")
    else:
        # print(result.content.decode())
        Result = result.content.decode()
        pic_url = re.findall('src="(.*?)" alt', Result)

        if len(pic_url) == 0:
            print("没读到")
        else:

            List = list(filter(lambda x: len(x) < 100, pic_url))


def downloadpic():
    num = 1
    for each in List:
        print('正在下载第' + str(num) + '张图片，图片地址：' + str(each))
        try:
            if each is not None:

                picture = requests.get(url=each, timeout=7)
            else:
                continue
        except BaseException:
            print("当前图片无法下载")
            continue
        else:
            string = str(num) + '.jpg'
            with open(string, "wb") as f:
                f.write(picture.content)
                num += 1


if __name__ == '__main__':
    funGetUrl()
    print('经过检测图片共有%d张' % len(List))
    downloadpic()
