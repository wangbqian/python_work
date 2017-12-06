from functools import reduce
def  str2float(s):
    ind = s.index('.')
    l1 = int(s[0:ind])
    l2 = s[-1:ind-1:-1]

    # print(l2+'fanli')
    def char2num(s2):
        return {'.': 0,'0': 0.0, '1': 1.0, '2': 2.0, '3': 3.0, '4': 4.0, '5': 5.0, '6': 6.0, '7': 7.0, '8': 8.0, '9': 9.0}[s2]

    # def positive(x,y):
    #     return x*10+y
    def negative(x,y):
        return x/10+y

    return l1+reduce(negative,map(char2num,l2))
print("str2float(\'123.456\') =", str2float('123.456'))
