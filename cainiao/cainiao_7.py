'''
7.有一串长的字符串 names="LI XIA  ,ZHAO MING  ,LAO WANG *,DA XIONG >,LI MEI MEI,CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG,DU GU QIU BAI,QIAO FENG"
要求：
1).过滤出所以的名字，去掉每个名字的左右的空格和乱码，每个名字的首字母大小
比如'LAO WANG *'，处理成'Lao Wang'
2).统计出所有名字里面名字最长
'''


names = 'LI XIA  ,ZHAO MING  ,LAO WANG *,DA XIONG >,LI MEI MEI,'\
        'CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG,'\
        'DU GU QIU BAI,QIAO FENG'

def problem7(names):
    
    names_dict = {name.title().strip(' >*'):len(name) for name in names.split(',')}
    print(sorted(names_dict.items(),key=lambda x:x[1],reverse=True))

problem7(names)


# lo = {name+'**':len(name)*2 for name in names.split(',')}
# print('lo: ',lo)