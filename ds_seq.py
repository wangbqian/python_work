shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或下标（Subscription）操作符 #
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Character 0 is',name[0])


# Slicing on a list # 
print('\nItem 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])


#从某一字符串中切片# 
print('\ncharacters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -2 is',name[1:-2])
print('characters start to end is',name[:])

print('Step is -2',shoplist[::-2])