#coding=utf-8
import requests
import re
import os
import json

url = 'https://pvp.qq.com/web201605/js/herolist.json'
html = requests.get(url)
html_json = html.json(encoding='utf-8')



hero_name = list(map(lambda x: x['cname'], html_json))
hero_number = list(map(lambda x :x ['ename'],html_json))

def main():
    ii =0
    for v in hero_number:
        os.mkdir("/Users/fuyiweng/Desktop/hero"+hero_name[ii].encode("gbk"))
        os.chdir("/Users/fuyiweng/Desktop/hero"+hreo_name[ii].encode("gbk"))

        ii += 1
        for u in range(12):
            onehero_links = "https://game.gting.cn/images/yxzj/img201606/skin/hero-info/" \
                + str(v) + "/" + str(v) +"-bigskin-" + str(u) + ".jpg"
            image = requests.get(onehero_links)
            if image.status_code == 200:
                iv = re.split("-",onehero_links)
                open(iv[-1],'wb').write(image.content)


main()