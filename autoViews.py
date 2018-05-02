#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""刷访问量的脚本，使用的方法是调用fireFox浏览器。"""

from multiprocessing import Pool
from selenium import webdriver  # 导入webdriver包
import random


def driver_addcounts(webs, n):
    """启动浏览器"""
    driver = webdriver.Firefox()  # 初始化一个火狐浏览器实例：driver

    webslist = []
    for name, url in  webs.items():
        webslist.append(url)

    for i in range(0, n):
        urlk = random.randint(0, len(webslist)-1)
        urli = webslist[urlk]
        driver.maximize_window() # 最大化浏览器
        driver.get(urli) # 通过get()方法，打开一个url站点
        print("the working :", urli)

    driver.quit()  # 关闭并退出浏览器


if __name__ == '__main__':
    #你需要刷浏览量的名称及urls
    webs = {'阿里技术详解图册': 'https://blog.csdn.net/qq_27527961/article/details/80084406',
            'Python前六行': 'https://blog.csdn.net/qq_27527961/article/details/80067898',
            'python-reduce-神秘的第三参数': 'https://blog.csdn.net/qq_27527961/article/details/80056638',
            'python中字符串报错': 'https://blog.csdn.net/qq_27527961/article/details/80056626',
            '修改字符串': 'https://blog.csdn.net/qq_27527961/article/details/80054291',
            '时间杀手-for循环': 'https://blog.csdn.net/qq_27527961/article/details/80051710',
            'autopep8': 'https://blog.csdn.net/qq_27527961/article/details/80037853',
            '爬虫简介': 'https://blog.csdn.net/qq_27527961/article/details/80033892',
            'R语言模型协方差': 'https://blog.csdn.net/qq_27527961/article/details/80033253',
            'Python-pep8中文规范链接': 'https://blog.csdn.net/qq_27527961/article/details/80024185', }
    print("start the polls\n")
    p = Pool(10)#同时开的浏览器数量
    n = int(input("your needs numbers\n"))#需要刷几篇内容
    #由此，该脚本刷新的浏览次数一共是 p * n
    for i in range(11):
        p.apply_async(driver_addcounts, args=(webs, n,))
    p.close()
    p.join()
    print('All jobs is over')
