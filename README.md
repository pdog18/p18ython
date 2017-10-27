##文件说明



1. 分析一个`Java`文件，取出可能是单词的字符串，重新写入到另外一个文件中
2. 将另外一个文件中的所有字符串添加到扇贝单词本中




# 使用方法

1. clone

2. 在项目中创建config.py，设置以下参数

   * cookie
   * url 
   * id

   参数解释：

   cookie 就是你登录以后获得的cookie，

   url 就是扇贝提交单词的url 一般为 (https://www.shanbay.com/api/v1/wordlist/vocabulary/)

   id 就是你的单词本中的单元，每个单元可以添加200个单词，超过上限不能继续添加。

3. 将你需要分析的文件放入`store`文件夹中，修改`find_word_in_javaclass.py` `main`函数中的第一个参数为文件名

4. 运行`find_word_in_javaclass.py`会将分析后的字符串放入`result`文件夹中`out_file`文件

5. 运行`add_wordlist.py` 会上传单词到单词本中，为了防止过快请求被`ban`我设置了`300ms`的间隔



# todo

1. 分析一个文件夹内所有文件
2. 上传单词时如果达到200个的单元上限，自动创建新的单元继续上传
3. 不用设置cookie参数，自动获取cookie
4. 对上传失败的单词进行记录，存入黑名单中