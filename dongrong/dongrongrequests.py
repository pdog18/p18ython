import json

from requests_html import HTMLSession

from config import headers
from prelist import prelist

session = HTMLSession()

regular1 = ''


def main():
    url = "http://47.98.48.109/site/prelist"

    # 返回一个 response 对象
    response = session.get(url=url, headers=headers)

    content = response.html.find("a.preCard")

    print(len(content))
    for element in content:
        data_id = element.attrs['data-id']

        prelist(data_id)


if __name__ == '__main__':
    main()
