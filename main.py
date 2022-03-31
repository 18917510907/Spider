# -*- coding:utf-8 -*-

# 导包,发起请求使用urllib库的request请求模块
import urllib.request

# urlopen()向URL发请求,返回响应对象,注意url必须完整
response = urllib.request.urlopen('http://www.baidu.com/')
print(response)

html = response.read().decode('utf-8')

print(html)

# 导入模块
import urllib.request

# 向网站发送get请求
response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
print(html)

from urllib import request

# 定义变量：URL 与 headers
url = 'http://httpbin.org/get'  # 向测试网站发送请求
# 重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# 1、创建请求对象，包装ua信息
req = request.Request(url=url, headers=headers)
# 2、发送请求，获取响应对象
res = request.urlopen(req)
# 3、提取响应内容
html = res.read().decode('utf-8')
print(html)

from fake_useragent import UserAgent

# 实例化一个对象
ua = UserAgent()
# 随机获取一个ie浏览器ua
print(ua.ie)
print(ua.ie)
# 随机获取一个火狐浏览器ua
print(ua.firefox)
print(ua.firefox)

# 导入parse模块
from urllib import parse

# 构建查询字符串字典
query_string = {
    'wd': '爬虫'
}
# 调用parse模块的urlencode()进行编码
result = parse.urlencode(query_string)
# 使用format函数格式化字符串，拼接url地址
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

from urllib import request
from urllib import parse

url = 'http://www.baidu.com/s?wd={}'
# 想要搜索的内容
word = input('请输入搜索内容:')
params = parse.quote(word)
full_url = url.format(params)

# 全局取消证书验证

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 重构请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
# 创建请求对应
req = request.Request(url=full_url, headers=headers)
# 获取响应对象
res = request.urlopen(req)
# 获取响应内容
html = res.read().decode("utf-8")

filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)

# 修改后的代码
from urllib import request
from urllib import parse


# 拼接URL地址
def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    # 此处使用urlencode()进行编码
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url


# 发请求,保存本地文件
def request_url(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    # 请求对象 + 响应对象 + 提取内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 主程序入口
if __name__ == '__main__':
    word = input('请输入搜索内容:')
    url = get_url(word)
    filename = word + '.html'
    request_url(url, filename)
############

from urllib import request, parse
import time
import random
from ua_info import ua_list  # 使用自定义的ua池


# 定义一个爬虫类
class TiebaSpider(object):
    # 初始化url属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    # 1.请求函数，得到页面，传统三步
    def get_html(self, url):
        req = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        # windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
        # linux不会存在上述问题，可以直接使用decode('utf-8')解码
        html = res.read().decode()  # "gbk","ignore")
        return html

    # 2.解析函数，此处代码暂时省略，还没介绍解析模块
    def parse_html(self):
        pass

    # 3.保存文件函数
    def save_html(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    # 4.入口函数
    def run(self):
        name = input('输入贴吧名：')
        begin = int(input('输入起始页：'))
        stop = int(input('输入终止页：'))
        # +1 操作保证能够取到整数
        for page in range(begin, stop + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': str(pn)
            }
            # 拼接URL地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            # 发请求
            html = self.get_html(url)
            # 定义路径
            filename = '{}-{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 提示
            print('第%d页抓取成功' % page)
            # 每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1, 2))


# 以脚本的形式启动爬虫
if __name__ == '__main__':
    start = time.time()
    spider = TiebaSpider()  # 实例化一个对象spider
    spider.run()  # 调用入口函数
    end = time.time()
    # 查看程序执行时间
    print('执行时间:%.2f' % (end - start))  # 爬虫执行时间

import re

html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>

<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
# 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
pattern = re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
r_list = pattern.findall(html)
print(r_list)
# 整理数据格式并输出
if r_list:
    for r_info in r_list:
        print("影片名称：", r_info[0])
        print("影片主演：", r_info[1].strip())
        print(20 * "*")

from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list


# 定义一个爬虫类
class DoubanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        # 正则表达式
        re_bds = '<div class="hd">.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;.*?</p>'
        # 生成正则表达式对象
        pattern = re.compile(re_bds, re.S)
        # r_list: [('我不是药神','徐峥,周一围,王传君','2018-07-05'),...] 列表元组
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, r_list):
        # 生成文件对象
        with open('douban.csv', 'a', newline='', encoding="utf-8") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            # 整理数据
            for r in r_list:
                name = r[0].strip()
                director = r[1].strip()
                # 上映时间：2018-07-05
                # 切片截取时间
                starring = r[2].strip()
                time = r[3].strip()[0:4]
                L = [name, director, starring, time]
                # print(L)
                # 写入csv文件
                writer.writerow(L)
                print(name, time, director, starring)

    # 主函数
    def run(self):
        # 抓取第一页数据
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))


