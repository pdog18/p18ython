import os
import requests
from PIL import Image
from io import BytesIO


# 这个方法是 用来下载图片的
# stage 是第几回
# save_path 是保存的路径
def download_image(stage, save_path='./outputs'):
    #todo 根据stage 获得 当前回总共有几页
    pages = 20
    print("start download pages is : {} , save_path is :{}".format(pages, save_path))

    #todo 更具stage 获得当前回的baseurl
    base_url = 'http://jpgcdn.dmzx.com/img/00%2F58%2F358%2F2000016781%2F{}.jpg'
    for i in range(1, pages):
        page = str(i).zfill(4)

        url = base_url.format(page)

        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        target_dir = '{}/_{}'.format(save_path, stage)
        if not os.path.exists(target_dir):
            print('create dir, name is {}'.format(target_dir))
            os.makedirs(target_dir)

        image.save(os.path.join(target_dir, '{}.jpg'.format(page)))
        print("{} save success".format(page))

    print("end")
    pass


if __name__ == '__main__':
    download_image(341)
