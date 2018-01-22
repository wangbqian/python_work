"""
6.给定一个字符串,寻找没有字符串重复的最长子字符串.
比如:"abcabcbb" 找到的是"abc",长度为3，比如"bbbbb"找到的是"b",长度为1


"""
s = 'abcabwbbd'


# def problem(s):
#     getlist = []
#     s_list = list(s)
#     for i in range(len(s_list)):
#         if s_list[i] in getlist:
#             return getlist,i
#         else:
#             getlist.append(s_list[i])

# new_list,num = problem(s)
# print(''.join(new_list),num)




def max_unique_str(s1):
    for i in range(len(s1)):
        contain = []
        contain.append(s1[i])
        for j in range(i+1,len(s1)):
            if s1[j] in contain:
                yield contain
                break
            else:
                contain.append(s1[j])

print(sorted([''.join(x) for x in max_unique_str(s)],key=lambda x:len(x),reverse=True)[0])