# 以脚本方式启动
if __name__ == '__main__':
    # 捕捉异常错误
    try:
        spider = DoubanSpider()
        spider.run()
    except Exception as e:
        print("错误:", e)

import pymysql
import cryptography

db = pymysql.connect(host='localhost', user='root', password='chenhaowei5', database='doubandb')

cursor = db.cursor()

# 第一种方法：编写sql语句，使用占位符传入相应数据
sql = "insert into filmtab values('%s','%s','%s','%s')" % ('星际穿越', '2014', '克里斯托弗·诺兰', '马修·麦康纳，安妮·海瑟薇')
print(sql)
cursor.execute(sql)

db.commit()

cursor.close()
db.close()

# 爬信息，放入sql数据库中

# coding=utf-8
from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list


# 定义一个爬虫类
class DoubanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.db = pymysql.connect(host='localhost', user='root', password='chenhaowei5', database='doubandb')
        self.cursor = self.db.cursor()

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        # 正则表达式
        re_bds = '<div class="hd">.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;.*?</p>'
        # 生成正则表达式对象
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, r_list):
        # 生成文件对象
        L = []
        sql = 'insert into filmtab values(%s,%s,%s,%s)'
        # 整理数据
        for r in r_list:
            t = (
                r[0].strip(),
                r[3].strip()[0:4],
                r[1].strip(),
                r[2].strip(),
            )
            L.append(t)
            print(t)
            try:
                self.cursor.executemany(sql, L)
                # 将数据提交数据库
                self.db.commit()
            except:
                # 发生错误则回滚
                self.db.rollback()
                print("skip one")

        def run(self):
            # 抓取第一页数据
            for offset in range(0, 11, 10):
                url = self.url.format(offset)
                self.get_html(url)
                # 生成1-3之间的浮点数
                time.sleep(random.uniform(1, 3))
            self.cursor.close()
            self.db.close()


import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 以脚本方式启动
if __name__ == '__main__':
    start = time.time()
    spider = DoubanSpider()
    spider.run()
    end = time.time()
    print("执行时间:%.2f" % (end - start))

# -*- coding: utf-8 -*-
from urllib import request
import re
import time
import random
import pymysql
from hashlib import md5
from ua_info import ua_list
import sys


