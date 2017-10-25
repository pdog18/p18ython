
import requests
import time
import config

# config 里面写你自己的url 和 cookie
# url 一般是 https://www.shanbay.com/api/v1/wordlist/vocabulary/
url = config.url
cookie = config.cookie

def main():
    with open('out_file') as f:
        word = f.readline()
        while word:
            word = f.readline()
            replaced = word.replace('\n', '')
            print(replaced)
            time.sleep(2)
            add_wordlist(word)
    pass

def add_wordlist(word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 '
                      'Safari/537.36',
        'Cookie': cookie
    }

    print(headers)

    data = {
        'id': 585211,
        'word': word
    }
    r = requests.post(url, headers=headers, data=data)
    print(r.content)
    pass
    pass



if __name__ == '__main__':
    main()
