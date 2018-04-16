import requests
import os

from PIL import Image
from io import BytesIO


# 这个方法是 用来下载图片的
# stage 是第几回
# save_path 是保存的路径
def download_image(stage, img_url, save_path='./outputs'):
    print("start download")

    response = requests.get(img_url)

    image = Image.open(BytesIO(response.content))

    target_dir = '{}/_{}'.format(save_path, stage)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    image.save(os.path.join(target_dir, '{}'.format(img_url[-7:])))
    print("save success")

    pass