class MovieSkySpider(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.db = pymysql.connect(host='localhost', user='root', password='chenhaowei5', database='movieskydb',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    # 1.请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        # 本网站使用gb2312的编码格式
        html = res.read().decode('gb2312', 'ignore')

        return html

    # 2.正则解析函数
    def re_func(self, re_bds, html):
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)

        return r_list

    # 3.提取数据函数
    def parse_html(self, one_url):
        # 调用请求函数，获取一级页面
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # 获取二级页面链接
        # link_list: ['/html//html/gndy/dyzz/20210226/61131.html','/html/xxx','','']
        link_list = self.re_func(re_bds, one_html)
        for link in link_list:
            # 判断是否需要爬取此链接
            # 1.获取指纹
            # 拼接二级页面url
            two_url = 'https://www.dytt8.net' + link
            s = md5()
            # 加密url，需要是字节串
            s.update(two_url.encode())
            # 生成指纹，获取十六进制加密字符串，
            finger = s.hexdigest()
            # 2.通过函数判断指纹在数据库中是否存在
            if self.is_hold_on(finger):
                # 抓取二级页面数据
                self.save_html(two_url)
                time.sleep(random.randint(1, 2))
                # 抓取后，把想用的url专属指纹存入数据库
                ins = 'insert into request_finger values (%s)'
                self.cursor.execute(ins, [finger])
                self.db.commit()
            else:
                sys.exit('更新完成')

    # 4.判断链接是否已经抓取过
    def is_hold_on(self, finger):
        # 查询数据库
        sql = 'select finger from request_finger where finger=%s'
        # execute()函数返回值为受影响的行数（即0或者非0）
        r = self.cursor.execute(sql, [finger])
        # 如果为0表示没有抓取过
        if not r:
            return True

    # 5.解析二级页面，获取数据（名称与下载链接）
    def save_html(self, two_url):
        two_html = self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1>\</div>.*?<a.*?href="(.*?)".*?>.*?style="BACKGROUND-COLOR:.*?</a>'
        # film_list: [('name','downloadlink'),(),(),()]
        film_list = self.re_func(re_bds, two_html)
        print(film_list)
        # 插入数据库
        sql = 'insert into movieinfo values(%s,%s)'
        # L = list(film_list[0])
        self.cursor.executemany(sql, film_list)
        self.db.commit()

    # 主函数
    def run(self):
        # 二级页面后四页的正则表达式略有不同，需要重新分析
        for i in range(1, 2):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = MovieSkySpider()
    spider.run()

import requests

url = 'http://baidu.com'
response = requests.get(url)
print(response)

import requests

data = {
    'name': '编程帮',
    'url': "www.biancheng.net"
}
response = requests.get('http://httpbin.org/get', params=data)
# 直接拼接参数也可以
# response = requests.get(http://httpbin.org/get?name=gemey&age=22)
# 调用响应对象text属性，获取文本信息
print(response.text)

import requests

url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=38785274,1357847304&fm=26&gp=0.jpg'
# 简单定义浏览器ua信息
headers = {'User-Agent': 'Mozilla/4.0'}
# 读取图片需要使用content属性
html = requests.get(url=url, headers=headers).content
# 以二进制的方式下载图片
with open('/Users/ericchen/Desktop/python_logo.jpg', 'wb') as f:
    f.write(html)

from lxml import etree
parse_html = etree.HTML(html)

from lxml import etree
html_str = '''
<div>
    <ul>
         <li class="item1"><a href="link1.html">Python</a></li>
         <li class="item2"><a href="link2.html">Java</a></li>
         <li class="site1"><a href="c.biancheng.net">C语言中文网</a>
         <li class="site2"><a href="www.baidu.com">百度</a></li>
         <li class="site3"><a href="www.jd.com">京东</a></li>
     </ul>
</div>
'''
html = etree.HTML(html_str)
# tostring()将标签元素转换为字符串输出，注意：result为字节类型
result = etree.tostring(html)
print(result.decode('utf-8'))
r_list = parse_html.xpath('xpath表达式')

# coding:utf8
import requests
from lxml import etree
from ua_info import ua_list
import random
class MaoyanSpider(object):
    def __init__(self):
        self.url='https://maoyan.com/board/4?offset=50'
        self.headers={'User-Agent':random.choice(ua_list)}
    def save_html(self):
        html=requests.get(url=self.url,headers=self.headers).text
        #jiexi
        parse_html=etree.HTML(html)
        # 基准 xpath 表达式，匹配10个<dd>节点对象
        dd_list=parse_html.xpath('//dl[@class="board-wrapper"]/dd') #列表放10个dd
        print(dd_list)
        # .// 表示dd节点的所有子节点后代节点
        # 构建item空字典将提取的数据放入其中
        item={}
        for dd in dd_list:
            # 处理字典数据，注意xpath表达式匹配结果是一个列表，因此需要索引[0]提取数据
            item['name']=dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star']=dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time']=dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            #输出数据
            print(item)
    def run(self):
        self.save_html()
if __name__ == '__main__':
    spider=MaoyanSpider()
    spider.run()

