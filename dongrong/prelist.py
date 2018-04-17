import json

from requests_html import HTMLSession

from config import headers

session = HTMLSession()

'3KGycDMbJwHwUHSmagssYPLDG2mlvtUHPXB4Pphm'

def prelist(data_id):

    url = 'http://47.98.48.109/common/card/getDetailWithFill?cardInfoId=' + data_id + '&input_type=1'

    response = session.get(url=url, headers=headers)
    bean = json.loads(response.content)

    title = bean['data']['cardinfo']['title'][:7]          # 定价-013-
    code1 = bean['data']['tableCells']['2'][1]['content']  # 债权（户）编码
    code2 = bean['data']['tableCells']['4'][1]['content']  # 借款合同编码

    print()
    print('保证合同编码 = {}'.format(code2))
    result = title + str(code1) + "-" + str(code2)
    print(result)


