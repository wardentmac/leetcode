# 输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数


def hammingWeight(n: int) -> int:
    result = 0
    while n:
        result += n & 1
        n >>= 1
    return result


print(hammingWeight(0o0000000000000000000000000001011))
