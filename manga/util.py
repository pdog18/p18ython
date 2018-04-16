import re

#如果不是数字则返回0
def get_number(text):
    result = re.sub("\D", "", text)
    if result.isdigit():
        return result
    else:
        return '0'
