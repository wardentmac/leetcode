# 给你一个仅包含小写英文字母和'?'字符的字符串s，请你将所有的'?'转换为若干小写字母使最终的字符串不包含任何连续重复的字符。


# 如果当前为问号，用a替换，替换时，如果不是第一位且等于前面的或者不是最后一位等于后面的，尝试用b替换，然后是c（三个字母就够了）
def modifyString(s: str) -> str:
    res = list(s)
    n = len(res)
    for i in range(n):
        if res[i] == "?":
            for extra in "abc":
                if not (i > 0 and res[i - 1] == extra or i < n - 1 and res[i + 1] == extra):
                    res[i] = extra
                    break
    return "".join(res)


print(modifyString("?ab?cd"))
