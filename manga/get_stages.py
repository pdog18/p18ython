
from requests_html import HTMLSession

# 根据目录找到对应的回 共有多少页
from entity import Entity
from util import get_number

def stage_catch():
    session = HTMLSession()
    r = session.get('http://www.dmzx.com/manhua/358/')
    div = r.html.find('.subsrbelist')
    list_a = div[0].find('ul')[0].find('a')  # 找到对应目录列表
    entities = []

    for a in list_a:
        pages = get_number(a.text.split()[-1])
        stage = get_number(a.text.split()[-2])

        # print("pages = {} ".format(pages))

        # print("stage = {}".format(stage))
        url = a.attrs['href']
        # print(url)

        entity = Entity(pages, stage, url)

        entities.append(entity)

    # 写入文件
    # with open("./outputs/beans.json", "w") as f:
    #     f.write(json.dumps(entities))
    return entities
