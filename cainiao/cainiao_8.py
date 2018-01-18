'''
8.数字1到5可以被写成:one,two,three,four,five,因此这些字母的总长度为:
3+3+5+4+4=19,现在求序列1到1000(包括1000),这些数字写成单词，总长度为多少？
注意:
    比如 342(three hundred and forty-two)为23字母,空格和-不计算
    比如 115(one hundred and fifteen)为20个字母
    比如 1000(one hundred)为11个字母    
'''

mapping={1:'one',2:'two',3:'three',4:'four',5:'five',
         6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
         11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
         16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
         30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
         80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}


def less_than_twenty(n):
    if n <= 20 and n >0:
        return mapping[n]

def less_than_hundred(n):
    if n > 20 and n < 100:
        a,b = int(n/10),n%10

        return mapping[a*10] if b == 0 else mapping[a*10]+mapping[b]


def less_than_thousand(n):
    words=[]
    if n >= 100 and n <1000:
        a,b = int(n/100),n%100
        words.append(mapping[a])
        words.append(mapping[100])
        if b>0 and b<=20:
            words.append('and')
            words.append(less_than_twenty(b))
        if b>20:
            words.append('and')
            words.append(less_than_hundred(b))
    return ''.join(words)

def get_words(n):
    if n>0 and n<=20:
        return less_than_twenty(n)
    elif n<100:
        return less_than_hundred(n)
    elif n>=100 and n<1000:
        return less_than_thousand(n)
    elif n == 1000:
        return 'onethousand'

res = map(get_words,[x for x in range(1,1001)])

print(sum(map(len,res)))
