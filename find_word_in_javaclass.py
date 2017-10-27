import os

write_file = 'out_file'


# 将文件中获取到的所有单词写入文件中
def write_words(word_dict):
    exists = os.path.exists('result')
    print(exists)

    if not exists:
        mkdir = os.mkdir('result')
        print(mkdir)
    out_file = 'result/{}'.format(write_file)
    with open(out_file, 'a') as f:
        for word, count in word_dict.items():
            f.write(word)
            f.write('\n')


# 找到一行中的单词，用list返回
def _find_continuity(line):
    result = []
    temp = ''
    for c in line:
        if c.isalpha():
            if c.isupper():
                if len(temp) == 0:  # 说明是一开始
                    temp += c
                elif len(temp) == 1:  # 说明是驼峰法的特殊变量等 :如 mAndroid
                    temp = ''
                else:  # 说明是一个驼峰变量
                    word = temp
                    result.append(word.lower())
                    temp = c
            else:
                temp += c
        else:
            if len(temp) < 2:
                temp = ''
                continue
            else:
                word = temp
                temp = ''
                result.append(word.lower())

    return result
    pass


def get_word(file):
    with open(file) as f:
        line = f.readline()

        word_dict = {}
        while line:
            continuity = _find_continuity(line)
            if len(continuity) < 1:
                line = f.readline()
                continue
            for word in continuity:
                count = word_dict.get(word, 0)
                word_dict[word] = count + 1

            line = f.readline()

        print(word_dict)
        print(len(word_dict))
        write_words(word_dict)
        pass
    pass


def main(path):
    store = os.listdir(path)

    for f in store:
        full_path = path + '/{}'.format(f)
        isfile = os.path.isfile(full_path)
        isdir = os.path.isdir(full_path)
        if isfile:
            get_word(full_path)
        elif isdir:
            temp_path = (path + '/{}').format(f)
            main(temp_path)
            pass
        else:
            print('什么也不是')

    print(store)


    # file = store
    # get_word(file)


if __name__ == '__main__':

    exists = os.path.isdir('store')

    if not exists:
        raise ('not find dir : store')

    main('store')
