# 给你一个下标从0开始的字符串和一个字符，找出字符第一次出现的下标i，反转字符串中从下标0开始、直到下标i结束（含下标i）的那段字符。
# 如果字符串中不存在字符，则无需进行任何操作。


# 根据ch切片成一个列表，首个值加ch反转，其他组加ch加上去，最后一组加上去
def reversePrefix_1(word: str, ch: str) -> str:
    if ch not in word:
        return word
    else:
        i = ""
        j = ""
        word_list = word.split(ch)
        for index in range(len(word_list)):
            if index == 0:
                i = word_list[index] + ch
            elif index == len(word_list) - 1:
                j += word_list[index]
            else:
                j += word_list[index] + ch
        return "".join(reversed(i)) + j


# 冒号的用法
def reversePrefix(word: str, ch: str) -> str:
    index = word.find(ch)
    if index == -1:
        return word
    else:
        return word[index::-1] + word[index+1:]


print(reversePrefix("xyxzxe", "z"))
