from requests_html import HTMLSession

from config import headers

session = HTMLSession()


def get_detail():
    url = "http://47.98.48.109/common/card/getDetailWithFill"
    params = {
        'cardInfoId': 'e7a2d4484045488a8162e2464cf193da',
        'input_type': '1',
    }
    # 返回一个 response 对象
    response = session.get(url=url, headers=headers, params=params)

    print(response.text)
    pass


if __name__ == '__main__':
    get_detail()
    pass
