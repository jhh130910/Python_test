import re

string="abcdefg  acbdgef  abcdgfe  cadbgfe"

#带括号与不带括号的区别
#不带括号
regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
#输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

match
匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。

search
在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。

findall
在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。

finditer
在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

from __future__ import print_function
import re

content = '333STR1666STR299'
regex = r'([A-Z]+(\d))'

if __name__ == '__main__':
    print(re.match(regex, content)) ##content的开头不符合正则，所以结果为None。

    ##只会找一个匹配，match[0]是regex所代表的整个字符串，match[1]是第一个()中的内容，match[2]是第二对()中的内容。
    match = re.search(regex, content)
    print('\nre.search() return value: ' + str(type(match)))
    print(match.group(0), match.group(1), match.group(2))  

    result1 = re.findall(regex, content)
    print('\nre.findall() return value: ' + str(type(result1)))
    for m in result1:
        print(m[0], m[1])

    result2 = re.finditer(regex, content)
    print('\nre.finditer() return value: ' + str(type(result2)))
    for m in result2:
        print(m.group(0), m.group(1), m.group(2))  ##字符串
