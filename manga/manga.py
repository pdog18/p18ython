from download_img import download_image
from get_img_array import get_img_url_for_entity
from get_stages import stage_catch
from util import get_number


# todo 剧场版的被排除了
def over(entity):
    return int(get_number(entity.stage)) > 340


if __name__ == '__main__':

    # 根据目录获取所有回合，及每个回合有的椰树
    entities = stage_catch()

    # 这里过滤了一下 只下载了340话以上的。
    results = list(filter(over, entities))

    # 遍历集合找出，每个回合对应的所有图片的集合
    for entity in results:
        img_urls = get_img_url_for_entity(entity.url)

        # 遍历图片集合，下载并保存到文件夹中。
        for img in img_urls:
            download_image(entity.stage, img)

