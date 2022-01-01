# 一个单词列表s，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）
# 给你一个s和一个整数k ，请你将s截断 ，使截断后的句子仅含前k个单词。返回截断s后得到的句子

# 依空格对str切片，依次插入str和空格，判断如果是最后一位，则只插入str不插入空格
def truncateSentence_1(s: str, k: int) -> str:
    result = ""
    num = 0
    for word in s.split():
        result += word
        num += 1
        if num == k:
            break
        else:
            result += " "
    return result


# python自带函数
def truncateSentence_2(s: str, k: int) -> str:
    return " ".join(s.split()[0:k])


# print(truncateSentence("hello warden wang", 2))
