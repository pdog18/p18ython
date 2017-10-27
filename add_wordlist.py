import requests
import time
import config

# config 里面写你自己的url 和 cookie
# url 一般是 https://www.shanbay.com/api/v1/wordlist/vocabulary/
url = config.url
cookie = config.cookie
id = config.id

def main():
    with open('result/out_file') as f:
        word = f.readline()
        while word:
            replaced = word.replace('\n', '')
            print(replaced)
            time.sleep(0.3)
            add_wordlist(id,replaced)
            word = f.readline()
pass


def add_wordlist(id,word):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,ko;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.shanbay.com',
        'Origin': 'https://www.shanbay.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie
    }

    data = 'id={}&word={}'.format(id,word)
    r = requests.post(url, headers=headers, data=data)

    print(r.content)



if __name__ == '__main__':
    main()
