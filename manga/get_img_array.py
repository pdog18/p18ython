from requests_html import HTMLSession

base_url = 'http://jpgcdn.dmzx.com/img/'


# 传入当前回主页，返回一个包含所有图片的list
def get_img_url_for_entity(index_url):
    session = HTMLSession()
    r = session.get(index_url)
    js_list = r.html.find('script')

    result = ((js_list[0].full_text).split('&#13')[-1])
    base_array = result.split('picAy')

    img_url_list = []

    for b in base_array:
        if '=' not in b:
            continue
        else:
            splited = b.split('=')

            img_url_list.append("{}{}".format(base_url, splited[1][1:-2]))  # 这里是图片的地址

    return img_url_list
