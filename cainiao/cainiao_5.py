"""

5.给定2个字符串s1,s2,判定s2能否给s1做循环移位得到字符串的包含。比如:
s1="AABBCD",s2="CDAA".要求2种解法


"""

s1="AABBCD"
s2="CDAA"

def problem(src_str,des_str):
    new_str = src_str + src_str
    if des_str in new_str:
        return True
    else:
        return False

print(problem(s1,s2))