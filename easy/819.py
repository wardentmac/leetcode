from typing import List
import re
# 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
# 题目保证至少有一个词不在禁用列表中，而且答案唯一。
# 禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母


# 将所有非字母用" "代替后转为小写字母，然后定义一个字典取每个词出现的次数，在ban里就赋值为-1
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()  # 去除段落里的标点符号
    paragraph = paragraph.split()
    dicts = {}
    for word in paragraph:
        if word not in dicts:
            dicts[word] = 1
        else:
            dicts[word] += 1
    for i in dicts:
        if i in banned:
            dicts[i] = -1
    return max(dicts, key=dicts.get)


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
