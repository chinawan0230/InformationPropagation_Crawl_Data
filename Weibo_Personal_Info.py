# -*- coding: utf-8 -*-
# 根据weibo_Uid表中数据爬取微博用户关注数、粉丝数、微博总数用以分析用户的个人影响力以及该用户的最近200条微博信息，用以分析用户的兴趣特征
# 微博用户id: 1496814565，1866614673，2544035510

import urllib.request
import json
import csv
import os
import xlwt

# 定义要爬取的微博大V的微博ID
from xlwt import Workbook

id = '1866614673'

# 设置代理IP
proxy_addr = "122.241.72.191:808"

# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    print(proxy)
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data

# 获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type') == 'weibo'):
            containerid = data.get('containerid')
    return containerid

# 获取微博大V账号的用户基本信息，如：微博昵称、微博地址、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    print(url)
    data = use_proxy(url, proxy_addr)
    print(data)
    content = json.loads(data).get('data')  # 内容根据Json动态加载获得
    print(content)
    name = content.get('userInfo').get('screen_name')
    print("微博昵称："+name+"\n")

path = os.getcwd() + "/weibo_info_detail.csv"
csvfile = open(path, 'a+', encoding='utf-8', newline='')
writer = csv.writer(csvfile)
writer.writerow(('scheme', 'created_at', 'text', 'reposts_count', 'comments_count', 'attitudes_count'))

# 获取微博内容信息,并保存到Excel表格中，内容包括：发布时间、每条微博的内容、点赞数、评论数、转发数等
def get_weibo(id, file):
    i = 1
    while True:
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
                    card_type = cards[j].get('card_type')
                    if(card_type == 9):
                        mblog = cards[j].get('mblog')
                        scheme = cards[j].get('scheme')
                        created_at = mblog.get('created_at')
                        text = mblog.get('text')
                        reposts_count = mblog.get('reposts_count')
                        comments_count = mblog.get('comments_count')
                        attitudes_count = mblog.get('attitudes_count')
                        print((scheme, created_at, text, reposts_count, comments_count, attitudes_count))
                        writer.writerow((scheme, created_at, text, reposts_count, comments_count, attitudes_count))
                i += 1
            else:
                break

        except Exception as e:
            print(e)
            pass

if __name__=="__main__":
    file = id+".txt"
    get_userInfo(id)
    get_weibo(id, file)



