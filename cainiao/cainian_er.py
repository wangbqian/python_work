'''
题目：mini文件搜索工具
每个人电脑上都安装了Python无论是py2.7还是py3.6,假如你的是py2.7:
搜索整个py2.7下面的所有目录(包括子目录)，里面的所有文件:
1.统计出整个py2.7目录下一共有多少个文件夹和文件
2.找到文件大小最大的哪个文件
3.找到文件名最长的哪个文件
'''

from __future__ import division
import os

path='/Users/fuyiweng/Desktop/hero'

def search_file(path):
    folders = []
    files_info = []
    if not os.path.exists(path):
        print('Path : {} not exists!'.format(path))
        return None

    for root,dirs,files in os.walk(path):
        folders.extend(dirs)
        for f in files:
            #得到文件全路径，需要使用os.path.join(dirpath, name).
            f_path=os.path.join(root,f)
            #得到文件大小
            f_size=round(os.path.getsize(f_path),3)
            files_info.append((f,f_size,f_path))

    display(folders,files_info)


def display(folders,files_info):
    print('folders: ',folders)
    print('files_info ',files_info)
    longest_file=sorted(files_info,key=lambda x:len(x[0]),reverse=True)[0][0]
    largest_file=sorted(files_info,key=lambda x:x[1],reverse=True)[0][2]
    largest_file_size=sorted(files_info,key=lambda x:(x[1]),reverse=True)[0][1]


    
    print('Total folders:{},Total files:{}'.\
        format(len(folders),len(files_info)))

    print('Longest file name:{},len:{}'.\
        format(longest_file,len(longest_file)))

    print('Largest file name:{} : size:{}'.\
        format(largest_file,str(round(largest_file_size/1024/1024))+'M'))

    print('Total size:{}'.format(sum([item[1] for item in files_info])))

search_file(path)